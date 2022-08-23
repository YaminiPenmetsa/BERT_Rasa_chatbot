# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.types import DomainDict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionStorytelling(Action):

    def name(self) -> Text:
        return "action_storytelling"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.get_slot("storytelling")
        print(value)
        
        if value == "Yes":
            dispatcher.utter_message(reponse = "utter_yes")
        elif value == "No":
            dispatcher.utter_message(reponse = "utter_no")
        else:
            dispatcher.utter_message("Please select the correct options")
        return []

        
