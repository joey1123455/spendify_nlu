import requests
import json

def post_to_server(url, body):
    destination = "" 
    header = ""
    body = json.dumps(body)

def validate_items_data(items):
    CATEGORIES = ['Transportation', 'Sales Expense', 'Rent', 'Food', 'Medical',
    'Utility Bills', 'Clothing', 'Sports', 'Education', 'Housing', 'Debt Payments',
    'Personal', 'Personal & Discretionary']
    for i in range(len(items)):
        if items[i] not in CATEGORIES:
            print(items[i])
            items.pop(i)
            items.insert(i,'Miscellaneous')
    items = set(items)
    return items

raw_items = ['Transportation', '']