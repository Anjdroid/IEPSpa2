# Import libraries
import requests
import re
from lxml import html
import json

page1 = 'WebPages/rtvslo.si/Audi A6 50 TDI quattro_ nemir v premijskem razredu - RTVSLO.si.html'
page2 = 'WebPages/rtvslo.si/Volvo XC 40 D4 AWD momentum_ suvereno med najboljs╠îe v razredu - RTVSLO.si.html'
page3 = 'WebPages/overstock.com/jewelry01.html'
page4 = 'WebPages/overstock.com/jewelry02.html'
page5 = 'WebPages/hm/Dresses _ Maxi, Party, Evening & More _ H&M GB.html'
page6 = 'WebPages/ebay/headphones _ eBay.html'






















































































































def openCachedFile(page):
	return open(page, 'r').read()

def regexForRtvSlo(pageContent):
    #Title
    ##regex_title_simple = r"<h1>(.*)<\/h1>"
    regex_title = r"<header class=\"article-header\">(.|\n)*?<h1>(.*?)<\/h1>"

    match = re.compile(regex_title).search(pageContent)
    title = match.group(2)
    #print("Found title: '{}'".format( title ))

    #Author and timestamp
    regex_author_timestamp = r'<div class="author-timestamp">\s+<strong>(.*?)<\/strong>\|\s+([0-9]{2}\.\s+[a-z]*\s+[0-9]{4}\s+ob\s+[0-9]{2}:[0-9]{2})'

    match = re.compile(regex_author_timestamp).search(pageContent)
    author = match.group(1)
    timestamp = match.group(2)
    #print("Found author: '{}'".format(author))
    #print("Found timestamp: '{}'".format(timestamp))

    #Subtitle
    regex_subtitle = r'<div class="subtitle">(.*)</div>'

    match = re.compile(regex_subtitle).search(pageContent)
    subtitle = match.group(1)
    #print("Found subtitle: '{}'".format(subtitle))

    #Lead
    regex_lead = r'<p class="lead">(.*)</p>'

    match = re.compile(regex_lead).search(pageContent)
    lead = match.group(1)
    #print("Found lead: '{}'".format(lead ))

    #Content
    regex_content = r'<article class="article">((.|\n)*?)</article>'

    match = re.compile(regex_content).search(pageContent)
    extracted_html = match.group(0)
    content = " "
    ##print("Found html content: '{}'".format( match.group(0) ))

    regex_content_p = r'<p( class="Body")?>(?!<iframe.*?</iframe>)((.|\n)*?)</p>'
    matches = re.finditer(regex_content_p, extracted_html)
    for match in matches:
        ##print("Found content_u: '{}'".format(match.group(2)))
        content = content + match.group(2).replace("<br>", " ").replace("<strong>", " ").replace("</strong>", " ")

    #print("Found content: '{}'".format( content ))

    dataItem = {
        "Author": author,
        "PublishedTime": timestamp,
        "Title": title,
        "SubTitle": subtitle,
        "Lead": lead,
        "Content": content
    }
    return json.dumps(dataItem, indent=4, ensure_ascii=False)


def regexForOverstock(pageContent):
    #List price
    listprice = []
    regex_listprice = r'List Price:.*<s>(.*)</s>'

    matches = re.finditer(regex_listprice, pageContent)
    for match in matches:
        #print("Found list price: '{}'".format( match.group(1) ))
        listprice.append(match.group(1))

    #Price
    price = []
    regex_price = r'Price:.*<span class="bigred"><b>(.*)</b></span>'

    matches = re.finditer(regex_price, pageContent)
    for match in matches:
        #print("Found price: '{}'".format( match.group(1) ))
        price.append(match.group(1))

    #Saving and saving percent
    saving = []
    savingPercent = []
    regex_save = r'You Save:.*<span class="littleorange">(\$[0-9\.,]*) \(([0-9]{1,3}%)\)</span>'

    matches = re.finditer(regex_save, pageContent)
    for match in matches:
        #print("Found Saving: '{}'".format(match.group(1)))
        #print("Found SavingPercent: '{}'".format( match.group(2) ))
        saving.append(match.group(1))
        savingPercent.append(match.group(2))


    #Title
    title = []
    regex_title = r'<td valign="top">\s*<a href=".*?"><b>(.*)</b></a>'

    matches = re.finditer(regex_title, pageContent)
    for match in matches:
        #print("Found title: '{}'".format( match.group(1) ))
        title.append(match.group(1))

    #Content
    content = []
    regex_content = r'<span class="normal">((.|\n)*?)<br>'

    matches = re.finditer(regex_content, pageContent)
    for match in matches:
        content_pretified = match.group(1).replace("\n", " ").replace("  ", " ")
        #print("Found content: '{}'".format(content_pretified))
        content.append(content_pretified)

    dataList = []
    for i in range(len(listprice)):
        dataItem = {
            "Title": title[i],
            "Content": content[i],
            "ListPrice": listprice[i],
            "Price": price[i],
            "Saving": saving[i],
            "SavingPercent": savingPercent[i]
        }
        dataList.append(dataItem)
    return json.dumps(dataList, indent = 4)

pageContent1 = openCachedFile(page1)
pageContent2 = openCachedFile(page2)
print(regexForRtvSlo(pageContent1))
print(regexForRtvSlo(pageContent2))

pageContent3 = openCachedFile(page3)
pageContent4 = openCachedFile(page4)

print("First page overstock:")
print(regexForOverstock(pageContent3))
print("Second page overstock:")
print(regexForOverstock(pageContent4))
