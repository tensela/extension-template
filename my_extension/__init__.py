"""My extension: an example of everything an extension can add to Tensela. Keep what you need, delete the rest.

    a node        Fold: a folded line, as in a folded plate roof (it computes, also in the process that computes)
    an action     Extensions → Count the nodes
    a menu entry  right click on a node → Add a Fold (a change to the project, that Ctrl+Z undoes)
    a panel       Extensions → My extension: the node chosen (it hears when the chosen node changes)
    an icon       fold.svg, on the card of the node and in the menus

Tensela calls register(tensela) when the extension is turned on, and unregister() (if there is one) when it is turned
off. Everything it added goes away by itself. The texts are written in English and translated in extension.toml.
"""
import numpy as np

from tensela.data import Data
from tensela.geometry import POINT, curve_by_points
from tensela.language import tr
from tensela.nodes import Input


def fold(length, folds, rise, name=None):
    """The node's function: its inputs by name, and `name` (the node's). It gives a Data (here, a curve)."""
    folds = max(1, int(folds))
    x = np.linspace(0.0, float(length), 2 * folds + 1)
    z = np.where(np.arange(x.size) % 2 == 1, float(rise), 0.0)
    points = Data(np.column_stack([x, np.zeros_like(x), z]), ("point",), kind=POINT)
    return curve_by_points(points, along="point", smooth=False, name=name)


def count_nodes(window):
    """An action: it receives the window, and does something once (it is not turned on or off). Say what it did
    where it is seen: here a small message; for something less important, window.statusBar().showMessage(…)."""
    from PySide6.QtWidgets import QMessageBox
    n = len(window.project.graph.nodes) if window.project is not None else 0
    QMessageBox.information(window, tr("My extension"), tr("The project has {n} nodes.").format(n=n))


def add_fold(window, node):
    """A menu entry on a node: it receives the window and the node's name. To change the project, the window's
    edit_project: your function changes a copy, and the copy takes its place as one step that Ctrl+Z undoes."""
    def change(project):
        new = project.graph.node("Fold", None, length=10, folds=4, rise=1)
        project.export.append(new.name)
    window.edit_project(change, tr("A Fold node"))


class Chosen:
    """The panel: what the node chosen is (it hears the window: tensela.on("selected", …))."""
    label = None


def panel(window):
    from PySide6.QtCore import Qt
    from PySide6.QtWidgets import QLabel
    Chosen.label = QLabel(tr("No node chosen."))
    Chosen.label.setWordWrap(True)
    Chosen.label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
    return Chosen.label


def selected(window, node):
    if Chosen.label is None:
        return
    if node is None or window.project is None or node not in window.project.graph.nodes:
        Chosen.label.setText(tr("No node chosen."))
    else:
        kind = window.project.graph.nodes[node].kind.name
        Chosen.label.setText(tr("Chosen: {node} ({kind}).").format(node=node, kind=tr(kind)))


def register(tensela):
    tensela.icon("fold", "my_extension/fold.svg")
    tensela.node("Fold", "Curves", (Input("length", 12.0, single=True), Input("folds", 4, single=True),
                                    Input("rise", 1.2, single=True)), "fold", fold,
                 "A folded line, as in a folded plate roof: its length, how many folds and how high.", icon="fold")
    tensela.action("Count the nodes", count_nodes, "How many nodes the project has", icon="fold")
    tensela.menu("node", "Add a Fold", add_fold, "A new Fold node, seen in 3D (Ctrl+Z undoes it)", icon="fold")
    tensela.panel("My extension: the node chosen", panel)
    tensela.on("selected", selected)


def unregister():
    Chosen.label = None
