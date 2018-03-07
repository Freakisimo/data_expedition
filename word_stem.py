# -*- coding: utf-8 -*-

import pymongo
import Stemmer
import operator
import pandas as pd

from collections import Counter
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

    all_words = []
    for d in doc:
        # all_words += stemmer.stemWords( normalize_words(d["_id"][0]) )
        all_words += normalize_words(d["_id"][0])
    word_count = Counter(all_words)
    word_count_sorted = sorted( word_count.items(), key=operator.itemgetter(1) )
    pprint( word_count_sorted )

if __name__ == '__main__':
    steam_odd_collection()
