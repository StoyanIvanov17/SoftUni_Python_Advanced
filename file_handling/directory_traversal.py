import os


def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

#                          *** THIS IS BETTER OPTIMIZED ***
            extensions[extension] = extensions.get(extension, []) + [filename]

#                                 *** THAN THIS ***
#                         if extension not in extensions:
#                             extensions[extension] = []
#                         extensions[extension].append(filename)

        elif os.path.isdir(file):
            save_extensions(file)


directory = input()
extensions = {}
save_extensions(directory)
