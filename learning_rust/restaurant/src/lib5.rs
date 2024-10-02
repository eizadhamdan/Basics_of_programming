//bringing two different modules into scope
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> fmt::Result {
    //--function definition--
}

fn function2() -> io::IoResult<()> {
    //--function definition--
}
