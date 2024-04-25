auction_end = False
logo = '''
 ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________
                         `'-------'`
                       .-------------.
                      /_______________

'''

print(logo)
bids = {}

def check_higher_bids (bid_record):
    highest_bid = 0
    winner_name = ''
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner_name = bidder
    print(f'O vencedor foi: {winner_name}, com um lance de: R${highest_bid}')

while not auction_end:
    bidder_name = input('Qual o seu nome: ')
    bidder_value = float(input('Qual o seu lance: R$'))
      
    bids[bidder_name] = bidder_value
   
    end_auction = input("Digite 'sim' para outro lance ou 'não' para encerrar o leilão'.\n").lower()
    if end_auction == "não":
       auction_end = True
       check_higher_bids(bids) 
       print("Encerrando")

