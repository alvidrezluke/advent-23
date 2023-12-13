use std::fs;

fn main() {
    let (scratchers, numbers) = read_data(&"day4lukeinput.txt");
    
    let mut scratcher_quantity: Vec<u64> = vec![1; scratchers.len()];
    let mut scratchers_to_play: Vec<u64> = vec![1; scratchers.len()];
    
    let mut sum: u64 = 0;
    let mut end: bool = false;

    while !end {
        let prev_scratcher_quantity = scratcher_quantity.clone();
        scratchers_to_play = play_scratchers(&scratchers_to_play, &scratchers, &numbers);
        scratcher_quantity = vec_element_add(&scratchers_to_play, &prev_scratcher_quantity);

        if vec_elements_equal(&prev_scratcher_quantity, &scratcher_quantity) { end = true }
    }
    for el in scratcher_quantity { sum += el }
    println!("Sum: {}", sum)
}

fn parse_numbers(input: &str) -> Vec<u64> {
    return input.trim()
                .split(" ")
                .collect::<Vec<_>>()
                .into_iter()
                .filter(|x| !x.is_empty())
                .collect::<Vec<_>>()
                .into_iter()
                .map(|x| x.parse::<u64>().unwrap())
                .collect();
}

fn vec_element_add(vec_1: &Vec<u64>, vec_2: &Vec<u64>) -> Vec<u64> {
    return vec_1.iter().zip(vec_2.iter()).map(|(&a, &b)| a + b).collect()
}

fn vec_elements_equal(vec_1: &Vec<u64>, vec_2: &Vec<u64>) -> bool {
    return vec_1.iter().zip(vec_2).filter(|&(a, b)| a == b).count() == vec_1.len()
}

fn read_data(filename: &str) -> (Vec<Vec<u64>>, Vec<Vec<u64>>) {
    let text = fs::read_to_string(filename).expect("Unable to find file.");
    let rounds = text.split("\n");
    let mut scratchers: Vec<Vec<u64>> = vec![];
    let mut numbers: Vec<Vec<u64>> = vec![];

    for round in rounds {
        let (card, nums) = round.trim().split_once("|").expect("Could not split round");
        let (_, card_nums_str) = card.trim().split_once(":").expect("Could not split card");
        let card_nums = parse_numbers(card_nums_str);
        scratchers.push(card_nums.clone());
        let elf_nums = parse_numbers(nums);
        numbers.push(elf_nums.clone());
    }
    return (scratchers, numbers);
} 

fn play_card(card: &Vec<u64>, numbers: &Vec<u64>) -> u64 {
    return card.into_iter().filter(|x| numbers.contains(x)).collect::<Vec<_>>().len() as u64;
}

fn play_scratchers(scratchers_to_play: &Vec<u64>, scratchers: &Vec<Vec<u64>>, numbers: &Vec<Vec<u64>>) -> Vec<u64> {
    let mut won_scratchers: Vec<u64> = vec![0; scratchers.len()];
    for i in 0..scratchers_to_play.len() {
        if scratchers_to_play[i] > 0 {
            let wins = play_card(&scratchers[i], &numbers[i]);
            for j in (i + 1)..(i + 1 + wins as usize) {
                won_scratchers[j] = won_scratchers[j] + scratchers_to_play.get(i).expect("Unable to fetch");
            }
        }
    }
    return won_scratchers;
}