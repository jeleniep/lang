from GeneratorHelpers import GeneratorHelpers

class LLVMGenerator:
    llvm_text = {
      "header": "",
      "base": "",
      "function": ""
    }
    counter = {
      "header": 1,
      "base": 1,
      "function": 0
    }
    context = "base"
    var_range = "base"
    
    # header_text = ""
    # function_text = ""
    # main_text = ""
    # tmp = 1
    # tmp_header = 1
    # tmp_function = 1

    def __init__(self):
        self.variables = {}
        self.variables[self.var_range] = {
          "base": {}
        }
        self.functions = {}

    def load_values(self, val_a, val_b):
      var_type_a = GeneratorHelpers.checkType(val_a)
      var_type_b = GeneratorHelpers.checkType(val_b)
      a = val_a
      b = val_b
      if (var_type_a == 'var'):
        var_type = GeneratorHelpers.find_variable(val_a, self.variables, self.var_range)
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = load {var_type}, {var_type}* %{val_a}\n"
        a = f"%{self.counter[self.context]}"
        self.counter[self.context] += 1
        var_type_a = var_type

      if (var_type_b == 'var'):
        var_type = GeneratorHelpers.find_variable(val_a, self.variables, self.var_range)
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = load {var_type}, {var_type}* %{val_b}\n"
        b = f"%{self.counter[self.context]}"
        self.counter[self.context] += 1
        var_type_b = var_type

      return a, b, var_type_a, var_type_b

    def calculate(self, a, b, operator):
      print("operator")
      return  {
          '+': lambda a, b: self.add(a, b),
          '-': lambda a, b: self.minus(a, b),
          '*': lambda a, b: self.mul(a, b),
          '/': lambda a, b: self.div(a, b)
      }[operator](a, b)
    
    def add(self, val_a, val_b):
      a, b, var_type_a, var_type_b = self.load_values(val_a, val_b)
      if (var_type_a == 'double' or var_type_b == 'double'):
        a = a if (a[0] == '%') else str(float(a))
        b = b if (b[0] == '%') else str(float(b)) 
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = fadd double {a}, {b}\n"      
      else:
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = add nsw i32 {a}, {b}\n"      
      self.counter[self.context] += 1
      return f"%{self.counter[self.context]-1}"

    def minus(self, val_a, val_b):
      a, b, var_type_a, var_type_b = self.load_values(val_a, val_b)
      if (var_type_a == 'double' or var_type_b == 'double'):
        a = a if (a[0] == '%') else str(float(a))
        b = b if (b[0] == '%') else str(float(b))
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = fsub double {a}, {b}\n"      
      else:
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = sub nsw i32 {a}, {b}\n"      
      self.counter[self.context] += 1
      return f"%{self.counter[self.context]-1}"

    def mul(self, val_a, val_b):
      a, b, var_type_a, var_type_b = self.load_values(val_a, val_b)
      if (var_type_a == 'double' or var_type_b == 'double'):
        print(val_a, a, "as", type(a))
        a = a if (a[0] == '%') else str(float(a))
        b = b if (b[0] == '%') else str(float(b)) 
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = fmul double {a}, {b}\n"      
      else:
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = mul nsw i32 {a}, {b}\n"      
      self.counter[self.context] += 1
      return f"%{self.counter[self.context]-1}"

    def div(self, val_a, val_b):
      a, b, var_type_a, var_type_b = self.load_values(val_a, val_b)
      print("types", var_type_a, var_type_b)
      if (var_type_a == 'double' or var_type_b == 'double'):
        a = a if (a[0] == '%') else str(float(a))
        b = b if (b[0] == '%') else str(float(b)) 
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = fdiv double {a}, {b}\n"      
      else:
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = div nsw i32 {a}, {b}\n"      
      self.counter[self.context] += 1
      return f"%{self.counter[self.context]-1}"

    def declare(self, id, var_type):
      name = str(id)
      var_type_str = str(var_type)
      print(var_type_str, "123123123")
      if name not in self.variables[self.var_range]:
        if (var_type_str == "string"):
          self.llvm_text[self.context] += f"%{name} = alloca {GeneratorHelpers.declare_types[var_type_str]}\n"
          self.llvm_text[self.context] += f"%{self.counter[self.context]} = call noalias i8* @malloc(i64 255) #3\n"
          self.llvm_text[self.context] += f"store i8* %{self.counter[self.context]}, i8** %{name}\n"
          self.counter[self.context] += 1
        else:
          self.llvm_text[self.context] += f"%{name} = alloca {GeneratorHelpers.declare_types[var_type_str]}\n"
        self.variables[self.var_range][name] = GeneratorHelpers.declare_types[var_type_str]
      else:
          raise Exception(f"ERROR: Redeclaration of variable {name}")


    def assign(self, id, value):
      name = str(id)
      var_type = GeneratorHelpers.find_variable(name, self.variables, self.var_range)
      if (var_type == "i8*"):
        val = str(value)[:-1] + "\\00\""
        title = f"@str.{self.counter['header']}"
        self.counter["header"] += 1
        self.llvm_text["header"] += f"{title} = constant [{len(str(value)) - 1} x i8] c{val}\n"    
        # self.llvm_text[self.context] += f"store i8* getelementptr inbounds ([{len(str(value)) - 1} x i8], [{len(str(value)) - 1} x i8]* {title}, i32 0, i32 0), i8** %{name}\n"
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = load i8*, i8** %{name}"
        self.counter[self.context] += 1
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = call i8* @strcpy(i8* %{self.counter[self.context] - 1}, i8* getelementptr inbounds ([{len(str(value)) - 1} x i8], [{len(str(value)) - 1} x i8]* {title}, i32 0, i32 0))"
        self.counter[self.context] += 1
        return
      elif (type(value) == str and value[0] == "%"):
        self.llvm_text[self.context] += f"store {self.variables[self.var_range][name]} {value}, {self.variables[self.var_range][name]}* %{name}\n"
      elif (self.variables[self.var_range][name] == 'i32'):
        value = int(value)
      self.llvm_text[self.context] += f"store {self.variables[self.var_range][name]} {value}, {self.variables[self.var_range][name]}* %{name}\n"


    def printf(self, id):
      name = str(id)
      var_type = GeneratorHelpers.find_variable(name, self.variables, self.var_range)
      printf_type = GeneratorHelpers.printf_types[var_type]
      if (var_type == "i8*"):
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = load i8*, i8** %{id}\n"
      else:
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = load {var_type}, {var_type}* %{name}\n"
      self.counter[self.context] += 1
      self.llvm_text[self.context] += f"%{self.counter[self.context]} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({printf_type[0]}, i32 0, i32 0), {printf_type[1]} %{self.counter[self.context]-1})\n"
      self.counter[self.context] += 1


    def scanf(self, id):      
      name = str(id)
      local_id = id
      var_type = GeneratorHelpers.find_variable(name, self.variables, self.var_range)
      scanf_type = GeneratorHelpers.scanf_types[var_type]
      if (var_type == "i8*"):
        self.llvm_text[self.context] += f"%{self.counter[self.context]} = load i8*, i8** %{id}\n"
        local_id = self.counter[self.context]
        self.counter[self.context] += 1
        print("stretrtrtr")
      self.llvm_text[self.context] += f"%{self.counter[self.context]} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ({scanf_type[0]}, i32 0, i32 0), {scanf_type[1]} %{local_id})\n"
                                  #  %4 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i8* %3)

      self.counter[self.context] += 1
   

    def generate(self):
      text = ""
      text += "declare i32 @printf(i8*, ...)\n"
      text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
      text += "@str = constant [3 x i8] c\"%s\\00\"\n"
      text += "@strp = constant [4 x i8] c\"%d\\0A\\00\"\n"
      text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
      text += "@strpd = constant [4 x i8] c\"%f\\0A\00\"\n"
      text += "@strsd = constant [4 x i8] c\"%lf\\00\"\n"
      text += self.llvm_text["header"] + "\n"
      text += self.llvm_text["function"] + "\n"
      text += "define i32 @main() nounwind{\n"
      text += self.llvm_text["base"]
      text += "ret i32 0 }\n"
      text += "; Function Attrs: nounwind\n"
      text += "declare noalias i8* @malloc(i64) #1\n"
      text += "; Function Attrs: nounwind\n"
      text += "declare i8* @strcpy(i8*, i8*) #1\n"
      return text
   