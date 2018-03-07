# -*- coding: utf-8 -*-

import pymongo
import Stemmer
import pandas as pd
from pprint import pprint


stemmer = Stemmer.Stemmer('spanish')
db = pymongo.MongoClient().opendataday

# print stemmer.stemWords(['camionero','camiones','camion','camionera'])

def normalize_words(desc):
    words = desc.split(" ")
    return [s.encode('ascii', 'ignore').decode('ascii').lower() for s in words]


def steam_odd_collection():
    doc = db.contrataciones.aggregate([
        {
          "$match": {
            "records.compiledRelease.tender.description": {"$exists": True},
            "records.compiledRelease.tender.status": "complete"
          }
        },
        {
          "$group":{ "_id":"$records.compiledRelease.tender.description" }
        }
      ])

    for d in doc:
        print normalize_words(d["_id"][0])

if __name__ == '__main__':
    steam_odd_collection()
