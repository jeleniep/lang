from LLVMGenerator import LLVMGenerator
from GeneratorHelpers import GeneratorHelpers



class WhileLLVMGenerator:


    def __init__(self, generator: LLVMGenerator):
        self.generator = generator
        self.params = []
        self.start_id = None

    def begin_while(self, cmp):
        values = []
        val_type = ""
        for i in range(2):
            if (cmp.value(i).ID() is not None):
                name = str(cmp.value(i).ID())
                val_type = GeneratorHelpers.find_variable(name, self.generator.variables, self.generator.var_range)
                values.append(f"%{name}")
            else:
                val = str(
                    cmp.value(i).INT_VALUE() or  
                    cmp.value(i).DOUBLE_VALUE()
                )
                val_type = "i32" if cmp.value(i).INT_VALUE() is not None else "double"
                values.append(val)
        self.generator.counter[self.generator.context]
        placeholder = "afterWhilePlaceholder"
        self.generator.llvm_text[self.generator.context] += f"br label %{self.generator.counter[self.generator.context]}\n\n"
        self.generator.llvm_text[self.generator.context] += f"; <label>:{self.generator.counter[self.generator.context]}: \n"
        self.start_id = self.generator.counter[self.generator.context]
        self.generator.counter[self.generator.context] +=1
        init_string = GeneratorHelpers.parse_cmp(cmp, val_type, values, self.generator.counter, self.generator.context)
        self.generator.llvm_text[self.generator.context] += init_string
        self.generator.llvm_text[self.generator.context] += f"br i1 %{self.generator.counter[self.generator.context] - 1}, label %{self.generator.counter[self.generator.context]}, label %{placeholder} \n\n"
        self.generator.llvm_text[self.generator.context] += f"; <label>:{self.generator.counter[self.generator.context]}: \n"
        self.generator.counter[self.generator.context] +=1

        pass
    
    def end_while(self):
        lines = self.generator.llvm_text[self.generator.context].split("\n")
        if ("br label" not in lines[len(lines) - 2]):
            self.generator.llvm_text[self.generator.context] += f"br label %{self.start_id} \n\n"
        self.generator.llvm_text[self.generator.context] += f"; <label>:{self.generator.counter[self.generator.context]}: \n"
        self.generator.llvm_text[self.generator.context] = self.generator.llvm_text[self.generator.context].replace("afterWhilePlaceholder", str(self.generator.counter[self.generator.context]))
        self.generator.counter[self.generator.context] +=1
        pass