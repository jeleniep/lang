from LLVMGenerator import LLVMGenerator
from GeneratorHelpers import GeneratorHelpers



class FunctionLLVMGenerator:


    def __init__(self, generator: LLVMGenerator):
        self.generator = generator
        self.params = []
        self.returned_type = None

    def declare_function(self, name, returned_type):
        if (self.generator.context == "function"):
          raise Exception(f"ERROR: Cannot declare function {name} in function {self.generator.var_range}")
    
        if (name in self.generator.functions):
          raise Exception(f"ERROR: Redeclaration of function {name}")

        self.generator.functions[name] = {
            "returned_type": GeneratorHelpers.declare_types[returned_type],
            "params": []
        }
        self.generator.context = "function"
        self.generator.var_range = name
        self.generator.variables[name] = {}
        self.returned_type = GeneratorHelpers.declare_types[returned_type]

        self.generator.llvm_text[self.generator.context] += (
            f"define {GeneratorHelpers.declare_types[returned_type]} @{name}"
        ) 


    def define_function_params(self):
        params_types_string = ""
        params_names_string = ""
        for param in self.params:
            if (params_types_string == ""):
                params_types_string += param['returned_type']
            else:
                params_types_string += f", {param['returned_type']}"
            self.generator.functions[self.generator.var_range]["params"].append({
                "returned_type": param["returned_type"],
                "name": param["name"]
            })
            self.generator.variables[self.generator.var_range][param["name"]] = param["returned_type"]
            params_names_string += f"%{param['name']} = alloca {param['returned_type']}\n" 
            params_names_string += f"store {param['returned_type']} %{self.generator.counter['function']}, {param['returned_type']}* %{param['name']}\n"
            self.generator.counter["function"] += 1
        params_names_string += f"%retVal = alloca {self.returned_type}\n" 
        self.generator.llvm_text[self.generator.context] += f"({params_types_string}) #0 {{  \n" + params_names_string
        
        self.params = []
        self.generator.counter["function"] += 1

    def add_function_param(self, var_type, name):
        self.params.append({
                "returned_type": GeneratorHelpers.declare_types[var_type],
                "name": name
            })

    def return_expression(self, value):
        val = ""
        if (value.ID() is not None):
            val = f"%{str(value.ID())}"
            self.generator.llvm_text[self.generator.context] += f"%{self.generator.counter[self.generator.context]} = load {self.returned_type}, {self.returned_type}* {val}\n"
            self.generator.llvm_text[self.generator.context] += f"store {self.returned_type} %{self.generator.counter[self.generator.context]}, {self.returned_type}* %retVal\n"
            self.generator.counter[self.generator.context] += 1
        else:
            val = str(
                value.INT_VALUE() or  
                value.DOUBLE_VALUE() or
                value.STRING_VALUE()
            )
            self.generator.llvm_text[self.generator.context] += f"store {self.returned_type} {val}, {self.returned_type}* %retVal\n"

        self.generator.llvm_text[self.generator.context] += f"br label %return_placeholder \n"

       

    def call_function(self, name, args, assign = False):
        print(self.generator.var_range)
        if (name not in self.generator.functions):
          raise Exception(f"ERROR: Function {name} does not exist.")

        returned_type = self.generator.functions[name]["returned_type"]
        args_string = ""
            
        for i, param in enumerate(self.generator.functions[name]["params"]):
            value = args.value(i).ID() if hasattr(args.value(i), 'ID') else None
            var_type = None
            if (value is not None):
                value = str(value)
                var_type = GeneratorHelpers.find_variable(value, self.generator.variables, self.generator.var_range)
                self.generator.llvm_text[self.generator.context] += f"%{self.generator.counter[self.generator.context]} = load {var_type}, {var_type}* %{value}\n"
                value = f"%{self.generator.counter[self.generator.context]}"
                self.generator.counter[self.generator.context] += 1
                if (var_type != param['returned_type']):
                    raise Exception(f"ERROR: Variable {value} should be a {param['returned_type']}.")
            else: 
                value = (
                args.value(i).INT_VALUE() or
                args.value(i).DOUBLE_VALUE() or
                args.value(i).STRING_VALUE()
                )
            if (args_string == ""):
                print("1e")
                args_string += f"{param['returned_type']} {value}"
            else:
                print("2e")
                args_string += f", {param['returned_type']} {value}"
        self.generator.llvm_text[self.generator.context] += f"%{self.generator.counter[self.generator.context]} = call {returned_type} @{name}({args_string})\n"
        self.generator.counter[self.generator.context] += 1
        returned_id = f"%{self.generator.counter[self.generator.context] - 1}"
        self.generator.returned_types[returned_id] = returned_type
        return returned_id

    def end_declare_function(self):
        lines = self.generator.llvm_text[self.generator.context].split("\n")
        print("test2", lines[len(lines) - 2],  "spacja", f"; <label>:return_placeholder ")
        if (f"; <label>:{self.generator.counter[self.generator.context] - 1}" not in lines[len(lines) - 2]):
            self.generator.llvm_text[self.generator.context] += f"; <label>:{self.generator.counter[self.generator.context]}:\n"
            self.generator.llvm_text[self.generator.context] = self.generator.llvm_text[self.generator.context].replace("return_placeholder", str(self.generator.counter[self.generator.context]))
            self.generator.counter[self.generator.context] += 1 
        else:
            self.generator.llvm_text[self.generator.context] = self.generator.llvm_text[self.generator.context].replace("return_placeholder", str(self.generator.counter[self.generator.context] - 1))
            
        self.generator.llvm_text[self.generator.context] += f"%{self.generator.counter[self.generator.context]} = load {self.returned_type}, {self.returned_type}* %retVal\n"
        self.generator.llvm_text[self.generator.context] += f"ret {self.returned_type} %{self.generator.counter[self.generator.context]} \n"
        self.generator.llvm_text[self.generator.context] += f"}} \n"
        self.generator.context = "base"
        self.generator.var_range = "base"
        self.returned_type = None
        self.generator.counter["function"] = 0