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

from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui.main_window import MainWindowUI
from splitter.planar import *
from splitter.coupler import *
from splitter.splitter import ONU
from splitter.json import SplitterJSONEncoder, SplitterJSONDecoder

import json
import os

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

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.root_item = None
        self.save_path = None
        self.current_item = None
        self.ui = MainWindowUI(self)
        self.tree_widget = self.ui.tree_widget
        self.add_button = self.ui.add_splitter_button
        self.delete_button = self.ui.delete_splitter_button
        self.splitter_type_combo = self.ui.splitter_type_combo
        self.fiber_length_spin = self.ui.fiber_length_spin
        self.init_tree()
        self.init_splitter_type_spin()
        self.current_item = None

        self.add_button.clicked.connect(self.on_add_splitter)
        self.delete_button.clicked.connect(self.on_delete_splitter)
        self.ui.action_file_exit.triggered.connect(self.on_exit)
        self.ui.action_file_save.triggered.connect(self.on_save)
        self.ui.action_file_save_as.triggered.connect(self.on_save_as)
        self.ui.action_file_open.triggered.connect(self.on_open)

    def init_tree(self):
        self.root_item = RootItem()
        self.tree_widget.addTopLevelItem(self.root_item)
        self.tree_widget.currentItemChanged.connect(self.on_current_changed)

    def init_splitter_type_spin(self):
        for t in SPLITTER_TYPES:
            self.splitter_type_combo.addItem(t[0])

    @staticmethod
    def _can_add_childs(item):
        if item is None:
            return False
        return item.childCount() < item.max_childs

    def on_current_changed(self, current, previous):
        self.current_item = current
        self.delete_button.setEnabled(current is None or not current.is_root)
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

    def on_exit(self):
        self.app.quit()

    def on_save_as(self):
        save_path = QFileDialog.getSaveFileName(self, 'Select file to save', filter='GPlannerSave (*.gpsave)',
                                                options=QFileDialog.DontConfirmOverwrite)
        if not save_path[0]:
            return

        if os.path.isfile(save_path[0]):
            reply = QMessageBox.question(self, 'File already exists', 'Save file already exists. Overwrite?',
                                         QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.No:
                return
        self.save_path = save_path[0]
        self.save_data()

    def on_save(self):
        if not self.save_path:
            self.on_save_as()
        else:
            self.save_data()

    def on_open(self):
        open_path = QFileDialog.getOpenFileName(self, 'Select file to open', filter='GPlannerSave (*.gpsave)')
        if not open_path[0]:
            return

        self.save_path = open_path[0]
        self.load_data()

    def load_data(self):
        try:
            with open(self.save_path, 'r') as lf:
                obj = json.load(lf, cls=SplitterJSONDecoder)
                self.root_item = obj
                self.tree_widget.clear()
                self.tree_widget.addTopLevelItem(obj)
        except IOError as e:
            QMessageBox.critical(self, 'Error', 'Failed to load data: %s' % str(e))

    def save_data(self):
        try:
            with open(self.save_path, 'w') as sf:
                json.dump(self.root_item, sf, cls=SplitterJSONEncoder)
        except IOError as e:
            QMessageBox.critical(self, 'Error', 'Failed to save data: %s' % str(e))

