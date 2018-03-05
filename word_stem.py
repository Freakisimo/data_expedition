import pymongo
import Stemmer
import pandas as pd
from pprint import pprint


stemmer = Stemmer.Stemmer('spanish')
db = pymongo.MongoClient().opendataday

# print stemmer.stemWords(['camionero','camiones','camion','camionera'])

def is_list(item):
    return isinstance(item, list) or isinstance(item, tuple)

def is_dict(item):
    return isinstance(item, dict)


def depth_structure(doc, with_value=True, current=[], row=[]):
    if is_dict(doc):
        for k,v in doc.items():
            current.append(k)
            if is_dict(v):
                for d in depth_structure(v, with_value, current):
                    pass
            elif is_list(v):
                for i in v:
                    for j in depth_structure(i, with_value, current):
                        pass
            else:
                if with_value:
                    current.append(v)
                row.append(current)
                current = []
    else:
        current.append(doc)
    return row

def steam_odd_collection():
    doc = db.contrataciones.find().limit(3)
    doc_structure = [depth_structure(x) for x in list(doc)]
    # contracts_list = []
    # for row in doc:
    #     for release in row["records"][0]["releases"]:
    #         if 'contracts' in release:
    #             contracts = release["contracts"]
    #             if not 'status' in contracts:
    #                 contract_dict = {}
    #                 for contract in contracts:
    #                     contract_dict["title"] = contract["title"]
    #                     contract_dict["buyers"] = contract["buyers"][0]["name"] if "buyers" in contract else None
    #                     contract_dict["period"] = contract["period"]
    #                     contract_dict["dateSigned"] = contract["dateSigned"] if "dateSigned" in contract else None
    #                     if "valueWithTax" in contract:
    #                         contract_dict["amount"] = contract["valueWithTax"]["amount"]
    #                         contract_dict["currency"] = contract["valueWithTax"]["currency"]
    #                         budgetClassification = contract["implementation"]["budgetBreakdown"][0]['budgetClassification']
    #                         contract_dict["description"] = ""
    #                         for row in budgetClassification:
    #                             if 'description' in row:
    #                                 contract_dict["description"] += row["description"]
    #                 contracts_list.append(contract_dict)

    # df = pd.DataFrame(contracts_list)
    # print df['description']
    # df['description_list'] = df['description'].apply(lambda row:row.split(','))

if __name__ == '__main__':
    steam_odd_collection()
