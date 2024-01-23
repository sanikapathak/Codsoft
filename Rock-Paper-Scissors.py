import random

a = "Lets play Rock - Paper - Scissors"
print(a.center(50, "-"))

#define rules for the game
print('\nWinning rules of the game Rock-Paper-Scissors are :\n' +
      "Rock vs Paper -> Paper is winner \n" +
      "Rock vs Scissors -> Rock is winner \n" +
      "Paper vs Scissors -> Scissor is winner \n")


def get_player_choice():

  player_choice = input("Enter a choice (rock, paper, scissors): ")
  while player_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice, Please choose rock, paper, or scissors.")
    player_choice = input("Choose rock, paper, or scissors: ").lower()
  return player_choice


def get_computer_choice():
  return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(player_choice, computer_choice):
  if player_choice == computer_choice:
    return "It's a tie!"
  elif (player_choice == 'rock' and computer_choice == 'scissors') or \
     (player_choice == 'scissors' and computer_choice == 'paper') or \
     (player_choice == 'paper' and computer_choice == 'rock'):
    return "You win!"
  else:
    return "You lose!"


def display_result(player_choice, computer_choice, result):

  print("\nYou chose: ", player_choice)
  print("Computer chose: ", computer_choice)
  print("\nResult is: ", result)


def play_game():
  player_choice = get_player_choice()
  computer_choice = get_computer_choice()
  result = determine_winner(player_choice, computer_choice)
  display_result(player_choice, computer_choice, result)
  return result


def main():
  player_score = 0
  computer_score = 0

  while True:
    result = play_game()
    if 'win' in result.lower():
      player_score += 1
    elif 'lose' in result.lower():
      computer_score += 1

    print("\nScore = Your score:", player_score, "\nComputer score:", computer_score)

    #ask user if they want to play again
    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
      print("\nGame Over!!")
      break


if __name__ == "__main__":
  main()
