from . helper_functions import validate_items_data
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class AddIncomeAction(Action):

    def name(self) -> Text:
        return "add_income"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        income = tracker.get_slot("amount")
        source = tracker.get_slot("income_category")
        date = tracker.get_slot("date")
        details = tracker.get_slot("additional_details")
        current_state = tracker.current_state()
        sender = current_state["sender_id"]
        context = {
            "sender_id": sender,
            "intent": "add income",
            "amount": income,
            "category": source,
            "date": date,
            "additional_details": details
        }
        return []

class AddExpenseAction(Action):

    def name(self) -> Text:
        return "add_expense"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        raw_item_list = tracker.get_slot("expense_item")
        item = validate_items_data(raw_item_list)
        expense_amount = tracker.get_slot("expense_amount")
        date = tracker.get_slot("date")
        details = tracker.get_slot("additional_details")
        current_state = tracker.current_state()
        sender = current_state["sender_id"]
        context = {
            "sender_id": sender,
            "intent": "add expense",
            "amount": expense_amount,
            "category": item,
            "date": date,
            "additional_details": details
        }
        print(context)
        print('hi')
        print(tracker.latest_message['entities'])
        print(tracker.current_state())
        return []

class CreateBudgetAction(Action):

    def name(self) -> Text:
        return "create_budget"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        item = tracker.get_slot("budget_item")
        budget_amount = tracker.get_slot("budget_amount")
        date = tracker.get_slot("date")
        details = tracker.get_slot("additional_details")
        current_state = tracker.current_state()
        sender = current_state["sender_id"]
        context = {
            "sender_id": sender,
            "intent": "create_budget",
            "amount": budget_amount,
            "category": item,
            "date": date,
            "additional_details": details
        }
        return []
