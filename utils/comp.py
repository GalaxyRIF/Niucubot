import urllib.request
from bs4 import BeautifulSoup
# process command to get get_comp args, then call get_comps and return

events_map={
        ".3":"333",
        ".333":"333",
        ".3bf":"333bf",
        ".333bf":"333bf",
        ".4":"444",
        ".444":"444",
        ".4bf":"444bf",
        ".444bf":"444bf",
        ".5":"555",
        ".555":"555",
        ".5bf":"555bf",
        ".555bf":"555bf",
        ".6":"666",
        ".666":"666",
        ".7":"777",
        ".777":"777",
        ".clock":"clock",
        ".cl":"clock",
        ".pyr":"pyram",
        ".pyram":"pyram",
        ".py":"pyram",
        ".p":"pyram",
        ".mega":"minx",
        ".minx":"minx",
        ".skewb":"skewb",
        ".sk":"skewb",
        ".sq":"sq1",
        ".sq1":"sq1",
    }

# events argument parser
# eg .comp -rcn -soc -e4/5/6+7

def events_parser(message):
    """
    If not specified , return 'all'
    Else, return a sequence of events"""
    # beginning with ".comp"
    content=message[5:]
    if content=="":
        return "all"
    else:
        events=[]
        stack=""
        for i in range(len(content)):
            if content[i]!="+":
                stack=stack+content[i]
            else:
                if stack in events_map.keys():
                    events.append(events_map[stack])
                else:
                    # Fail to identify rhe event, considered Null event
                    pass
        # todo: modify get_comp to adapt to list of events
        return events

# reads competition info
def get_comp(events="all",region="UK",comp_type=["open","closed","upcoming","full","progress"]):
    """
    Return a list of tuple of the form ("comp-name","comp-location","comp-date")
    type: on, upcoming, all
    Default url set to https://www.worldcubeassociation.org/competitions?region=United+Kingdom&search=&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list 
    which is the url for U.K. competitions
    """
    if region in ("uk","UK","u.k."):
        url_competition_list="https://www.worldcubeassociation.org/competitions?region=United+Kingdom&search=&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list"
    elif region in ("eu","EU","europe","Europe"):
        url_competition_list="https://www.worldcubeassociation.org/competitions?region=_Europe&search=&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list"
    elif region in ("china","cn","CN","China"):
        url_competition_list="https://www.worldcubeassociation.org/competitions?region=China&search=&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list"
    elif region in ("Asia","asia","as"):
        url_competition_list="https://www.worldcubeassociation.org/competitions?region=_Asia&search=&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list"    
    else:
        url_competition_list="https://www.worldcubeassociation.org/competitions?region=all&search=&state=present&year=all+years&from_date=&to_date=&delegate=&show_registration_status=on&display=list"
    competition_list_html=urllib.request.Request(url_competition_list, headers={'User-Agent': 'User-Agent:Mozilla/5.0'})
    html_decoded=urllib.request.urlopen(competition_list_html).read().decode(encoding='utf-8')
    bs=BeautifulSoup(html_decoded,"html.parser")
    comps_on=[]
    if "progress" in comp_type:
        try:
            comps_on+=bs.find(class_="col-md-12",id=("in-progress-comps")).find(class_="list-group").find_all(class_="list-group-item not-past")
        except:
            pass
    if ("open" in comp_type) or ("closed" in comp_type) or ("full" in comp_type) or ("upcoming" in comp_type):
        try:
            comps_on+=bs.find(class_="col-md-12",id=("upcoming-comps")).find(class_="list-group").find_all(class_="list-group-item not-past")
        except:
            pass
    if comps_on==[]:
        return None
    # else:
    #     comps_on+=bs.find(class_="col-md-12",id=("upcoming-comps")).find(class_="list-group").find_all(class_="list-group-item not-past")
    #     try:
    #         ongoningcomps=bs.find(class_="col-md-12",id=("in-progress-comps")).find(class_="list-group").find_all(class_="list-group-item not-past")
    #         comps_on+=ongoningcomps
    #     except:
    #         pass

    comp_info=[]
    for each in comps_on:
        comp_name=each.find("a",href=True).contents[0]
        comp_loc=each.find(class_="location").contents
        comp_location=comp_loc[1].contents[0]+comp_loc[2][:-9]
        comp_date=each.find(class_="date").contents[2][8:-7]
        l=each.contents[1].contents[1]
        if "red" in l["class"]:
            if not "closed" in comp_type:
                continue
            status="Registration closed"
        elif "orange" in l["class"]:
            if not "full" in comp_type:
                continue
            status="full"
        elif "green" in l["class"]:
            status="open"
            if not "open" in comp_type:
                continue
        elif "blue" in l["class"]:
            status=l["title"]
            if not "upcoming" in comp_type:
                continue
        elif "hourglass" in l["class"]:
            status="Competition in progress!"
            if not "progress" in comp_type:
                continue
        comp_info.append((comp_name,comp_location,comp_date,status))
    return comp_info



def return_comps(contents):
    # contents is [".comp","arg1","arg2","arg3","arg4"]
    # arg types: status, region, events
    # -e events -r region -s status
    # -s: f for full, o for open, c for closed, u for upcoming
    events="all"
    region="UK"
    comp_type=[]
    num=10
    for i in contents[1:]:
        if "-e" in i:
            pass
        elif "-r" in i:
            region=i[2:]
        elif "-s" in i:
            if 'f' in i[2:]:
                comp_type.append("full")
            if  'o' in i[2:]:
                comp_type.append("open")
            if  'c' in i[2:]:
                comp_type.append("closed")
            if  'u' in i[2:]:
                comp_type.append("upcoming")
            if  'p' in i[2:]:
                comp_type.append("progress")
        elif "-n" in i :
            num=min(30,int(i[2:]))
    if comp_type==[]:
        comp_type=["open","closed","upcoming","full"]
    
    comp_list=get_comp(events,region,comp_type)
    if comp_list is None:
        return "No competition found!!!"
    if region=="all":
        region_txt=""
    else:
        region_txt=" in %s"%region
    num=min(num,len(comp_list))
    txt="%d Recent competitions%s:\n"%(num,region_txt)
    comp_list=comp_list[:num]
    for i in range(len(comp_list)):
        each=comp_list[i]
        txt+=f"{i+1}. {each[0]} | {each[1]} | {each[2]} | {each[3]}\n"
    return txt[:-1]


