numbers = [1, 3, 5, 7, 9, 10]
# return back the object
new = list(map(lambda x: x - x*5/1000, numbers))
print(new)

names = ["Ditto", "Heyyo"]
cap_name = list(map(str.capitalize,names))
cap_full = list(map(str.upper,names))
print(cap_name)
print(cap_full)