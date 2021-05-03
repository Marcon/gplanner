from typing import Optional, Callable, Dict, Any, List, Tuple

import splitter.splitter as splitter_module
import splitter.planar as planar_module
import splitter.coupler as coupler_module
from .coupler import *
from .planar import RootItem
from .splitter import TITLE_COLUMN
import json


class SplitterJSONEncoder(json.JSONEncoder):
    def default(self, obj: AbstractSplitterItem):
        if issubclass(type(obj), AbstractSplitterItem):
            return {
                'type': type(obj).__name__,
                'fiber_length': obj.fiber_length,
                'title': obj.text(TITLE_COLUMN),
                'childs': [obj.child(i) for i in range(obj.childCount())]
            }


class SplitterJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if 'type' not in obj or 'childs' not in obj or 'fiber_length' not in obj:
            return obj
        class_ = None
        for mod in [splitter_module, planar_module, coupler_module]:
            try:
                class_ = getattr(mod, obj['type'])
            except AttributeError:
                continue
            break

        if not class_:
            return obj

        if class_ is RootItem:
            result = class_()
        elif class_ is Drop:
            result = class_(parent=None, title=obj['title'], att=0.0)
        else:
            result = class_(parent=None, fiber_length=obj['fiber_length'])

        if class_.__name__.startswith('Coupler'):
            drop = None
            line = None
            for child in obj['childs']:
                child.parent = result
                if child.text(TITLE_COLUMN) == 'Drop':
                    drop = child
                else:
                    line = child
            drop.set_attenuation(result.drop_att)
            line.set_attenuation(result.line_att)
            result.takeChildren()

            result.add_child(drop)
            result.add_child(line)
            return result

        for child in obj['childs']:
            result.add_child(child)

        return result

