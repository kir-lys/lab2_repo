#b. Реализуйте в нём следующие функции: 
# i. Переворот строки (“hello, world” ­> “dlrow ,olleh”) 

str_s = "hello, world"
str_r = ""

print(str_s)

for i in str_s:
    str_r =  i + str_r

print(str_s[::-1])

print(str_r)
