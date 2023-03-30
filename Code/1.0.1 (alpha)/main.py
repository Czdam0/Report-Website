import webbrowser, time, pymsgbox

print("1 for http")
print("2 for https")
print("3 to scan only domain")
print("4 for full scan")

def Report(url):
    webbrowser.open_new_tab("https://phish.report/"+url)
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://safebrowsing.google.com/safebrowsing/report_phish/")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://www.microsoft.com/en-us/wdsi/support/report-unsafe-site")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://www.fortiguard.com/webfilter")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://www.brightcloud.com/tools/url-ip-lookup.php")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://threatcenter.crdf.fr/submit_url.html")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://report.netcraft.com/report")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://urlfiltering.paloaltonetworks.com/")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://phishing.eset.com/en-us/report")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://global.sitesafety.trendmicro.com/index.php")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://www.bitdefender.com/consumer/support/answer/29358/")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://sitelookup.mcafee.com/")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://csi.forcepoint.com/")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://sitereview.symantec.com/#/")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://www.spam404.com/report.html")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://www.avira.com/en/analysis/submit-url")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://talosintelligence.com/reputation_center")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://opentip.kaspersky.com/")
    input("press 1 for next report website")
    webbrowser.open_new_tab("https://reportfraud.ftc.gov/#/")



type = str(input(""))
if type == "1" or "2" or "3" or "4":

    if type == "1":
        print("please copy url without dir like this www.example.com and no like this https://www.example.com/home")
        url = input("url?")
        print("http scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/https%253A%252F%252F"+url)
        print("Do you want to report this site?")
        print("1 = yes 2 = no")
        report = str(input())
        if report == "1":
            Report(url)
        else:
            quit()
    elif type == "2":
        print("please copy url without dir like this www.example.com and no like this https://www.example.com/home")
        url = input("url?")
        print("https scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/http%253A%252F%252F"+url)
        print("Do you want to report this site?")
        print("1 = yes 2 = no")
        report = str(input())
        if report == "1":
            Report(url)
        else:
            quit()
    elif type == "3":
        print("please copy url without dir like this www.example.com and no like this https://www.example.com/home")
        url = input("url?")
        print("Domain scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/domain/"+url)
        print("Do you want to report this site?")
        print("1 = yes 2 = no")
        report = str(input())
        if report == "1":
            Report(url)
        else:
            quit()
    elif type == "4":
        print("please copy url without dir like this www.example.com and no like this https://www.example.com/home")
        url = input("url?")
        print("full scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/domain/"+url)
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/https%253A%252F%252F"+url)
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/http%253A%252F%252F"+url)
        print("Do you want to report this site?")
        print("1 = yes 2 = no")
        report = str(input())
        if report == "1":
            Report(url)
        else:
            quit()
    else:
        print("error") 
        pymsgbox.alert('Report a Website had an error', 'error')
        quit()
else:
    print("error") 
    pymsgbox.alert('Report a Website had an error', 'error')
    quit()
