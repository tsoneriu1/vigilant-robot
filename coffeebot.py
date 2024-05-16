#!/usr/bin/env python3
soup = 0

# Define your functions
def coffee_bot():
   
  print("Welcome to the Cafe!")
  size = get_size()

  drink_type = get_drink_type()
  print('Ok, that\'s a {} {}.'.format(size, drink_type))
  name = input('Can I get your name please? ')
  print("Thanks, {}! Your drink will be ready soon".format(name))
  return True

def get_size():
  res = input('What size drink can I get for you?\n [a] Small \n [b] Medium \n [c] Large\n ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    noSoup()
    print("Choose a letter (a,b,c)")
    return get_size() 
  return res

def get_drink_type():
  res = input('What type of drink would you like?\n [a] Cold Brew \n [b] Mocha \n [c] Latte\n ')
  if res == 'a':
    return 'cold brew'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    noSoup()
    print("Choose a letter (a,b,c)")

    return get_drink_type() 
  return res

def order_latte():
  res = input('What kind of milk would you like for your latte?\n [a] Oat Milk \n [b] Cow Milk \n [c] Soy Milk\n ')
  if res == 'a':
    return 'oat latte'
  elif res == 'b':
    return 'milk latte'
  elif res == 'c':
    return 'soy latte'
  else:
    noSoup()
    print("Choose a letter (a,b,c)")
    return order_latte() 
  return res
  return 0

def noSoup():
  global soup
  soup = soup + 1
  if soup > 10:
    print(""""
              ,-.          ,-.
         /   \        /   \
       .'       `.    .'       `.
      /  /\/\/\/\  \  /  /\/\/\/\  \
     |  |          | |  |          | |
     |  |          | |  |          | |
     |  |  NO      | |  |          | |
     |  |  SOUP    | |  |          | |
     |  |  FOR     | |  |          | | 
     |  |  YOU     | |  |          | |
     |  |          | |  |          | |
     |  |          | |  |          | |
     |  |          | |  |          | |
     \  \________/  /  \________/  /
      `._          _.'    `._          _.'
        `--------`        `--------`
    """")
    exit()

# Call coffee_bot()!
coffee_bot()
