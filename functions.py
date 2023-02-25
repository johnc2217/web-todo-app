FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of
    to-do items.
    """
    with open(filepath, "r") as file_read:
        todos_read = file_read.readlines()
    return todos_read


def write_todos(todos_write, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file_write:
        file_write.writelines(todos_write)


if __name__ == "__main__":
    print(get_todos())
