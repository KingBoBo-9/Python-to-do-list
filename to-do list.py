# I need to make a while loop that prints the following commands:
# a) add task
# b) remove task
# c) view list 

def main():
    print("a) Add task")
    print("b) Remove task")
    print("c) View list")
    
    while True:
        
        ans = input("Enter command: ")
        ans = ans.lower()

        if ans == "a":
            task_to_add = input("Task to add: ")
            add_task(task_to_add)
        elif ans == "b":
            task_to_remove = input("Task to remove: ")
            remove_task(task_to_remove)
        elif ans == "c":
            print(to_do_list)



def add_task(task):
    return to_do_list.append(task)
    
def remove_task(task):
    return to_do_list.remove(task)
    
            

to_do_list = []
main()