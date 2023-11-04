#!/usr/bin/python3

import importlib
module = importlib.import_module('variable_load_5', package=None)
a_value = getattr(module, 'a')
print(a_value)
