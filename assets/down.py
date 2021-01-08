import os
while 1:
    url = input("Asset URL: ")
    name = input("Save as: ")
    
    os.system("wget -O " + name + " --no-check-certificate " + url)
    
    os.system("clear")
    print("URL: https://cdn.jsdelivr.net/gh/orange2008/cloudflare-workers-blog@master/assets/" + name)
