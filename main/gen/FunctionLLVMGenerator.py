from LLVMGenerator import LLVMGenerator
from GeneratorHelpers import GeneratorHelpers



class FunctionLLVMGenerator:


    def __init__(self, generator: LLVMGenerator):
        self.generator = generator
        self.params = []
        self.returned_type = None

    def declare_function(self, name, returned_type):
        self.generator.context = "function"
        self.generator.var_range = name
        self.returned_type = GeneratorHelpers.declare_types[returned_type]
        self.generator.functions[name] = {
            "returned_type": GeneratorHelpers.declare_types[returned_type],
            "params": []
        }
        self.generator.llvm_text[self.generator.context] += (
            f"define {GeneratorHelpers.declare_types[returned_type]} @{name}"
        ) 


    def define_function_params(self):
        params_types_string = ""
        params_names_string = ""
        for param in self.params:
            if (params_types_string == ""):
                params_types_string += param['type']
            else:
                params_types_string += f", {param['type']}"
            self.generator.functions[self.generator.var_range]["params"].append({
                "type": param["type"],
                "name": param["name"]
            })
            params_names_string += f"%{param['name']} = alloca {param['type']}\n" 
            params_names_string += f"store {param['type']} %{self.generator.counter['function']}, {param['type']}* %{param['name']}\n"
            self.generator.counter["function"] += 1
        params_names_string += f"%retVal = alloca {self.returned_type}\n" 
        self.generator.llvm_text[self.generator.context] += f"({params_types_string}) #0 {{  \n" + params_names_string
        
        self.params = []
        self.generator.counter["function"] += 1

    def add_function_param(self, var_type, name):
        self.params.append({
                "type": GeneratorHelpers.declare_types[var_type],
                "name": name
            })


    def call_function(self, name, args):
        print(self.generator.functions)
        returned_type = self.generator.functions[name]["returned_type"]
        args_string = ""
        for i, param in enumerate(self.generator.functions[name]["params"]):
            value = args.value(i).ID() 
            var_type = None
            if (value):
                var_type = GeneratorHelpers.find_variable(value, self.generator.variables, self.generator.var_range)
                if (var_type != param['returned_type']):
                    raise Exception(f"ERROR: Variable {value} should be a {param['returned_type']}.")
            else: 
                value = (
                args.value(i).INT_VALUE() or
                args.value(i).DOUBLE_VALUE() or
                args.value(i).STRING_VALUE()
                )
            if (args_string == ""):
                args_string += f"{param['returned_type']} {value}"
            else:
                args_string += f", {param['returned_type']} {value}"

        f"call {returned_type} @{name}({args_string} i32 1, i32 %19, float 3.000000e+00)"
        pass

    def end_declare_function(self):
        self.generator.llvm_text[self.generator.context] += f"%{self.generator.counter[self.generator.context]} = load {self.returned_type}, {self.returned_type}* %retVal\n"
        self.generator.llvm_text[self.generator.context] += f"ret {self.returned_type} %{self.generator.counter[self.generator.context]} \n"
        self.generator.llvm_text[self.generator.context] += f"}} \n"
        self.generator.context = "base"
        self.generator.var_range = "base"
        self.returned_type = None
        self.generator.counter["function"] = 0