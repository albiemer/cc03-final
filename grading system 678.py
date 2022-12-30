
#import gc
import sqlite3

greference = [1, 1.25, 1.50, 1.75, 2, 2.25, 2.50, 2.75, 3]

class cgrade():
    
    lgrade = float(0)
    
    def __init__(self, *sub):
        
        self.avg = (sub[0] + sub[1] + sub[2])/3
        self.name = sub[3]

    def average(self):
        if self.avg == 100:
            cgrade.lgrade = float(1)
        elif self.avg >= 98 and self.avg <= 99:
            cgrade.lgrade = float(1.25)
        elif self.avg >= 96 and self.avg <= 98:
            cgrade.lgrade = float(1.50)
        elif self.avg >= 93 and self.avg <= 95:
            cgrade.lgrade = float(1.75)
        elif self.avg >= 88 and self.avg <= 92:
            cgrade.lgrade = float(2)
        elif self.avg >= 85 and self.avg <= 87:
            cgrade.lgrade = float(2.25)
        elif self.avg >= 83 and self.avg <= 84:
            cgrade.lgrade = float(2.50)
        elif self.avg >= 80 and self.avg <= 82:
            cgrade.lgrade = float(2.75)
        elif self.avg >= 75 and self.avg <= 80:
            cgrade.lgrade = float(3)
        elif self.avg >= 70 and self.avg <= 74:
            cgrade.lgrade = float(4)
        else:
            cgrade.lgrade = float(5)
    
        return cgrade.lgrade
    
    def remarks(self, other):
        if cgrade.lgrade in other:
            return 'Passed'
        else:
            return 'Failed'
    
    def tosave(self):
        conn = sqlite3.connect("studentrec.db")
        c = conn.cursor()
        
        c.execute('''
          CREATE TABLE IF NOT EXISTS grade_table
          ([Id] INTEGER PRIMARY KEY, [Name] TEXT, [Total_score] INTEGER, [Grade] REAL)
          ''')
        
        c.execute("insert into grade_table(Name, Total_score, Grade) values(?,?,?)", \
                  (self.name, self.avg, cgrade.lgrade))
        conn.commit()
        conn.close()
        
    def showallstudent(self):
        conn = sqlite3.connect("studentrec.db")
        c = conn.cursor()
        c.execute("select * from grade_table")
        row = c.fetchall()
        conn.commit()
        conn.close()
        return row
            
    

print("***********************Garading system**************")

name = input("Student Name 'Last, First': ")

math = float(input("Enter Grade in Math: "))
eng = float(input("Enter Grade in English: "))
sci = float(input("Enter Grade in Science: "))
cg = cgrade(math, eng, sci, name)
print("#########################################")
print("Student Name: ", name)
    
print("Grade: ", cg.average())
print("Remarks: ", cg.remarks(greference))
cg.tosave()

print("DATABASE: ", cg.showallstudent())

del cg    #to avoid memory leaks


print("#########################################")