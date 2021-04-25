from GeneratorHelpers import GeneratorHelpers

def checkType(var):
    try: 
        float(var)
        return 'float'
    except ValueError:
        try: 
            int(var)
            return 'int'
        except ValueError:
            if (var[0] == "%"):
              return 'internal'
            return 'var'

class LLVMGenerator:
    header_text = ""
    main_text = ""
    tmp = 1

    def __init__(self):
        self.variables = {}

    def load_values(self, val_a, val_b):
      var_type_a = checkType(val_a)
      var_type_b = checkType(val_b)
      a = val_a
      b = val_b
      if (var_type_a == 'var'):
        if val_a in self.variables:
          var_type = self.variables[val_a]
          self.main_text += f"%{self.tmp} = load {var_type}, {var_type}* %{val_a}\n"
          a = f"%{self.tmp}"
          self.tmp += 1
          var_type_a = var_type
        else:
          raise Exception(f"ERROR: Variable {val_a} not exist")
      if (var_type_b == 'var'):
        if val_b in self.variables:
          var_type = self.variables[val_b]
          self.main_text += f"%{self.tmp} = load {var_type}, {var_type}* %{val_b}\n"
          b = f"%{self.tmp}"
          self.tmp += 1
          var_type_b = var_type
        else:
          raise Exception(f"ERROR: Variable {val_b} not exist")

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
      if (var_type_a == 'float' or var_type_b == 'float'):
        a = a if (a[0] == '%') else str(float(a))
        b = b if (b[0] == '%') else str(float(b)) 
        self.main_text += f"%{self.tmp} = fadd double {a}, {b}\n"      
      else:
        self.main_text += f"%{self.tmp} = add nsw i32 {a}, {b}\n"      
      self.tmp += 1
      return f"%{self.tmp-1}"

    def minus(self, val_a, val_b):
      a, b, var_type_a, var_type_b = self.load_values(val_a, val_b)
      if (var_type_a == 'float' or var_type_b == 'float'):
        a = a if (a[0] == '%') else str(float(a))
        b = b if (b[0] == '%') else str(float(b))
        self.main_text += f"%{self.tmp} = fsub double {a}, {b}\n"      
      else:
        self.main_text += f"%{self.tmp} = sub nsw i32 {a}, {b}\n"      
      self.tmp += 1
      return f"%{self.tmp-1}"

    def mul(self, val_a, val_b):
      a, b, var_type_a, var_type_b = self.load_values(val_a, val_b)
      if (var_type_a == 'float' or var_type_b == 'float'):
        print(val_a, a, "as", type(a))
        a = a if (a[0] == '%') else str(float(a))
        b = b if (b[0] == '%') else str(float(b)) 
        self.main_text += f"%{self.tmp} = fmul double {a}, {b}\n"      
      else:
        self.main_text += f"%{self.tmp} = mul nsw i32 {a}, {b}\n"      
      self.tmp += 1
      return f"%{self.tmp-1}"

    def div(self, val_a, val_b):
      a, b, var_type_a, var_type_b = self.load_values(val_a, val_b)
      if (var_type_a == 'float' or var_type_b == 'float'):
        a = a if (a[0] == '%') else str(float(a))
        b = b if (b[0] == '%') else str(float(b)) 
        self.main_text += f"%{self.tmp} = fdiv double {a}, {b}\n"      
      else:
        self.main_text += f"%{self.tmp} = div nsw i32 {a}, {b}\n"      
      self.tmp += 1
      return f"%{self.tmp-1}"

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
        if (type(value) == str and value[0] == "%"):
          self.main_text += f"store {self.variables[name]} {value}, {self.variables[name]}* %{name}\n"
        elif (self.variables[name] == 'i32'):
          value = int(value)
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
   