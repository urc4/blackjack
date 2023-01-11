# Do I need to import classes here? Hopefully not, cause it works the way it is

# Maybe could potentially remove player as argument and instead just give 
# out its attributes needed for the funcion. Can I use kwargs?
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

def player_choice(name):
   choice = 'wrong'
   # hit requests an extra card and stay the opposite
   while choice not in ['h','s']:
      choice = input(f'{name} choose to hit(h) or stay(s): ')
      if choice not in ['h','s']:
         print('Pick a valid choice. Please try again.')

   return choice

def valid_hand(hand_value,name):
   if hand_value > 21:
      print(f'{name}, it is a BUST!')
      return False
   else: 
      return True


def gameon(name):
   choice = 'wrong'
   # hit requests an extra card and stay the opposite
   while choice not in ['y','n']:
      choice = input(f'Does {name} want to keep losing money? Yes(y) or No(n): ')
      if choice not in ['y','n']:
         print('Pick a valid choice. Please try again.')

   if choice == 'y':
      return True
   else:
      return False