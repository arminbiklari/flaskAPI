import pandas as pd 
import json

class DataAnalyst:
    name_list = list()
    path_of_csv = list()
    def __init__(self, *args):
        self.path_of_csv = args




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
        def check_name():
            data = func()
            # check if the name is in the list
            for names in data["Name"]:
                if name in names:
                    data = data.loc[data["Name"] == names]
                    return data.to_json(orient="index")
                else:
                    return f"{name} not found"
        # def salary_search(name):
        #     data = check_name(name)
        #     salary = data["Salary"]
        #     return salary.item()
        def search_details(*args):
            data = check_name()
            # conver data string to a dictionary
            data = json.loads(data)
            for arg in args:
                for key in data.keys():
                    if arg in key:
                        return data[key]
        return search_details if details else check_name