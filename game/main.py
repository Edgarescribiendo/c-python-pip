import random

def board():
  print(
  '''
  
        Bienvenido al GRAN TORNEO DE JANKENPON!!!

               Elige sabiamente tu opcion
                (piedra, papel o tijeras)
      ''')


def options():
  opt_3 = ('piedra','papel','tijeras') 
  user_opt = input('Elige el usuario una opcion ').lower()
  user2_pc = random.choice(opt_3)
  print(f'la opcion de la pc es : {user2_pc}')
  
  
  return user_opt, user2_pc
  
def choose_opt(user_opt, user2_pc, counter_user,counter_user2): 

  if user_opt == 'tijeras' and user2_pc == 'piedra':  
      counter_user2 += 1
      print(f'''
      El pc a anotado un punto a su favor. 
      
 puntuacion es la siguiente:
      Primer usuario {counter_user},  pc {counter_user2}.''')
      
  elif user_opt == 'tijeras' and user2_pc == 'papel':
    counter_user += 1
    print(f'''
    El usuario a anotado un punto a su favor. 
    
 puntuacion es la siguiente:
      Usuario {counter_user}, pc {counter_user2}.''')
  
  elif user_opt == 'tijeras' and user2_pc == 'tijeras':
    print(f'''
    Ningún usuario a anotado un punto a su favor.  
    
 puntuacion es la siguiente:
    Usuario {counter_user},  pc {counter_user2}.''')

  elif user_opt == 'piedra' and user2_pc == 'tijeras':
    counter_user += 1
    
    print(f'''
    El usuario a anotado un punto a su favor. 
    
 puntuacion es la siguiente:
    Usuario {counter_user},  pc {counter_user2}.''')

  elif user_opt == 'piedra' and user2_pc == 'papel':
    counter_user2 += 1
    print(f'''
    El  pc a anotado un punto a su favor. 
    
 puntuacion es la siguiente:
    Usuario {counter_user},  pc {counter_user2}.''')

  elif user_opt == 'piedra' and user2_pc == 'piedra':
    
    print(f'''
    Ningún usuario a anotado un punto a su favor.  
    
 puntuacion es la siguiente:
    Usuario {counter_user},  pc {counter_user2}.''')

  elif user_opt == 'papel' and user2_pc == 'tijeras':
    
    counter_user2 += 1
    print(f'''
    El  pc a anotado un punto a su favor. 
    
 puntuacion es la siguiente:
    Usuario {counter_user},  pc {counter_user2}.''')

  elif user_opt == 'papel' and user2_pc == 'piedra':
    counter_user += 1
    
    print(f'''
    El usuario a anotado un punto a su favor. 
    
 puntuacion es la siguiente:
    Usuario {counter_user},  pc {counter_user2}.''')

  elif user_opt == 'papel' and user2_pc == 'papel':
    
    print(f'''
    Ningún usuario a anotado un punto a su favor. 
    
 puntuacion es la siguiente:
    Usuario {counter_user},  pc {counter_user2}.''')
    
  else:
    print('Una de las opciones no esta permitida')

  return counter_user,counter_user2


def process(counter_user,counter_user2,round):
  
  while True :
  
    if counter_user < 2 and counter_user2 < 2:
      print(f'''
    {round} ronda                          
    ''')
      round += 1
    
      
      user_opt,user2_pc = options()
      counter_user,counter_user2 = choose_opt(user_opt,user2_pc,counter_user,counter_user2)    
    
    
    
    elif counter_user == 2:
      print('''
      Ganador usuario 1''')
      break
    elif counter_user2 == 2:
      print('''                                             
    Ganador  pc ''')
      break
    else:
      break
      
     
  else: 
    exit()



def run():  
  counter_user = 0 
  counter_user2 = 0
  round = 1
  
  board()
  process(counter_user,counter_user2,round)
  
  
if __name__ == '__main__':
  run()