import random


def choose_option():
  options = ('piedra', 'papel', 'tijera')
  user = False

  while user == False:
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
      print('esa opcion no es valida')
      continue
    else:
      user = True

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)

  return user_option, computer_option


def rounds_win():
  while True:
    rounds_to_win = int(input('Rondas a vencedoras para ganar (hasta 100):'))
    if rounds_to_win in range(1, 101):
      return rounds_to_win
    else:
      print('esa opcion no es valida')
      continue


def posibilities(user_option, computer_option, user_wins, computer_wins):
  choses = {'papel': 0, 'tijera': 1, 'piedra': 2}
  
  '''Aqui obtendremos el valor de la eleccion que elejimos y a su vez la llave del mismo (use la forma mas dificil a proposito):'''
  
  user_option = choses[user_option]
  user_option_key = list(choses.keys())[list(choses.values()).index(user_option)]
  computer_option = choses[computer_option]
  computer_option_key = list(choses.keys())[list(choses.values()).index(computer_option)]
  
  '''tambien se peude hacer asi mas simple creando otra variable que almacene el valor de nuestra eleccion y dejando intacta la variable de nuestra opcion:
  
  user_value = choses[user_option]
  computer_value = choses[computer_option]
  
  ya luego para el print solo usariamos directamente "user_option" y "computer_option" '''
  
  if user_option == computer_option:
    print('Empate!')
  elif user_option == (computer_option - 1):
    print(computer_option_key + ' gana a ' + user_option_key)
    print('computer gano!')
    computer_wins += 1
  else:
    print(user_option_key + ' gana a ' + computer_option_key)
    print('user gano!')
    user_wins += 1

  return user_wins, computer_wins


def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1

  rounds_to_win = rounds_win()

  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    user_option, computer_option = choose_option()

    user_wins, computer_wins = posibilities(user_option, computer_option,
                                            user_wins, computer_wins)
    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    if computer_wins == rounds_to_win:
      print('El ganador es la computadora')
      break

    if user_wins == rounds_to_win:
      print('El ganador es el usuario')
      break

  return


run_game()