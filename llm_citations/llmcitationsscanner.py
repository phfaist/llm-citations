
from pylatexenc.latexnodes.nodes import LatexNodesVisitor


class CitationsScanner(LatexNodesVisitor):
    def __init__(self):
        super().__init__()
        self.encountered_citations = []

    def get_encountered_citations(self):
        return self.encountered_citations

    # ---

    def visit_macro_node(self, node):
        if hasattr(node, 'llmarg_cite_items'):
            # it's a citation node with citations to track
            for cite_item in node.llmarg_cite_items:
                cite_prefix, cite_key = cite_item
                self.encountered_citations.append(
                    dict(
                        cite_prefix=cite_prefix,
                        cite_key=cite_key,
                        encountered_in=dict(
                            resource_info=node.latex_walker.resource_info,
                            what=f"{node.latex_walker.what} @ {node.pos}",
                        )
                    )
                )

        super().visit_macro_node(node)
