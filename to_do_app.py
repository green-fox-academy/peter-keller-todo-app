import sys

def import_file(file_name):
    file = open(file_name, 'r')
    text = file.readlines()
    file.close()
    items = []

    for line in text:
        dictionary = {}
        if line[0] == "0":
            dictionary["complete"] = False
        if line[0] == "1":
            dictionary["complete"] = True
        task = line[2:]
        dictionary['task'] = task
        items.append(dictionary)
    return items
        
todo = sys.argv[0]


#everything_else = sys.argv[2:]
#print(everything_else)


def get_arguments():
    arguments = sys.argv[1:]
    list_arguments = ["-a", "-l", "-c", "-r"]
    if len(arguments) == 0:
        return False
    if arguments[0] in list_arguments:
        return arguments
    else:
        return False


def check_task(items):
    text = ""
    i = 1
    for line in items:
        text += str(i) + " - "
        if line["complete"] == False:
            text +=  "[ ] "  
        else:
            text += "[X] "  
        text += line['task']
        i += 1
    print(text)
    
#def complete_task(items):


#sys.argv[2:]

def controller():
    todos = import_file("todo_app.txt")
    arguments = get_arguments()
    if not arguments:
        print("""Command Line Todo application 
            ============================= 
            Command line arguments: 
             -l   Lists all the tasks 
             -a   Adds a new task 
             -r   Removes an task 
             -c   Completes an task""") 
    elif arguments[0] == "-l":
        print(todos)
    elif arguments[0] == "-c":
        check_task(todos)
    elif arguments[0] == "-r":
        print("Unable to remove: no index provided")
    elif arguments[0] == "-a":
        print("Unable to add: no task provided")
        
controller()