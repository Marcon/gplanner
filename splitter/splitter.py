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
import PySide2.QtWidgets
from PySide2.QtWidgets import QTreeWidgetItem

TITLE_COLUMN = 0
SIGNAL_ATT_COLUMN = 1
FIBER_LENGTH_COLUMN = 2
FREE_CONNECTORS_COLUMN = 3

FIBER_ATT = 0.36


class AbstractSplitterItem(QTreeWidgetItem):
    max_childs = 0
    is_root = False

    def __init__(self, parent=None, item_title='Undefined', splitter_att=0.0, fiber_length=0):
        super().__init__(parent, 0)
        self.parent = parent
        self.fiber_length = fiber_length
        self.splitter_att = splitter_att
        self.setText(TITLE_COLUMN, item_title)
        self.setText(SIGNAL_ATT_COLUMN, str(self.signal_attenuation()))
        self.setText(FIBER_LENGTH_COLUMN, str(self.fiber_length)+'km')
        self.update_free_connectors()

    def addChild(self, child):
        super().addChild(child)
        self.update_free_connectors()

    def removeChild(self, child):
        super().removeChild(child)
        self.update_free_connectors()

    def update_free_connectors(self):
        self.setText(FREE_CONNECTORS_COLUMN, str(self.get_free_connectors()))

    def get_free_connectors(self):
        return self.max_childs - self.childCount()

    def signal_attenuation(self):
        if self.parent is None:
            return - FIBER_ATT * self.fiber_length - self.splitter_att
        return self.parent.signal_attenuation() - FIBER_ATT * self.fiber_length - self.splitter_att


class ONU(AbstractSplitterItem):
    def __init__(self, parent, fiber_length):
        self.max_childs = 0
        super().__init__(parent, 'ONU', 0.0, fiber_length)

