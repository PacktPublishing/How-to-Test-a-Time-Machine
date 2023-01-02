'''
  Class to represent a node
'''
class NodeClass:
    """ Class to represent a node"""
    url=""
    window_handle=""
    actions={}
    acted=[]
    count=-1
    def __init__(self, url):
        self.url = url
    def add_handle(self, window_handle):
        """method to add a handle to the node"""
        self.window_handle = window_handle
