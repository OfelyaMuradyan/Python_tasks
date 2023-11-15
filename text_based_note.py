id = 0
di = dict()
ls = []
ls2 = []

def note_creation(note):
    global id
    id += 1
    di[id] = note
    print("Note is created.")

def note_listing():
    for i in di.keys():
        ls = [(i, di[i])]
    print(ls)

def note_retrieval():
    try:
        k = int(input("Enter ID: "))
        if k in di.keys():
            print(di[k])
            return
        else:
            raise KeyError("The note doesn't exist")
    except KeyError as e:
        return e
    
def note_deletion():
    try: 
        j = int(input("Enter ID: "))
        if j in di.keys():
            tmp = list(di.keys())[j] - 1
            di[tmp] = di.pop(list(di.keys())[j])
        else:
            raise KeyError("The note does not exist")
    except KeyError as e:
        return e
    
def search_notes():
    k = input("Input the word you want to search: ")
    for i in di.values():
        if k in i:
            ls2.append(i)
    print(ls2)

def text_based_note(func, note = None):
    if func == "create":
        if note != "" and note is not None:
            note_creation(note)
        else:
            print("Note is empty")
            return
    elif func == "list":
        note_listing()
        return
    elif func == "retrieve":
        note_retrieval()
    elif func == "delete":
        note_deletion()
        return
    elif func == "search":
        search_notes()
        return
    else:
        print("Invalid input")

text_based_note("create", "do classes")
text_based_note("create", "go for a walk")
print(di)
text_based_note("retrieve")
text_based_note("delete")
text_based_note("search")