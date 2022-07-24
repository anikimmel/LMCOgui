# this file contains all the machining types
# eventually, these will be objects
from Utility import db_utils
global machiningTypes

plans = db_utils.getProcessPlans()

machiningTypes = []
for plan in plans:
    machineType = plan["ManufacturingMethod"]
    if machineType in machiningTypes:
        continue
    else:
        machiningTypes.append(machineType)

