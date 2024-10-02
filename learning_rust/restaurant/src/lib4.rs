use rand::{CryptoRng, ErrorKind::Transient, Rng}; //using nested paths

use std::io::{self, Write};

use std::io::*; //all public items in io are now in scope

mod front_of_house; //the definition of this module is in the file with the same name as this module

// use self::front_of_house::hosting;
pub use crate::front_of_house::hosting;
//external code can now reference hosting as well

pub fn eat_at_restaurant() {
    let secret_number = rand::thread_rng().gen_range(1, 101);

    front_of_house::hosting::add_to_waitlist();
    front_of_house::hosting::add_to_waitlist();
    front_of_house::hosting::add_to_waitlist();

    hosting::add_to_waitlist();
}
