num_frames = 5
page_size = 1024
memory = [None] * num_frames
page_queue = []


def allocate_page(page_number):
    if page_number in page_queue:
        return  

    if len(page_queue) == num_frames:
        old_page = page_queue.pop(0)
        memory[memory.index(old_page)] = None

    page_queue.append(page_number)
    empty_frame = memory.index(None)
    memory[empty_frame] = page_number

def access_page(page_number):
    if page_number in page_queue:
        page_queue.remove(page_number)
        page_queue.append(page_number)
        return True
    else:
        return False

def display_memory_status():
    global memory;
    print("Memory Status:")
    for i in range(num_frames):
        page = memory[i]
        if page is not None:
            print(f"Frame {i + 1}: Page {page}")
        else:
            print(f"Frame {i + 1}: Empty")


  
def virtual_memory(func):
    if func == 'allocate':
        page_number = int(input("Enter page number to allocate: "))
        allocate_page(page_number)
        print(memory)
    elif func == 'page access':
        page_number = int(input("Enter page number to access: "))
        if access_page(page_number):
            print(f"Page {page_number} is in memory.")
        else:
            print(f"Page {page_number} is not in memory.")
    elif func == 'displat memory status':
        display_memory_status()
    else:
        print("Invalid input")

    print("Update")


virtual_memory('allocate')