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


################# XPATH THINGS

def openPageContent(page):
	return open(page, 'rb').read()

def xpathForRtvSlo(page):
	# TODO: additionally clean strings
	# TODO: extract content!!
	# TODO: better Xpaths?? skrajsat??
	
	# download page
	pageContent = openPageContent(page)
	tree = html.fromstring(pageContent)

	# author
	author = str(tree.xpath('//*[@id="main-container"]/div[position()=3]/div/div[1]/div[1]/div/text()')[0])
	print("Found author: ", author)

	# published time
	publishedTime = str(tree.xpath('//*[@id="main-container"]/div[position()=3]/div/div[1]/div[position()=2]/text()')[0])
	print("Found publishedTime: '%s'." % publishedTime)
	publishedTime = publishedTime.replace('\n\t\t', '')

	# title
	title = str(tree.xpath('//*[@id="main-container"]/div[position()=3]/div/header/h1/text()')[0])
	print("Found title: '%s'." % title)

	# subtitle
	subTitle = str(tree.xpath('//*[@id="main-container"]/div[position()=3]/div/header/div[position()=2]/text()')[0])
	print("Found subtitle: '%s'." % subTitle)

	# lead
	lead = str(tree.xpath('//*[@id="main-container"]/div[position()=3]/div/header/p/text()')[0])
	print("Found lead: '%s'." % lead)

	# TODO: extract content properly
	content = str(tree.xpath('//*[@id="main-container"]/div[position()=3]/div/div[position()=2]')[0])
	print("Found content: '%s'." % content)

	# Extract the image URL
	#imageUrl = str(tree.xpath('//*[@id="container"]/div/div[1]/div[1]/div[1]/div/div[2]/a/img/@src')[0])
	#print("Found imageUrl: '%s'." % imageUrl)

	dataItem = {
	    "Author": author,
	    "PublishedTime": publishedTime,
	    "Title": title,
	    "SubTitle" : subTitle,
	    "Lead" : lead,
	    "Content" : content
	}

	print("Output object:\n%s" % json.dumps(dataItem, indent = 4,  ensure_ascii=False))

def xpathForOverstock(page, numOfItems):
	# TODO: additionally clean strings
	# TODO: shorten xpaths!!!!!
	
	# download page
	pageContent = openPageContent(page)
	tree = html.fromstring(pageContent)

	myData = []

	path = '/html/body/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody'

	""" dynamically traverse table?
	table = tree.xpath(path)
	count = 1
	for tbody in table:
		for row in tbody.xpath('./tr'):
			# Title
			if count >= 21:
				if count % 2 == 0:
					title = str(row.xpath('./td[2]/a/b/text()')[0])
			if count % 2 == 1:
				title = str(row.xpath('./td[2]/a/b/text()')[0])
			count += 1
			print("Found title: ", title)"""

	
	for x in range(1, numOfItems, 2):

		if (x >= 21):
			x += 1
		print(x)
		# Title
		title = str(tree.xpath(path+'/tr['+str(x)+']/td[2]/a/b/text()')[0])
		print("Found title: ", title)

		# Content
		content = str(tree.xpath(path+'/tr['+str(x)+']/td[2]/table/tbody/tr/td[2]/span/text()')[0])
		print("Found content: '%s'." % content)

		# ListPrice
		listprice = str(tree.xpath(path+'/tr['+str(x)+']/td[2]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/s/text()')[0])
		print("Found listprice: '%s'." % listprice)

		# Price
		price = str(tree.xpath(path+'/tr['+str(x)+']/td[2]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/span/b/text()')[0])
		print("Found price: '%s'." % price)

		# Saving + saving percent
		save = str(tree.xpath(path+'/tr['+str(x)+']/td[2]/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/span/text()')[0])
		saving = save.split('(')[0].strip(" ")
		print("Found saving: '%s'." % saving)

		# SavingPercent
		savingpercent = save.split('(')[1].strip(" )")
		content = content.replace('\n', ' ')
		dataItem = {
		    "Title": title,
		    "Content": content,
		    "ListPrice": listprice,
		    "Price" : price,
		    "Saving" : saving,
		    "SavingPercent" : savingpercent
		}

		myData.append(dataItem)
	print("Output object:\n%s" % json.dumps(myData, indent = 4))

xpathForRtvSlo(page1)
xpathForRtvSlo(page2)

xpathForOverstock(page3, 31)
xpathForOverstock(page4, 17)

