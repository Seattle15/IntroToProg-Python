# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Hedy Khalatbari>,<07.26.2021>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # Data storage file
objFile = None # An object that represents a file
strData = ""   # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary; {Priority, Task}
lstTable = []  # A list that acts as a 'table' of dictionary rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt from a Python list of dictionaries rows
# Step 1A - Add all data as dicRow to lstTable
dicRow = {"priority":"high", "task":"take puppy to vet"}
lstTable.append(dicRow)
dicRow = {"priority":"low", "task":"schedule gutter cleaning"}
lstTable.append(dicRow)
dicRow = {"priority":"low", "task":"find a new gardener"}
lstTable.append(dicRow)
dicRow = {"priority":"high", "task":"make a dentist appointment"}
lstTable.append(dicRow)
# Step 1B - Write the value of the dictionary elements to the text file
objFile = open(strFile, "w")
for row in lstTable:
    objFile.write(row["priority"] + ", " + row["task"] + "\n")
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for presentation

    # Step 3 - Show the current items in the table in order of priority (high versus low)
    if (strChoice.strip() == '1'):
        lstTable = []   # reset to empty list to ensure we do not get duplicate entries
        objFile = open(strFile, "r")
        for row in objFile:
            strData = row.split(",")
            dicRow = {"priority": strData[0], "task": strData[1].strip()}
            # high priority tasks are added to the beginning of the table
            if strData[0] == 'high':
                lstTable.insert(0, dicRow)
            # low priority tasks are added to the end of the table
            elif strData[0] == 'low':
                lstTable.append(dicRow)
        # print each dictionary on a separate row
        print("Your current to do list in order of priority is: ")
        for item in lstTable:
            print(item)
        objFile.close()
        continue

    # Step 4 - Add a new item and write it to the text file
    elif (strChoice.strip() == '2'):
        # ask for task input and perform lower and strip methods on input
        task = input("Enter task: ")
        task = task.lower()
        task = task.strip()
        # ask for priority input and perform lower and strip methods on input
        priority = input("Enter priority (high or low): ")
        priority = priority.lower()
        priority = priority.strip()
        # check for correct user input of priority as either high or low
        if priority == 'high' or priority == 'low':
            # add inputs to a dictionary
            dicRow = {"priority": priority, "task": task}
            # write inputs to text file in append mode
            objFile = open(strFile, "a")
            objFile.write(dicRow["priority"] + ", " + dicRow["task"] + "\n")
            objFile.close()
            print("Task added to to-do list")
        else:
            print("Invalid choice. Please choose from menu")
        continue

    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        priorities = []   # local list variable
        tasks = []        # local list variable
        # ask user for input and perform lower and strip methods on input
        task_remove = input("Which task would you like to remove?  ")
        task_remove = task_remove.lower()
        task_remove = task_remove.strip()
        # open file to read each row and append contents to tasks and priorities lists
        objFile = open(strFile, "r")
        for row in objFile:
            strData = row.split(",")
            priority = strData[0]
            priorities.append(priority)
            task = strData[1]
            task = task.strip()  # strip the \n
            tasks.append(task)
        objFile.close()
        # check if task_remove is in tasks list and if present remove it &
        # delete the corresponding priority from priorities list
        if task_remove in tasks:
            removed_index = tasks.index(task_remove)  # check for the index
            tasks.remove(task_remove)
            del priorities[removed_index]  # remove the same index from priorities list
            print("The task was on your to-do list and is now deleted")
        # otherwise let user know that the task was not in the task list
        else:
            print("The task was not on your to-do list")
        # update the text file with remaining priority-task pairs
        lstTable = []  # reset to empty list to ensure we do not get duplicate entries
        counter = 0
        for i in tasks:
            dicRow = {"priority": priorities[counter], "task": tasks[counter]}
            counter += 1
            lstTable.append(dicRow)
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["priority"] + ", " + row["task"] + "\n")
        objFile.close()
        continue

    # Step 6 - Save tasks to ToDoList.txt file
    # The data is saved to file with each step, therefore no action is required here -
    # other than a message letting the user know the data is saved
    elif (strChoice.strip() == '4'):
        print("Data saved to file")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Press the ENTER key to exit")
        input()
        break  # and Exit the program
