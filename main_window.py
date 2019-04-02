#     Copyright (c) 2019 Evgeniy Dolgikh <marcon@atsy.su>
#     This file is part of gplanner.
#
#     gplanner is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     gplanner is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with gplanner.  If not, see <https://www.gnu.org/licenses/>.

from PySide2.QtWidgets import QMainWindow, QTreeWidgetItem, QMenu, QAction
from PySide2.QtCore import Qt, SLOT, SIGNAL
from ui.main_window import Ui_MainWindow
from splitter.planar import *
from splitter.coupler import *
from splitter.splitter import ONU

SPLITTER_TYPES = (
    ('Planar 1x2', Splitter1x2),
    ('Planar 1x3', Splitter1x3),
    ('Planar 1x4', Splitter1x4),
    ('Planar 1x6', Splitter1x6),
    ('Planar 1x8', Splitter1x8),
    ('Planar 1x12', Splitter1x12),
    ('Planar 1x16', Splitter1x16),
    ('Planar 1x24', Splitter1x24),
    ('Planar 1x32', Splitter1x32),
    ('Planar 1x64', Splitter1x64),
    ('Planar 1x128', Splitter1x128),
    ('Coupler 50/50', Coupler50x50),
    ('Coupler 45/55', Coupler45x55),
    ('Coupler 40/60', Coupler40x60),
    ('Coupler 35/65', Coupler35x65),
    ('Coupler 30/70', Coupler30x70),
    ('Coupler 25/75', Coupler25x75),
    ('Coupler 20/80', Coupler20x80),
    ('Coupler 15/85', Coupler15x85),
    ('Coupler 10/90', Coupler10x90),
    ('Coupler 5/95', Coupler5x95),
    ('ONU', ONU),
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tree_widget = self.ui.treeWidget
        self.add_button = self.ui.addSplitterButton
        self.delete_button = self.ui.deleteSplitterButton
        self.splitter_type_combo = self.ui.splitterTypeCombo
        self.fiber_length_spin = self.ui.fiberLengthSpin
        self.init_tree()
        self.init_splitter_type_spin()
        self.current_item = None

        self.add_button.clicked.connect(self.on_add_splitter)
        self.delete_button.clicked.connect(self.on_delete_splitter)

    def init_tree(self):
        self.tree_widget.addTopLevelItem(RootItem())
        self.tree_widget.currentItemChanged.connect(self.on_current_changed)

    def init_splitter_type_spin(self):
        for t in SPLITTER_TYPES:
            self.splitter_type_combo.addItem(t[0])

    @staticmethod
    def _can_add_childs(item):
        return item.childCount() < item.max_childs

    def on_current_changed(self, current, previous):
        self.current_item = current
        self.delete_button.setEnabled(not current.is_root)
        self.add_button.setEnabled(self._can_add_childs(current))

    def on_add_splitter(self):
        if self.current_item is None:
            return
        child = SPLITTER_TYPES[self.splitter_type_combo.currentIndex()][1](self.current_item,
                                                                           self.fiber_length_spin.value())
        self.current_item.addChild(child)
        self.current_item.setExpanded(True)

    def on_delete_splitter(self):
        parent = self.current_item.parent
        self.current_item.parent = None
        parent.removeChild(self.current_item)
