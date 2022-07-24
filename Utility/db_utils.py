import json
import requests
from Utility import MaterialTypes
# from pymongo import MongoClient

request_counter = 0

# def insert_json():
#     # Making Connection
#     myclient = MongoClient("mongodb://localhost:27017/")
#
#     # database
#     db = myclient["GFG"]
#
#     # Created or Switched to collection
#     # names: GeeksForGeeks
#     Collection = db["data"]
#
#     # Loading or Opening the json file
#     with open('data.json') as file:
#         file_data = json.load(file)
#
#     # Inserting the loaded data in the Collection
#     # if JSON contains data more than one entry
#     # insert_many is used else insert_one is used
#     if isinstance(file_data, list):
#         Collection.insert_many(file_data)
#     else:
#         Collection.insert_one(file_data)


def getBids(design, preferences, quantity, earliest_start, due):
    materials = preferences[0]
    manufacturing = preferences[1]
    businesses = preferences[2]
    request = {"Name": "request" + str(request_counter), "Part": design, "SupplierNames": businesses,
               "Quantity": int(quantity), 'EarliestStartDate': earliest_start.replace(' ', 'T'),
               'DueDate': due.replace(' ', 'T')}
    pp_info = getProcessPlans()
    plans = []
    specific_materials = []
    for material in materials:
        specific_materials += MaterialTypes.specifics[material]
    for plan in pp_info:
        if (plan['ManufacturingMethod'] in manufacturing) and (plan['Material'] in specific_materials):
            plans.append(plan['Name'])
    request['ProcessPlans'] = plans
    r = requests.post('http://localhost:9090/generate-bid', data=json.dumps(request))
    print(f"Status Code: {r.status_code}, Response: {r.json()}")

    return processResponse(r.json())


def getProcessPlans():
    part_plan_info = open('C:\\Users\\Annie\\PycharmProjects\\LMCOgui\\Utility\\Data\\PartProcessPlans.json')
    plans = json.load(part_plan_info)
    part_plan_info.close()
    return plans


def getSpecificPlan(plan_name):
    plans = getProcessPlans()
    for plan in plans:
        if plan["Name"] == plan_name:
            return plan


def processResponse(response):
    data = response["data"]
    max_cost = 0
    max_time = 0
    max_mass = 0
    clean_bids = []
    for bid in data:
        plan = getSpecificPlan(bid["processPlan"])
        if float(bid["cost"]) > max_cost:
            max_cost = float(bid["cost"])
        if float(bid["leadTime"]) > max_time:
            max_time = float(bid["leadTime"])
        if float(plan["NetGrams"]) > max_mass:
            max_mass = float(plan["NetGrams"])

        clean_bid = {
            "cost": float(bid["cost"]),
            "time": float(bid["leadTime"]),
            "mass": float(plan["NetGrams"]),
            "link": plan["Link"]
        }
        clean_bids.append(clean_bid)

    dataMaxes = {
        "cost": max_cost,
        "time": max_time,
        "mass": max_mass
    }
    return clean_bids, dataMaxes
