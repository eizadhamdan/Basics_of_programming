enum IpAddressKind {
    V4(u8, u8, u8, u8),
    V6(String),
}

enum Message {
    Quit,
    MOve {x: i32, y: i32},
    Write(String),
    ChangeColor(i32, i32, i32),
}

impl Message {
    fn message_print_function() {
        println!("Implementation block is running!");
    }
}

struct IpAddress {
    kind: IpAddressKind,
    address: String,
}

fn main() {
    let localhost = IpAddressKind::V4(127, 0, 0, 1);
}

fn route(ip_kind: IpAddressKind) {}
