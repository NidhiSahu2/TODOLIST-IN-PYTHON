def task():
    task =[] #enpty list
    print("---WELCOME TO THE TASK MANGEMENT APP---")



    total_task= int(input("Enter how many task you want to add="))
    for i in range (1,total_task+1):
        task_name = input(f"enter the task[i]=")## increase the task 
        task.append(task_name)


        print("today tasks are\n (task)")


        while True:
            operation = int(input("Enter 1-add\n 2 update /n 3 delete \n view \n Exit/stop"))
            if operation==1:
                add=input("enter a task whatever you want= add ")
                task.append(add)
                print(f"task {add} has been successfully added ")

            elif operation== 2:
                updated_val =input ("enter the task name you want to update=")
                if updated_val in task:
                 up=input("Enter a task") 
                ind =task.index(updated_val)   #2
                task[ind]=up
                print(f"updated task {up}")


                
    
            elif operation==3:
                del_val=input("which task to you want to delete=")
                if del_val in task:
                    ind = task.index(del_val)
                    del task[ind]
                    print(f"Task {del_val} has been deleted...")

                elif operation==4:
                    print(f"total task ={task}")
                elif operation==5:
                    print("closing task....")


