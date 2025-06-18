def add_hour_one(element):
    result = element.copy()
    result["hour"] = element["time"][-5:]
    return result

def add_hour(list_temp):
    result = []
    for element in list_temp:
        result.append(add_hour_one(element))
    return result

class FilterModule(object):
    def filters(self):
        return {
            'add_hour': add_hour
        }
