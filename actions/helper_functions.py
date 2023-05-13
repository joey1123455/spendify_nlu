import requests
import json

def post_to_server(url, body):
    destination = "" 
    header = ""
    body = json.dumps(body)


def validate_income(item):
    '''
    converts incomplete income categories into complete categories to be passed to the 
    database.
    @item: the income category being passed through.
    @incomp: a list of expected incomplete categories.

    returns: the modified item or the original item.
    '''
    incomp = ['Rental', 'Intrest', 'Gift', 'Donation']
    if item in incomp:
        if item == 'Rental':
            item = 'Rental Income'
            return item
        elif item == 'Intrest':
            item = 'Intrest Income'
            return item
        elif item == 'Gift' or item == 'Donation':
            item = 'Gift/Donation'
            return item
    return item


def validate_category(item):
    '''
    converts incomplete expense or budget categories into complete categories before
    pushing to the database
    @item: the expense to be converted.
    @incomp: a list of expected incomplete categories.
    
    returns: the completed category'''
    incomp = ['Business', 'Utility', 'Personal', 'Debt']
    if item in incomp:
        if item == 'Business':
            item = 'Sales Expense'
            return item
        elif item == 'Utility':
            item = 'Utility Bills'
            return item 
        elif item == 'Personal':
            item = 'Personal & Discretionary'
            return item
        elif item == 'Debt':
            item = 'Debt Payments'
            return item
    return item


def gen_details(amount, category, date, type):
    '''
    Generates additional details for each transaction
    @amount: the amount to be recorded
    @category: the transaction category
    @date: the transaction date
    @type: the transaction type
    
    return: the description
    '''
    if type == 'Income':
        des = f'{type} of {amount} was made on {date} through {category}. This transaction was recorded with the whatsapp chat bot.'
        return des
    else:
        des = f'A {type} was made for {category} of {amount}. This transaction was recorded with the whatsapp chat bot.'
        return des
