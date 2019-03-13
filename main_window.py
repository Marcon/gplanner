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

TITLE_COLUMN = 0
SIGNAL_LOSS_COLUMN = 1


class AbstractTreeItem(QTreeWidgetItem):
    def __init__(self, parent=None, item_title='Undefined', signal_loss=0.0):
        super().__init__(parent, 0)
        self.parent = parent
        self.max_childs = 0
        self.is_root = False
        self.signal_loss = signal_loss
        self.setText(TITLE_COLUMN, item_title)
        self.setText(SIGNAL_LOSS_COLUMN, str(self.child_signal_loss()))

    def child_signal_loss(self):
        if self.parent is None:
            return self.signal_loss
        return self.parent.child_signal_loss()-self.signal_loss


class RootItem(AbstractTreeItem):
    def __init__(self):
        super().__init__(None, 'Root', 0.0)
        self.is_root = True
        self.max_childs = 1


class Splitter1x2(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x2', 4.3)
        self.max_childs = 2


class Splitter1x3(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x3', 6.2)
        self.max_childs = 3


class Splitter1x4(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x4', 7.4)
        self.max_childs = 4


class Splitter1x6(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x6', 9.5)
        self.max_childs = 6


class Splitter1x8(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x8', 10.7)
        self.max_childs = 8


class Splitter1x12(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x12', 12.5)
        self.max_childs = 12


class Splitter1x16(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x16', 13.9)
        self.max_childs = 16


class Splitter1x24(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x24', 16.0)
        self.max_childs = 24


class Splitter1x32(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x32', 17.2)
        self.max_childs = 32


class Splitter1x64(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x64', 21.5)
        self.max_childs = 64


class Splitter1x128(AbstractTreeItem):

    def __init__(self, parent):
        super().__init__(parent, '1x128', 25.5)
        self.max_childs = 128


class TreeItem(QTreeWidgetItem):

    def __init__(self, parent=None, item_title='Undefined', signal_loss='0'):
        super().__init__(parent, 0)
        self.setText(TITLE_COLUMN, item_title)
        self.setText(SIGNAL_LOSS_COLUMN, signal_loss)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tree_widget = self.ui.treeWidget
        self.init_tree()

    def init_tree(self):
        self.tree_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree_widget.setColumnCount(2)
        self.tree_widget.setHeaderLabels(['Title', 'Signal Loss'])
        self.tree_widget.addTopLevelItem(RootItem())
        self.tree_widget.connect(SIGNAL('customContextMenuRequested(QPoint)'), self.on_custom_menu_requested)

    @staticmethod
    def _can_add_childs(item):
        return item.childCount() < item.max_childs

    def on_custom_menu_requested(self, point):
        item = self.tree_widget.itemAt(point)
        if item is None:
            return

        menu = QMenu(self)
        if self._can_add_childs(item):
            add_default_splitter_menu = menu.addMenu('Add planar splitter')

            add_1_to_2_splitter_act = QAction('Add 1x2 splitter')
            add_1_to_2_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x2))
            add_default_splitter_menu.addAction(add_1_to_2_splitter_act)

            add_1_to_3_splitter_act = QAction('Add 1x3 splitter')
            add_1_to_3_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x3))
            add_default_splitter_menu.addAction(add_1_to_3_splitter_act)

            add_1_to_4_splitter_act = QAction('Add 1x4 splitter')
            add_1_to_4_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x4))
            add_default_splitter_menu.addAction(add_1_to_4_splitter_act)

            add_1_to_6_splitter_act = QAction('Add 1x6 splitter')
            add_1_to_6_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x6))
            add_default_splitter_menu.addAction(add_1_to_6_splitter_act)

            add_1_to_8_splitter_act = QAction('Add 1x8 splitter')
            add_1_to_8_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x8))
            add_default_splitter_menu.addAction(add_1_to_8_splitter_act)

            add_1_to_12_splitter_act = QAction('Add 1x12 splitter')
            add_1_to_12_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x12))
            add_default_splitter_menu.addAction(add_1_to_12_splitter_act)

            add_1_to_16_splitter_act = QAction('Add 1x16 splitter')
            add_1_to_16_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x16))
            add_default_splitter_menu.addAction(add_1_to_16_splitter_act)

            add_1_to_24_splitter_act = QAction('Add 1x24 splitter')
            add_1_to_24_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x24))
            add_default_splitter_menu.addAction(add_1_to_24_splitter_act)

            add_1_to_32_splitter_act = QAction('Add 1x32 splitter')
            add_1_to_32_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x32))
            add_default_splitter_menu.addAction(add_1_to_32_splitter_act)

            add_1_to_64_splitter_act = QAction('Add 1x64 splitter')
            add_1_to_64_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x64))
            add_default_splitter_menu.addAction(add_1_to_64_splitter_act)

            add_1_to_128_splitter_act = QAction('Add 1x128 splitter')
            add_1_to_128_splitter_act.triggered.connect(lambda: self.on_add_splitter(item, Splitter1x128))
            add_default_splitter_menu.addAction(add_1_to_128_splitter_act)

            add_percent_splitter_menu = menu.addMenu('Add percent splitter')
            add_50_to_50_splitter_act = QAction('Add 50/50 splitter')
            add_percent_splitter_menu.addAction(add_50_to_50_splitter_act)
            add_45_to_55_splitter_act = QAction('Add 45/55 splitter')
            add_percent_splitter_menu.addAction(add_45_to_55_splitter_act)
            add_40_to_60_splitter_act = QAction('Add 40/60 splitter')
            add_percent_splitter_menu.addAction(add_40_to_60_splitter_act)
            add_35_to_65_splitter_act = QAction('Add 35/65 splitter')
            add_percent_splitter_menu.addAction(add_35_to_65_splitter_act)
            add_30_to_70_splitter_act = QAction('Add 30/70 splitter')
            add_percent_splitter_menu.addAction(add_30_to_70_splitter_act)
            add_25_to_75_splitter_act = QAction('Add 25/75 splitter')
            add_percent_splitter_menu.addAction(add_25_to_75_splitter_act)
            add_20_to_80_splitter_act = QAction('Add 20/80 splitter')
            add_percent_splitter_menu.addAction(add_20_to_80_splitter_act)
            add_15_to_85_splitter_act = QAction('Add 15/85 splitter')
            add_percent_splitter_menu.addAction(add_15_to_85_splitter_act)
            add_10_to_90_splitter_act = QAction('Add 10/90 splitter')
            add_percent_splitter_menu.addAction(add_10_to_90_splitter_act)
            add_5_to_95_splitter_act = QAction('Add 5/95 splitter')
            add_percent_splitter_menu.addAction(add_5_to_95_splitter_act)

        if not item.is_root:
            add_onu_act = QAction('Add ONU')
            remove_act = QAction('Remove')
            menu.addAction(add_onu_act)
            menu.addAction(remove_act)

        # test_act = QAction('Test')
        # test_act.triggered.connect(lambda: self.on_context_action(item, 1))
        # menu.addAction(test_act)
        menu.exec_(self.ui.treeWidget.viewport().mapToGlobal(point))

    def on_context_action(self, item, action_type=0):

        new_item = TreeItem(item, 'Child', '10')
        item.addChild(new_item)
        item.setExpanded(True)

    @staticmethod
    def on_add_splitter(item, splitter_cls):
        item.addChild(splitter_cls(item))
        item.setExpanded(True)
