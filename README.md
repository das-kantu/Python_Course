<h1>Python Dictionaries</h1>



```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

```
<h3>Dictionary</h3>
<b>Dictionaries are used to store data values in key:value pairs.</b>

<b>A dictionary is a collection which is ordered*, changeable and do not allow duplicates.</b>
<b>Dictionaries are written with curly brackets, and have keys and values:</b>

<b>Example:</b>

<b>Create and print a dictionary:</b>

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```
<h2>Dictionary Items</h2>
<h3>Dictionary items are ordered, changeable, and do not allow duplicates.</h3>

<h3>Dictionary items are presented in key:value pairs, and can be referred to by using the key name.</h3>

<b>Example</b>
<b>Print the "brand" value of the dictionary:</b>

```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

```

<h3>Changeable</h3>
<b>Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.</b>
<h2>Duplicates Not Allowed</h2>
<b>Dictionaries cannot have two items with the same key:</b>

<h3>Example</h3>
<b>Duplicate values will overwrite existing values:</b>

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

```
<h3>Dictionary Length</h3>
<b>To determine how many items a dictionary has, use the len() function:</b>

<h2>Example</h2>
<b>Print the number of items in the dictionary:<b>

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
```
<h2>Dictionary Items - Data Types</h2>
<b>The values in dictionary items can be of any data type:<b>

```python
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

```
<h2>type()</h2>
<b>From Python's perspective, dictionaries are defined as objects with the data type 'dict':</b>

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
```
<h2>The dict() Constructor</h2>
<b>It is also possible to use the dict() constructor to make a dictionary.</b>

<h2>Example</h2>
<b>Using the dict() method to make a dictionary:</b>

```python
thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict)

```
<h2> Access Dictionary Items</h2>

<h3>Accessing Items</h3>
<b>You can access the items of a dictionary by referring to its key name, inside square brackets:</b>

```python

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
```

<h2>Get Keys</h2>
<b>The keys() method will return a list of all the keys in the dictionary.</b>

```python

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)

```

<h2>Get Values</h2>
<b>The values() method will return a list of all the values in the dictionary.</b>

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)

```

<h2>The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.</h2>

<h3>Example</h3>
<b>Make a change in the original dictionary, and see that the values list gets updated as well:</b>

```python

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

```
<h2>Get Items</h2>
<h3>The items() method will return each item in a dictionary, as tuples in a list.</h3>

<b>Example<b>
<b>Get a list of the key:value pairs<b>

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)


```
<h2>Check if Key Exists</h2>
<b>To determine if a specified key is present in a dictionary use the in keyword:</b>

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

```
<h3>Change Values</h3>
<b>You can change the value of a specific item by referring to its key name:</b>

```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)
```

<h1>Update Dictionary</h1>
<h2>The update() method will update the dictionary with the items from the given argument.</h2>

<h3>The argument must be a dictionary, or an iterable object with key:value pairs.</h3>

```python

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

```
<h1>Add Dictionary Items</h1>
<h2>Adding Items</h2>
<h3>Adding an item to the dictionary is done by using a new index key and assigning a value to it:</h3>

<b>Example</b>

```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
```

<h1>Update Dictionary</h1>
<h2>The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.</h2>

<h3>The argument must be a dictionary, or an iterable object with key:value pairs.</h3>

<b>Example</b>
<h3>Add a color item to the dictionary by using the update() method:</h3>

```python

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)

```

<h1>Removing Items</h1>
<h2>There are several methods to remove items from a dictionary:</h2>

<b>ExampleGet your own Python Server</b>
<b>The pop() method removes the item with the specified key name:</b>

```python

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

```

 
<h1>Loop Through a Dictionary</h1>
<h2>You can loop through a dictionary by using a for loop.</h2>

<h3>When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.</h3>

<b>ExampleGet your own Python Server</b>
<b>Print all key names in the dictionary, one by one:</b>

```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
```

<h1>Nested Dictionaries</h1>
<h2>Nested Dictionaries</h2>
<h3>A dictionary can contain dictionaries, this is called nested dictionaries.</h3>

<b>ExampleGet your own Python Server</b>
<b>Create a dictionary that contain three dictionaries:</b>

```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

```


