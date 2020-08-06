import random

money = 1000

# Function to print bank


def bank():
    print("Bank: " + str(money) + "\n")

# Helper function to check string input


def is_not_string(player_guess):
    if (type(player_guess) is not str):
        print("Player's guess must be of type string")
        return True
    return False


# Helper function to check integer input
def is_not_int(bet_amount):
    if (type(bet_amount) is not int):
        print("Player's bet must be of type integer")
        return True
    return False

# Helper function to check validity of bet amount


def bet_is_invalid(bet_amount):

    # Check for negative or 0 bet
    if (bet_amount <= 0):
        print(str(bet_amount) +
              " is not a valid bet amount. Please bet a positive value.")
        return True

    # Check for unaffordable bet
    if (bet_amount > money):
        print("You can not afford ${}! Your bank is ${}.".format(
            str(bet_amount), str(money)))
        return True

    # Otherwise bet is NOT invalid and game can continue
    return False


# Helper function to announce wager
def announce_wager(player_call, bet_amount):
    print("Player bets ${} on {}...".format(str(bet_amount), player_call))


# Coin flip game


def coin_flip(player_guess=None, bet_amount=None):
    # Check for correct input types
    if (is_not_string(player_guess) or is_not_int(bet_amount)):
        return 0

    # Check for valid guess value
    player_guess = player_guess.strip().lower()
    if (player_guess != "heads" and player_guess != "tails"):
        print("Please choose either \"heads\" or \"tails\".")
        return 0

    # Check bet is valid
    if (bet_is_invalid(bet_amount)):
        return 0

    # Report player's bet
    announce_wager(player_guess, bet_amount)

    # Determine 50/50 coin flip result
    coin = ""
    if random.randint(0, 1) == 0:
        coin = "tails"
    else:
        coin = "heads"

    # Compare guess to result and define outcome
    if (player_guess == coin):
        print("Coin landed on {}. Player wins {} rupee!!".format(
            coin, str(bet_amount)))
        return bet_amount
    else:
        print("Coin landed on {}. Player loses {} rupee.".format(
            coin, str(bet_amount)))
        return -bet_amount

# Die roll game


def die_roll(player_guess=None, bet_amount=None):
    # Check for correct input types
    if (is_not_string(player_guess) or is_not_int(bet_amount)):
        return 0

    # Check player guess for valid value
    player_guess = player_guess.strip().lower()
    if (player_guess != "even" and player_guess != "odd"):
        print("Please guess either \"odd\" or \"even\".")
        return 0

    # Check bet is valid
    if (bet_is_invalid(bet_amount)):
        return 0

    # Report player's bet
    announce_wager(player_guess, bet_amount)

    # Convert guess string odd/even into int 0 or 1 for modulo check
    player_guess_int = 0
    if (player_guess == "odd"):
        player_guess_int = 1

    # Randomise rolls
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_sum = roll1 + roll2
    odd_even = roll_sum % 2

    # Announce result
    print("The die rolls are {} and {}, for a total of {}.".format(
        str(roll1), str(roll2), str(roll_sum)))

    if (odd_even == player_guess_int):
        print("Player wins {} euro!!".format(str(bet_amount)))
        return bet_amount
    else:
        print("Player loses {} euro.".format(str(bet_amount)))
        return -bet_amount


# Pick a card game

def pick_a_card(bet_amount=None):
    player_card = random.randint(0, 12)
    dealer_card = random.randint(0, 12)
    deck = ["Ace", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "Jack", "Queen", "King"]

    # Check bet is of type integer
    if (is_not_int(bet_amount)):
        return 0

    # Check bet is valid
    if (bet_is_invalid(bet_amount)):
        return 0

    # Report player's bet
    announce_wager("card", bet_amount)

    # Announce cards and result
    if (player_card > dealer_card):
        print("Player's card is {}. Dealer's card is {}. Player wins {} dollars!!".format(
            deck[player_card], deck[dealer_card], str(bet_amount)))
        return bet_amount
    elif (player_card < dealer_card):
        print("Player's card is {}. Dealer's card is {}. Player loses {} dollars.".format(
            deck[player_card], deck[dealer_card], str(bet_amount)))
        return -bet_amount
    else:
        print("Player's card is {}. Dealer's card is {}. It's a tie! Stake returned.".format(
            deck[player_card], deck[dealer_card]))
        return 0


# Roulette game
def roulette(player_guess=None, bet_amount=None):
    # Dictionary of valid guesses
    bet_categories = ["odd", "even", "high", "low", "00"]
    # Shortcut to populate dictionary with "0", "1", "2"...
    for i in range(37):
        bet_categories.append(str(i))

    # Check for correct input types
    if (is_not_string(player_guess) or is_not_int(bet_amount)):
        return 0

    # Check for invalid bet category
    player_guess = player_guess.strip().lower()
    if (player_guess not in bet_categories):
        print("'{}' is not a supported bet type. Please enter one of the following: odd, even, high, low, number 0-36 or 00".format(player_guess))
        return 0

    # Check bet amount is valid
    if (bet_is_invalid(bet_amount)):
        return 0

    # Report player's bet
    announce_wager(player_guess, bet_amount)

    # Randomise winning number
    winner_int = random.randint(0, 37)
    winner = str(winner_int)
    if (winner_int == 37):
        winner = "00"
    winner_sentence = "The winning number is __{}__. ".format(winner)

    # If bet on single
    if (winner == player_guess):
        print(winner_sentence +
              "Player wins {} pounds JACKPOT!!!!".format(str(bet_amount * 38)))
        return bet_amount * 38

    # If bet on odd/even or high/low
    if (player_guess == "even" or player_guess == "odd" or player_guess == "high" or player_guess == "low"):
        # String representation of winning categories. 0 and 00 will be excluded and empty string remains => loss
        winner_odd_even = ""
        winner_high_low = ""

        # Define winner category variables
        if (winner_int % 2 == 0):
            winner_odd_even = "even"
        elif (winner_int % 2 == 1 and winner_int != 37):
            winner_odd_even = "odd"
        if (winner_int in range(1, 19)):
            winner_high_low = "low"
        elif (winner_int in range(19, 37)):
            winner_high_low = "high"

        # Announce outcome
        if (player_guess == winner_odd_even or player_guess == winner_high_low):
            print(winner_sentence + "Player wins {} pounds.".format(str(bet_amount)))
            return bet_amount
        else:
            print(winner_sentence + "Player loses {} pounds.".format(str(bet_amount)))
            return -bet_amount

    # Else a losing single bet
    print(winner_sentence + "Player loses {} pounds.".format(str(bet_amount)))
    return -bet_amount


# Call your game of chance functions here
print("COIN TOSS")
money += coin_flip("TailS", 20)
money += coin_flip("heads!", 35)
money += coin_flip("tails", 20000)
money += coin_flip("heads", 0.0)
money += coin_flip("bingo!", 10)
money += coin_flip(True, 10)
money += coin_flip("tails")
bank()

print("DIE ROLL")
money += die_roll("Even", 10)
money += die_roll("odd", 5)
money += die_roll("even", 20000)
money += die_roll("even", -24)
money += die_roll("rainbow", 10)
bank()

print("PICK A CARD")
money += pick_a_card(20)
money += pick_a_card(40)
money += pick_a_card(-7)
money += pick_a_card(30000)
money += pick_a_card()
money += pick_a_card("Queen")
bank()

print("ROULETTE")
money += roulette("5", 10)
money += roulette("even", 25)
money += roulette("HIgH", 30)
money += roulette("38", 10)
money += roulette("bulls EYE", 50)
money += roulette("00", 10)
money += roulette("12", 15000)
money += roulette()

bank()
