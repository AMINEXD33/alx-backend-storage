#!/usr/bin/env python3
""" a module that have one function """

def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)