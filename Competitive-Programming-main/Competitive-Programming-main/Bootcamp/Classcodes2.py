# class Student:
#     def __init__(self,id,name):
#         self.roll_no=id
#         self.name=name

# x=Student(5,'abc')
# print(x.roll_no)
# print(x.name)

# class Student:
#     exams_given=['1oth_Boards','!2th-Boards']
#     def __init__(self,id):
#         self.roll_no=id
#         self.college='AB'

# x=Student(5)
# y=Student(7)
# x.exams_given.append('JEE')
# y.exams_given.append('NEET')

# print(x.roll_no)
# print(y.roll_no)

# print(x.exams_given)
# print(y.exams_given)

# print(x.college)
# print(y.college)

# x.college='BC'

# print(x.college)
# print(y.college)


# class Employee:
#     holidays=['Holi']

#     def __init__(self,id,dept,sal):
#         self.id=id
#         self.dept=dept
#         self.sal=sal

#     def get_tax(self):
#         return 0.3*(self.sal)
    
#     @classmethod
#     def get_holidays(cls):
#         return cls.holidays
    
    
# emp1=Employee(1001,'Mech',10000)
# emp2=Employee(1002,'Insurance',20000)
# print(emp1.id,emp1.dept,emp1.sal)
# print(emp1.get_tax())
# print(Employee.get_holidays())


# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def distance_from_origin(self):
#         return round((self.x**2+self.y**2)**0.5,2)
    
#     def distance_from_other_point(self,p):
#         return round(((self.x-p.x)**2+(self.y-p.y)**2)**0.5,2)
    
#     def is_equal(self,p):
#         if (self.x==p.x) and (self.y==p.y):
#             return True
#         return False
    
#     def dot_product(self,p):
#         return ((self.x*p.x)+(self.y*p.y))
    
#     def vector_product(self,p):
#         return ((self.x*p.y)-(self.y*p.x))
    
#     def unit_vector(self):
#         return round(self.x/((self.x**2)+(self.y**2))**0.5,2),round(self.y/((self.x**2)+(self.y**2))**0.5,2)
    
# p1=Point(1,2)
# p2=Point(3,4)
# p3=Point(1,2)

# print(p1.distance_from_origin())
# print(p2.distance_from_origin())

# print(p1.distance_from_other_point(p2))
# print(p2.distance_from_other_point(p1))

# print(p2.is_equal(p1))
# print(p1.is_equal(p3))
# print(p3.is_equal(p2))

# print(p1.dot_product(p2),p2.dot_product(p3),p3.dot_product(p1),sep='\n')

# print(p1.vector_product(p2),p2.vector_product(p3),p3.vector_product(p1),sep='\n')

# print(p1.unit_vector(),p2.unit_vector(),p3.unit_vector(),sep='\n')

# class Complex:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def add(self,b):
#         return (self.x+b.x,self.y+b.y)
    
#     def subtract(self,b):
#         return (self.x-b.x,self.y-b.y)
    
#     def modulus(self):
#         return ((self.x)**2+(self.y)**2)**0.5
    
#     def real(self):
#         return (self.x)
    
#     def img(self):
#         return (self.y)
    
#     def conj(self):
#         return self.x,self.y*-1
    
# n1=Complex(2,-4)
# n2=Complex(-3,3)

# print(n1.real(),n1.img())
# print(n2.real(),n2.img())
# print(n1.modulus())
# print(n2.modulus())
# print(n1.conj())
# print(n2.conj())
# print(n1.add(n2))
# print(n1.subtract(n2))

class Mat:
    def __init__(self,l):
        self.l=l
    
    def add(self,m):
        nl=[]
        for i in range(len(self.l)):
            for j in range(len(self.l[0])):
                nl.append(self.l[i][j]+m.l[i][j])
        return nl
    
    def subtract(self,m):
        nl=[]
        for i in range(len(self.l)):
            for j in range(len(self.l[0])):
                nl.append(self.l[i][j]-m.l[i][j])
        return nl
    
    
    
m1=Mat([[1,2],[3,4]])
m2=Mat([[2,1],[4,3]])
print(m1.add(m2))