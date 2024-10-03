fn main() {
    let mut s = String::from("foo");
    s.push_str("bar");
    s.push('!');
    println!("{}", s);

    let s1 = String::from("Hello, ");
    let s2 = String::from("world!");

    //here we are moving the ownership of s1 into s3 and we're taking the characters in s2 and appending them to s3
    let s3: String = s1 + &s2;

    println!("{}", s3);

    //using the format macro
    let word1 = String::from("Hi ");
    let word2 = String::from("user!");
    let combined = format!("{}{}", word1, word2);

    println!("{}", combined);
}
