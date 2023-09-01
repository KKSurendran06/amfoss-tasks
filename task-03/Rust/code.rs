fn is_prime(n: u32) -> bool {
    if n < 2 {
        return false;
    }

    for i in 2..n {
        if n % i == 0 {
            return false;
        }
    }

    true
}

fn main() {
    println!("Enter a number");
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let N: u32 = input.trim().parse().unwrap();

    for i in 2..N {
        if is_prime(i) {
            println!("{}", i);
        }
    }
}
