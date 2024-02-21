

def sendRequest():
    location = "testLocation"
    query = '[out:json];area["admin_level"="8"]["name"="' + location + '"];out body;node"highway"="speed_camera";out body;>;out skel qt;'
    return query
    

def main():
    print("test")
    print(sendRequest)


if __name__ == "__main__":
    main()


