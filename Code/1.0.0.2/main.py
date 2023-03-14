import webbrowser
print("1 for http")
print("2 for https")
print("3 to scan only domain")
print("4 for full scan")

type = str(input(""))
if type == "1" or "2" or "3" or "4":
    print("please copy url without dir like this www.example.com and no like this https://www.example.com/home")
    url = input("url?")
    if type == "1":
        print("http scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/https%253A%252F%252F"+url)
    elif type == "2":
        print("https scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/http%253A%252F%252F"+url)
    elif type == "3":
        print("Domain scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/domain/"+url)
    elif type == "4":
        print("full scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/domain/"+url)
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/https%253A%252F%252F"+url)
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/http%253A%252F%252F"+url)
    else:
        quit()

    if type == "1" or "2" or "3" or "4":
        print("Do you want to report this site?")
        print("1 = yes 2 = no")
        report = str(input())
        if report == "1":
            webbrowser.open_new_tab("https://phish.report/"+url)
        else:
            quit()
    else:
        quit()
else:
    print("error please type only 1 2 3 or 4") 
    quit()


