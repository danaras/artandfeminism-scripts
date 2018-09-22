import csv

firstline = True
count = 0

output1 = open('output-ns0-newTRUE-deletedFALSE.csv', 'w')
csvWriter1 = csv.writer(output1)
csvWriter1.writerow(['language','title','new','deleted'])
output2 = open('output-ns0-newFALSE-deletedFALSE.csv', 'w')
csvWriter2 = csv.writer(output2)
csvWriter2.writerow(['language','title','new','deleted'])
output3 = open('output-ns118-deletedFALSE.csv', 'w')
csvWriter3 = csv.writer(output3)
csvWriter3.writerow(['language','title','URL','new','deleted'])
output4 = open('output-ns0or118-deletedTRUE.csv', 'w')
csvWriter4 = csv.writer(output4)
csvWriter4.writerow(['language','title','URL','course_slug','new','deleted'])
output5 = open('output-other.csv', 'w')
csvWriter5 = csv.writer(output5)
with open('artfeminism_2017-articles-2018-01-22(1).csv', 'r') as f:
	reader = csv.reader(f)
	for line in reader:
		if firstline:    #skip first line
			firstline = False
			continue
		info = list(line)
		wiki = info[2].encode('utf8')
		if "wikidata" not in wiki:
			language = wiki.split('.')[0]
			language = language.encode('utf8')
			count = count+1
			print language
			print count
			title = info[0].replace('_', ' ')
			title = title.decode('utf8')
			title = title.encode('utf8')
			print title
			ns = int(info[1])
			new = str(info[5]).lower().encode('utf8')
			deleted = str(info[6]).lower().encode('utf8')
			if (ns is 0) and ("true" in new) and ("false" in deleted):
				csvWriter1.writerow([language, title, new, deleted])
			if (ns is 0) and ("false" in new) and ("false" in deleted):
				csvWriter2.writerow([language, title, new, deleted])
			if (ns is 118) and ("false" in deleted):
				csvWriter3.writerow([language, title, info[3], new, deleted])
			if ((ns is 118) or (ns is 0))and ("true" in deleted):
				csvWriter4.writerow([language, title, info[3], info[9], new, deleted])
