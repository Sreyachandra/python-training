text="welcome to python"
print(text)                                                  #welcome to python
print(len(text))                                             #17
text="""
 python is a high-level language
 general purpose programming language
 interpreted language
 """
print(text)                                                   #python is a high-level language
                                                              #general purpose programming language
                                                              #interpreted language
text="welcome to python"
print(text[2])                                                #1
print(text+ ' programming')                                   #welcome to python programming
#string methods
a="Python"
print(a.lower())                                              #python
print(a.upper())                                              #PYTHON
print(a.isalnum())                                            #True
print(a.isalpha())                                            #True
print(a.isdecimal())                                          #Flse
print(a.isdigit())                                            #False
print(a.islower())                                            #False
print(a.isupper())                                            #False
print(a.capitalize())                                         #Python
print(a.strip())                                              #python
#string slicing
s='this is a pen'
print(s[3:6])                                                 #s i
print(s[2:4])                                                 #is
print(s[:-2])                                                 #this is a p
print(s[:2])                                                  #th
print(s[:])                                                   # this is a pen
print(s[0:7:2])                                               #ti s
a=[1,2,3,4,5,6,7]
print(a[::3])                                                 #[1,4,7]
print(a[::-2])                                                #[7,5,3,1]
#string formatting
value=2.791514
print(f'approximate value={value:.2f}')
car={'tires':4,'doors':2}
print(f' car={car}')                                          #car={‘tires’:4,’doors’:2}
#check string
text="this is a book"
print("book" in text)                                         #True
#check if NOT
text="this is a book"
print("pen"not in text)                                       #True
