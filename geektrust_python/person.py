class Person(object):
    """Person node which holds the fields of a person."""

    def __init__(self, name):
        """Constructor of the class.
        @name : Name of the person. This is a mandatory field for every person.
        """
        self.name = name
        self.mother = None
        self.spouse = None
    
    def get_siblings(self, sibling_gender=None):
        """Function that will return the siblings list based on the gender given.
        @sibling_gender : Gender of the sibling. If not provided, then all siblings irrespective
            of gender will be returned in a list. Only Male and Female classes are accepted here.
        """
        if not self.mother: # This can happen for the head nodes (King and spouse)
            return []
        siblings_names = list()
        for child in self.mother.children:
            if self == child: # Current object is excluded.
                continue
            if sibling_gender != None and not isinstance(child, sibling_gender):
                continue
            siblings_names.append(child)
        return siblings_names
    
    def get_parents_siblings(self, parent_gender, sibling_gender):
        """Function that gets siblings list for the given parent type.
        @parent_gender : Type of parent. For mother, Female class has to be provided,
            whereas for father Male class needs to be provided.
        @sibling_gender : Gender of the sibling has to be provided as 
            Male class or Female class.
        """
        if not self.mother:
            return
        if isinstance(self.mother, parent_gender):
            parent = self.mother
        else:
            parent = self.mother.spouse
        if not parent:
            return
        parents_siblings = parent.get_siblings(sibling_gender)
        return parents_siblings

    def get_siblings_in_law(self, in_law_gender):
        """Function to get the list of siblings-in-law.
        @in_law_gender : Gender of the in-law. This is accepter as Male or Female class.
        """
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
    """Subclass of person who is male."""

    def __init__(self, name):
        """Constructor.
        @name : Name of the person.
        """
        super().__init__(name)
    
    def get_child_by_gender(self, child_gender):
        """Function to get the child by gender.
        @child_gender : Gender of child which is accepted as Male or Female class.
        """
        if not self.spouse:
            return
        return self.spouse.get_child_by_gender(child_gender)


class Female(Person):
    """Subclass of person who is a female."""
    
    def __init__(self, name):
        """Constructor.
        @name : Name of the person which is passed to the parent class.
        """
        super().__init__(name)
        self.children = list()
    
    def add_child(self, child):
        """Function to add child to a mother.
        @child : Child object
        """
        self.children.append(child)
    
    def get_child_by_gender(self, child_gender):
        """Function to get children with given .
        @child_gender : Gender of child which is accepted as Male or Female class.
        """
        kids_of_gender = list()
        for child in self.children:
            if isinstance(child, child_gender):
                kids_of_gender.append(child.name)
        return kids_of_gender