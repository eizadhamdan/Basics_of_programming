fn main() {
    //dangling reference
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}

// The Rules of References-
//1. At any given time, we can have either one mutable reference or any number of immutable references.
//2. References must always be valid.