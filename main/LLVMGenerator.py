from GeneratorHelpers import GeneratorHelpers
class LLVMGenerator:
    header_text = ""
    main_text = ""
    tmp = 1

    def __init__(self):
        self.variables = {}

    def declare(self, id, var_type):
      name = str(id)
      var_type_str = str(var_type)
      if name not in self.variables:
        self.main_text += f"%{name} = alloca {GeneratorHelpers.declare_types[var_type_str]}\n"
        self.variables[name] = GeneratorHelpers.declare_types[var_type_str]
      else:
          raise Exception(f"ERROR: Redeclaration of variable {name}")


    def assign(self, id, value):
      name = str(id)
      if name in self.variables:
        self.main_text += f"store {self.variables[name]} {value}, {self.variables[name]}* %{name}\n"
      else:
          raise Exception(f"ERROR: Variable {name} not exist")

    def printf(self, id):
      name = str(id)
      if name in self.variables:
        var_type = self.variables[name]
        printf_type = GeneratorHelpers.printf_types[var_type]
        self.main_text += f"%{self.tmp} = load {var_type}, {var_type}* %{name}\n"
        self.tmp += 1
        self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({printf_type[0]}, i32 0, i32 0), {printf_type[1]} %{self.tmp-1})\n"
        self.tmp += 1
      else:
          raise Exception(f"ERROR: Variable {name} not exist")

    def scanf(self, id):      
      name = str(id)
      if name in self.variables:
        var_type = self.variables[name]
        scanf_type = GeneratorHelpers.scanf_types[var_type] 
        self.main_text += f"%{self.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ({scanf_type[0]}, i32 0, i32 0), {scanf_type[1]} %{id})\n"
        self.tmp += 1
   

    def generate(self):
      text = ""
      text += "declare i32 @printf(i8*, ...)\n"
      text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
      text += "@strp = constant [4 x i8] c\"%d\\0A\\00\"\n"
      text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
      text += "@strpd = constant [4 x i8] c\"%f\\0A\00\"\n"
      text += "@strsd = constant [4 x i8] c\"%lf\\00\"\n"
      text += self.header_text
      text += "define i32 @main() nounwind{\n"
      text += self.main_text
      text += "ret i32 0 }\n"
      return text
   