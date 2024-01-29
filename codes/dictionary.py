dict={"brand":"ford","model":"mustang","year":1964}
print(dict)
print(dict["brand"])
print(len(dict))
x=dict.get("model")
x=dict.keys()
print(x)

car={"brand":"ford",
      "model":"mustang",
      "year":1964
      }
x=car.keys()
print(x) #before change

car["color"]="white"
print(x)
print(car)
if "model" in car:
    print("yes")


car.update({"year":2000})
print(car)
car.pop("model")
print(car)

# for loop

for x in car:
    print(x)

for x in car:
    print(car[x])

for x, y in car.items():
  print(x, y)

newcar=car.copy()
print(newcar)



#nested dictionary

family={
    "child1":{
        "name":"rajat",
        "age":"21",
    },
    "child2":{
        "name":"bob",
        "age":"20",

    }
}
print(family)
print(family["child1"]["name"])