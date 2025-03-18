 bank-account assignment


In this assignment, you will use the object-oriented programming paradigm to
model a bank account in Python. Like in the previous assignments, we are not
building a user interface, but underlying data structures and functionality
which will be thoroughly tested.

We will provide a polished API so that other developers can use our code to
build their applications. That means, special attention will be given to
implement data model methods such as `__str__` and `__repr__`.


## Design

### Account class

The account class represents a bank account. It is constructed without any
arguments.

#### Example: create a new account instance
```python
my_account = Account()
```

| Property              | Description
| -----------           | ---
| `transactions`        | A list of Transaction instances
| `get_balance()`       | A method which returns the account balance
| `deposit(amount)`     | A method which creates a deposit transaction
| `withdraw(amount)`    | A method which creates a withdrawal transaction


#### Example: making transactions
Here's an example of how the end product usage could look:
```python
>>> account = Account()
>>> account.deposit(1000)
>>> account.get_balance()
200.0
>>> account.withdraw(800)
>>> account.get_balance()
190.0
```

### Transaction class

A transaction class represents a monetary transaction event. It has two
properties: an amount, and a timestamp.

| Property                      | Description
| ------------                  | --
| `amount: float, int, Decimal` | The amount entered in the constructor
| `timestamp: datetime`         | The date & time which the transaction occurred.


A `Transaction` class must be instantiated with an amount argument, and has an
optional `timestamp` which defaults to `None`. If the timestamp is not
provided, it is automatically set to the current date & time.

```python
>>> from banking import Transaction
>>> transaction = Transaction(100.0)
>>> transaction.timestamp
datetime.datetime(2018, 12, 31, 8, 3, 1)
>>> transaction.amount
100.0

>>> import datetime as dt
>>> transaction = Transaction(10, dt.datetime(2002, 1, 10))
>>> transaction.timestamp
datetime.datetime(2002, 1, 10, 0, 0, 0)
```

### Requirements & Evaluation
- `(/1)` Write you classes in a module called `banking.py`
- `(/1)` Write your tests in a module called `test_banking.py`
-  Write a class called `Transaction` as defined above:
    - `(/2)` Class definition
    - `(/4)` `__init__` method & tests ensuring that:
        - The amount parameter is bound to `self`
        - The provided optional timestamp parameter is bound to `self`. If no
          value is provided, use the current datetime.
    - `(/2)` `__repr__` which returns an appropriate string + test. Remember,
    good practice for a `repr` is to produce a string which can be copy &
    pasted into the interpreter to reproduce a similar instance.
    - `(/2)` `__str__` which returns a string containing both the timestamp and
      amount. E.g.
        - `2019-01-01: +$1,234.56`
        - `2020-01-01: -$17.25`

- Write a class called Account as defined above:
    - `(/2)` Class definition
    - `(/6)` A deposit method which:
        - `(/1)` Is named `deposit`
        - `(/1)` Accepts a single parameter called amount
        - `(/2)` The amount is converted to a positive value + tests
        - `(/2)` A new instance of `Transaction` is created using the amount.
                 The new transaction instance is then appended to the account's
                 `transactions`. Provide test(s).
    - `(/6)` A withdraw method which:
        - `(/1)` Is named `withdraw`
        - `(/1)` Accepts a single parameter called amount
        - `(/2)` The amount is converted to a negative value + tests
        - `(/2)` A new instance of `Transaction` is created with the converted
          amount. The instance is appended to the list of transactions. Provide
          test(s).
    - `(/5)` A balance retrieval method which:
        - `(/1)` Is named `get_balance`
        - `(/4)` Returns the sum of all transaction amounts stored on the
          object.
            - If no transactions exist, this should return 0
            - If the transactions consist of a deposit of 100, a withdrawl of
              90, and deposit of 10, the balance should be 20.
            - Challenge: see if you can figure out how to use the `sum()`
              function on the transactions list


### Code style
The final commit must have a green checkmark beside it as a result of a
successful Travis CI run.

**-1% will be deducted** from the assignment for each code violation.



### Warning about default values
**Note:** Beware of mutable default values as class properties. Read the
following article on a common "gotcha" surrounding the defining default values
using mutable types like lists and dicts.

https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments

The same situation described applies to classes. Example:
```python
# Danger!
class MyClass:
    my_list = []


# Safe
class MyClass:
    def __init__(self):
        self.my_list = []
```
