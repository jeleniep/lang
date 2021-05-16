
class GeneratorHelpers:
    scanf_types = {
        "i32": ["[3 x i8], [3 x i8]* @strs", "i32*"],
        "double": ["[4 x i8], [4 x i8]* @strsd", "double*"],
        "i8*": ["[3 x i8], [3 x i8]* @str", "i8*"]
    }

    printf_types = {
        "i32": ["[4 x i8], [4 x i8]* @strp", "i32"],
        "double": ["[4 x i8], [4 x i8]* @strpd", "double"],
        "i8*": ["[3 x i8], [3 x i8]* @str", "i8*"]
    }

    declare_types = {
        "int": "i32",
        "float": "double",
        "string": "i8*"
    }
   
    @staticmethod
    def find_variable(var_name, variables, var_range):
        if var_name in variables[var_range]:
          var_type = variables[var_range][var_name]
          return var_type
        elif var_name in variables["base"]:
            var_type = variables[var_range][var_name]
            return var_type
        else:
          raise Exception(f"ERROR: Variable {var_name} not exist")
  
    @staticmethod
    def checkType(var):
        try: 
            float(var)
            return 'double'
        except ValueError:
            try: 
                int(var)
                return 'int'
            except ValueError:
                if (var[0] == "%"):
                    return 'internal'
                return 'var'
   