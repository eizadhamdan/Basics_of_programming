fn main() {
    value_in_cents(Coin::Quarter(USState::Alabama));
}

#[derive(Debug)]
enum USState {
    Alabama,
    Maine,
    California,
    Washington,
    Florida,
    Arkansas,
    Kansas,
    // ....
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(USState),
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky Penny");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}", state);
            25
        }
    }
}