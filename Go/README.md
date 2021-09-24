## Go (Things that I didn't know

#### Primitive Types and Declarations
* Literals (1_234, 1_2_3_4, 6.03e23)
* Go lets you use an integer literal in floating point expressions or even assign an integer literal to a floating point variable. This is because literals in Go are untyped
* The reason why int64 and uint64 are the idiomatic choice in this situation is that Go doesn’t have generics (yet) and doesn’t have function overloading. Without these features, you’d need to write many functions with slightly different names to implement your algorithm. Using int64 and uint64 means that you can write the code once and let your callers use type conversions to pass values in and convert data that’s returned.
* no other type can be converted to a bool, implicitly or explicitly
* const in Go is very limited. Constants in Go are a way to give names to literals. They can only hold values that the compiler can figure out at compile time.
* Constants can be typed or untyped. An untyped constant works exactly like a literal; it has no type of its own, but does have a default type that is used when no other type can be inferred. A typed constant can only be directly assigned to a variable of that type.
* Untyped constant declaration (`const x = 10`), Valid assignments (`var y int = x`, var z float64 = x, var d byte = x)
* The compiler’s unused variable check is not exhaustive. As long as a variable is read once, the compiler won’t complain

#### Composite Types
