// Activity 5

function getComputerChoice() {
    const randomNumber = Math.floor(Math.random() * 3);
    if (randomNumber === 0) {
        return "rock";
    } else if (randomNumber === 1) {
        return "paper";
    } else if (randomNumber === 2) {
        return "scissors";
    }
}

function determineWinner(userChoice, computerChoice) {
    if (userChoice === computerChoice) {
        return "The game is a tie!";
    } else if (userChoice === "rock" && computerChoice === "scissors") {
        return "You win!";
    } else if (userChoice === "paper" && computerChoice === "rock") {
        return "You win!";
    } else if (userChoice === "scissors" && computerChoice === "paper") {
        return "You win!";
    } else {
        return "You lose!";
    }
}

function playGame() {
    // get user choice
    let userChoice = "paper"; // paper or scissors
    
    if (userChoice === "rock" || userChoice === "paper" || userChoice === "scissors") {
        // proceed with the game. DO NOT CALL THE FUNCTION AGAIN.
    } 
    else if (userChoice === "ROCK" || userChoice === "PAPER" || userChoice === "SCISSORS") {
    }
    else {
        console.log("What the hell is that?"); // handle invalid input
        return;
    }

    // else {
    //     console.log("Just play the freaking game properly jesus."); // handle invalid input
    // }

    // get computer choice
    let computerChoice = getComputerChoice();
    
    // determine winner
    let result = determineWinner(userChoice, computerChoice);
    
    // display results
    console.log(`You chose: ${userChoice}.`);
    console.log(`Computer chose: ${computerChoice}.`);
    console.log(`Result: ${result}`);
}

playGame();