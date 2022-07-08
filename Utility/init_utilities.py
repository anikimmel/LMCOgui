
def save_preferences(values):
    materials = []
    manufacturing = []
    businesses = []

    for i in range(9):
        if values['matcheck' + str(i)]:
            materials.append('matcheck' + str(i))

    for i in range(6):
        if values['mancheck' + str(i)]:
            manufacturing.append('mancheck' + str(i))

    for i in range(2):
        if values['buscheck' + str(i)]:
            businesses.append('buscheck' + str(i))

    return materials, manufacturing, businesses
