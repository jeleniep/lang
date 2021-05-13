
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
   
   