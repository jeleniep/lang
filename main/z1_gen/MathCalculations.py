from LLVMGenerator import LLVMGenerator

def calculate(a, b, operator):
    return  {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }[operator](float(a), float(b))

def representsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

class MathCalculations:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.operator = None
        self.parent = None
        self.containVariable = False

    def build(self, arr, generator: LLVMGenerator):
        print(arr)
        op = ['+', '-', '*', '/']
        head = None
        current = head 
        for elem in arr:
            new = MathCalculations()
            if(elem in op):
                # print(op, elem)
                new.operator = elem
                new.containVariable = False
            else: 
                new.value = elem
                new.containVariable = not representsFloat(elem)
            if (not head):
                head = new
            else:
                current = head
                lastVisited = None
                found = True
                while found:
                    if(current.left):
                        if(current.left.operator):
                            lastVisited = current
                            current = current.left
                        elif (current.left.value):
                            temp = True
                            while (found and temp):
                                if(current.right):
                                    if(current.right.operator):
                                        if (current.right == lastVisited):
                                            lastVisited = current
                                            current = current.parent
                                        else:    
                                            lastVisited = current
                                            current = current.right
                                            temp = False
                                    elif(current.right.value):
                                        lastVisited = current
                                        current = current.parent
                                else:
                                    new.parent = current
                                    current.right = new
                                    found = False
                    else:
                        new.parent = current
                        current.left = new
                        found = False
        head.display()
        head.optimize()
        head.display()
        val_id = head.createLLVM(generator)
        head.display()

        return val_id

    def optimize(self):
        found = True
        head = self
        current = head
        lastVisited = None
        operator = None
        while(found):
            # head.display()
            # print("\n", lastVisited, current.left, (current.left == lastVisited), current.left and not (current.left == lastVisited), "\n")
            if (current.left):
                if (current.left.containVariable and current.right.value):
                    current.containVariable = True
                    if (current.parent):                        
                        current = current.parent
                    else: 
                        found = False   
                    continue
                elif(current.left.operator and (not current.left.containVariable)):
                    lastVisited = current
                    current = current.left
                    continue
                elif (current.left.value):
                    if (current.right):
                        if (current.right.containVariable and current.left.value):
                            current.containVariable = True
                            if (current.parent):                        
                                current = current.parent
                            else: 
                                found = False                      
                            continue
                        elif(current.right.operator and (not current.right.containVariable)):
                            lastVisited = current
                            current = current.right
                            continue
                        elif (current.right.value):
                            if (representsFloat(current.left.value) and representsFloat(current.right.value)):
                                current.value = calculate(current.left.value, current.right.value, current.operator)
                                current.operator = None
                                current.left = None
                                current.right = None
                                current = head
                                continue                            

            if (current.right):
                if(current.right.operator and (not current.right.containVariable)):
                    lastVisited = current
                    current = current.right
                    continue
                else:
                    found = False 
            else:
                found = False    


        return 


    def createLLVM(self, generator: LLVMGenerator):
        found = True
        head = self
        current = head
        lastVisited = None
        operator = None
        while(found):
            head.display()
            # print("\n", lastVisited, current.left, (current.left == lastVisited), current.left and not (current.left == lastVisited), "\n")
            if (current.left):
                # print("left", current.left.operator, current.left.value)
                if (current.left.operator):
                    current = current.left                    
                elif (current.left.value):
                    if (current.right):
                        if (current.right.operator):
                            print("cr")
                            current = current.right
                            continue
                        elif(current.right.value):
                            print("crv")
                            calc_id = generator.calculate(str(current.left.value), str(current.right.value), current.operator)
                            current.value = calc_id
                            current.operator = None
                            current.left = None
                            current.right = None
                            current = head
            elif (current.right):
                print("right")
                if(current.right.operator):
                    current = current.right
                    continue
                else:
                    print("end1")
                    found = False 
            else:
                print("end2")
                found = False    

        print("z heada", head.value)
        return head.value


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % (str(self.value or self.operator) + str(self.containVariable))
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % (str(self.value or self.operator) + str(self.containVariable))
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % ((self.value or self.operator) + str(self.containVariable))
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % ((self.value or self.operator) + str(self.containVariable))
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


