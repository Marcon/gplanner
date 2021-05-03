from .splitter import AbstractSplitterItem
import json


class SplitterJSONEncoder(json.JSONEncoder):
    def default(self, obj: AbstractSplitterItem):
        if issubclass(type(obj), AbstractSplitterItem):
            return {
                'type': type(obj).__name__,
                'fiber_length': obj.fiber_length,
                'childs': [obj.child(i) for i in range(obj.childCount())]
            }