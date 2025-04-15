class Father:
    def skill(self):
        print("hey!")

class Mother:
    def talent(self):
        print("Mothers talent: singing")

class Child(Father,Mother):
    def ability(self):
        print("Childs ability:crying ")

child = Child()
child.skill()
child.talent()
child.ability()
