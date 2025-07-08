def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            task = input("Enter a task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' removed.")
            else:
                print("Task not found.")
        elif choice == '3':
            print("Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '4':
            break
        else:
            print("Invalid option.")

todo_list()
