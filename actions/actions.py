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
             with open('C:/Users/HP/Desktop/BITS/2nd Year/PS1/Rasa Project/Data/claim_status.csv','r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row[2]==id:
                        dispatcher.utter_message("Your claim is "+row[3]+"\n")
                        if(row[3]=="Approved"):
                            dispatcher.utter_message("Your claim amount is "+row[4]+"\n")
                        elif(row[3]=="Pending"):
                            dispatcher.utter_message("We ask that you check again in a few days\n")
                        elif(row[3]=="Rejected"):
                            dispatcher.utter_message("We are sorry but your damages are not covered under the policy that you purchased.\n")
                            
             return[]           