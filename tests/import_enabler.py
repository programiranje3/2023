#%%
# Enable import from my_module.py. Based on https://stackoverflow.com/a/35273613/1899061.
# Putting my_module.py in the root directory (without this cell) used to work, but then suddenly stopped working.
import os
import sys
my_module_path = os.path.abspath(os.path.join('..'))
if my_module_path not in sys.path:
    sys.path.append(my_module_path)


#%%
