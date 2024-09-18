fn main() {
    let s1 = String::from("hello");
    let (s2, len) = calculate_length(s1);
    println!("The length of '{}' is {}", s2, len);

    println!("---------------------------------------");

    let s3 = String::from("morning");
    let length_string = calculate_length_another(&s3);          //passing strings as reference is called borrowing
    println!("The length of '{}' is {}", s3, length_string);
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len();           //len() returns the length of a string
    
    (s, length)
}

//references are immutable
fn calculate_length_another(a_string: &String) -> usize {
    let length_of_string = a_string.len();

    length_of_string
}