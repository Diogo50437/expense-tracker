from datetime import datetime
import json
import csv
import pandas as pd
from tabulate import tabulate

print ("Please choose the desired operation: \n" \
"- To see a full list of expenses enter E\n" \
"- To add an expense enter A\n" \
"- To remove an expense enter R\n" \
"- To update an expense enter U")

def list():
  expenses = pd.read_csv('expenses.csv', index_col=False)
  print(tabulate(expenses, headers='keys', tablefmt='psql', showindex=False))
    

def add():
    expenses = pd.read_csv('expenses.csv')

    description = input("Expense description: ")
    ammount = input("Expense ammount: ")
    date = datetime.today().strftime('%d-%m-%Y')

    expense = {
        'ID': [len(expenses)+1],
        'Description': [description],
        'Ammount': [ammount + "€"],
        'Date': [date]
    }

    dataframe = pd.DataFrame(expense)
    dataframe.to_csv('expenses.csv', mode='a', index=False, header=False)

def remove():
    row = input("Select Row number you want to delete: ")
    row = int(row)-1

    expenses = pd.read_csv('expenses.csv', index_col=False) 
    expenses.drop([row],inplace=True)

    #expenses = expenses.drop([row])
    print(tabulate(expenses, headers='keys', tablefmt='psql', showindex=False))
    #expenses.to_csv('expenses.csv', mode='a', index=False, header=False)

def update():
    print("update")


def switch (operation):
    if operation == "E":
        list()
    elif operation == "A":
        add()
    elif operation == "R":
        remove()
    elif operation == "E":
        update()
    else:
        print("Unknown operation!")

operation = input()
#while True:
switch(operation.upper())