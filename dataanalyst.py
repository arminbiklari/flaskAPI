"""
this app for analyst data and process data with pandas 
"""
import pandas as pd 
import json

def Name_dataframe(*args, lower=False):
    name = list()
    def it_path():
        for arg in args:
            data = pd.read_csv(arg)
            data = pd.DataFrame(data)
            name.append(data["Name"])
        return data
    def lower():
        for i in range(len(name)):
            name[i] = name[i].str.lower()
        return name
    return it_path 

def search_engin(func, name, details=True):
    def check_name(*args):
        data = func()
        # check if the name is in the list
        for names in data["Name"]:
            if name in names:
                data = data.loc[data["Name"] == names]
                return data.to_json()
            else:
                return False

    def search_details(*args):
        details = dict()    # create a dictionary for return data as a json format 
        data = check_name() # create an instance of check_name function for get peroper data
        if data:        # check if the data is not False
            data = json.loads(data) # convert data string to a dictionary
            for arg in args:
                for key in data.keys():     # check if the key is in the dictionary
                    if arg in key:
                        for value in data[key].values():
                            details.update({key:value})
            return details                                      
        else:
            return check_name()
    return search_details if details else check_name

file = "/home/armin/python_project/TestsFiles/nba.csv"
# name = "Avery Bradley"
# search = search_engin(Name_dataframe(file), name, details=True)
# value = search("Name", "Salary", "Team")
# print(value)
