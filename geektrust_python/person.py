
class Person(object):

    def __init__(self, name):
        self.name = name
        self.mother = None
        self.spouse = None
    
    def get_siblings(self, sibling_gender=None):
        if not self.mother:
            return []
        siblings_names = list()
        for child in self.mother.children:
            if self == child:
                continue
            if sibling_gender != None and not isinstance(child, sibling_gender):
                continue
            siblings_names.append(child)
        return siblings_names
    
    def get_parents_siblings(self, parent_type, sibling_gender):
        if not self.mother:
            return
        if isinstance(self.mother, parent_type):
            parent = self.mother
        else:
            parent = self.mother.spouse
        if not parent:
            return
        parents_siblings = parent.get_siblings(sibling_gender)
        return parents_siblings

    def get_siblings_in_law(self, in_law_gender):
        siblings_in_law = list()
        spouse = self.spouse
        if spouse:
            siblings_in_law += spouse.get_siblings(in_law_gender)
        siblings = self.get_siblings()
        for sibling in siblings:
            if sibling not in siblings_in_law and sibling.spouse:
                siblings_in_law.append(sibling.spouse)
        return siblings_in_law
        
    



class Male(Person):

    def __init__(self, name):
        super().__init__(name)
    
    def get_child_by_gender(self, GenderClass):
        if not self.spouse:
            return
        return self.spouse.get_child_by_gender(GenderClass)


class Female(Person):
    
    def __init__(self, name):
        super().__init__(name)
        self.children = list()
    
    def add_child(self, child):
        self.children.append(child)
    
    def get_child_by_gender(self, GenderClass):
        kids_of_gender = list()
        for child in self.children:
            if isinstance(child, GenderClass):
                kids_of_gender.append(child.name)
        return kids_of_gender