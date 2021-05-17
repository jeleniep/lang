from LLVMGenerator import LLVMGenerator
from GeneratorHelpers import GeneratorHelpers



class IfLLVMGenerator:


    def __init__(self, generator: LLVMGenerator):
        self.generator = generator
        self.params = []
        self.returned_type = None

    def begin_if(self, cmp, is_else):
        values = []
        val_type = ""
        for i in range(2):
            if (cmp.value(i).ID() is not None):
                values.append(f"%{str(cmp.value(i).ID())}")
                val_type = GeneratorHelpers.find_variable(str(cmp.value(i).ID()), self.generator.variables, self.generator.var_range)
            else:
                val = str(
                    cmp.value(i).INT_VALUE() or  
                    cmp.value(i).DOUBLE_VALUE()
                )
                val_type = "i32" if cmp.value(i).INT_VALUE() is not None else "double"
                values.append(val)
        self.generator.counter[self.generator.context]
        placeholder = "elsePlaceholder" if is_else is not None else "afterIfPlaceholder"
        init_string = GeneratorHelpers.parse_cmp(cmp, val_type, values, self.generator.counter, self.generator.context)
        self.generator.llvm_text[self.generator.context] += init_string
        self.generator.llvm_text[self.generator.context] += f"br i1 %{self.generator.counter[self.generator.context] - 1}, label %{self.generator.counter[self.generator.context]}, label %{placeholder} \n\n"
        self.generator.llvm_text[self.generator.context] += f"; <label>:{self.generator.counter[self.generator.context]}: \n"
        self.generator.counter[self.generator.context] +=1
        pass


    def add_else(self):
        lines = self.generator.llvm_text[self.generator.context].split("\n")
        if ("br label" not in lines[len(lines) - 2]):
            self.generator.llvm_text[self.generator.context] += f"br label %afterIfPlaceholder \n\n"
        self.generator.llvm_text[self.generator.context] += f"; <label>:{self.generator.counter[self.generator.context]}: \n"
        self.generator.llvm_text[self.generator.context] = self.generator.llvm_text[self.generator.context].replace("elsePlaceholder", str(self.generator.counter[self.generator.context]))
        self.generator.counter[self.generator.context] +=1
        pass    
    
    def end_if(self):
        lines = self.generator.llvm_text[self.generator.context].split("\n")
        if ("br label" not in lines[len(lines) - 2]):
            self.generator.llvm_text[self.generator.context] += f"br label %afterIfPlaceholder \n\n"
        self.generator.llvm_text[self.generator.context] += f"; <label>:{self.generator.counter[self.generator.context]}: \n"
        self.generator.llvm_text[self.generator.context] = self.generator.llvm_text[self.generator.context].replace("afterIfPlaceholder", str(self.generator.counter[self.generator.context]))
        self.generator.counter[self.generator.context] +=1
        pass