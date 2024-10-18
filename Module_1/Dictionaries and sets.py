# Работа со словарями
my_dict = {"Nikita": 1999, "Gena": 2001, "Max": 2005}
print("Dict:",my_dict)
print("Existing value:",my_dict["Nikita"])
print("Not existing value:",my_dict.get("Anton"))
my_dict.update({"Anton": 2000,
                "Mihail": 1998})
a = my_dict.pop("Gena")
print("Delete value:",a)
print("Modified dictionary:", my_dict)
# Работа с множествами
my_set = {1,2,3,1,1,"Mode",(1,2,3)}
print(my_set)
my_set.add(9)
my_set.discard(1)
print(my_set)