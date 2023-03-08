class ToDoList:

    def __init__(self, name):
        self.id = None
        self.name = name
        self.tasks = []

    def setName(self, name) :
        self.name = name
