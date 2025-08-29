
import random, os

balance = 5000
game = True
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def get_balance():
  return balance

def random_card():
  return random.choice(cards)

def clear_screen():
  os.system('cls')

def add_random_card(maze):
  while True:
    next_card = random_card()
    if next_card not in maze:
      break
  maze.append(next_card)

def sum_cards(maze):
  total = 0
  for card in maze:
    if card != 'J' and card != 'Q' and card != 'K':
        total += card
    else:
      total += 10
  
  if 11 in maze and total > 21:
    total -= 10
  return total

def print_stats(player_stats, dealer_stats):
  print(f'\nYou: {player_stats} -> {sum_cards(player_cards)}')
  print(f'Dealer: {dealer_stats} -> {sum_cards(dealer_cards)}\n')

def manage_balance(win, bet):
  if win == -1:
    return -bet
  elif win == 1:
    return bet
  else:
    return 0
  
def print_state(win):
  if win == -1:
    print('Player loses.')
  elif win == 1:
    print('Player wins!')
  else:
    print('Draw.')

while game:
  clear_screen()
  print(f'Balance: {balance}')
  while True:
    bet = int(input('\nWhat\'s your bet?: '))
    clear_screen()
    if bet <= balance and bet > 0:
      break
    elif bet > balance:
      print('You don\'t have enought money.')
    else:
      print('Invalid bet.')
  player_cards = []
  dealer_cards = []
  win = 1

  player_cards.append(random_card())
  dealer_cards.append(random_card())


  can_continue = True
  while can_continue:
    while True:
      print_stats(player_cards, dealer_cards)
      add_or_pass = input('Type \'add\' if you want to keep going or \'pass\' if you want to stop: ')
      clear_screen()
      if add_or_pass == 'add' or add_or_pass == 'pass':
        break
    if add_or_pass == 'add':
      add_random_card(player_cards)

      if sum_cards(player_cards) > 21:
        can_continue = False
        win = -1

      clear_screen()
    else:
      can_continue = False
  
  if win == -1:
    balance += manage_balance(win, bet)
  else:
    final_player_sum = sum_cards(player_cards)
    while sum_cards(dealer_cards) < final_player_sum:
      add_random_card(dealer_cards)
    
    final_dealer_sum = sum_cards(dealer_cards)
    if final_dealer_sum <= 21 and final_dealer_sum > final_player_sum:
      win = -1
    elif final_dealer_sum == final_player_sum:
      win = 0
    balance += manage_balance(win, bet)


  while True:
    print_stats(player_cards, dealer_cards)
    print_state(win)
    print(f'Balance: {balance}\n')
    another = input('Type \'yes\' if you want to make another bet. Type \'no\' if not: ')
    if another == 'yes':
      break
    elif another == 'no':
      game = False
      break
    clear_screen()
  clear_screen()