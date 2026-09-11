- Python Data Types
    
    # Python Data Types
    
    Data types specify the type of data that a variable can store.
    
    ## 🗒️ Built-in Data Types
    
    | Category | Data Types | Main Use |
    | --- | --- | --- |
    | **Text Type** | `str` | Stores text and characters |
    | **Numeric Types** | `int` | Stores whole numbers |
    |  | `float` | Stores decimal numbers |
    |  | `complex` | Stores complex numbers |
    | **Sequence Types** | `list` | Stores a collection of items |
    |  | `tuple` | Stores an ordered collection of items |
    |  | `range` | Represents a sequence of numbers |
    | **Mapping Type** | `dict` | Stores data as key-value pairs |
    | **Set Types** | `set` | Stores a collection of items |
    |  | `frozenset` | Stores an immutable set |
    | **Boolean Type** | `bool` | Stores "True" or "False" values |
    | **Binary Types** | `bytes` | Stores binary data |
    |  | `bytearray` | Stores mutable binary data |
    |  | `memoryview` | Provides access to data in memory |
    | **None Type** | `NoneType` | Represents "None" |
    
    ---
    
    ## 🔎 Getting the Data Type
    
    Use the `type()` function to check the data type of an object.
    
    ```python
    x = 5
    print(type(x))
    ```
    
    **Output:**
    
    ```
    <class 'int'>
    ```
    
    ---
    
    ## ⚙️ Setting the Data Type
    
    The data type is automatically set when a value is assigned to a variable.
    
    | Example | Data Type |
    | --- | --- |
    | `x = "Hello World"` | `str` |
    | `x = 20` | `int` |
    | `x = 20.5` | `float` |
    | `x = 1j` | `complex` |
    | `x = ["apple", "banana", "cherry"]` | `list` |
    | `x = ("apple", "banana", "cherry")` | `tuple` |
    | `x = range(6)` | `range` |
    | `x = {"name": "John", "age": 36}` | `dict` |
    | `x = {"apple", "banana", "cherry"}` | `set` |
    | `x = frozenset({"apple", "banana", "cherry"})` | `frozenset` |
    | `x = True` | `bool` |
    | `x = b"Hello"` | `bytes` |
    | `x = bytearray(5)` | `bytearray` |
    | `x = memoryview(bytes(5))` | `memoryview` |
    | `x = None` | `NoneType` |
    
    ---
    
    ## 🛠️ Setting a Specific Data Type
    
    Python provides constructor functions to specify a data type.
    
    | Constructor | Data Type | Example |
    | --- | --- | --- |
    | `str()` | `str` | `str("Hello World")` |
    | `int()` | `int` | `int(20)` |
    | `float()` | `float` | `float(20.5)` |
    | `complex()` | `complex` | `complex(1j)` |
    | `list()` | `list` | `list(("apple", "banana", "cherry"))` |
    | `tuple()` | `tuple` | `tuple(("apple", "banana", "cherry"))` |
    | `range()` | `range` | `range(6)` |
    | `dict()` | `dict` | `dict(name="John", age=36)` |
    | `set()` | `set` | `set(("apple", "banana", "cherry"))` |
    | `frozenset()` | `frozenset` | `frozenset(("apple", "banana", "cherry"))` |
    | `bool()` | `bool` | `bool(5)` |
    | `bytes()` | `bytes` | `bytes(5)` |
    | `bytearray()` | `bytearray` | `bytearray(5)` |
    | `memoryview()` | `memoryview` | `memoryview(bytes(5))` |
   