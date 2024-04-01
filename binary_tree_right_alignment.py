class Node:
    root = None

    def __init__(self):
        self.root

    def insert(self, key, root=""):
        if root == "":
            root = self.root
        if root is None:
            polozka = {
                'left': None,
                'right': None,
                'val': key
            }
            if self.root == None:
                self.root = polozka
            return polozka

        else:
            if root['val'] < key:
                root['right'] = self.insert(key, root['right'])
                print("prava" + str(key))
                return root
            else:
                root['left'] = self.insert(key, root['left'])
                print("leva" + str(key))
                return root

    def root_value(self):
        if self.root != None:
            return self.root['val']
        else:
            return "strom je prazdny"

    def reverse_inorder(self, root=""):
        if root == "":
            root = self.root
        if root:
            self.reverse_inorder(root['right'])
            print(root['val'])
            self.reverse_inorder(root['left'])


node = Node()
node.insert(5)
node.insert(3)
node.insert(7)
node.insert(4)
node.reverse_inorder()
