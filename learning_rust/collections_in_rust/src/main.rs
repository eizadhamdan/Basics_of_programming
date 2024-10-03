fn main() {
    let a = [1, 2, 3]; //an array of signed 32-bit integers
    let mut v: Vec<i32> = Vec::new(); //a vector of signed 32-bit integers
    v.push(1);
    v.push(2);
    v.push(3);

    {
        let v2 = vec![1, 2, 3];
    }
}
