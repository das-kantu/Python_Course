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

<h1>Example:</h1>
<h2>Create a Tuple:</h2>

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```


<h1>Tuple Items</h1>
<ol>
  <li>Tuple items are ordered, unchangeable, and allow duplicate values.</li>

  <li>Tuple items are indexed, the first item has index [0], the second item has index [1] etc.</li>
</ol>

<h2>Ordered</h2>
<b>When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.</b>

<h2>Unchangeable</h2>
<b>Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.</b>

<h2>Allow Duplicates</h2>
<b>Since tuples are indexed, they can have items with the same value:</b>

<h1>Example</h1>
<b>Tuples allow duplicate values:</b>

```python
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```

<h1>Tuple Length</h1>
<h2>To determine how many items a tuple has, use the len() function:</h2>

<b>Example</b>
<b>Print the number of items in the tuple:</b>

```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

```

<h1>Access Tuple Items</h1>
<h2>Access Tuple Items</h2>
<h3>You can access tuple items by referring to the index number, inside square brackets:</h3>

<b>ExampleGet your own Python Server</b>
<b>Print the second item in the tuple:</b>
```python

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

```
<h1>Negative Indexing</h1>
<h2>Negative indexing means start from the end.</h2>

<b>-1 refers to the last item, -2 refers to the second last item etc.</b>

<b>Example</b>
<b>Print the last item of the tuple:</b>

```python

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

```
<h1>Range of Indexes</h1>
<h2>You can specify a range of indexes by specifying where to start and where to end the range.</h2>

<h3>When specifying a range, the return value will be a new tuple with the specified items.</h3>

<b>Example</b>
<b>Return the third, fourth, and fifth item:</b>

```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
```
<h1>Range of Negative Indexes</h1>
<h2>Specify negative indexes if you want to start the search from the end of the tuple:</h2>

<b>Example</b>
<b>This example returns the items from index -4 (included) to index -1 (excluded)</b>

```python

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

```
<h1>Update Tuples</h1>
<b>Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.</b>

<h3>But there are some workarounds.</h3>

<b>Change Tuple Values</b>
<ol>
  <li>Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.</li>

  <li>But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.</li>
</ol>

<h3>Example:</h3>
<b>Convert the tuple into a list to be able to change it:</b>

```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

```
<h1>Unpack Tuples</h1>
<h2>Unpacking a Tuple</h2>
<b>When we create a tuple, we normally assign values to it. This is called "packing" a tuple:</b>

<b>ExampleGet your own Python Server</b>
<b>Packing a tuple:</b>
```python
fruits = ("apple", "banana", "cherry")
print(fruits)
```
<h2>Using Asterisk*</h2>
<h3>If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:</h3>

<b>Example</b>
<b>Assign the rest of the values as a list called "red":</b>

```python

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

```

<h1>Loop Tuples</h1>
<h2>Loop Through a Tuple</h2>
<h3>You can loop through the tuple items by using a for loop.</h3>

<b>ExampleGet your own Python Server</b>
<b>Iterate through the items and print the values:</b>
```python
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
```
<h1>Loop Through the Index Numbers</h1>
<h2>You can also loop through the tuple items by referring to their index number.</h2>

<h3>Use the range() and len() functions to create a suitable iterable.</h3>

<b>Example</b>
<b>Print all items by referring to their index number:</b>

```python
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
```

<h1>Join Tuples</h1>
<h2>Join Two Tuples</h2>
<b>To join two or more tuples you can use the + operator:</b>

<b>ExampleGet your own Python Server</b>
<b>Join two tuples:</b>

```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```
<h1>Multiply Tuples</h1>
<h2>If you want to multiply the content of a tuple a given number of times, you can use the * operator:</h2>

<b>Example</b>
<b>Multiply the fruits tuple by 2:</b>

```python
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
```
<h1>Python Lists</h1>

<h2>List</h2>
<ol>
 <li>Lists are used to store multiple items in a single variable.</li>

  <li>Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.</li>

  <li>Lists are created using square brackets:</li>
</ol>
<b>Example:</b>
<b>Create a List:</b>


```python

thislist = ["apple", "banana", "cherry"]
print(thislist)

```

<h1>List Items</h1>
<ol>
 <li>List items are ordered, changeable, and allow duplicate values.</li>

  <li>List items are indexed, the first item has index [0], the second item has index [1] etc.</li>

</ol>

<h1>Ordered</h1>
<ol>
  <li>When we say that lists are ordered, it means that the items have a defined order, and that order will not change.</li>

  <li>If you add new items to a list, the new items will be placed at the end of the list.</li>
</ol>

<h1>Changeable</h1>
<h2>The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.</h2>

<h1>Allow Duplicates</h1>
<h2>Since lists are indexed, lists can have items with the same value:</h2>

<h1>Example</h1>
</h2>Lists allow duplicate values:</h2>

```python

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

```

<h1>List Length</h1>
<h2>To determine how many items a list has, use the len() function:</h2>

<b>Example:</b>
<b>Print the number of items in the list:</b>

```python

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

```
<h1>The list() Constructor</h1>
<b>It is also possible to use the list() constructor when creating a new list.</b>

<b>Example</b>
<b>Using the list() constructor to make a List:</b>

```python

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

```
<h1>Access List Items</h1>
<h2>Access Items</h2>
<b>List items are indexed and you can access them by referring to the index number:</b>

<b>Example:</b>
<b>Print the second item of the list:</b>

```python

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

```
<h1>Negative Indexing</h1>
<h2>Negative indexing means start from the end</h2>

<b>-1 refers to the last item, -2 refers to the second last item etc.</b>

<b>Example</b>
<b>Print the last item of the list:</b>


```python
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

```
<h1>Range of Indexes</h1>
<h2>You can specify a range of indexes by specifying where to start and where to end the range.</h2>

<h3>When specifying a range, the return value will be a new list with the specified items.</h3>

<h2>Example:</h2>
<b>Return the third, fourth, and fifth item:</b>

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```

<h1>Range of Negative Indexes</h1>
<h2>Specify negative indexes if you want to start the search from the end of the list:</h2>

<h2>Example:</h2>
<h3>This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):</h3>

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

```
<h1>Change List Items</h1>
<h1>Change Item Value</h1>
<h2>To change the value of a specific item, refer to the index number:</h2>

<h3>Example:</h3>
<b>Change the second item:</b>

```python

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

```
<h1>Change a Range of Item Values</h1>
<h2>To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:</h2>

<h3>Example</h3>
<b>Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":</b>

```python

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

```

<h1>Add List Items</h1>
<h2>Append Items</h2>
<h3>To add an item to the end of the list, use the append() method:</h3>

<h2>Example:</h2>
<b>Using the append() method to append an item:</b>

```python

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

```
<h1>Insert Items:</h1>
<h2>To insert a list item at a specified index, use the insert() method.</h2>
<h3>The insert() method inserts an item at the specified index:</h3>

<h2>Example</h2>
<b>Insert an item as the second position:</b>

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

```

<h2>Extend List</h2>
<h3>To append elements from another list to the current list, use the extend() method.</h3>

<h3>Example:</h3>
<b>Add the elements of tropical to thislist:</b>

```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
```

<h1>Remove List Items</h1>
<h2>Remove Specified Item</h2>
<h3>The remove() method removes the specified item.</h3>

<h2>Example:</h2>
<b>Remove "banana":</b>

```python

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

```
<h1>Remove Specified Index</h1>
<h2>The pop() method removes the specified index.</h2>

<h3>Example:</h3>
<b>Remove the second item:</b>

```python

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

```
<h2>If you do not specify the index, the pop() method removes the last item.</h2>

<h3>Example</h3>
<b>Remove the last item:</b>

```python

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

```
<h1>Clear the List</h1>
<h2>The clear() method empties the list.</h2>

<h3>The list still remains, but it has no content.</h3>

<h3>Example:</h3>
<b>Clear the list content:</b>

```python

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

```
<h1>Loop Lists</h1>
<h2>Loop Through a List</h2>
<h3>You can loop through the list items by using a for loop:</h3>

<h2>Example:</h2>
<b>Print all items in the list, one by one:</b>

```python

thislist = ["apple", "banana", "cherry"]
for x in thislist:

  print(x)
```


<h1>List Comprehension</h1>
<h2>List Comprehension</h2>
<h3>List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.</h3>

<h2>Example:</h2>

<ol>
    <li>Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.</li>
    <li>Without list comprehension you will have to write a for statement with a conditional test inside:</li>
</ol>

<h1>Example</h1>


```python

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

```
<h1>Sort Lists</h1>
<h2>Sort List Alphanumerically</h2>
<h3>List objects have a sort() method that will sort the list alphanumerically, ascending, by default:</h3>

<h2>Example:</h2>
<b>Sort the list alphabetically:</b>



```python

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

```
<h1>Sort Descending</h1>
<h2>To sort descending, use the keyword argument reverse = True:</h2>

<h3>Example:</h3>
<b>Sort the list descending:</b>

```python

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

```

<h1>Copy a List</h1>

<h1>Use the copy() method</h1>
<h2>You can use the built-in List method copy() to copy a list.</h2>

<h3>Example:<h3>
<b>Make a copy of a list with the copy() method:</b>

```python

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

```
<h1>Use the slice Operator</h1>
<h2>You can also make a copy of a list by using the : (slice) operator.</h2>

<h2>Example:</h2>
<b>Make a copy of a list with the : operator:</b>

```python

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

```



