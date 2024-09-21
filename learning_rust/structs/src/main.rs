struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

fn main() {
    let mut user1 = User {
        email: String::from("abcdefgh@gmail.com"),
        username: String::from("testUser"),
        active: true,
        sign_in_count: 1,
    };

    let name = user1.username;
    user1.username = String::from("newUser");

    let user2 = build_user(
        String::from("abcd123@gmail.com"), 
        String::from("anotherUser"),
    );

    let user3 = User{
        email: String::from("12345abcdefg@gmail.com"),
        username: String::from("anotherTestUser"),
        ..user2
    };
}

fn build_user(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}
