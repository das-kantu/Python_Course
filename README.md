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
<h1>Python Sets</h1>

<h1>Set</h1>
<h2>Sets are used to store multiple items in a single variable.</h2>

<h3>Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage</h3>.

<b>A set is a collection which is unordered, unchangeable*, and unindexed.</b>

<b>* Note: Set items are unchangeable, but you can remove items and add new items.</b>

<b>Sets are written with curly brackets.</b>

<b>ExampleGet your own Python Server</b>
<h3>Create a Set:</h3>

```python
thisset = {"apple", "banana", "cherry"}
print(thisset)
```

<h1>Set Items</h1>
<h2>Set items are unordered, unchangeable, and do not allow duplicate values.</h2>

<h1>Unordered</h1>
<h2>Unordered means that the items in a set do not have a defined order.</h2>

<h1>Set items can appear in a different order every time you use them, and cannot be referred to by index or key.</h1>

<h1>Unchangeable</h1>
<h2>Set items are unchangeable, meaning that we cannot change the items after the set has been created.</h2>
<b>Set items are unchangeable, meaning that we cannot change the items after the set has been created.</b>

<h1>Duplicates Not Allowed</h1>
<b>Sets cannot have two items with the same value.</b>

<h1>Example</h1>
<b>Duplicate values will be ignored:</b>

```python
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


```

<h1>Get the Length of a Set</h1>
<h2>To determine how many items a set has, use the len() function.</h2>

<b>Example</b>
<h2>Get the number of items in a set:</h2>


```python
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


```

<h1>Access Set Items</h1>
<h2>Access Items</h2>
<b>You cannot access items in a set by referring to an index or a key.</b>

<b>But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.</b>

<h3>ExampleGet your own Python Server</h3>
<b>Loop through the set, and print the values:</b>

```python
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)


```

<h1>Add Set Items</h1>
<h2>Add Items</h2>
<b>Once a set is created, you cannot change its items, but you can add new items.</b>

<h3>To add one item to a set use the add() method.</h3>

<b>Add an item to a set, using the add() method:</b>

<h2>Example:</h2>

<b>Add an item to a set, using the add() method:</b>

```python
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
```
<h1>Add Sets</h1>
<h2>To add items from another set into the current set, use the update() method.</h2>

<h3>Example</h3>
<b>Add elements from tropical into thisset:</b>

```python 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
```

<h1>Remove Set Items</h1>
<h2>Remove Item</h2>
<h3>To remove an item in a set, use the remove(), or the discard() method.</h3>

<b>ExampleGet your own Python Server</b>
<b>Remove "banana" by using the remove() method:</b>
```python
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

```
<h1>Join Sets</h1>
<ol>
  
 <li>There are several ways to join two or more sets in Python.</li>

<li>The union() and update() methods joins all items from both sets.</li>

<li>The intersection() method keeps ONLY the duplicates.</li>

<li>The difference() method keeps the items from the first set that are not in the other set(s).</li>

<li>The symmetric_difference() method keeps all items EXCEPT the duplicates.</li>
</ol>

<h2>Union</h2>
<h3>The union() method returns a new set with all items from both sets.</h3>

<b>Example:</b>
<b>Join set1 and set2 into a new set:</b>

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

```

<h1>You can use the | operator instead of the union() method, and you will get the same result.</h1>

<b>Example</b>
<b>Use | to join two sets:</b>

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
```

<h2>Join Multiple Sets</h2>
<h3>All the joining methods and operators can be used to join multiple sets.</h3>

<b>When using a method, just add more sets in the parentheses, separated by commas:</b>

<b>Example</b>
<b>Join multiple sets with the union() method:</b>

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

```

<h1>Intersection</h1>
<ol>

  <li>Keep ONLY the duplicates</li>

  <li>The intersection() method will return a new set, that only contains the items that are present in both sets.</li>
</ol>
<b>Example</b>
<b>Join set1 and set2, but keep only the duplicates:</b>

```python

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

```

<h1>You can use the & operator instead of the intersection() method, and you will get the same result.</h1>

<b>Example</b>
<b>Use & to join two sets:</b>

```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

```
<h1>Difference</h1>
<b>The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.</b>

<b>Example</b>
<b>Keep all items from set1 that are not in set2:</b>

```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
```

<h1>Python Tuples</h1>

<h2>Tuple</h2>
<ol>
  <li>Tuples are used to store multiple items in a single variable.</li>

  <li>Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.</li>

  <li>A tuple is a collection which is ordered and unchangeable.</li>

  <li>Tuples are written with round brackets.</li>
  </ol>


