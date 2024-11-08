class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join([f' {prop}="{self.props[prop]}"' for prop in self.props])

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def get_children(self):
        return self.children

    def get_tag(self):
        return self.tag

    def get_value(self):
        return self.value

    def get_props(self):
        return self.props

    def set_children(self, children):
        self.children = children

    def set_tag(self, tag):
        self.tag = tag

    def set_value(self, value):
        self.value = value

    def set_props(self, props):
        self.props = props


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def __str__(self):
        return f"{self.tag}: {self.value}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

    def __str__(self):
        return f"{self.tag}: {self.children}"

    def add_child(self, child):
        if self.children is None:
            self.children = []
        self.children.append(child)

    def remove_child(self, child):
        if self.children is None:
            return
        self.children.remove(child)

    def get_children(self):
        return self.children

    def set_children(self, children):
        self.children = children

    def get_child(self, index):
        return self.children[index]
    
    def get_child_count(self):
        return len(self.children)

    def get_child_index(self, child):
        return self.children.index(child)
    
    def replace_child(self, index, child):
        self.children[index] = child

    def insert_child(self, index, child):
        self.children.insert(index, child)

    def append_child(self, child):
        self.children.append(child)

    def prepend_child(self, child):
        self.children.insert(0, child)

