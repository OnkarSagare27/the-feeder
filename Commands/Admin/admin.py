import os
import json
from Functions import utils

async def give_perms(user_id: int, sub_type: str):
    buyers = []
    file = open('Database/buyers_data.json', 'r')
    buyers = json.load(file)
    file.close()
    user_found = []
    if len(buyers) != 0 :
        for i in range(len(buyers)):
            if int(buyers[i]["user_id"]) == user_id:
                user_found.append(i)
                if sub_type == "1 Month":
                    end = utils.date_after_X_months_and_Y_days(1)
                elif sub_type == "2 Months and 2 weeks":
                    end = utils.date_after_X_months_and_Y_days(2,14)
                elif sub_type == "7 Months":
                    end = utils.date_after_X_months_and_Y_days(7)
                else:
                    end = "Lifetime"
                buyers[i]["user_data"]["sub_type"] = sub_type
                buyers[i]["user_data"]["sub_start"] = utils.current_ist_date()
                buyers[i]["user_data"]["sub_end"] = end

                with open('Database/buyers_data.json', "w") as jsonFile:
                    json.dump(buyers, jsonFile)

                return(["UPDATED",utils.current_ist_date(), end])
    
    if len(user_found) == 0:
        if sub_type == "1 Month":
            end = utils.date_after_X_months_and_Y_days(1)
        elif sub_type == "2 Months and 2 weeks":
            end = utils.date_after_X_months_and_Y_days(2,14)
        elif sub_type == "7 Months":
            end = utils.date_after_X_months_and_Y_days(7)
        else:
            end = "Lifetime"
        buyers.append({"user_id":f"{user_id}","user_data":{"sub_type":f"{sub_type}","sub_start":f"{utils.current_ist_date()}","sub_end":f"{end}"}})
        file = open('Database/buyers_data.json', 'w')
        json.dump(buyers, file)
        file.close()
        buyers_list = []
        file1 = open('Database/buyers_list.json', 'r')
        buyers_list = json.load(file1)
        file1.close()
        buyers_list.append(int(user_id))
        file1 = open('Database/buyers_list.json', 'w')
        json.dump(buyers_list, file1)
        file1.close()

        return(["ADDED",utils.current_ist_date(), end])

async def remove_perms(user_id: int):
    buyers_list = []
    file = open('Database/buyers_list.json', 'r')
    buyers_list = json.load(file)
    file.close()
    user_found = []
    if len(buyers_list) != 0 :
        for i in range(len(buyers_list)):
            if int(buyers_list[i]) == user_id:
                user_found.append(1)
                index = buyers_list.index(user_id)
                del buyers_list[index]
                with open('Database/buyers_list.json', "w") as jsonFile:
                    json.dump(buyers_list, jsonFile)
                buyers_data = []
                file = open('Database/buyers_data.json', 'r')
                buyers_data = json.load(file)
                file.close()
                if len(buyers_data) != 0 :
                    for i in range(len(buyers_data)):
                        if int(buyers_data[i]["user_id"]) == user_id:
                            del buyers_data[i]
                            with open('Database/buyers_data.json', "w") as jsonFile:
                                json.dump(buyers_data, jsonFile)
                                user_found.append(2)
                                return("REMOVED")
    
    if len(user_found) == 0:
        return("USER NOT FOUND")
    elif len(user_found) == 1:
        return("ERROR IN DATA")

async def give_perms2(user_id: int, started:str,end:str,sub_type: str):
    buyers = []
    file = open('Database/buyers_data.json', 'r')
    buyers = json.load(file)
    file.close()
    user_found = []
    if len(buyers) != 0 :
        for i in range(len(buyers)):
            if int(buyers[i]["user_id"]) == user_id:
                # user_found.append(i)
                # if sub_type == "1 Month":
                #     end = utils.date_after_X_months_and_Y_days(1)
                # elif sub_type == "2 Months and 2 weeks":
                #     end = utils.date_after_X_months_and_Y_days(2,14)
                # elif sub_type == "7 Months":
                #     end = utils.date_after_X_months_and_Y_days(7)
                # else:
                #     end = "Lifetime"
                buyers[i]["user_data"]["sub_type"] = sub_type
                buyers[i]["user_data"]["sub_start"] = started
                buyers[i]["user_data"]["sub_end"] = end

                with open('Database/buyers_data.json', "w") as jsonFile:
                    json.dump(buyers, jsonFile)

                return(["UPDATED",utils.current_ist_date(), end])
    
    if len(user_found) == 0:
        # if sub_type == "1 Month":
        #     end = utils.date_after_X_months_and_Y_days(1)
        # elif sub_type == "2 Months and 2 weeks":
        #     end = utils.date_after_X_months_and_Y_days(2,14)
        # elif sub_type == "7 Months":
        #     end = utils.date_after_X_months_and_Y_days(7)
        # else:
        #     end = "Lifetime"
        buyers.append({"user_id":f"{user_id}","user_data":{"sub_type":f"{sub_type}","sub_start":f"{started}","sub_end":f"{end}"}})
        file = open('Database/buyers_data.json', 'w')
        json.dump(buyers, file)
        file.close()
        buyers_list = []
        file1 = open('Database/buyers_list.json', 'r')
        buyers_list = json.load(file1)
        file1.close()
        buyers_list.append(int(user_id))
        file1 = open('Database/buyers_list.json', 'w')
        json.dump(buyers_list, file1)
        file1.close()

        return(["ADDED",started, end])