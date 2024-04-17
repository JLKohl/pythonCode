
def main():
        
    task_list = []

    secret_word = "yes"
    counter = 0

    while True:
        word = input("Would you like to add a task? \ntype 'yes' to add or press enter for next: ").lower()
        counter = counter + 1
        if word == secret_word:
            task = input("What task would you like to add? ")
            task_list.append(task)
        if word != secret_word or counter == 10: 
            break
         
    list_to_txt("user_tasks.txt", task_list)

    view_list = int(input("would you like to see your task list?\n 1 for Yes, 2 for No  "))
    if view_list == 1:
        print(print_list("user_tasks.txt"))
    elif view_list == 2:
        print(' ')

    clear_list = int(input("would you like to clear the list? \n 3 for Yes, 4 for No  "))
    if clear_list == 3:
        open('user_tasks.txt', 'w').close()
        print('your list has been cleared.')
    elif clear_list == 4:
        print('your list has not been cleared.')

def list_to_txt(file, list):

    with open(file, 'a') as f:
        for line in list:
            f.write(f"{line}\n")

def print_list(file):

    lines = None
    with open(file, "rt") as infile:

        string = infile.read()

    lines = string.splitlines()

    return lines

if __name__ == "__main__":
    main()