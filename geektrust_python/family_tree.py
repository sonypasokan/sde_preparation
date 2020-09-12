from person import Male, Female

class FamilyTree:

    def __init__(self, male_name, female_name):
        self.family_root = None
        self._start_family_tree(male_name, female_name)
        self._establish_family_tree()
    
    def add_relatives_from_file(self, file_content):
        for line in file_content:
            keywords = line.split()
            if not keywords:
                continue
            command = keywords[0].lower()
            if command == "get_relationship" and len(keywords) == 3:
                self.get_relative(keywords[1], keywords[2])
            elif command == "add_child" and len(keywords) == 4:
                child_added = self.add_child(keywords[1], keywords[2], keywords[3])
                if child_added:
                    print("CHILD_ADDITION_SUCCEEDED")
            else:
                print("WRONG_OPERATION")
        
    def _start_family_tree(self, male_name, female_name):
        male_person = Male(male_name)
        female_person = Female(female_name)
        male_person.spouse = female_person
        female_person.spouse = male_person
        self.family_root = male_person
    
    def _establish_family_tree(self):
        self.add_child("Anga", "Chit", "Male")
        self.add_child("Anga", "Ish", "Male")
        self.add_child("Anga", "Vich", "Male")
        self.add_child("Anga", "Aras", "Male")
        self.add_child("Anga", "Satya", "Female")
        self.add_spouse("Chit", "Amba")
        self.add_spouse("Vich", "Lika")
        self.add_spouse("Aras", "Chitra")
        self.add_spouse("Satya", "Vyan")
        self.add_child("Amba", "Dritha", "Female")
        self.add_child("Amba", "Tritha", "Female")
        self.add_child("Amba", "Vritha", "Male")
        self.add_child("Lika", "Vila", "Female")
        self.add_child("Lika", "Chika", "Female")
        self.add_child("Chitra", "Jnki", "Female")
        self.add_child("Chitra", "Ahit", "Male")
        self.add_child("Satya", "Asva", "Male")
        self.add_child("Satya", "Vyas", "Male")
        self.add_child("Satya", "Atya", "Female")
        self.add_spouse("Dritha", "Jaya")
        self.add_spouse("Jnki", "Arit")
        self.add_spouse("Asva", "Satvy")
        self.add_spouse("Vyas", "Krpi")
        self.add_child("Dritha", "Yodhan", "Male")
        self.add_child("Jnki", "Laki", "Male")
        self.add_child("Jnki", "Lavnya", "Female")
        self.add_child("Satvy", "Vasa", "Male")
        self.add_child("Krpi", "Kriya", "Male")
        self.add_child("Krpi", "Krithi", "Female")

    
    def add_spouse(self, person_name, spouse_name):
        person = self._find_person(self.family_root, person_name)
        if not person:
            print("PERSON_NOT_FOUND", spouse_name)
            return
        if isinstance(person, Male):
            spouse = self._create_child(spouse_name, "female")
        else:
            spouse = self._create_child(spouse_name, "male")
        person.spouse = spouse
        spouse.spouse = person
    
    def add_child(self, mother_name, child_name, child_gender):
        child = self._create_child(child_name, child_gender)
        mother = self._find_person(self.family_root, mother_name)
        if not mother:
            print("PERSON_NOT_FOUND")
            return
        if not isinstance(mother, Female):
            print("CHILD_ADDITION_FAILED")
            return
        child.mother = mother
        mother.add_child(child)
        return True
    
    def get_relative(self, person_name, relationship):
        person = self._find_person(self.family_root, person_name)
        if not person:
            print("PERSON_NOT_FOUND")
            return
        relationship = relationship.lower()
        if relationship == "son":
            relatives = person.get_child_by_gender(Male)
        elif relationship == "daughter":
            relatives = person.get_child_by_gender(Female)
        elif relationship == "siblings":
            relatives = person.get_siblings()
        elif relationship == "paternal-uncle":
            relatives = person.get_parents_siblings(parent_type=Male, sibling_gender=Male)
        elif relationship == "maternal-uncle":
            relatives = person.get_parents_siblings(parent_type=Female, sibling_gender=Male)
        elif relationship == "paternal-aunt":
            relatives = person.get_parents_siblings(parent_type=Male, sibling_gender=Female)
        elif relationship == "maternal-aunt":
            relatives = person.get_parents_siblings(parent_type=Female, sibling_gender=Female)
        elif relationship == "sister-in-law":
            relatives = person.get_siblings_in_law(Female)
        elif relationship == "brother-in-law":
            relatives = person.get_siblings_in_law(Male)
        if not relatives:
            print("NONE")
            return
        print(" ".join([relative.name for relative in relatives]))
    
    def _find_person(self, current_person, person_name_to_find, spouse_checked=False):
        if current_person.name == person_name_to_find:
            return current_person
        if current_person.spouse and not spouse_checked:
            person_found = self._find_person(current_person.spouse, person_name_to_find, True)
            if person_found:
                return person_found
        if isinstance(current_person, Male):
            return
        for child in current_person.children:
            person_found = self._find_person(child, person_name_to_find)
            if not person_found:
                continue
            return person_found    
    
    def _create_child(self, child_name, child_gender):
        if child_gender.lower() == "male":
            child = Male(child_name)
        elif child_gender.lower() == "female":
            child = Female(child_name)
        else:
            child = None
        return child