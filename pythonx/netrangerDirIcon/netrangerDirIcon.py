def node_highlight_content_l(node):
    if node.isDir:
        if node.expanded:
            return '📂', 46
        else:
            return '📁', 46
    else:
        return '', 0
