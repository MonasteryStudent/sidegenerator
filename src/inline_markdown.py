from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        splits = old_node.text.split(delimiter, 2)
        if len(splits) == 1:
            raise ValueError(f'invalid markdown syntax: "{delimiter}" not found')
        i = 0
        while i < 3:
            if splits[i] != '':
                if i == 0:
                    new_nodes.append(TextNode(splits[i], old_node.text_type))
                elif i == 1:
                    new_nodes.append(TextNode(splits[i], text_type))
                else:
                    new_splits = splits[i].split(delimiter, 2)
                    if len(new_splits) == 1:
                        new_nodes.append(TextNode(splits[i], old_node.text_type))
                    else:
                        splits = new_splits
                        i = -1
            i += 1
                    
    return new_nodes