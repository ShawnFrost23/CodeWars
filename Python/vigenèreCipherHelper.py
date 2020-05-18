class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key
    
    def encode(self, text):
        ret = ""
        for i in range(0, len(text)):
            if text[i] in self.alphabet:
                tempAsciiCode = self.alphabet.index(text[i])
                if i >= len(self.key):
                    j = i % len(self.key)
                    keyAscii = self.alphabet.index(self.key[j])
                else: keyAscii = self.alphabet.index(self.key[i])
                newAscii = tempAsciiCode + keyAscii
                if newAscii >= len(self.alphabet):
                    newAscii = newAscii % len(self.alphabet)
                    ret += self.alphabet[newAscii]
                else: ret += self.alphabet[newAscii]
            else: ret += text[i]
        return ret
                
              
    
    def decode(self, text):
        ret = ""
        for i in range(0, len(text)):
            if text[i] in self.alphabet:
                tempAsciiCode = self.alphabet.index(text[i])
                if i >= len(self.key):
                    j = i % len(self.key)
                    keyAscii = self.alphabet.index(self.key[j])
                else: keyAscii = self.alphabet.index(self.key[i])
                newAscii = tempAsciiCode - keyAscii
                if newAscii >= len(self.alphabet):
                    newAscii = newAscii % len(self.alphabet)
                    ret += self.alphabet[newAscii]
                else: ret += self.alphabet[newAscii]
            else: ret += text[i]
        return ret
                

# Visual representation:

# "my secret code i want to secure"  // message
# "passwordpasswordpasswordpasswor"  // key
# Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.

# Example

# var alphabet = 'abcdefghijklmnopqrstuvwxyz';
# var key = 'password';

# creates a cipher helper with each letter substituted
#  by the corresponding character in the key
# var c = new VigenèreCipher(key, alphabet);

# c.encode('codewars'); // returns 'rovwsoiv'
# c.decode('laxxhsj');  // returns 'waffles'
# Any character not in the alphabet must be left as is. For example (following from above):

# c.encode('CODEWARS'); // returns 'CODEWARS'