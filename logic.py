def player_bet(player):
   
   bet_amt = 'wrong'
   print(f'{player.name} has ${player.balance}')
   
   while bet_amt.isdigit() == False or int(bet_amt) > player.balance:
      
      bet_amt = input(f'\n{player.name}, place your bet for this round: $')

      if bet_amt.isdigit() == False:
         print('Enter a valid amount. Please try again.')
      if int(bet_amt) > player.balance:
         print(f'Your bet of ${bet_amt} can not top your balance of ${player.balance}')
         print('Please enter a valid amount.')

   return int(bet_amt)

def player_choice(player):
   choice = 'wrong'
   # hit requests an extra card and stay the opposite
   while choice not in ['h','s']:
      choice = input(f'{player.name} choose to hit(h) or stay(s): ')
      if choice not in ['h','s']:
         print('Pick a valid choice. Please try again.')

   return choice

def valid_hand(hand_value):
   if hand_value > 21:
      print('BUST!')
      return False
   else: 
      return True


# Could make the game automatically take in and understand the player's mind!!!
# instead of asking for him to choose between one or eleven
def hand_value(jock):
   hand_value = 0
   ace_count = 0
   
   for card in jock.all_cards:
      if card.rank == 'Ace':
         ace_count += 1
      else:
         hand_value += card.value
   
   if ace_count == 0:
      return hand_value
   else:
      possible_hand_values = [hand_value]*(ace_count+1)
      for index in range(ace_count+1):
         possible_hand_values[index] += (ace_count-index)*1 + index*11
      best_hand = min(possible_hand_values)
      for index in range(1,ace_count+1):
         if possible_hand_values[index] <= 21:
            best_hand = possible_hand_values[index]
      return best_hand


def gameon(player):
   choice = 'wrong'
   # hit requests an extra card and stay the opposite
   while choice not in ['y','n']:
      choice = input(f'Does {player.name} want to keep losing money? Yes(y) or No(n): ')
      if choice not in ['y','n']:
         print('Pick a valid choice. Please try again.')

   if choice == 'y':
      return True
   else:
      return False