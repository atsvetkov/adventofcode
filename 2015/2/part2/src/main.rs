use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path> {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {
    if let Ok(lines) = read_lines("input.txt") {
        let mut total = 0;
        for line in lines {
            if let Ok(sizes) = line {
                let mut arr = [0,0,0];
                let mut i = 0;
                for size in sizes.split("x") {
                    let s = size.parse::<i32>().unwrap();
                    arr[i] = s;
                    i += 1;
                }
                let per = [2*(arr[0]+arr[1]), 2*(arr[1]+arr[2]), 2*(arr[2]+arr[0])];
                total += arr[0]*arr[1]*arr[2] + per.iter().min().unwrap();
            }
        }
        println!("{}", total);
    }
}
