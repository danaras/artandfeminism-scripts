This folder contains 3 scripts that are used for Art and Feminism wikidata organization.
1) parse-dashboard-allarticles.py
2) sort-for-p5008.py
3) parse-other.py

1) parse-dashboard-allarticles.py
	This is the script to organize the csv file that is downloaded from the dashboard.
	It separates articles into 5 csv files:
		newly created not deleted articles
		already existing not deleted articles
		drafted not deleted articles
		deleted articles
Instructions:
	Move the pages edited CSV to “artandfeminism-scripts-master” folder
	Tell the Python file where to find the data
		Open parse-dashboard-allarticles.py in a text editor
		Change the file name in line 3 which reads dashboardCSV = 'artfeminism_2018-articles-2018-09-22.csv'
		to put your new CSV in between the single quotes.
		Save the file
	Run the Python file
		Open Terminal and navigate to the “artandfeminism-scripts-master” folder. “cd” is the command for changing
		directory. Type “cd “ then drag the folder icon onto Terminal.
		Type “python parse-dashboard-allarticles.py” and hit enter
		The script will spit out a bunch of text, and create a bunch of sorted CSV files

2) sort-for-p5008.py
	This is a script that sorts articles into red, green, gray lists.
	Red list - no tracking for a+f will be done for these articles
	Green list - these articles will be tracked for a+f so quick statements are generated for these articles to add
	p5008
	Grey list - needs human review on whether these articles should be tracked

	* This script uses red-green-list.csv under the Resources file. (make sure you have the file there)

Instructions:
	Move the articles csv to “artandfeminism-scripts-master” folder
	Tell the Python file where to find the data
		Open sort-for-p5008.py in a text editor
		Change the file name in line 3 which reads inputFile = 'all-categories-QS.csv' to put your new CSV in
		between the single quotes.
		Save the file
	Run the Python file
		Open Terminal and navigate to the “artandfeminism-scripts-master” folder. “cd” is the command for changing
		directory. Type “cd “ then drag the folder icon onto Terminal.
		Type “python sort-for-p5008.py” and hit enter
		The script will spit out a bunch of text, and create a bunch of sorted CSV files

3) parse-other.py
	This script will sort your output-other.csv file that quicksheets.py generated under "needs human review/" folder
	into 4 files:
		Male_other.csv
		Human_other.csv
		Art_other.csv
		Other_other.csv

	* This script uses the library/ folder and Resources/artValues.csv file to run.

Instructions:
	Move the output-other.csv to “artandfeminism-scripts-master” folder
	Tell the Python file where to find the data
		Open parse-other.py in a text editor
		Change the file name in line 108 which reads inputfile = "All new A+F articles needing review 2018 - NEW
		other copy.csv" to put your new CSV in between the single quotes.
		Save the file
	Run the Python file
		Open Terminal and navigate to the “artandfeminism-scripts-master” folder. “cd” is the command for changing
		directory. Type “cd “ then drag the folder icon onto Terminal.
		Type “python parse-other.py” and hit enter
		The script will spit out a bunch of text, and create a bunch of sorted CSV files
