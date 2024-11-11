import inspect


class Introspection:
    def __init__(self, obj):
        self.obj = obj

    def module_info(self) -> str:
        if inspect.getmodule(self) is None:
            return '__main__'
        else:
            str_module = str(inspect.getmodule(self)).split(' ')[1]
            return str_module

    def attr_info(self) -> list:
        list_attrs = []
        for attr in dir(self):
            if not callable(getattr(self, attr)):
                list_attrs.append(attr)
        return list_attrs

    def method_info(self) -> list:
        list_methods = []
        for method in dir(self):
            if callable(getattr(self, method)):
                list_methods.append(method)
        return list_methods


def introspection_info(obj) -> dict:
    obj_info = {}
    obj_info.update({'type': type(obj),
                     'module': Introspection.module_info(obj),
                     'methods': Introspection.method_info(obj),
                     'attributes': Introspection.attr_info(obj)})
    return obj_info


info_text = 'text'
info = introspection_info(info_text)
print(info)
print(introspection_info(Introspection))
