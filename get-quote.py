import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)
  last = 13
  rnd = random.randint(0, last)
  quotes = quotes + ["some more text"]
  print(quotes[14])

if __name__== "__main__":
  primary()
