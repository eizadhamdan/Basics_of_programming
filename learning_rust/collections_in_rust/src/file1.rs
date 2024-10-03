fn main() {
    let v = vec![1, 2, 3, 4, 5];

    //this is an immutable reference
    let third_elem = &v[2];
    println!("The third element is {}", third_elem);

    // a safer way to get an element from a vector, this prevents runtime errors.
    match v.get(2) {
        Some(third) => println!("The third element is {}", third),
        None => println!("Third element doesn't exist!"),
    }
}
