from functions import Calculator


class ChildImp(Calculator):

    num2= 120

    def __init__(self):
        Calculator.__init__(self,3,9)

    def getDaten(self):
        return self.num2 + self.addition()

obj1 = ChildImp()
print(obj1.getDaten())

#String

str = "   Single platform"
str1 = "python Single"

print(str[3])

print(str[0:6])

print (str in str1)

print(str.split(" "))
print(str.strip())

file = open('test.txt')
#print(file.read(5))

line = file.readline()
while line!="":
    print(line)
    line = file.readline()

for line in file.readlines():
    print(line)
file.close()

