import classes as cs
import logic as lgc

#How can I introduce the ability for multiple players
#to play at once, maybe a dictionary...

# Maybe add later some extra functionalities like doubling down
# spllitting pairs and others

# Game logic alltogether
#name = input('Player name: ')
#balance = int(input('Initial balance: '))

player = cs.Player()
dealer = cs.Dealer()

game_on = True
round_count = 0
# for some reason I cant get to round 2
while game_on:
   round_count += 1
   # Check if players can bet
   # We assume the dealer has an infinite amount of chatter (or not).
   if player.balance < 0:
      end ='-'*50
      print(f'\n{player.name} has run out of money. Game over, mf.\n{end}')
      game_on = False
      break

   # Start a new round
   round_boundary = '-'*40
   print(f'\n{round_boundary} Round {round_count} {round_boundary}\n')
   new_deck = cs.Deck()
   new_deck.shuffle()
   player.clear_hand()
   dealer.clear_hand()
   
   # Place bet
   bet_amt = lgc.player_bet(player)
   player.place_bet(bet_amt)

   # Give out initial cards
   for num in range(2):
      player.add_cards(new_deck.deal_one())
      dealer.add_cards(new_deck.deal_one())
   
   player.print_cards()
   dealer.print_cards(1)

   # Choose to hit or to stay
   player_hand = player.hand_value()
   val_hand = lgc.valid_hand(player_hand,player.name)
   # Maybe can introduce this to while loop down below
   if val_hand == False:
      game_on = lgc.gameon(player.name)
      break


   choice = lgc.player_choice(player.name)
   while choice == 'h' and val_hand == True:
      player.add_cards(new_deck.deal_one())
      player.print_cards()
      dealer.print_cards(1)
      choice = lgc.player_choice(player.name)
      player_hand = player.hand_value()
      val_hand = lgc.valid_hand(player_hand,player.name)

   if val_hand == False:
      print(f'{player.name} you have lost your bet\n{dealer.name} keeps it.')
      game_on = lgc.gameon(player.name)
      break


   player.print_cards()
   dealer.print_cards()

   dealer_hand = dealer.hand_value()
   val_hand = lgc.valid_hand(dealer_hand,dealer.name)

   while dealer_hand < 17:
      dealer.add_cards(new_deck.deal_one())
      player.print_cards()
      dealer.print_cards()
      dealer_hand = dealer.hand_value()
      val_hand = lgc.valid_hand(dealer_hand,dealer.name)

   if val_hand == False or player_hand > dealer_hand: 
      player.deposit(bet_amt*1.5)
      print(f'Congrats, {player.name}!\nYou have earned ${bet_amt*1.5}')
      game_on = lgc.gameon(player.name)
      break
   elif player_hand == dealer_hand:
      player.deposit(bet_amt)
      print(f'It is a two way tie.\nTake back your bet of ${bet_amt}')
      game_on = lgc.gameon(player.name)
      break
   else:
      print(f'{player.name} you have lost your bet\n{dealer.name} keeps it.')
      game_on = lgc.gameon(player.name)
      break
   
   