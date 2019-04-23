from .global_objs import Global
from anytree import Node


class Rule():
    def __init__(self, name):
        # List of paths you can take from here, i.e. the RHS of
        # the rule, e.g. LHS of X -> Y | Z is ['Y', 'Z']
        self.RHS = []
        self.name = name

        # Memoization
        self.mem = {}

    def add_choice(self, obj_list):
        """Add a choice to the list of paths the rule can choose from.

        obj_list (list of str): The names of the code objects that
                                    must be available to go this path
        """
        self.RHS.append(obj_list)

    def check(self, parent_node):
        """Checks if this rule can be applied next by trying all its paths."""
        org_cursor = Global.cursor
        if org_cursor in self.mem:
            Global.cursor = self.mem[org_cursor][1]
            if self.mem[org_cursor][0]:
                self.mem[org_cursor][2].parent = parent_node
            return self.mem[org_cursor][0]
        
        for choice in self.RHS:
            success = True
            cur_node = Node('%s_%s' % (self.name, Global.cursor))
            for code_obj in choice:
                if not (code_obj == 'NULL' or Global.code_objs[code_obj].check(cur_node)):
                    success = False
                    break
            if success:
                cur_node.parent = parent_node
                # Memoize that it succeeded and the save the
                # new cursor and the tree node
                self.mem[org_cursor] = [True, Global.cursor, cur_node]
                return True
            Global.cursor = org_cursor
        
        # Memoize that it failed and the cursor didn't change
        self.mem[org_cursor] = [False, org_cursor]
        return False
