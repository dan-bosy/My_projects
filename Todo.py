tasks = {}
index = 0

def add_task():
    global index
    try:
        task_name = input('Enter task name: ')
        description = input('Enter task description: ')
        tasks[index] = {task_name: description}
        print(f'Task added at index {index}')
        index += 1
    except Exception as e:
        print('Something went wrong:', e)

def update_task():
    try:
        idx = int(input('Enter task index to update: '))
        if idx not in tasks:
            print('Index not found.')
            return
        old_name = input('Enter current task name: ')
        if old_name not in tasks[idx]:
            print('Task not found in that index.')
            return
        new_name = input('Enter new task name: ')
        new_description = input('Enter new task description: ')
        tasks[idx] = {new_name: new_description}
        print('Task updated.')
    except Exception as e:
        print('Something went wrong:', e)

def view_task():
    try:
        choice = int(input('1. View by index  2. View all: '))
        if choice == 1:
            idx = int(input('Enter task index: '))
            if idx not in tasks:
                print('Index not found.')
            else:
                for k, v in tasks[idx].items():
                    print(f'Name: {k}, Description: {v}')
        elif choice == 2:
            if not tasks:
                print('No tasks available.')
            for idx, kv in tasks.items():
                for name, desc in kv.items():
                    print(f'Index: {idx} | Name: {name}, Description: {desc}')
        else:
            print('Invalid choice.')
    except Exception as e:
        print('Error:', e)

def remove_task():
    try:
        choice = int(input('1. Remove entire index  2. Remove task inside index: '))
        if choice == 1:
            idx = int(input('Enter index: '))
            if idx in tasks:
                del tasks[idx]
                print('Task index removed.')
            else:
                print('Invalid index.')
        elif choice == 2:
            idx = int(input('Enter index: '))
            if idx not in tasks:
                print('Invalid index.')
                return
            task_name = input('Enter task name to remove: ')
            if task_name in tasks[idx]:
                del tasks[idx][task_name]
                print('Task removed.')
                # Remove the index entirely if empty
                if not tasks[idx]:
                    del tasks[idx]
            else:
                print('Task not found in that index.')
        else:
            print('Invalid choice.')
    except Exception as e:
        print('Error:', e)

def main():
    while True:
        print('''
Welcome to Todo App
==========================
Options:
1. Add task
2. Update task
3. View task
4. Remove task
5. Exit
''')
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                add_task()
            elif choice == 2:
                update_task()
            elif choice == 3:
                view_task()
            elif choice == 4:
                remove_task()
            elif choice == 5:
                print('Exiting...')
                break
            else:
                print('Invalid choice.')
        except Exception as e:
            print('Error:', e)

if __name__ == '__main__':
    main()
