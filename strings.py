# string methods in python
a='mystring is this'
print("1)",a.center(30))
print("2)",a.count("i"))
print("3)",a.encode())
print("4",a.find("th"))
print("{:.2f}".format(2.4353))
print("5)",a.index("i"))
print("6)","+".join(("John","Hard","Daniel")))       # joins the iterables
print("7)",a.rjust(30))
print("8)",a.ljust(30)) 
print("9)",a.lstrip())                         
print("7)",a.translate(a.maketrans("this","that")))
print("10)",a.replace("this","that"))
print("7)",a.split())
b="3435"
print("7)",b.isdigit())
print("8)",b.isnumeric())
