fn main() {
    let mut s1 = String::from("This is ");
    change(&mut s1);        //we can only have one reference
    //it is done to prevent data race

    println!("{}", s1);

    println!("-----------------------------------------------");

    let mut s2 = String::from("Hello");
    let r1 = &s2;
    //we can have multiple mutable references
    // let r2 = &mut s2;            //we can't have a mutable reference if immutable references exist
    println!("{}", r1);

    let r3 = &mut s2;
    println!("{}", r3);
}

fn change(some_string: &mut String) {
    some_string.push_str("a word.");
}
