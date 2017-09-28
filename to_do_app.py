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
        dictionary['task'] = task[:-1]
        items.append(dictionary)
    return items
        
todo = sys.argv[0]


def get_arguments():
    arguments = sys.argv[1:]
    list_arguments = ["-a", "-l", "-c", "-r"]
    if len(arguments) == 0:
        return False
    if arguments[0] in list_arguments:
        return arguments
    else:
        return False


def controller():
    arguments = get_arguments()
    if not arguments:
        print("gebasz")
    elif arguments[0] == "-l":
        todos = import_file("todo_app.txt")
        print(todos)
    elif arguments[0] == "-c":
        print("agrahareg")
    elif arguments[0] == "-r":
        print("afadf")
    elif arguments[0] == "-a":
        print("eas")
        
controller()

 #   if arguments not in list_arguments:
 #       print("Command line arguments: '\
#              -l   Lists all the tasks '\
 #             -a   Adds a new task '\
#              -r   Removes an task '\
 #             -c   Completes an task")
#    if arguments is "-l":
#        pass
