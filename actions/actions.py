# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class AddIncomeAction(Action):

    def name(self) -> Text:
        return "add_income"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        income = tracker.get_slot("amount")
        source = tracker.get_slot("income_category")
        date = tracker.get_slot("date")
        details = tracker.get_slot("income_additional_details")
        print(income)
        print(source)
        print(date)
        print(details)
        return []

class AddExpenseAction(Action):

    def name(self) -> Text:
        return "add_expense"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        item = tracker.get_slot("expense_item")
        expense_amount = tracker.get_slot("expense_amount")
        date = tracker.get_slot("date")
        details = tracker.get_slot("expense_additional_details")
        print(item)
        for i in item:
            print(i)
        print(expense_amount)
        print(date)
        print(details)
        return []
