## Go (Things that I didn't know)

#### Primitive Types and Declarations
* Literals (`1_234`, `1_2_3_4`, `6.03e23`)
* Go lets you use an integer literal in floating point expressions or even assign an integer literal to a floating point variable. This is because literals in Go are untyped
* The reason why `int64` and `uint64` are the idiomatic choice in this situation is that Go doesn’t have generics (yet) and doesn’t have function overloading. Without these features, you’d need to write many functions with slightly different names to implement your algorithm. Using `int64` and `uint64` means that you can write the code once and let your callers use type conversions to pass values in and convert data that’s returned.
* no other type can be converted to a `bool`, implicitly or explicitly
* `const` in Go is very limited. Constants in Go are a way to give names to literals. They can only hold values that the compiler can figure out at compile time.
* Constants can be typed or untyped. An untyped constant works exactly like a literal; it has no type of its own, but does have a default type that is used when no other type can be inferred. A typed constant can only be directly assigned to a variable of that type.
* Untyped constant declaration (`const x = 10`), Valid assignments (`var y int = x`, `var z float64 = x`, `var d byte = x`)
* The compiler’s unused variable check is not exhaustive. As long as a variable is read once, the compiler won’t complain

#### Composite Types
* You can specify array like this `var x = [12]int{1, 5: 4, 6, 10: 100, 15}` = `[1, 0, 0, 0, 0, 4, 6, 0, 0, 0,100, 15]`
* Go considers the size of the array to be part of the type of the array.
* In Go, nil is an identifier that represents the lack of a value for some types. Like the untyped numeric constants we saw in the previous chapter, nil has no type, so it can be assigned or compared against values of different types.
* The rules as of Go 1.14 are to double the size of the slice when the capacity is less than 1,024 and then grow by at least 25% afterward.
* The full slice expression protects against append
```
    x := make([]int, 0, 5)
	x = append(x, 1, 2, 3, 4)
	y := x[:2:2]
	z := x[2:4:4]
	fmt.Println(cap(x), cap(y), cap(z))
	y = append(y, 30)
	x = append(x, 60)
	z = append(z, 70)
	fmt.Println("x:", x)
	fmt.Println("y:", y)
	fmt.Println("z:", z)
```
* It copies as many values as it can from source to destination, limited by whichever slice is smaller, and returns the number of elements copied. The capacity of x and y doesn’t matter; it’s the length that’s important.
* go vet blocks a type conversion to string from any integer type other than rune or byte.
* You can also declare that a variable implements a struct type without first giving the struct type a name. This is called an anonymous struct
* Go does allow you to perform a type conversion from one struct type to another if the fields of both structs have the same names, order, and types

#### Blocks, Shadows, and Control Structures


#### Concurrency in Go
* Go cocurrency model is based on CSP (Communicating Sequential Processes).
* More concurrency doesn’t automatically make things faster, and it can make code harder to understand.
* Concurrency is a tool to better structure the problem you are trying to solve. Whether or not concurrent code runs in parallel (at the same time) depends on the hardware and if the algorithm allows it.
* Whether or not you should use concurrency
in your program depends on how data flows through the steps in your program.
* **Use concurrency when you want to combine data from multiple operations that can operate independently.**
* If you are not sure if concurrency will help, first
write your code serially, and then write a benchmark to compare performance with a concurrent implementation.
* Goroutines are lightweight **processes** managed by the Go runtime.
* When a Go program starts, the Go runtime creates a number of threads and launches a single goroutine to run your program. All of the goroutines created by your program, including the initial one, are assigned to these threads automatically by the Go runtime scheduler, just as the operating system schedules threads across CPU cores.
* When you pass a channel to a function, you are really passing a pointer to the channel. Also like maps and slices, the zero value for a channel is nil.
* Be aware that closing a channel is only required if there is a goroutine waiting for the channel to close (such as one using a for-range loop to read from the channel).
* Another advantage of select choosing at random is that it prevents one of the most common causes of deadlocks: acquiring locks in an inconsistent order.
* Whenever you launch a goroutine function, you must make sure that it will eventually exit.
* Buffered channels are useful when you know how many goroutines you have launched, want to limit the number of goroutines you will launch, or want to limit the amount of work that is queued up.
* Buffered channels work great when you want to either gather data back from a set of goroutines that you have launched or when you want to limit concurrent usage.
* If you are waiting on several goroutines, you need to use a WaitGroup , which is found in the sync package in the standard library.
* Use mutex when your goroutines read or write a shared value, but don’t process the value.
* Rule of thumbs:
	* If you are coordinating goroutines or tracking a value as it is transformed by a
series of goroutines, use channels.
	* If you are sharing access to a field in a struct, use mutexes.
	* If you discover a critical performance issue when using channels and you cannot find any other way
to fix the issue, modify your code to use a mutex.
* Goroutine will only exit if the main routine exit, it will not stop if a function simply return
```
package main

import (
	"fmt"
	"time"
)

func test() {
	go func() {
		time.Sleep(5 * time.Millisecond)
		fmt.Println("test")
	}()
	
	return
}

func main() {

	test()
	fmt.Println("test1")
	time.Sleep(10 * time.Millisecond)
}

```

#### Modules, Packages and Imports
* Library management in Go is based around three concepts: ***repositories***,  ***modules***, and ***packages***.
  * **Repositories** is just like Github repo
  * **Module** is the root of a Go library or application, stored in a **repository**. It also consists one or more packages.
* In Go, we usually use the path to the module repository where the module is found. For example, `github.com/lauchokyip/hello-world`
```
module github.com/lauchokyip/helloworld

go 1.15

require (
  github.com/shopspring/decimal v1.2.0.
)
```
* Every `go.mod` file starts with a `module` declaration. Followed by the minimum compatible version of Go. . `require` section lists the modules that your module depends on and the minimum version required for each one.
* We need to specify an **import** path when importing from anywhere besides the standard library. 
* [How do you structure your go apps](https://www.youtube.com/watch?v=1rxDzs0zgcE)
  * Group by function

  



#### More
* [Pointers vs values in parameters and return values](https://stackoverflow.com/questions/23542989/pointers-vs-values-in-parameters-and-return-values)
