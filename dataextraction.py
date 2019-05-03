# Import libraries
import requests
import re


# We rather use the locally-cached file as it may have changed online.
pageContent = open('WebPages\\rtvslo.si\Audi A6 50 TDI quattro_ nemir v premijskem razredu - RTVSLO.si.html', 'r').read()
print("Page content:\n'%s'." % pageContent)

# Get the article date

#todo: find correct regex working on it now
regex = r"Audi A6 50 TDI quattro: nemir v premijskem razredu"

match = re.compile(regex).search(pageContent)
title = match.group(0)
print("Found title: '%s'." % title)

matches = re.finditer(regex, pageContent)
for match in matches:
    print("Found date: '{}'.".format( match.group(0) ))