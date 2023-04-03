import webbrowser, pymsgbox, unhandled_exit
unhandled_exit.activate()

def error(reasonerror):
    if reasonerror == "" or " ":
        print("error") 
        pymsgbox.alert('Report a Website had an error', 'error')
        quit()
    else:
        print("error "+reasonerror) 
        pymsgbox.alert('Report a Website had an error '+reasonerror, 'error '+reasonerror)
        quit()    

def checkreason(reason):
    if reason != "" or " ":
        return reason
    else:
        print("url empty")
        error("url empty")

    
def checkurl(url):
    if url != "" or " ":
        return url
    else:
        print("url empty")
        error("url empty")

def checknext(check):
    if check == 'stop':
        print("stop")
        quit()
    else:
        return print("good")

def Report(url):

    reason = checkreason(pymsgbox.prompt('Please submit a reason for reporting this website?'))
    webbrowser.open_new_tab("https://phish.report/"+url)
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://safebrowsing.google.com/safebrowsing/report_phish/?url=http://"+url+"/")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://www.microsoft.com/en-us/wdsi/support/report-unsafe-site")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://support.drweb.com/new/urlfilter")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://help.guard.io/hc/en-us/requests/new")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://www.fortiguard.com/webfilter")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://www.brightcloud.com/tools/url-ip-lookup.php")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://threatcenter.crdf.fr/submit_url.html")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://report.netcraft.com/report")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://urlfiltering.paloaltonetworks.com/")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://phishing.eset.com/en-us/report")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://scumware.org/add_url.php")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://www.avast.com/report-malicious-file.php")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://global.sitesafety.trendmicro.com/index.php")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://www.bitdefender.com/consumer/support/answer/29358/")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://sitelookup.mcafee.com/")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://csi.forcepoint.com/")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://sitereview.symantec.com/#/")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://www.spam404.com/report.html")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://www.avira.com/en/analysis/submit-url")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://talosintelligence.com/reputation_center")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://opentip.kaspersky.com/")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://reportfraud.ftc.gov/#/")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://www.cisa.gov/report")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://www.ic3.gov/Home/ComplaintChoice")
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("mailto:reportphishing@apple.com?subject="+url+"&body="+url+"%20rwas%20repoted%20using%20an%20automated%20tool%20for%20the%20reason"+reason)
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("mailto:reportphishing@apwg.org?subject="+url+"&body="+url+"%20rwas%20repoted%20using%20an%20automated%20tool%20for%20the%20reason"+reason)

type = pymsgbox.confirm('Do you want to report this site?', 'Report', ["http", 'https', 'scan only domain', 'full scan'])
print(type)

if type == "http" or "https" or "scan only domain" or "full scan":

    if type == "http":
        print("please copy url without dir like this www.example.com and no like this https://www.example.com/home")
        url = checkurl(pymsgbox.prompt('url? (please copy url without dir like this www.example.com and no like this https://www.example.com/home)'))
        print(url)
        print("http scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/https%253A%252F%252F"+url)
        print("Do you want to report this site?")
        report = pymsgbox.confirm('Do you want to report this site?', 'Report', ["Yes", 'No'])
        print(report)
        if report == "Yes":
            Report(url)
        else:
            exit()
    elif type == "https":
        print("please copy url without dir like this www.example.com and no like this https://www.example.com/home")
        url = checkurl(pymsgbox.prompt('url? (please copy url without dir like this www.example.com and no like this https://www.example.com/home)'))
        print(url)
        print("https scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/http%253A%252F%252F"+url)
        print("Do you want to report this site?")
        report = pymsgbox.confirm('Do you want to report this site?', 'Report', ["Yes", 'No'])
        print(report)
        if report == "Yes":
            Report(url)
        else:
            exit()
    elif type == "scan only domain":
        print("please copy url without dir like this www.example.com and no like this https://www.example.com/home")
        url = checkurl(pymsgbox.prompt('url? (please copy url without dir like this www.example.com and no like this https://www.example.com/home)'))
        print(url)
        print("Domain scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/domain/"+url)
        print("Do you want to report this site?")
        report = pymsgbox.confirm('Do you want to report this site?', 'Report', ["Yes", 'No'])
        print(report)
        if report == "Yes":
            Report(url)
        else:
            exit()
    elif type == "full scan":
        print("please copy url without dir like this www.example.com and no like this https://www.example.com/home")
        url = checkurl(pymsgbox.prompt('url? (please copy url without dir like this www.example.com and no like this https://www.example.com/home)'))
        print(url)
        print("full scan")
        webbrowser.open_new_tab("https://www.virustotal.com/gui/domain/"+url)
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/https%253A%252F%252F"+url)
        webbrowser.open_new_tab("https://www.virustotal.com/gui/search/http%253A%252F%252F"+url)
        print("Do you want to report this site?")
        report = pymsgbox.confirm('Do you want to report this site?', 'Report', ["Yes", 'No'])
        print(report)
        if report == "Yes":
            Report(url)
        else:
            exit()
    else:
        error()
else:
    error()
