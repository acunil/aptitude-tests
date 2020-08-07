let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

// Called at the start of each new round to generate new secret target number 0-9 (inclusive).
function generateTarget() {
  return Math.floor(Math.random() * 10);
}

// Called each round to determine which guess is closest to target number.
function compareGuesses(humanGuess, computerGuess, target) {
  let distanceHuman = Math.abs(target - humanGuess);
  let distanceComp = Math.abs(target - computerGuess);
  return distanceHuman <= distanceComp;
}

// Increases winner's score by 1 each round.
function updateScore(winner) {
  winner === "human" ? humanScore++ : computerScore++;
}

// Progresses the round number at the end of each round.
function advanceRound() {
  currentRoundNumber++;
}
