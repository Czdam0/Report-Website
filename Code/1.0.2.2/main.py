import webbrowser, pymsgbox, unhandled_exit
unhandled_exit.activate()

def error(reasonerror):
    if reasonerror.strip() == "":
        print("error") 
        pymsgbox.alert('Report a Website had an error code undefined', 'error')
        quit()
    else:
        print("error "+reasonerror) 
        pymsgbox.alert('Report a Website had an error code '+reasonerror, 'error code '+reasonerror)
        quit()    

def checkreason(reason):
    if reason.strip() != "":
        return reason.strip()
    else:
        print("reason empty")
        error("reason empty")

def checkurl(url):
    if url.strip() != "":
        return url.strip()
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
    print(reason)
    webbrowser.open_new_tab("https://phish.report/"+url)
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("https://safebrowsing.google.com/safebrowsing/report_phish/?url=http://"+url+"/")

    urls = [  "https://www.microsoft.com/en-us/wdsi/support/report-unsafe-site",    "https://forms.gle/7ZU62nbFeTdGDFsn8",  "https://support.drweb.com/new/urlfilter",    "https://help.guard.io/hc/en-us/requests/new",    "https://www.fortiguard.com/webfilter",    "https://www.abuseipdb.com/report",    "https://www.brightcloud.com/tools/url-ip-lookup.php",    "https://threatcenter.crdf.fr/submit_url.html",    "https://www.malwareurl.com/listing-urls.php",    "https://urlhaus.abuse.ch/browse/",    "https://badbitcoin.org/report/",    "https://www.urlvoid.com/",    "https://report.netcraft.com/report",    "https://urlfiltering.paloaltonetworks.com/",    "https://phishing.eset.com/en-us/report",    "https://scumware.org/add_url.php",    "https://www.avast.com/report-malicious-file.php",    "https://global.sitesafety.trendmicro.com/index.php",    "https://www.bitdefender.com/consumer/support/answer/29358/",    "https://sitelookup.mcafee.com/",    "https://csi.forcepoint.com/",    "https://sitereview.symantec.com/#/",    "https://www.spam404.com/report.html",    "https://www.avira.com/en/analysis/submit-url",    "https://talosintelligence.com/reputation_center",    "https://opentip.kaspersky.com/",    "https://reportfraud.ftc.gov/#/",    "https://www.cisa.gov/report",    "https://reporting.actionfraud.police.uk/reporting",    "https://www.ic3.gov/Home/ComplaintChoice"]

    for i in range(len(urls)):
        checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
        webbrowser.open_new_tab(urls[i])

    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("mailto:reportphishing@apple.com?subject="+url+"&body="+url+"%20was%20repoted%20using%20an%20automated%20tool%20for%20the%20reason "+reason)
    checknext(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
    webbrowser.open_new_tab("mailto:reportphishing@apwg.org?subject="+url+"&body="+url+"%20was%20repoted%20using%20an%20automated%20tool%20for%20the%20reason "+reason)

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
        error("")
else:
    error("")