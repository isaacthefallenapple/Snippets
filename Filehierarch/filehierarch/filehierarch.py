import pathlib


def filehierarch(dir, depth=0):
    dir = pathlib.Path(dir)
    if depth == 0:
        print(dir.name)
        print("\\")
        for sub_dir in dir.iterdir():
            filehierarch(sub_dir, depth + 1)
            print("|")
    else:
        tree_list = []
        for d in range(depth):
            tree_list.append("| ")
        tree_string = "".join(tree_list)
        if dir.is_dir():
            if list(dir.glob("*")):
                print(tree_string + dir.name)
                print(tree_string + "\\")
            else:
                print(tree_string + dir.name + "/")
            for sub_dir in dir.iterdir():
                filehierarch(sub_dir, depth + 1)
        else:
            print("".join(tree_list) + dir.name)

