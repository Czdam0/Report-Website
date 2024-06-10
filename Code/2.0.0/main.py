import webbrowser
import pymsgbox
import unhandled_exit
import requests
import json
import urllib3
from urllib.parse import urlparse

# Settings
email = pymsgbox.prompt('Please enter your email.')
name = pymsgbox.prompt('Please enter your name.')
urls_to_send_report = ["https://www.microsoft.com/en-us/wdsi/support/report-unsafe-site",
                "https://app.netbeacon.org/new-report",
                "https://support.drweb.com/new/urlfilter",
                "https://help.guard.io/hc/en-us/requests/new",
                "https://submit.gdatasoftware.com/url?lang=en",
                "https://www.fortiguard.com/webfilter",
                "https://www.abuseipdb.com/report",
                "https://www.brightcloud.com/tools/url-ip-lookup.php",
                "https://threatcenter.crdf.fr/submit_url.html",
                "https://www.malwareurl.com/listing-urls.php",
                "https://urlhaus.abuse.ch/browse/",
                "https://badbitcoin.org/report/",
                "https://urlfiltering.paloaltonetworks.com/",
                "https://phishing.eset.com/en-us/report",
                "https://scumware.org/add_url.php",
                "https://www.avg.com/en-us/report-malicious-file",
                "https://www.avast.com/report-malicious-file.php",
                "https://global.sitesafety.trendmicro.com/index.php",
                "https://www.bitdefender.com/consumer/support/answer/29358/",
                "https://sitelookup.mcafee.com/",
                "https://csi.forcepoint.com/",
                "https://sitereview.symantec.com/#/",
                "https://www.spam404.com/report.html",
                "https://www.avira.com/en/analysis/submit-url",
                "https://talosintelligence.com/reputation_center",
                "https://opentip.kaspersky.com/",
                "https://reportfraud.ftc.gov/#/",
                "https://www.cisa.gov/report",
                "https://reporting.actionfraud.police.uk/reporting",
                "https://www.ic3.gov/Home/ComplaintChoice"]


try:
    
    def prepare():
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        unhandled_exit.activate()

        print("Please copy the URL with the protocol and ending slash. For example, enter it as https://www.example.com/login rather than www.example.com")
        url = pymsgbox.prompt('URL? (Please copy the URL with the protocol and ending slash. For example, enter it as https://www.example.com/login rather than www.example.com)')
        print(url)
        return url
    url = prepare()

    def report_to_netcraft(reason, domain):
        urls_to_report = [f"https://{domain}/", f"http://{domain}/"]

        try:
            r = requests.post('https://report.netcraft.com/api/v3/report/urls', json={
                "email": email,
                "urls": [{
                    "reason": reason,
                    "url": urls_to_report,
                }],
            })
            r.raise_for_status()  

            response_json = r.json()
            print("Response JSON:", response_json)
            

        except requests.RequestException as e:
            print('An error occurred during the request:', str(e))
        except json.JSONDecodeError as e:
            print('Error parsing JSON response:', str(e))
            return None  

    def get_domain_from_url(url):
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return domain

    def error(reasonerror):
        if reasonerror.strip() == "":
            print("error")
            pymsgbox.alert('Report a Website had an error code undefined', 'error')
            quit()
        else:
            print("error " + reasonerror)
            pymsgbox.alert('Report a Website had an error code ' + reasonerror, 'error code ' + reasonerror)
            quit()

    def check_reason(reason):
        if reason.strip() != "":
            return reason.strip()
        else:
            print("reason empty")
            error("reason empty")

    # Check URL
    def check_url(url, domain):
        if url.strip() != "":
            webbrowser.open_new_tab(f"https://www.virustotal.com/gui/domain/{domain}")
            webbrowser.open_new_tab(f"https://www.virustotal.com/gui/search/https%253A%252F%252F{domain}")
            webbrowser.open_new_tab(f"https://www.virustotal.com/gui/search/http%253A%252F%252F{domain}")
            webbrowser.open_new_tab(f"https://www.urlvoid.com/update/{domain}")
            print("Do you want to report this site?")
            report = pymsgbox.confirm('Do you want to report this site?', 'Report', ["Yes", 'No'])
            print(report)
            if report == "Yes":
                start_report(url, domain)
            else:
                exit()
        else:
            print("url empty")
            error("url empty")

    # Check next step
    def check_next(check):
        if check == 'stop':
            print("stop")
            quit()
        else:
            return print("good")
        
    # Report a website
    def start_report(url, domain):
        reason = check_reason(pymsgbox.prompt('Please submit a reason for reporting this website?'))
        print(reason)
        print(report_to_netcraft(reason, url))
        webbrowser.open_new_tab(f"https://phish.report/{url}")

        check_next(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
        webbrowser.open_new_tab(f"mailto:reportphishing@apple.com?subject={url}&body={url}%20was%20reported%20using%20an%20automated%20tool%20for%20the%20reason%20{reason}")
        check_next(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
        webbrowser.open_new_tab(f"mailto:reportphishing@apwg.org?subject={url}&body={url}%20was%20reported%20using%20an%20automated%20tool%20for%20the%20reason%20{reason}")
        check_next(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
        webbrowser.open_new_tab(f"mailto:reportphishing@antiphishing.org?subject={url}&body={url}%20was%20reported%20using%20an%20automated%20tool%20for%20the%20reason%20{reason}")
        check_next(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
        webbrowser.open_new_tab(f"mailto:phishing-report@us-cert.gov?subject={url}&body={url}%20was%20reported%20using%20an%20automated%20tool%20for%20the%20reason%20{reason}")
        check_next(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
        webbrowser.open_new_tab(f"mailto:samples@sophos.com?subject=Sample%20submitted%20for%20analysis%20{url}&body={url}%20was%20reported%20using%20an%20automated%20tool%20for%20the%20reason%20{reason}")

        check_next(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
        webbrowser.open_new_tab(f"https://safebrowsing.google.com/safebrowsing/report_phish/?url=http://{url}/")

        for i in range(len(urls_to_send_report)):
            check_next(pymsgbox.confirm('Continue?', 'continue?', ["continue", 'stop']))
            webbrowser.open_new_tab(urls_to_send_report[i])

    domain = get_domain_from_url(url)
    check_url(url, domain)

except Exception as e:
    error_type = str(e)
    print('An error occurred: ' + error_type)
    exit()
