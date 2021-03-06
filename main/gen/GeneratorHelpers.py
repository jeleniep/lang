
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

    comparators_int = {
        '<': "slt",
        '==' : "eq" ,
        '>' :  "sgt",
        '<=' : "sle",
        '>=' : "sge",
        '!=': "ne"
    }

    comparators_float = {
        '<': "olt",
        '==' : "oeq" ,
        '>' :  "ogt",
        '<=' : "ole",
        '>=' : "oge",
        '!=': "one"
    }
   
    @staticmethod
    def find_variable(var_name, variables, var_range):
        print(var_name, variables)
        global_var_name = f"@{var_name}"
        print(variables[var_range][var_name], var_name)
        if var_name in variables[var_range]:
          var_type = variables[var_range][var_name]
          return var_type
        elif global_var_name in variables["base"]:
            var_type = variables[var_range][global_var_name]
            return var_type
        else:
          raise Exception(f"ERROR: Variable {var_name} not exist")
  
    @staticmethod
    def checkType(var):
        try: 
            temp = int(var)
            if (str(temp) == var):
                return 'int'
            return 'double'
        except ValueError:
            try: 
                float(var)
                return 'double'
            except ValueError:
                if (var[0] == "%"):
                    return 'internal'
                return 'var'
   
    @staticmethod
    def parse_cmp(cmp, val_type, values, counter, context):
        returned_str = ""
        final_values = [values[0], values[1]]
        if(values[0][0] == "%"):
            returned_str += f"%{counter[context]} = load {val_type}, {val_type}* {values[0]} \n"
            final_values[0] = f"%{counter[context]}"
            counter[context] += 1
        if(values[1][0] == "%"):
            returned_str += f"%{counter[context]} = load {val_type}, {val_type}* {values[1]} \n"
            final_values[1] = f"%{counter[context]}"
            counter[context] += 1
        if (val_type == "i32"):
            comparator = GeneratorHelpers.comparators_int[str(cmp.COMPARATOR())]
            returned_str += f"%{counter[context]} = icmp {comparator} i32 {final_values[0]}, {final_values[1]} \n"
        else:
            comparator = GeneratorHelpers.comparators_float[str(cmp.COMPARATOR())]

            returned_str += f"%{counter[context]} = fcmp {comparator} double {final_values[0]}, {final_values[1]} \n"
        
        counter[context] += 1
        return returned_str