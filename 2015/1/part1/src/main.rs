use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    let path = Path::new("input.txt");
    let display = path.display();
    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };
    let mut input = String::new();
    match file.read_to_string(&mut input) {
        Err(why) => panic!("couldn't read {}: {}", display, why),
        Ok(_) => println!("Success"),
    }
    let mut count = 0;
    for c in input.chars() {
        if c == '(' {
            count += 1;
        } else {
            count -= 1;
        }
    }
    println!("Answer: {}", count);
}
