import fnmatch
import os


def find(pattern, path):
    """Responsible for finding files given a path an a regex

    :param pattern: A regex for the fnmatch() function. Generally the file extension.
    :param path: A path to search for files
    :returns: A list containing the files found

    """

    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

