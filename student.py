class Student:
    def _init_(self,studentId,first,last,gpa,major,advisor):
        self.studentId  = studentId
        self.first = first
        self.last = last
        self.gpa = gpa
        self.major = major
        self.advsior = advisor

    def getStudentId(self):
        return self.studentId
    def getFirst(self):
        return self.first
    def getLast(self):
        return self.last
    def getGpa(self):
        return self.gpa
    def getMajor(self):
        return self.major
    def getAdvisor(self):
        return self.Advisor
    def getStudentTuple(self):
        return(self.getFirst(),self.getLast(),self.getMajor(),self.getAdvisor(),self.getGpa())
    

