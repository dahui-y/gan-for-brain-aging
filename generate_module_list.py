from modulefinder import ModuleFinder
import pkg_resources
import pkgutil
import sys

# Create a ModuleFinder instance
f = ModuleFinder()

# Run the main script
f.run_script('run.py')

# Get names of all the imported modules
names = list(f.modules.keys())

# Get a sorted list of the root modules imported
basemods = sorted(set([name.split('.')[0] for name in names]))

# Function to check if a module is built-in
def is_builtin_module(module_name):
    return module_name in sys.builtin_module_names or module_name.startswith('_')

# Write the list of packages and their versions to a requirements file
with open('requirements.txt', 'w') as req_file:
    for mod in basemods:
        if is_builtin_module(mod):
            continue
        try:
            version = pkg_resources.get_distribution(mod).version
            req_file.write("{}=={}\n".format(mod, version))
        except pkg_resources.DistributionNotFound:
            req_file.write("{}\n".format(mod))





# from modulefinder import ModuleFinder

# # Create a ModuleFinder instance
# f = ModuleFinder()

# # Run the main script
# f.run_script('C:\\Users\\c2062183\\OneDrive - Newcastle University\\PhD\\Research\\GAN for Brain\\BrainAgeing-master\\BrainAgeing-master\\run.py')


# # Get names of all the imported modules
# names = list(f.modules.keys())

# # Get a sorted list of the root modules imported
# basemods = sorted(set([name.split('.')[0] for name in names]))

# # Write the list of packages to a requirements file
# with open('requirements.txt', 'w') as req_file:
#     for mod in basemods:
#         req_file.write("{}\n".format(mod))

# print("requirements.txt file created with the following packages:")
# print("\n".join(basemods))
