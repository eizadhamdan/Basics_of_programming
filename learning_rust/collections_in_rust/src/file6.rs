use unicode_segmentation::UnicodeSegmentation;

fn main() {
    let hello: String = String::from("Hello");

    //using the bytes method
    for b in hello.bytes() {
        println!("{}", b);
    } //this will give bytes

    //to get scalar values
    for c in hello.chars() {
        println!("{}", c);
    }

    //to get grapheme clusters
    for g in hello.graphemes(true) {
        println!("{}", g);
    }
}
