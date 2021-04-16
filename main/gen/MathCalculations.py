
class MathCalculations:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.operator = None
        self.parent = None

    def build(self, arr):
        print(arr)
        op = ['+', '-', '*', '/']
        head = None
        current = head 
        for elem in arr:
            new = MathCalculations()
            if(elem in op):
                print(op, elem)
                new.operator = elem
            else: 
                new.value = elem
            if (not head):
                head = new
            else:
                print("tu")
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
                            print("tu")
                            while (found and temp):
                                print("tu2", head.display())

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
        return head

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % (self.value or self.operator)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % (self.value or self.operator)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % (self.value or self.operator)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % (self.value or self.operator)
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


def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value or node.operator)
        printTree(node.right, level + 1)
