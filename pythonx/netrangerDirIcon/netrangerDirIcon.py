class NETRDirIcon(object):
    def __init__(self, api):
        self.api = api

    def node_highlight_content_l(self, node):
        if node.isDir:
            if node.expanded:
                return '📂', 46
            else:
                return '📁', 46
        else:
            return '', 0
