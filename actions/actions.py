from . helper_functions import validate_category, validate_income, gen_details
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class AddIncomeAction(Action):

    def name(self) -> Text:
        return "add_income_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        income = tracker.get_slot("amount")
        raw_source = tracker.get_slot("income_category")
        date = tracker.get_slot("date")
        current_state = tracker.current_state()
        sender = current_state["sender_id"]
        source = validate_income(raw_source)
        details = gen_details(income, source, date, 'Income')
        context = {
            "sender_id": sender,
            "intent": "add income",
            "amount": income,
            "category": source,
            "date": date,
            "additional_details": details
        }
        print(context)
        return [SlotSet("income_category", None), SlotSet("amount", None), SlotSet("date", None)]

class AddExpenseAction(Action):

    def name(self) -> Text:
        return "add_expense_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        raw_item = tracker.get_slot("category")
        expense_amount = tracker.get_slot("amount")
        date = tracker.get_slot("date")
        item = validate_category(raw_item)
        details = gen_details(expense_amount, item, date, 'Expense')
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
        return [SlotSet("category", None), SlotSet("amount", None), SlotSet("date", None)]

class CreateBudgetAction(Action):

    def name(self) -> Text:
        return "create_budget_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        raw_item = tracker.get_slot("category")
        item = validate_category(raw_item)
        budget_amount = tracker.get_slot("amount")
        date = tracker.get_slot("date")
        details = gen_details(budget_amount, item, date, 'Budget')
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
        print(context)
        return [SlotSet("category", None), SlotSet("amount", None), SlotSet("date", None)]
