## Summary

This repo is a practice of Decorator with Python.

To know the implementation of Decorator, you better familiar with Fisrt Class Function and Clousre.

*All the step is followed by [youtube channel](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) created by Corey Schafer.*

## [First-Class Function](https://www.youtube.com/watch?v=kr0mpwqttM0&t=10s)

First-Class Functions:
"A Programming language is said to have first-class functions if it treats functions as first-class citizens"

First-Class Citizen (Programming):
"A first-Class citizen (sometimes called first-class objects) in a programming language is an entity which supports all the operation generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable"

**In brief, if a programming language can treats functions as objects like varialbe. Then this programming language has first-class functions.**

For example:
 
```   
    def cube(num):
        return num ** 3

    def map(func, nums):
        num_list = []
        for num in nums:
            num_list.append(func(num))
        return num_list
```

Because we can pass function cube as an object to map function, so Python has First-Class Functions.

## [Closures](https://www.youtube.com/watch?v=swU3c34d2NQ&pbjreload=10)

Closures:
Wikipedia says, "A closure is a record storing a function together with an environment: a mapping associating free variable of the function with value or storage location to which the name was bound when the closure was created. A closure, unlike a plain function, allows the function to access those captured variables through the closure's reference to them, even when the function is invoked outside their scope."

**In brief, a closure contains inner function and outer function, the inner function can access the variable from outside variable which called free variable here and contribute to a variety of combination**

For example:
 
```   
    def outer_func():
        message = 'Hi'

        def inner_func():
            print(message)

        return inner_func

    func = outer_func()
    func()
```

Because outer_func() will return inner_func as object, then will can execute this object with parenthesis which is func() here.

## [Decorators](https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=212s)

Use Decorator in Python is just mark a "at" before the line of a function. There are four cases of decorators:

#### Decorator Function w/o args
```
    def decorateApple(f):
        def d_f(*args, **kargs):
            print("apple before call")
            result = f(*args, **kargs)
            print("apple after call")
            return result
        return d_f

    @decorateApple
    def print_hello():
        print("hello first time.")

    print_hello()
```

output
```
apple before call
hello first time.
apple after call
```

#### Decorator Function w/ args
```
    def decorateFruit(fruit, rotLevel):
        def outer_d_f(f):
            def d_f(*args, **kargs):
                print("%s %s before call" % (rotLevel, fruit))
                result = f(*args, **kargs)
                print("%s %s after call" % (rotLevel, fruit))
                return result
            return d_f
        return outer_d_f

    @decorateFruit('banana', 'new')
    def print_hello2():
        print("hello 2nd time.")

    @decorateFruit('guava', '50% rot')
    def print_hello3():
        print("hello 3th time.")

    print_hello2()
    print('')
    print_hello3()
```

output
```
apple before call
hello first time.
apple after call
```

#### Decorator Class w/o args
```
class decorateAppleClass(object):
    def __init__(self, f):
        self.f = f
    
    def __call__(self, *args, **kargs):
        print("apple before call")
        result = self.f(*args, **kargs)
        print("apple after call")
        return result


@decorateAppleClass
def print_hello4():
    print("hello 4th time.")

print_hello4()
```

output
```
    apple before call
    hello 4th time.
    apple after call
    Because outer_func() will return inner_func as object, then will can execute this object with parenthesis which is func() here.
```

#### Decorator Class w/ args
```
class decorateFruitClass(object):
    def __init__(self, fruit, rotLevel):
        self.fruit = fruit
        self.rotLevel = rotLevel

    def __call__(self, f):
        def d_f(*args, **kargs):
            print("%s %s before call" % (self.rotLevel, self.fruit))
            result = f(*args, **kargs)
            print("%s %s after call" % (self.rotLevel, self.fruit))
            return result
        return d_f

@decorateFruitClass('guava', '80% rot')
def print_hello5():
    print("hello 5th times.")

@decorateFruitClass('banana', '30% rot')
def print_hello6():
    print("hello 6th times.")

print_hello5()
print('')
print_hello6()
```

output
```
80% rot guava before call
hello 5nd time.
80% rot guava after call

30% rot banana before call
hello 6th time.
30% rot banana after call
```

## Conclusion

In this project, we practice the complete implementation of Decorator w/ and w/o arguments.

## Reference
1. [First-Class Function](https://www.youtube.com/watch?v=kr0mpwqttM0&t=10s)
2. [Closures](https://www.youtube.com/watch?v=swU3c34d2NQ&pbjreload=10)
3. [Decorators](https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=212s)
4. [Python Decorator 四種寫法範例 Code](http://ot-note.logdown.com)