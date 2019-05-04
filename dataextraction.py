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

# We rather use the locally-cached file as it may have changed online.
pageContent = open('WebPages/rtvslo.si/Audi A6 50 TDI quattro_ nemir v premijskem razredu - RTVSLO.si.html', 'r').read()
# print("Page content:\n'%s'." % pageContent)

# Get the article date

# todo: find correct regex working on it now
regex = r"Audi A6 50 TDI quattro: nemir v premijskem razredu"

match = re.compile(regex).search(pageContent)
title = match.group(0)
print("Found title: '%s'." % title)

matches = re.finditer(regex, pageContent)
for match in matches:
    print("Found date: '{}'.".format(match.group(0)))


def openPageContent(page):
    return open(page, 'rb').read()


def xpathForRtvSlo(pageContent):
    tree = html.fromstring(pageContent)

    # author
    author = str(tree.xpath('//div[@class="author-name"]/text()')[0])

    # published time
    publishedTime = str(tree.xpath('//div[@class="publish-meta"]/text()')[0])
    publishedTime = publishedTime.replace('\n\t\t', ' ')
    # title
    title = str(tree.xpath('//header[@class="article-header"]//h1/text()')[0])

    # subtitle
    subTitle = str(tree.xpath('//div[@class="subtitle"]/text()')[0])

    # lead
    lead = str(tree.xpath('//p[@class="lead"]/text()')[0])

    # TODO: extract content properly
    content = tree.xpath('//article[@class="article"]/p/text()')
    content = ''.join(content)

    dataItem = {
        "Author": author,
        "PublishedTime": publishedTime,
        "Title": title,
        "SubTitle": subTitle,
        "Lead": lead,
        "Content": content
    }
    return json.dumps(dataItem, indent=4, ensure_ascii=False)


def xpathForOverstock(pageContent):
    tree = html.fromstring(pageContent)

    myData = []
    path = '//table[2]//tr[1]/td[last()]//tr[2]//tbody'

    tdCount = len(tree.xpath(path + '/tr[count(*)]')) - 3

    for x in range(1, tdCount, 2):

        if (x >= 21):
            x += 1

        # Title
        title = str(tree.xpath(path + '/tr[' + str(x) + ']/td[2]//b/text()')[0])
        # Content
        content = str(tree.xpath(path + '/tr[' + str(x) + ']/td[2]//td[2]/span[@class="normal"]/text()')[0])
        content = content.replace('\n', ' ')

        # ListPrice
        listprice = str(tree.xpath(path + '/tr[' + str(x) + ']/td[2]//td[1]//tr[1]/td[2]/s/text()')[0])

        # Price
        price = str(tree.xpath(path + '/tr[' + str(x) + ']//td[1]//tr[2]/td[2]//b/text()')[0])

        # Saving + saving percent
        save = str(tree.xpath(path + '/tr[' + str(x) + ']/td[2]//td[1]//tr[3]/td[2]/span/text()')[0])
        saving = save.split('(')[0].strip(" ")

        # SavingPercent
        savingpercent = save.split('(')[1].strip(" )")

        dataItem = {
            "Title": title,
            "Content": content,
            "ListPrice": listprice,
            "Price": price,
            "Saving": saving,
            "SavingPercent": savingpercent
        }

        myData.append(dataItem)
    return json.dumps(myData, indent=4)



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


if __name__ == "__main__":
    pageContent1 = openPageContent(page1)
    print(xpathForRtvSlo(pageContent1))
    pageContent2 = openPageContent(page2)
    print(xpathForRtvSlo(pageContent2))
    pageContent3 = openPageContent(page3)
    print(xpathForOverstock(pageContent3))
    pageContent4 = openPageContent(page4)
    print(xpathForOverstock(pageContent4))

    pageContentrtv1 = openCachedFile(page1)
    pageContentrtv2 = openCachedFile(page2)
    print(regexForRtvSlo(pageContentrtv1))
    print(regexForRtvSlo(pageContentrtv2))

    pageContentov3 = openCachedFile(page3)
    pageContentov4 = openCachedFile(page4)

    print("First page overstock:")
    print(regexForOverstock(pageContentov3))
    print("Second page overstock:")
    print(regexForOverstock(pageContentov4))
