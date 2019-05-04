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
#print("Page content:\n'%s'." % pageContent)

# Get the article date

#todo: find correct regex working on it now
regex = r"Audi A6 50 TDI quattro: nemir v premijskem razredu"

match = re.compile(regex).search(pageContent)
title = match.group(0)
print("Found title: '%s'." % title)

matches = re.finditer(regex, pageContent)
for match in matches:
    print("Found date: '{}'.".format( match.group(0) ))


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
	    "SubTitle" : subTitle,
	    "Lead" : lead,
	    "Content" : content
	}
	return json.dumps(dataItem, indent = 4,  ensure_ascii=False)

def xpathForOverstock(pageContent):
	
	tree = html.fromstring(pageContent)

	myData = []
	path = '//table[2]//tr[1]/td[last()]//tr[2]//tbody'

	tdCount = len(tree.xpath(path+'/tr[count(*)]')) - 3

	for x in range(1, tdCount, 2):

		if (x >= 21):
			x += 1

		# Title
		title = str(tree.xpath(path+'/tr['+str(x)+']/td[2]//b/text()')[0])
		# Content
		content = str(tree.xpath(path+'/tr['+str(x)+']/td[2]//td[2]/span[@class="normal"]/text()')[0])
		content = content.replace('\n', ' ')

		# ListPrice
		listprice = str(tree.xpath(path+'/tr['+str(x)+']/td[2]//td[1]//tr[1]/td[2]/s/text()')[0])

		# Price
		price = str(tree.xpath(path+'/tr['+str(x)+']//td[1]//tr[2]/td[2]//b/text()')[0])

		# Saving + saving percent
		save = str(tree.xpath(path+'/tr['+str(x)+']/td[2]//td[1]//tr[3]/td[2]/span/text()')[0])
		saving = save.split('(')[0].strip(" ")

		# SavingPercent
		savingpercent = save.split('(')[1].strip(" )")

		dataItem = {
		    "Title": title,
		    "Content": content,
		    "ListPrice": listprice,
		    "Price" : price,
		    "Saving" : saving,
		    "SavingPercent" : savingpercent
		}

		myData.append(dataItem)
	return json.dumps(myData, indent = 4)

if __name__ == "__main__":
	
	pageContent1 = openPageContent(page1)
	print(xpathForRtvSlo(pageContent1))
	pageContent2 = openPageContent(page2)
	print(xpathForRtvSlo(pageContent2))
	pageContent3 = openPageContent(page3)
	print(xpathForOverstock(pageContent3))
	pageContent4 = openPageContent(page4)
	print(xpathForOverstock(pageContent4))

