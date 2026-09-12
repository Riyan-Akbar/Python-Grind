class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data == None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def InOrderChicken(self,r):
        if r is None:
            return
        else:
            self.InOrderChicken(r.left)
            print(r.data, end = " ")
            self.InOrderChicken(r.right)

    def PreOrderChicken(self,r):
            if r is None:
                return
            else:
                print(r.data, end = " ")
                self.PreOrderChicken(r.left)
                self.PreOrderChicken(r.right)

    def PostOrderChicken(self,r):
                if r is None:
                    return
                else:
                    self.PostOrderChicken(r.left)
                    self.PostOrderChicken(r.right)
                    print(r.data, end = " ")


if __name__ == '__main__':
    root = Node('g')
    root.insert('a')
    root.insert('k')
    root.insert('r')
    root.insert('e')
    root.insert('s')
    root.insert('y')
    root.insert('h')
    root.insert('d')
    root.insert('v')

    root.InOrderChicken(root)
    print()
    root.PreOrderChicken(root)
    print()
    root.PostOrderChicken(root)