class Father:
    def skill(self):
        print("Fathers skill:gardening")

class Mother:
    def talent(self):
        print("Mothers talent: singing")

class Child(Father,Mother):
    def ability(self):
        print("Childs ability:Painting")

child = Child()
child.skill()
child.talent()
child.ability()