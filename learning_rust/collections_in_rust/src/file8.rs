use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();

    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 20);

    scores.entry(String::from("Yellow")).or_insert(30); //this will create a new entry for Yellow
    scores.entry(String::from("Yellow")).or_insert(40); //this won't do anything
}
