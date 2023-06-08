fruits ={
    "fruit1" : "mango",
    "fruit2" : "apple",
    "fruit3" : "banana" 
}

print("fruits")
print(fruits.get("fruit1"))
print(fruits.get("fruit2"))
print(fruits.get("fruit3"))
print(fruits.get("fruit4"))
a = 56
print(fruits.get("fruit5",a))
print(fruits.get("fruit6",78))
t = fruits
print(t.pop("fruit2",4))
print(fruits)




