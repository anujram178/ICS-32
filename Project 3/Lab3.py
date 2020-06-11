class Assignment:
   def __init__(self, desc:str, score:float, total:float):
       self.desc = desc
       self.score = score
       self.total = total
       
   def getDescription(self)->str:
       return self.desc

   def getScore(self)->float:
       return self.score

   def getTotal(self)->float:
       return self.total

   def changeScore(self, score:float):
       self.score = score

class CategoryAssignment(Assignment):
   def __init__(self, desc:str, category:str, score:float, total:float):
       super().__init__(desc, score, total)
       self.category = category

   def getCategory(self)->str:
       return self.category

class Student:
   def __init__(self, studentId:int):
       self.studentId = studentId
       self.assignmentList = []

   def getId(self)->int:
       return self.studentId

   def addAssignment(self, score:Assignment):
       self.assignmentList.append(score)
       
   def getScore(self, assignmentName:str)->float:
       for assignment in self.assignmentList:
           if assignment.getDescription() == assignmentName:
               return assignment.getScore()
           
   def getScores(self)->list:
       return self.assignmentList

   def changeScore(self, assignmentName:str, score:float):
       for assignment in self.assignmentList:
           if assignmentName == assignment.getDescription():
               assignment.changeScore(score)

   def removeScore(self, assignmentName:str):
       for assignment in self.assignmentList:
           if assignmentName == assignment.getDescription():
               self.assignmentList.remove(assignment)


class Gradebook:
	def __init__(self):
		self.gradebookDict = {}

	def addStudent(self, student:Student):
		if student.getId() in self.gradebookDict:
			pass
		else:
			self.gradebookDict[student.getId()] = student

	def dropStudent(self, id:int):
		if id in self.gradebookDict:
			self.gradebookDict.pop(id)

	def search(self, id:int)->Student:
		return self.gradebookDict.get(id)

	def addAssignment(self, id:int, score:Assignment):
		if id in self.gradebookDict:
			if len(self.gradebookDict[id].assignmentList) == 0:
				self.gradebookDict[id].addAssignment(score)
			else:
				for assignment in self.gradebookDict[id].assignmentList:
					if score.getDescription() == assignment.getDescription():
						assignment.changeScore(score.getScore())
						return
				self.gradebookDict[id].addAssignment(score)


class TotalPointsGradebook(Gradebook):
	def __init__(self):
		super().__init__()
		self.studentAverageDict = {}
		
	def writeGradebookRecord(self, id:int, fileName:str):
		infile = open(fileName,'w')
		if id not in self.gradebookDict:
			infile.write("Student Not Found")
			infile.close()
			return 
		infile.write(str(id))
		infile.write('\n')
		score = 0
		total = 0
		for assignment in self.gradebookDict[id].assignmentList:
			score += assignment.getScore()
			total += assignment.getTotal()
			infile.write(assignment.getDescription())
			infile.write('\n')
			infile.write(f"{assignment.getScore()}/{assignment.getTotal()}")
			infile.write('\n')
		percentage = self.studentAverage(id)
		infile.write(f"Total: {score}/{total}")
		infile.write('\n')
		infile.write(f"Percentage: {percentage}")
		infile.close()

	def classAverage(self)->float:
		n = 0
		studentTotalAverage = 0
		for id in self.gradebookDict:
			studentTotalAverage += self.studentAverage(id)
			n += 1
		return studentTotalAverage/n

	def studentAverage(self, id:int):
		score = 0
		total = 0
		for assignment in self.gradebookDict[id].assignmentList:
			score += assignment.getScore()
			total += assignment.getTotal()
		return (score/total)*100


class CategoryGradebook(Gradebook):
	def __init__(self):
		super().__init__()
		self.categoryDict = {}
		self.studentAverageDict = {}

	def helper(self, id:int):
		totalPercentage = 0
		categoryScoreDict = {}
		categoryTotalDict = {}
		score = 0
		total = 0
		for assignment in self.gradebookDict[id].assignmentList:
			if assignment.getCategory() in categoryScoreDict:
				categoryScoreDict[assignment.getCategory()] += assignment.getScore()
				categoryTotalDict[assignment.getCategory()] += assignment.getTotal()
			else:
				categoryScoreDict[assignment.getCategory()] = assignment.getScore()
				categoryTotalDict[assignment.getCategory()] = assignment.getTotal()
		for category in categoryScoreDict:
			percentage = (categoryScoreDict[category]/categoryTotalDict[category])*100
			totalPercentage += percentage*self.categoryDict[category]*(0.01)
		self.studentAverageDict[id] = totalPercentage

	def addCategory(self, description:str, weight:float):
		self.categoryDict[description] = weight

	def isBalanced(self)->bool:
		totalWeight = 0
		for category in self.categoryDict:
			totalWeight += self.categoryDict[category]
		return totalWeight == 100

	def writeGradebookRecord(self, id:int, fileName:str):
		totalPercentage = 0
		categoryScoreDict = {}
		categoryTotalDict = {}
		infile = open(fileName, 'w')
		if id not in self.gradebookDict:
			infile.write("Student Not Found")
			infile.close()
			return
		infile.write(str(id))
		infile.write('\n')
		score = 0
		total = 0
		for assignment in self.gradebookDict[id].assignmentList:
			if assignment.getCategory() in categoryScoreDict:
				categoryScoreDict[assignment.getCategory()] += assignment.getScore()
				categoryTotalDict[assignment.getCategory()] += assignment.getTotal()
			else:
				categoryScoreDict[assignment.getCategory()] = assignment.getScore()
				categoryTotalDict[assignment.getCategory()] = assignment.getTotal()
			infile.write(f"{assignment.getCategory()}: {assignment.getDescription()}")
			infile.write('\n')
			infile.write(f"{assignment.getScore()}/{assignment.getTotal()}")
			infile.write('\n')
		for category in categoryScoreDict:
			percentage = (categoryScoreDict[category]/categoryTotalDict[category])*100
			infile.write(f"{category}: {str(percentage)}")
			infile.write('\n')
			totalPercentage += percentage*self.categoryDict[category]*(0.01)
		infile.write(f"Percentage: {totalPercentage}")
		infile.close()


	def classAverage(self)->float:
		total = 0
		n = 0
		for id in self.gradebookDict:
			self.helper(id)
		for id in self.studentAverageDict:
			n += 1
			total += self.studentAverageDict[id]
		return total/n
















   
               


       
   
       
       
       
       
   
       
       
   
       


x = {'a','b','c','d'}
x.remove('b')
print(x)

y = {'a','c','d'}
print(x == y)
