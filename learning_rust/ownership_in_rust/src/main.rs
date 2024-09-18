fn main() {
    println!("Learning about ownership in Rust.");

    //Ownership Rules----
    //1. Each value in Rust has a variable that's called its owner.
    //2. There can only be one owner at a time.
    //3. When the owner goes out of scope, the value will be dropped.

    {
        //s is not valid here, it's not yet declared
        let s = String::from("hello");        //s is valid from this point forward
        //we can do stuff here with s
    }   //this scope is now over, and s is nolonger valid

    let x = 5;
    let y = x;      //copy

    let s1 = String::from("Hello");
    // let s2 = s1;        //Move
    let s2 = s1.clone();

    println!("{}, world!", s1);         //this will throw a compile error if we move it

    let s = String::from("Good Morning");
    // takes_ownership(s);     //if we pass a parameter to a function it'll also move it
    // println!("{}", s);      //so this won't work here

    let a = 5;
    makes_copy(a);
    println!("{}", x);
}

fn takes_ownership(some_string: String) {
    println!("{}", some_string);
}

fn makes_copy(some_integer: i32) {
    println!("{}", some_integer);
}