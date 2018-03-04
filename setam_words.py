import pymongo
import Stemmer
import pandas as pd
from pprint import pprint


stemmer = Stemmer.Stemmer('spanish')
db = pymongo.MongoClient().opendataday

# print stemmer.stemWords(['camionero','camiones','camion','camionera'])

def steam_odd_collection():
    doc = db.contrataciones.find().limit(1000)
    contracts_list = []
    for row in doc:
        for release in row["records"][0]["releases"]:
            if 'contracts' in release:
                contracts = release["contracts"]
                if not 'status' in contracts:
                    contract_dict = {}
                    for contract in contracts:
                        contract_dict["title"] = contract["title"]
                        contract_dict["buyers"] = contract["buyers"][0]["name"] if "buyers" in contract else None
                        contract_dict["period"] = contract["period"]
                        contract_dict["dateSigned"] = contract["dateSigned"] if "dateSigned" in contract else None
                        if "valueWithTax" in contract:
                            contract_dict["amount"] = contract["valueWithTax"]["amount"]
                            contract_dict["currency"] = contract["valueWithTax"]["currency"]
                            budgetClassification = contract["implementation"]["budgetBreakdown"][0]['budgetClassification']
                            contract_dict["description"] = ""
                            for row in budgetClassification:
                                if 'description' in row:
                                    contract_dict["description"] += row["description"]
                    contracts_list.append(contract_dict)

    df = pd.DataFrame(contracts_list)
    print df['description']
    # df['description_list'] = df['description'].apply(lambda row:row.split(','))

if __name__ == '__main__':
    steam_odd_collection()
