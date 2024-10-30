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

