import requests

def fetch_rendam_user_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomusers/13"
    responce=requests.get(url)
    data=responce.json() 

    if data["success"] and "data" in data:
        user_data=data["data"]
        username=user_data["login"]["username"]
        password=user_data["login"]["password"]
        return username,password
    else:
        raise Exception("faild to fatch user data")

def main():
    try:
        username,password=fetch_rendam_user_freeapi()
        print(f"Username:{username} \n Password: {password}")
    except Exception as e:
        print(str(e))
              

if __name__=="__main__":
    main()