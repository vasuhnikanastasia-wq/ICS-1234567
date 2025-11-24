class Tree:
    species="Plant"
    def __init__(self, age): 
        self.age = int(age) 
    
    def grow(self, years):
        self.age += years
        print(f"Дерево підросло на {years} років. Новий вік: {self.age}")
        
    def display_species(self): 
        print(f"Це дерево належить до виду: {Tree.species}")

class Cherry(Tree):

    def __init__(self, age, variety): 
        super().__init__(age) 
        self.variety = str(variety) 
        self.has_cherries = False
        
    def set_harvest_status(self, has_cherries): 
        self.has_cherries = has_cherries
        if self.has_cherries:
            print("На вишневому дереві є ягоди!")
        else:
            print("Вишневе дерево без ягід.")

    def display_info(self): 
        print(f"Вишневе дерево: {self.variety} (Вік: {self.age} років). Плодоносить: {'Так' if self.has_cherries else 'Ні'}")