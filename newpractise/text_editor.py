class Editor:
    def __init__(self) -> None:
        self.st_undo = [] 
        self.st_redo = [] # only inserted after we do undo
        self.text = []
        self.compliment = {
            self._insert: self._delete,
            self._delete: self._insert
        }

    def insert(self, char, pos=None):
        pos = len(self.text)
        self._insert(pos, char)

    def _insert(self, pos, char, undo_redo=False):
        if pos <= len(self.text):
            self.text.insert(pos, char)

            # if normal , we put in undo insert
            if not undo_redo:
                self.st_undo.append(
                    (self._insert, char, pos)
                )

                # when you insert, then there is no redo
                if len(self.st_redo) > 0:
                    self.st_redo.clear()

    def _delete(self, pos, char, undo_redo=False):
        if len(self.text) > 0 and pos >= 0:
            if pos >= len(self.text):
                pos = len(self.text)-1
            char = self.text.pop(pos)

            # if normal , we put in undo insert
            if not undo_redo:
                self.st_undo.append(
                    (self._delete, char, pos)
                )

                # when you delete, then there is no redo
                if len(self.st_redo) > 0:
                    self.st_redo.clear()
        

    def delete(self, pos=None, char=None):
        pos = len(self.text)-1
        self._delete(pos, char)

        

    def undo(self):
        if len(self.st_undo) > 0:
            action, char, pos = self.st_undo.pop()
            fn_compliment = self.compliment[action]
            
            fn_compliment(pos, char, True)

            # add in the redo stack after undo
            self.st_redo.append(
                (fn_compliment, char, pos)
            )

    def redo(self):
        if len(self.st_redo) > 0:
            action, char, pos = self.st_redo.pop()
            fn_compliment = self.compliment[action]
            
            fn_compliment(pos,char, True)
            
            # now add in the undo stack after redo
            self.st_undo.append(
                (action, char, pos)
            )

    def printString(self):
        print("".join(self.text))


editor = Editor()
# ed.insert("a")
# ed.insert("b")
# ed.insert("c")
# ed.insert("d")
# ed.print()
# ed.delete()
# ed.undo()
# ed.insert("e")
# ed.print()
# ed.delete()
# ed.print()

# Case 1:
editor.insert("a")
editor.insert("b")
editor.printString()
print("case1")

# Case 2:
editor = Editor()
editor.insert("a")
editor.insert("b")
editor.undo()
editor.printString()
print("case2")

# Case 3:
editor = Editor()
editor.insert("a")
editor.insert("b")
editor.undo()
editor.printString()
editor.redo()
editor.printString()
print("case3")

# Case 4:
editor = Editor()
editor.insert("a")
editor.insert("b")
editor.undo()
editor.redo()
editor.redo()
editor.printString()
print("case4")

# Case 5:
editor = Editor()
editor.insert("a")
editor.insert("b")
editor.insert("c")
editor.undo()
editor.undo()
editor.undo()
editor.redo()
editor.redo()
editor.redo()
editor.undo()
editor.undo()
editor.undo()
editor.redo()
editor.redo()
editor.redo()
editor.printString()
print("case5")