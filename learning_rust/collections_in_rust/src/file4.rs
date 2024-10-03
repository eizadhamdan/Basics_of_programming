// Strings are stored as a collection of UTF-8 encoded bytes

fn main() {
    let s1 = String::new;
    let s2 = "Initial contents";
    let s3 = s2.to_string();
    let s4 = String::from("Initial contents");
}
