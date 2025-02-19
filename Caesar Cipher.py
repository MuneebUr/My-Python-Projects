
def ceaser_cipher():
     alphabet = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
     get_letter = ""
     ciphertext = []
     key = int(input("Enter key"))
     while key >26 or key < 0 :
         print("Try Again")
         key = int(input("Enter key"))
     else:
         print("Valid Key")

     text = str(input("Enter the text:")).strip().lower()

     for letter in text:
        get_letter =  alphabet.index(letter) + key
        ciphertext.append(alphabet[get_letter])
     print("".join(ciphertext)+" is the ciphertext")

ceaser_cipher()

############################################################################################################################################################################################################

def brute_decrypt():
     alphabet = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
     ciphertext = str((input("Enter Encrypted text:"))).lower().strip()
     get_letter = ""
     for i in range (0,26):
         pos_plaintext = []
         for letter in ciphertext:
             get_letter  =  alphabet.index(letter) + i
             pos_plaintext.append(alphabet[get_letter])
         print("".join(pos_plaintext) + " is the possible plaintext ")

brute_decrypt()

#############################################################################################################################################################################################################

