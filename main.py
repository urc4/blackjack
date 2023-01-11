import classes as cs
import logic as lgc

#How can I introduce the ability for multiple players
#to play at once, maybe a dictionary...

# Game logic alltogether
#name = input('Player name: ')
#balance = int(input('Initial balance: '))

player = cs.Player()
dealer = cs.Dealer()

game_on = True
round_count = 0

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
   player_hand = lgc.hand_value(player)
   val_hand = lgc.valid_hand(player_hand)
   # Maybe can introduce this to while loop down below
   if val_hand == False:
      game_on = False
      break


   choice = lgc.player_choice(player)
   while choice == 'h' and val_hand == True:
      player.add_cards(new_deck.deal_one())
      player.print_cards()
      dealer.print_cards(1)
      choice = lgc.player_choice(player)
      player_hand = lgc.hand_value(player)
      val_hand = lgc.valid_hand(player_hand)

   if val_hand == False:
      break


   player.print_cards()
   dealer.print_cards()

   dealer_hand = lgc.hand_value(dealer)
   val_hand = lgc.valid_hand(dealer_hand)

   if dealer_hand < 17:
      choice = lgc.player_choice(dealer)
   while choice == 'h' and val_hand == True:
      dealer.add_cards(new_deck.deal_one())
      player.print_cards()
      dealer.print_cards()
      choice = lgc.player_choice(dealer)
      dealer_hand = lgc.hand_value(dealer)
      val_hand = lgc.valid_hand(dealer_hand)

   if val_hand == False or player_hand > dealer_hand: 
      player.deposit(bet_amt*1.5)
      break
   elif player_hand == dealer_hand:
      player.deposit(bet_amt)
   else:
      pass
#this looks out of place and it doesnt work...why?
   game_on = lgc.gameon(player)
   