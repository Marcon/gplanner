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


class RootItem(AbstractSplitterItem):
    max_childs = 1
    is_root = True

    def __init__(self):
        super().__init__(None, 'OLT', 0.0)


class Splitter1x2(AbstractSplitterItem):
    max_childs = 2

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x2', 4.3, fiber_length)


class Splitter1x3(AbstractSplitterItem):
    max_childs = 3

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x3', 6.2, fiber_length)


class Splitter1x4(AbstractSplitterItem):
    max_childs = 4

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x4', 7.4, fiber_length)


class Splitter1x6(AbstractSplitterItem):
    max_childs = 6

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x6', 9.5, fiber_length)


class Splitter1x8(AbstractSplitterItem):

    max_childs = 8

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x8', 10.7, fiber_length)


class Splitter1x12(AbstractSplitterItem):

    max_childs = 12

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x12', 12.5, fiber_length)


class Splitter1x16(AbstractSplitterItem):

    max_childs = 16

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x16', 13.9, fiber_length)


class Splitter1x24(AbstractSplitterItem):
    max_childs = 24

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x24', 16.0, fiber_length)


class Splitter1x32(AbstractSplitterItem):
    max_childs = 32

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x32', 17.2, fiber_length)


class Splitter1x64(AbstractSplitterItem):
    max_childs = 64

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x64', 21.5, fiber_length)


class Splitter1x128(AbstractSplitterItem):
    max_childs = 128

    def __init__(self, parent, fiber_length):
        super().__init__(parent, '1x128', 25.5, fiber_length)
