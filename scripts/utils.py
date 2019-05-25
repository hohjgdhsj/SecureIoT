from collections import defaultdict
from datetime import datetime, timedelta


def parseEvidence(evidence):
    evidenceSplit = evidence.split()
    d = defaultdict()
    d['os'] = evidenceSplit[0]
    try:
        d['arch'] = evidenceSplit[10]
    except:
        d['arch'] = "NA"
    try:
        d['dev'] = evidenceSplit[1]
    except:
        d['dev'] = "NA"
    return d


def currentTime():
    return datetime.now().replace(microsecond=0)


def getPort(protocol):
    """ A list of ports we will check for """
    p = defaultdict()
    p["SSH"] = 22
    p["FTP"] = 21
    p["HTTP"] = 80
    p["Telnet"] = 23
    p["POP3"] = 110
    p["SMB"] = 445
    return p[protocol]


def getLast15Dates():
    dates = []
    for i in range(15):
        d = datetime.today() - timedelta(days=14 - i)
        dates.append(d.strftime('%Y-%m-%d'))
    return dates