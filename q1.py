#obtain Student List
def obtainStudentList():
      filename = "student.txt"
      with open(filename, "r") as f:
            str1 = f.read()
      lines = str1.split("\n")
      sList = {}
      for i in range(int(lines[0])):
            sList[i] = lines[i+1].split(" ")
      return sList

#write Average File
def writeAverageFile(sList):
      for i in range (len(sList)):
            average = int(sList[i][1]) + int(sList[i][2]) + int(sList[i][3])
            average /= 3
            average = round(average,2)
            sList[i].append(str(average))
      strSeperator = " "
      str1 = str(len(sList))
      for i in range (len(sList)):
            str1 = str1+"\n"+strSeperator.join(sList[i])
      filename = "output1.txt"
      with open(filename, "w") as f: 
            f.write(str1)

#viewLowScoreStudentFile
def viewLowScoreStudentFile(sList):
      count = 0
      lowScore = {}
      for i in range(len(sList)):
            for j in range(1,4):
                  if (int(sList[i][j])<50):
                        lowScore[count] = sList[i]
                        count += 1
                        break
      strSeperator = " "
      str2 = str(count)
      for i in range (len(lowScore)):
            str2 = str2+"\n"+strSeperator.join(lowScore[i])
      filename = "output2.txt"
      with open(filename, "w") as f:
            f.write(str2)

def main():
      sList = obtainStudentList()
      writeAverageFile(sList)
      sList = obtainStudentList()
      viewLowScoreStudentFile(sList)

main()
