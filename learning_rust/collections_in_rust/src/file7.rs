use std::collections::HashMap;

fn main() {
    let blue = String::from("Blue");
    let yellow = String::from("Yellow");

    let mut scores = HashMap::new();

    //this passes the ownership of the strings into the HashMap
    scores.insert(blue, 10);
    scores.insert(yellow, 50);

    let team_name = String::from("Blue");
    let score = scores.get(&team_name); //this returns an option

    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }
}
