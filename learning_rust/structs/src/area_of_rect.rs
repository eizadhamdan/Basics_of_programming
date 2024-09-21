// fn main() {
//     let width1: u32 = 30;
//     let height1: u32 = 50;

//     println!(
//         "The area of the rectangle is {} square pixels.",
//         area(width1, height1)
//     );
// }

// fn area(width: u32, height: u32) -> u32 {
//     width * height
// }

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32
}

//implementation block which has methods
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

//implementation block which has associated functions
impl Rectangle {
    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size
        }
    }
}

fn main() {
    let rect: Rectangle = Rectangle {
        width: 30,
        height: 50
    };

    let rect1: Rectangle = Rectangle {
        width: 10,
        height: 30
    };

    let rect2: Rectangle = Rectangle {
        width: 50,
        height: 100
    };

    let rect3: Rectangle = Rectangle::square(25);

    println!("rect can hold rect1: {}", rect.can_hold(&rect1));
    println!("rect can hold rect2: {}", rect.can_hold(&rect2));

    // println!("rect: {:#?}", rect);
    println!("rect: {:?}", rect);

    println!(
        "The area of the rectangle is {} square pixels.",
        // area(&rect)
        rect.area()
    );
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}