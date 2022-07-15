from dis import dis
import imp
from random import randint
import string
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv
import re

class ActionReadCSV(Action):
    def name(self) -> Text:
         return "action_csv"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = tracker.get_slot('claim_id')
        dispatcher.utter_message("Thank you for the information! Please wait a moment while I check your claim status.")
        with open('claim_status.csv','r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1]==id:
                    dispatcher.utter_message("Your claim is "+row[2]+"\n")
                    if(row[2]=="Approved"):
                        dispatcher.utter_message("Your claim amount is "+row[3]+"\n")
                        return[]
                    elif(row[2]=="Pending"):
                        dispatcher.utter_message("We ask that you check again in a few days\n")
                        return[]
                    elif(row[2]=="Rejected"):
                        dispatcher.utter_message("We are sorry but your damages are not covered under the policy that you purchased.\n")
                        return[]
        dispatcher.utter_message("Your entered name or id is incorrect, please type again.\n")
        return[]

class ActionWriteCSV(Action):
    def name(self) -> Text:
         return "action_write_csv"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = ""
        for i in range(6):
            id+=str(randint(0,9))
        name=tracker.get_slot('uname')
        with open('claim_status.csv','a',newline="") as file:
            writer = csv.writer(file)
            # tup1={name,id,"Pending","0"}
            # print(tup1)
            writer.writerow([name,id,"Pending",0])
        dispatcher.utter_message("Your request has been accepted. Your Claim Id is "+id+".")
        dispatcher.utter_message("Please remember this unique claim id for future reference. We will get back to you within a few days.")
        return[]