# definition_directive.py

from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.admonitions import Admonition
from docutils import nodes

class DefinitionDirective(Admonition):
    node_class = nodes.admonition

    def run(self):
        self.options['class'] = ['definition']
        (admonition_node,) = super().run()
        if self.arguments:
            title_text = 'Définition. '.join(self.arguments)
            admonition_node.insert(0, nodes.title(title_text, title_text))
        return [admonition_node]

def setup(app):
    app.add_directive("definition", DefinitionDirective)
