import json
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


def construct_request(design, preferences, quantity, earliest_start, due):
    materials = preferences[0]
    manufacturing = preferences[1]
    businesses = preferences[2]
    request = {"Name": "request" + str(request_counter), "Part": design, "SupplierNames": businesses,
               "Quantity": quantity, 'EarliestStartDate': earliest_start.replace(' ', 'T'),
               'DueDate': due.replace(' ', 'T')}
    part_plan_info = open('C:\\Users\\Annie\\PycharmProjects\\LMCOgui\\Utility\\Data\\PartProcessPlans.json')
    pp_info = json.load(part_plan_info)
    plans = []
    specific_materials = []
    for material in materials:
        specific_materials += MaterialTypes.specifics[material]
    for plan in pp_info:
        if (plan['ManufacturingMethod'] in manufacturing) and (plan['Material'] in specific_materials):
            plans.append(plan['Name'])
    part_plan_info.close()
    request['ProcessPlans'] = plans
    print(len(plans))
    return json.dumps(request)




