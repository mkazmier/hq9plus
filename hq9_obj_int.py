from sys import argv

class HQ9PlusPlus:
   def __init__(self):
      self.accumulator = 0

   def h(self):
      print("Hello, world!")
  
   def q(self, src):
      print(src)

   def nine(self):
      for i in range(99, 0, -1):
         print(("""{0} bottle{2} of beer on the wall,
               {0} bottle{2} of beer.
               Take one down, pass it around,
               {1} bottle{3} of beer on the wall.""".format(i, i-1 if i > 1 else 'No', '' if i == 1 else 's', '' if i-1 == 1 else 's')))
   
   def plus(self):
      self.accumulator += 1 
 
   def plusplus(self):

      class GenericSuperClass:
         def __init__(self):
            self.url = 'http://www.wolframalpha.com/input/?i=potassium+in+100+cubic+light+years+of+chocolate+ice+cream'
            # object-oriented nightmare
            self.self = self


      the_object = GenericSuperClass()
 
   def exec_code(self, code):
      valid = ['H', 'Q', '9', '+']
      for char in code:
         if char not in valid:
            print(("{} is not a valid HQ9+ command.".format(char)))
         elif char == 'H':
            self.h()
         elif char == 'Q':
            self.q(code)
         elif char == '9':
            self.nine()
         elif char == '+':
            self.plus()

def main():

   hq9 = HQ9PlusPlus()

   if len(argv) > 1:
      # if a source file is given, load and execute the code
      src = argv[1]
      with open(src, 'r') as f:
         code = f.read().rstrip()
      print(hq9.exec_code(code))
      return

   else:
      # start the REPL
      print("HQ9++ interpreter v 0.9.9.9.9.9\ntype 'help' for a list of commands, 'quit' to quit.")
      while True:
         usr_in = input('> ')
         if usr_in == 'quit':
            return
         elif usr_in == 'help':
            print("""Valid commands:\n
                  H\tprint 'Hello, world!'
                  Q\tprint own source code
                  9\tprint '99 bottles of beer' lyrics
                  +\tincrement the accumulator
                  ++\tinstantiate an object of Generic Supeclass""") 
         else:
            hq9.exec_code(usr_in)

main() 
