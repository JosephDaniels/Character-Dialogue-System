class StoryNode(object):
    def __init__(self):
        self.id = ""  # unique id for the node
        self.scene_name = "Scene Name"
        self.text = ""
        self.branches = []  # consists of tuples of ("Branch description text", a_story_node_id)
      