di = dict()
id = 0
ls2 = []

class InvalidInput(Exception):
    pass

def valid_addition(func):
    def wrapper(*args):
        try:
            if isinstance(args[0], str) and args[0] != "":
                global id;
                id += 1
                func(*args)
            else:
                return InvalidInput("error")
        except InvalidInput() as e:
            return e
    return wrapper

@valid_addition
def addition(des, pr, comp = "not completed"):
    di[id] = [des, pr, comp]

num1 = 0
def removal(des):
    global num1
    for i in list(di.values()):
        num1 += 1
        if des == i[0]:
            for j in range(num1, len(di.keys())):
                tmp = list(di.keys())[j] - 1
                di[tmp] = di.pop(list(di.keys())[j])
            return
        else:
            return "There isn't such a des"


def managing():
    task_id = int(input("Enter the task ID to mark as completed/not completed: "))
    for i in di.keys():
        if i == task_id:
            if di[i][2] == 'completed':
                di[i][2]= 'not completed'
            else:
                di[i][2] = 'completed'
            print("Des is updated.")
            return
        print("Des is not found")

di2 = { "imp": 1, 
        "medium": 2,
        "not imp": 3 }

def prior():
    for i in di.keys():
        ls2.append((i, di[i]))    
    ls2.sort(key = lambda x: di2[x[1][1]])
    return ls2 
    

def to_do_list(func, des = "",pr = "not imp", comp = "not completed"):
    if func == "add":
        addition(des, pr, comp)
    elif func == "remove":
        removal(des)
    elif func == "managing":
        managing()
    elif func == "prioritization":
        prior()

    print("Success")
to_do_list("add", "To go to Picsart ","medium", "completed")
to_do_list("add", "To go to Picsart 2", "imp", "completed")
to_do_list("managing")
to_do_list("prioritization")
to_do_list("remove", "To go to Picsart ")
