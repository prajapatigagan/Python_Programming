import sqlite3

con = sqlite3.connect('youtube_video.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                  time TEXT NOT NULL 
    )
''')

def list_video():
    pass

def add_video():
    pass

def update_video():
    pass

def delete_video():
    pass

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List all youtube videos ")
        print("2. Add a youtube videos ")
        print("3. update youtube videos details ")
        print("4. Delete a youtube videos")
        print("5. Exit the app")
        choice = input("Enter your choice :")

        if choice=='1':
            list_video()
        elif choice=='2':
            name=input("Enter video name")
            time=input("Enter video time")
            add_video(name,time)
        elif choice=='3':
            video_id=input("ENter video id to update: ")
            name=input("Enter video name: ")
            time=input("Enter video time: ")
            update_video(video_id,name,time)
        elif choice=='4':
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("invalid choice")
    con.close()

if __name__ =="__main__":
    main()