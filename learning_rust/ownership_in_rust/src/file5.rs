//Slices let us reference a contiguous sequence of elements of a collection instead of referencing the entire collection.
//Slices don't take the ownership of the underlying data.

fn main() {
    let mut s = String::from("Hello everyone");
    
    let hello = &s[0..5];           //let hello = &s[..5];           
    let world = &s[6..11];          //let world = &s[6..];
    println!("string slice-1: {}, string slice-2: {}", hello, world);
    
    let word = first_word_another(s);
    // s.clear();

    let array = [1, 2, 3, 4, 5];
    let slice = &a[0..2];
}

fn first_word(s: &String) -> usize {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }
    }

    s.len()
}

fn first_word_another(a_string: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}