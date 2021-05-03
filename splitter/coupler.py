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

from .splitter import AbstractSplitterItem


class Drop(AbstractSplitterItem):
    max_childs = 1

    def __init__(self, parent, title, att):
        super().__init__(parent, title, att, 0.0)


class Coupler(AbstractSplitterItem):
    max_childs = 2
    line_att = 0.0
    drop_att = 0.0

    def __init__(self, parent, title, fiber_length):
        super().__init__(parent, title, 0.0, fiber_length)
        self.add_drops()

    def add_drops(self):
        self.add_child(Drop(self, 'Drop', self.drop_att))
        self.add_child(Drop(self, 'Line', self.line_att))
        self.setExpanded(True)


class Coupler50x50(Coupler):

    drop_att = 3.17
    line_att = 3.19

    def __init__(self, parent, fiber_length):
        super().__init__(parent, 'Coupler 50/50', fiber_length)


class Coupler45x55(Coupler):

    drop_att = 3.73
    line_att = 2.71

    def __init__(self, parent, fiber_length):
        super().__init__(parent, 'Coupler 45/55', fiber_length)


class Coupler40x60(Coupler):

    drop_att = 4.01
    line_att = 2.34

    def __init__(self, parent, fiber_length):
        super().__init__(parent, 'Coupler 40/60', fiber_length)


class Coupler35x65(Coupler):

    drop_att = 4.56
    line_att = 1.93

    def __init__(self, parent, fiber_length):
        super().__init__(parent, 'Coupler 35/65', fiber_length)


class Coupler30x70(Coupler):

    drop_att = 5.39
    line_att = 1.56

    def __init__(self, parent, fiber_length):
        super().__init__(parent, 'Coupler 30/70', fiber_length)


class Coupler25x75(Coupler):

    drop_att = 6.29
    line_att = 1.42

    def __init__(self, parent, fiber_length):
        super().__init__(parent, 'Coupler 25/75', fiber_length)


class Coupler20x80(Coupler):

    drop_att = 7.11
    line_att = 1.06

    def __init__(self, parent, fiber_length):
        super().__init__(parent, 'Coupler 20/80', fiber_length)


class Coupler15x85(Coupler):

    drop_att = 8.16
    line_att = 0.76

    def __init__(self, parent, fiber_length):
        super().__init__(parent, 'Coupler 15/85', fiber_length)


class Coupler10x90(Coupler):

    drop_att = 10.08
    line_att = 0.49

    def __init__(self, parent, fiber_length):
        super().__init__(parent, 'Coupler 10/90', fiber_length)


class Coupler5x95(Coupler):

    drop_att = 13.70
    line_att = 0.32

    def __init__(self, parent, fiber_length):
        super().__init__(parent, 'Coupler 5/95', fiber_length)
