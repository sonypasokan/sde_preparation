from input_reader import InputReader
from family_tree import FamilyTree

def main():
    file_content = InputReader().read_input()
    family = FamilyTree(male_name="Shan", female_name="Anga")
    family.add_relatives_from_file(file_content)

    # f.get_relative("Pjali", "son")
    # f.get_relative("Vasa", "siblings")
    # f.get_relative("Atya", "sister-in-law")
    # f.add_child("Aria", "female", "Chitra")
    # f.get_relative("Lavnya", "maternal-aunt")
    # f.get_relative("Aria", "siblings")
    # f.get_relative("Chika", "Paternal-uncle")
    # f.get_relative("Jaya", "brother-in-law")

if __name__ == "__main__":
    main()