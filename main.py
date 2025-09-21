from tasks import get_todays_tasks

def main():
    for task in get_todays_tasks():
        print(task)



if __name__ == "__main__":
    main()