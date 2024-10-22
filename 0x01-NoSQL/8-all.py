#!/usr/bin/env python3
""" a module that get all docs from a db """


def list_all(mongo_collection):
    """ list all docs in a collection """
    result: list = mongo_collection.find()

    if result.count() == 0:
        return []

    return mongo_collection.find()
