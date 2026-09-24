import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test= json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
    
def List_all_videos(videos):
    print("\n")
    print("*"*20)
    def List_all_videos(videos):
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']}, Duration: {video['time']}")

def Add_Youtube_videos(videos):
    name=input("Enter videos name ")
    time=input("Enter videos Time ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def Update_Youtube_videos(videos):
    List_all_videos(videos)
    int(input("Enter the vadio no. to update"))
    if 1<=index<=len(videos):
        name=input("Enter the new Video name")
        time=input("Enter the new video time")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("invalid index")


def Delete_Youtube_videos(videos):
    List_all_videos(videos)
    index=int(input("Enter the video no. too be deleted"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index select")

def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube videos ")
        print("3. update youtube videos details ")
        print("4. Delete a youtube videos")
        print("5. Exit the app")
        choose = input("Enter your choice ")
        # print(videos)

        match choose:
            case '1':
                List_all_videos(videos)
            case '2':
                Add_Youtube_videos(videos)
            case '3':
                Update_Youtube_videos(videos)
            case '4':
                Delete_Youtube_videos(videos)  
            case '5':
                break
            case _:
                print("Invalid choice") 

if __name__ == "__main__":
    main()
           
