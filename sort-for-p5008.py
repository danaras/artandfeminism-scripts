import csv

inputFile = 'all-categories-QS.csv'
qidColumnNumber = 0
occupationQIDColumnNumber = 2
listFile = 'red-green-list.csv'
outputFile_green = 'green-' + inputFile
outputFile_red = 'red-' + inputFile
outputFile_grey = 'grey-' + inputFile

def createOutputCsv (outputFileName):
	outputCSV = open(outputFileName, 'w')
	csvWriter = csv.writer(outputCSV, delimiter='	')
	csvWriter.writerow(['QID'])
	return [outputCSV,csvWriter]
def getRedGreenList(listFileName):
	sortList = []
	with open(listFileName,'r') as csvFile:
		firstline = True
		reader = csv.reader(csvFile)
		for row in reader:
			if firstline:    #skip first line
				firstline = False
				continue
			info = list(row)
			sortList.append(info)
	return sortList

def writeOut(sorted, outputs):
	for qid in sorted[0]:
		outputs[0][1].writerow([qid,"P5008","Q24909800"])
		outputs[0][0].flush()

	for qid in sorted[1]:
		outputs[1][1].writerow([qid])
		outputs[1][0].flush()
	for qid in sorted[2]:
		outputs[2][1].writerow([qid])
		outputs[2][0].flush()

def parseCsv(input, sortList, qidColumnNo, occupationQIDColumnNo):
	with open(input,'r') as csvFile:
		greenQIDs = []
		redQIDs = []
		greyQIDs = []
		firstline = True
		reader = csv.reader(csvFile)
		for row in reader:
			if firstline:    #skip first line
				firstline = False
				continue
			info = list(row)
			for index, x in enumerate(sortList):
				if x[1] == info[occupationQIDColumnNumber]:
					if x[3] == 'y':	#add qid to green qid list
						greenQIDs.append(info[qidColumnNumber])
					elif x[3] == 'n':	#add qid to red qid list
						redQIDs.append(info[qidColumnNumber])
					else:	#add qid to grey qid list
						greyQIDs.append(info[qidColumnNumber])
				else:	#add qid to grey qid list
					greyQIDs.append(info[qidColumnNumber])
		# SORT THE LISTS (remove duplicates etc.)
		greenQIDs = list(set(greenQIDs))
		redQIDs = list(set(redQIDs) - set(greenQIDs))
		greyQIDs = list(set(greyQIDs) - set(greenQIDs) - set(redQIDs))
		return [greenQIDs,redQIDs,greyQIDs]

def main():
	print "Start"
	outputFiles  = []
	red_green_list = getRedGreenList(listFile)
	outputFiles.append(createOutputCsv(outputFile_green))
	outputFiles.append(createOutputCsv(outputFile_red))
	outputFiles.append(createOutputCsv(outputFile_grey))
	sortedList = parseCsv(inputFile, red_green_list, qidColumnNumber, occupationQIDColumnNumber)
	writeOut(sortedList, outputFiles)

main()
