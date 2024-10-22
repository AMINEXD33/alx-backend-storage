""" a module that have one function """


def insert_school(mongo_collection, **kwargs):
    """insert into collection based on kwargs"""
    mongo_collection.insert(kwargs)
