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
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name, time))
    con.commit()
def update_video(new_name,new_time,video_id):
    cursor.execute("UPDATE videos SET name=?,time=?,where id=?",(new_name,new_time,video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?", (video_id,))
    cursor.commit()
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