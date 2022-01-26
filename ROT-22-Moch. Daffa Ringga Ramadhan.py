"from string import maketrans"

rot13trans = "".maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234- ')

# Function to translate plain text
def rot13(text):
   return text.translate(rot13trans)
def main():
   txt = input("ROT 13 ALGORITM = ")
   print (rot13(txt))
	
if __name__ == "__main__":
   main()

# FravabxgborE = SeninoktobeR (ROT)