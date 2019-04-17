from src.parser import cursor, code_objs


class Rule():
    def __init__(self):
        # List of paths you can take from here, i.e. the RHS of
        # the rule, e.g. LHS of X -> Y | Z is ['Y', 'Z']
        self.RHS = []

    def add_choice(self, obj_list):
        """Add a choice to the list of paths the rule can choose from

        obj_list (list of str): The names of the code objects that
                                    must be available to go this path
        """
        self.RHS.append(obj_list)

    def check(self):
        """Checks if this rule can be applied next by trying all its paths"""
        for choice in self.RHS:
            org_cursor = cursor
            success = True
            for code_obj in choice:
                if code_objs[code_obj].check():
                    cursor += 1
                else:
                    success = False
                    break
            if success:
                return True
            cursor = org_cursor
        return False
