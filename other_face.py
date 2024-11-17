import requests
url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'
 
direct = "face_photo\\Other_face\\"

all_urls = list()
path = r"dev_urls.txt"

def find_http(stri):
    if "http" in stri:
        str1 = "http" + stri.split("http")[1].split(".jpg")[0] +".jpg"
        all_urls.append(str1)
    
        


def get_urls(file_path):
    with open(file_path, "r") as f:
        for stringy in f.readlines():
            find_http(stringy)


def get_files(urls, dir):
    for i in range(len(urls)):
        try:
            response = requests.get(urls[i])
            file_Path = dir + f"\{i}.jpg"
            if response.status_code == 200:
                with open(file_Path, 'wb') as file:
                    file.write(response.content)
                print('File downloaded successfully')
            else:
                print('Failed to download file')
        except Exception:
            continue



get_urls(path)
get_files(all_urls, direct)





