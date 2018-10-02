from urllib2 import Request, urlopen, URLError
import os, json, csv
import logging, sys
import re


from library.parseWikidata import parseWikidata

class ParseOther:
	def __init__(self, inputFileName, artValueFileName):
		self.inputFileName = inputFileName
		self.outputFolderName = self.inputFileName+" Parsed Outputs"
		self.artValueFileName = artValueFileName
		self.artValueList = []
		self.artValueListPrepared = False
		self.outputTitleRow = ["language","title","QID","P31","instance of","P21","gender","P106","occupation","WP first sentence"]

	def openCSVtoWrite(self):
		if not os.path.exists(self.outputFolderName):
			os.makedirs(self.outputFolderName)
		self.outputCSVArt = open(self.outputFolderName+"/Art_other.csv", 'w')
		self.csvWriterArt = csv.writer(self.outputCSVArt)
		self.csvWriterArt.writerow(self.outputTitleRow)

		self.outputCSVHuman = open(self.outputFolderName+"/Human_other.csv", 'w')
		self.csvWriterHuman = csv.writer(self.outputCSVHuman)
		self.csvWriterHuman.writerow(self.outputTitleRow)

		self.outputCSVMale = open(self.outputFolderName+"/Male_other.csv", 'w')
		self.csvWriterMale = csv.writer(self.outputCSVMale)
		self.csvWriterMale.writerow(self.outputTitleRow)

		self.outputCSVOther = open(self.outputFolderName+"/Other_other.csv", 'w')
		self.csvWriterOther = csv.writer(self.outputCSVOther)
		self.csvWriterOther.writerow(self.outputTitleRow)

	def prepareArtValueList(self):
		self.artValueList = []
		with open("Resources/"+self.artValueFileName) as f:
			firstline = True
			reader = csv.reader(f)
			for line in reader:
				if firstline:
					firstline = False
					continue
				info = list(line)
				if info:
					self.artValueList.append(info[0])
		self.artValueListPrepared = True

	def parseInputFile(self):
		self.openCSVtoWrite()
		self.prepareArtValueList()
		with open(self.inputFileName, 'rU') as csvFile:
			self.openCSVtoWrite()
			firstline = True
			reader = csv.reader(csvFile)
			for row in reader:
				if firstline:    #skip first line
					firstline = False
					continue
				info = list(row)
				language = info[0]
				title = info[1]
				qid = info[2]
				useQID = True
				WD = parseWikidata(language, title, qid, useQID)
				jsonData = WD.getWikiData()
				WD.getPData('P31')
				p31QID = WD.pData['P31'][0].encode('utf-8', 'ignore')
				p31Value = unicode(WD.pData['P31'][1],errors='ignore')
				# print p31Value
				gender = info[4]

				if p31QID == "Q5":
					if gender == "male":
						self.csvWriterMale.writerow([info[0],info[1],info[2],p31QID,p31Value,info[3],info[4],info[5],info[6],info[7]])
						self.outputCSVMale.flush()
					else:
						self.csvWriterHuman.writerow([info[0],info[1],info[2],p31QID,p31Value,info[3],info[4],info[5],info[6],info[7]])
						self.outputCSVHuman.flush()

				else:
					isArt = False
					for item in self.artValueList:
						searchKeyword = re.search(r'\b'+re.escape(item)+r'\b',p31Value, re.IGNORECASE)

						if searchKeyword:
							self.csvWriterArt.writerow([info[0],info[1],info[2],p31QID,p31Value,info[3],info[4],info[5],info[6],info[7]])
							self.outputCSVArt.flush()
							isArt = True
							break

					if not isArt:
						searchFirstSentence = re.search(r'\bart', info[7],re.IGNORECASE)

						if searchFirstSentence:
							# print searchFirstSentence
							self.csvWriterArt.writerow([info[0],info[1],info[2],p31QID,p31Value,info[3],info[4],info[5],info[6],info[7]])
							self.outputCSVArt.flush()
						else:
							self.csvWriterOther.writerow([info[0],info[1],info[2],p31QID,p31Value,info[3],info[4],info[5],info[6],info[7]])
							self.outputCSVOther.flush()



if __name__ == "__main__":
	parsing = ParseOther("All new A+F articles needing review 2018 - NEW other copy.csv", "artValues.csv")
	parsing.parseInputFile()
