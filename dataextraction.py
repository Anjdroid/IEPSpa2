# Import libraries
import requests
import re
from lxml import html
import json

page1 = 'WebPages/rtvslo.si/Audi A6 50 TDI quattro_ nemir v premijskem razredu - RTVSLO.si.html'
page2 = 'WebPages/rtvslo.si/Volvo XC 40 D4 AWD momentum_ suvereno med najboljs╠îe v razredu - RTVSLO.si.html'
page3 = 'WebPages/overstock.com/jewelry01.html'
page4 = 'WebPages/overstock.com/jewelry02.html'
page5 = 'WebPages/ebay/headphones _ eBay.html'
page6 = 'WebPages/ebay/laptops in _Computers, Tablets, and Networking_ _ eBay.html'



def openPageContent(page):
    # reading as a string to preserve UTF-8 encoding
    return open(page, 'r', errors='ignore').read()

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
    content = tree.xpath('//article[@class="article"]/p/text() | //p/strong/text() | //p/sub/text()')
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
        content = content + match.group(2).replace("<br>", " ").replace("<strong>", " ").replace("</strong>", " ").replace("<sub>", " ").replace("</sub>", " ")
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


def xpathForEbay(pageContent):
    tree = html.fromstring(pageContent)

    # Titles
    titles = tree.xpath('//h3[@class="s-item__title"]/text()'
                        '| //h3[@class="s-item__title"]/span[not(contains(@class, "LIGHT_HIGHLIGHT"))]/text()')

    # Conditions
    itemsConds = tree.xpath('//span[@class="SECONDARY_INFO"]/text()')

    # Locations
    itemsLocs = tree.xpath('//span[@class="s-item__location s-item__itemLocation"]/text()')

    # Shippings
    itemsShippings = tree.xpath('//span[@class="s-item__shipping s-item__logisticsCost"]/text()'
                              '| //span[@class="s-item__shipping s-item__logisticsCost"]/span[@class="BOLD"]/text()')

    # Buying methods
    # Buying method can be a bit or ability to purchase, that is why we extract two diferent elements
    itemsBuyMethods = tree.xpath('//span[@class="s-item__purchase-options s-item__purchaseOptions"]/text()'
                               '| //span[@class="s-item__bids s-item__bidCount"]/text()')

    # Prices
    itemsPrices = tree.xpath('//span[@class="s-item__price"]/span[contains(text(),"to")]/text()'
                           '| //span[@class="s-item__price"]/text()')

        # span can contain price in a form x$ to y$, both prices are in the same span, therefore
        # the following code merges two prices for the same item in one element in the list
    length = len(itemsPrices)
    i = 0
    while (i < length):
        if (itemsPrices[i] == " to "):
            element = itemsPrices[i - 1] + itemsPrices[i] + itemsPrices[i + 1]
            itemsPrices.pop(i + 1)
            itemsPrices.pop(i)
            itemsPrices.pop(i - 1)
            length -= 2
            itemsPrices.insert((i - 1), element)
            i -= 1
        i += 1

    # Desirabilities or hotness of items

    itemsHotness = tree.xpath('//div[@class="s-item__details clearfix"]'
                             '| //span[@class="s-item__hotness s-item__itemHotness"]/span[@class="BOLD NEGATIVE"]/text()')

        # Because  xpath does not tell us if an item has a certain property or not, or not that we know of,
        # we extract all items from the page(using class item details) as xpath objects
        # and then again only the items that have the property hotness which we extract as a text and combine the output,
        # now we have some duplicated items
        # the ones that have the hotness property we extracted them as an xpath object and also as a text(string)
        # in the code below we remove the xpath objects that also have a string representation
    length = len(itemsHotness)
    i = 0
    str_bolean = isinstance(itemsHotness[i], str)
    while (i < length):
        if (isinstance(itemsHotness[i], str)):
            itemsHotness.pop(i - 1)
            length -= 1
            i -= 1
        i += 1

        # Now we only have one istance of each item, but in difrent formats
        # Taking the items that are not strings from the list and inserting empty strings instead,
        # because those items have no property hotness
    i = 0
    while (i < len(itemsHotness)):
        if (not isinstance(itemsHotness[i], str)):
            itemsHotness.pop(i)
            itemsHotness.insert(i, "")
        i += 1

    dataList = []
    for i in range(len(itemsHotness)):
        dataItem = {
            "Title": titles[i],
            "ItemCondition": itemsConds[i],
            "Price": itemsPrices[i],
            "BuyingMethod": itemsBuyMethods[i],
            "ItemLocation": itemsLocs[i],
            "ShippingCost": itemsShippings[i],
            "ItemHotness": itemsHotness[i]
        }
        dataList.append(dataItem)
    return json.dumps(dataList, indent=4)


def regexForEbay(pageContent):

    # Titles

    titles = []
    regex_title = r'<h3 class="s-item__title">(<span class="LIGHT_HIGHLIGHT">.*?</span>)?(<span class="BOLD">)?(.*?)(</span>)?</h3>'

    matches = re.finditer(regex_title, pageContent)
    for match in matches:
        titles.append(match.group(3))


    # Item Conditionss

    item_conditions = []
    regex_itemCondition = r'<span class="SECONDARY_INFO">(.*?)</span>'

    matches = re.finditer(regex_itemCondition, pageContent)
    for match in matches:
        item_conditions.append(match.group(1))

    # Item Locations

    item_locations = []
    regex_location = r'<span class="s-item__location s-item__itemLocation">(.*?)</span>'

    matches = re.finditer(regex_location, pageContent)
    for match in matches:
        item_locations.append(match.group(1))

    # Item prices

    item_prices = []
    regex_price = r'<span class="s-item__price">(\$[0-9]*\.[0-9]*)(<span class="DEFAULT">)?(.*?)(</span>)?(\$[0-9]*\.[0-9]*)?</span>'

    matches = re.finditer(regex_price, pageContent)
    for match in matches:
        # if the price looks like : x$ to y$
        if (match.group(3) and match.group(5)):
            price = match.group(1) + match.group(3) + match.group(5)
        else:
            price = match.group(1)
        # print("Found price:"+price)
        item_prices.append(price)

    # Shippings

    item_shippings = []
    regex_shipping = r'<span class="s-item__shipping s-item__logisticsCost">(<span class="BOLD">)?(.*?)(</span>)?</span>'

    matches = re.finditer(regex_shipping, pageContent)
    for match in matches:
        # print("Found shipping: '{}'".format( match.group(2) ))
        item_shippings.append(match.group(2))

    # BuyMethods

    item_buymethods = []
    regex_buyMethod = r'<div class="s-item__detail s-item__detail--primary">((<span class="s-item__bids s-item__bidCount">)|(<span class="s-item__purchase-options s-item__purchaseOptions">))(.*?)</span>'

    matches = re.finditer(regex_buyMethod, pageContent)
    for match in matches:
        # print("Found buy method: '{}'".format(match.group(4)))
        item_buymethods.append(match.group(4))

    # Item Hotness

    items_hotness = []
    regex_itemHotness = r'<span class="s-item__hotness s-item__itemHotness" aria-label="">(<span class="clipped">.*?</span>)?<span class="BOLD NEGATIVE">(.*?)</span></span>'
    regex_all_item_details = r'<div class="s-item__details clearfix">.*?</li>'

    items = re.finditer(regex_all_item_details, pageContent)
    for el in items:
        match = re.compile(regex_itemHotness).search(el.group(0))
        if (match):
            item_hotness = match.group(2)
            # print(item_hotness)
        else:
            # print("nope")
            item_hotness = ""
        items_hotness.append(item_hotness)

    # JSON

    dataList = []
    for i in range(len(items_hotness)):
        dataItem = {
            "Title": titles[i],
            "ItemCondition": item_conditions[i],
            "Price": item_prices[i],
            "BuyingMethod": item_buymethods[i],
            "ItemLocation": item_locations[i],
            "ShippingCost": item_shippings[i],
            "ItemHotness": items_hotness[i]
        }
        dataList.append(dataItem)
    return json.dumps(dataList, indent=4)


if __name__ == "__main__":

    pageContent1 = openPageContent(page1)
    print('XPath Rtv 1: \n' + xpathForRtvSlo(pageContent1))
    print('Regex Rtv 1: \n' + regexForRtvSlo(pageContent1))

    pageContent2 = openPageContent(page2)
    print('XPath Rtv 2: \n' + xpathForRtvSlo(pageContent2))
    print('Regex Rtv 2: \n' + regexForRtvSlo(pageContent2))

    pageContent3 = openPageContent(page3)
    print('XPath Overstock 1: \n' + xpathForOverstock(pageContent3))
    print('Regex Overstock 1: \n' + regexForOverstock(pageContent3))

    pageContent4 = openPageContent(page4)
    print('XPath Overstock 2: \n' + xpathForOverstock(pageContent4))
    print('Regex Overstock 2: \n' + regexForOverstock(pageContent4))

    pageContent5 = openPageContent(page5)
    print('XPath Ebay 1: \n' + xpathForEbay(pageContent5))
    print('Regex Ebay 1: \n' + regexForEbay(pageContent5))

    pageContent6 = openPageContent(page6)
    print('XPath Ebay 2: \n' + xpathForEbay(pageContent6))
    print('Regex Ebay 2: \n' + regexForEbay(pageContent6))



