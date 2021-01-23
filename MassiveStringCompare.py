# ---------- Import Dependencies
#
#

from tkinter import filedialog, Tk


# ---------- Globals
#
#

version = "1.0"



# ========================================================================================================================

print ("\n")
print("* * * MassiveStringCompare " + version + " * * *")
print ("\n")

Tk().withdraw()

sourcefile = filedialog.askopenfilename(title = "Select file 1")

targetfile = filedialog.askopenfilename(title = "Select file 2")

resultfile = filedialog.asksaveasfilename(title = "Save result to", filetypes = [("Text Document", "*.txt")], initialfile = "CompareResult", defaultextension = ".txt")

sourceSet = set(open(sourcefile, encoding="utf8"))
targetSet = set(open(targetfile, encoding="utf8"))

NoMatch = sourceSet.difference(targetSet)

resulttext = (
				"* * * MassiveStringCompare " + version + " * * *  \n\n"

				"Result from compare job: \n\n"

				"file 1: " + sourcefile + "\n\n"

				"with \n\n"

				"file 2: " + targetfile + "\n\n"

				"--------------------------------------------------------- \n\n"
			)

if len(NoMatch) == 0:
	print ("All found! \n\n")
	
else:
	print (str(len(NoMatch)) + " differences found! See result file for more information. \n\n")
	with open(resultfile, "w+", encoding="utf-8") as file:
		file.write(resulttext)
		file.write("No match: \n\n")
		for item in NoMatch:
			file.write(item)
print("Done!")

