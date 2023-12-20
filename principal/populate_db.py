def read_file_and_create_objects(file_path, object_class, object_attributes, regex="|"):
    """
    Read a file and create objects based on the contents of the file.

    Args:
        file_path (str): The path to the file.
        object_class (type): The class of the objects to be created.
        object_attributes (list): The attributes that the objects should have.
        regex (str): The regex that separates the attributes in the file.

    Returns:
        list: A list of objects created from the file.

    """
    objects = []

    with open(file_path, "r") as fileobj:
        for line in fileobj.readlines():
            attributes = line.strip().split(regex)
            if len(attributes) != len(object_attributes):
                continue
            obj = object_class(**{attr: val for attr, val in zip(object_attributes, attributes)})
            objects.append(obj)

    return objects
