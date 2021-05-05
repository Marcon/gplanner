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
DESCRIPTION_COLUMN = 4

FIBER_ATT = 0.36


class AbstractSplitterItem(QTreeWidgetItem):
    max_childs = 0
    is_root = False

    def __init__(self, parent=None, item_title='Undefined', splitter_att=0.0, fiber_length=0):
        super().__init__(parent, 0)
        self.parent = parent
        self.fiber_length = 0
        self.splitter_att = 0.0
        self.description = ''
        self.setText(TITLE_COLUMN, item_title)
        self.setText(DESCRIPTION_COLUMN, '')
        self.set_attenuation(splitter_att)
        self.update_free_connectors()

    def set_description(self, description):
        self.setText(DESCRIPTION_COLUMN, description)

    def update_attenuation(self):
        self.setText(SIGNAL_ATT_COLUMN, "%.2f" % self.signal_attenuation())
        for i in range(self.childCount()):
            self.child(i).update_attenuation()

    def set_parent(self, parent):
        self.parent = parent
        self.update_attenuation()

    def set_attenuation(self, att):
        self.splitter_att = att
        self.update_attenuation()

    def set_fiber_length(self, length):
        self.fiber_length = length
        self.setText(FIBER_LENGTH_COLUMN, str(self.fiber_length) + 'km')

    def add_child(self, child):
        super().addChild(child)
        child.set_parent(self)
        self.update_free_connectors()

    def remove_child(self, child):
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

