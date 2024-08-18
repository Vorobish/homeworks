import inspect


class SomeClass:

    def __init__(self, attr):
        self.attribute_1 = attr

def introspection_info(obj):

    obj_class = SomeClass(obj)

    data = {}
    data.update({'type': type(obj).__name__})

    attrs = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if not callable(attr):
            attrs.append(attr_name)
    data.update({'attributes': attrs})

    methods = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if callable(attr):
            methods.append(attr_name)
    data.update({'methods': methods})

    module = ''
    if inspect.getmodule(obj):
        module = inspect.getmodule(obj)
    else:
        module = inspect.getmodule(obj_class)
    data.update({'module': module.__name__})

    return data

number_info = introspection_info(42)
print(number_info)
