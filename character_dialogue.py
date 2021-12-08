""" A system that handles character interactions and allows for intricate dialogue interaction trees. """

class Dialogue_System(object):
    def __init__(self):
        self.scenes = []  ## A list of all scenes loaded into the manager
        self.characters = []  # A list of all relevant characters who are in the current scene

    def add_scene(self, scene):
        self.scenes.append(scene)

    def remove_scene(self, scene):
        try:
            self.scenes.remove(scene)
        except ValueError:
            print ("Scene %s couldn't be removed, it doesn't exist!" % (scene))

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

class Scene(object):
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

class DialogueNode(object):
    def __init__(self, node_id = ""):
        self.text = ""  ## What the character is currently saying
        if node_id:  #Initialize a non-blank node id
            self.node_id = node_id
            self.load()
        elif node_id == "":  # Default
            self.node_id = -1  ## Defaults to -1 for an uninitialized Dialogue Nodule
        self.branches = {}  ## possible outcomes based on what you say linked to the node they bring you to

    def load(self):
        filename = "scenes/%s.txt" % (self.node_id)
        f = open(filename, mode='r')
        _data = ""
        for line in f:
            _data = _data+line
        #print ("data = %s" % (_data))
        self.set_text(_data)

    def set_text(self, words):
        for line in words:
            self.text = self.text+line

    def add_branch(self, response, outcome_node):
        self.branches[response] = outcome_node

    def print_text(self):
        print (self.text)

def test_1():
    dnode = DialogueNode(node_id="node-00-00-00-01")
    dnode.print_text()

if __name__ == "__main__":
    test_1()