class parent:
    def parent(self):
        print("one")

class child(parent):
    def child(self):
        print("two")
        super().parent()

obj=child()
obj.child()
