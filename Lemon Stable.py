import time
from datetime import datetime
import getpass

print ("Welcome to lemon. What Is Your Computer's User Name?")
username = input ('Answer:')

print ('-- Lemon Alpha --')
print ('Type Help For More Information')

def help ():
    print ('print - print some text')
    print ('math -  do some math')
    print ('time - tell the time')
    print ('lemon - brings you to the lemon website')
    print ('hangman - play a nice game of hangman')
    print ('credit - see the credits for this project')
    print ('calculator - open the calculator app on your computer')
    print ('note - note some stuff down')
    print ('uqm - open ur quan masters')
    print ('bounce - play a game of bounce!')
    print ('exit - exit the program')
    print ('maze - play the 2D maze game')
    print ('fibonacci - cauculate any fibbonacci number')
    print ('cauculate intrest - cauculate the intrest on your credit card based on some aspects')
    print ('disclaimer - read the disclamers on this product')


def disclaim ():
    print ('--DISCLAMER FOR THIS PRODUCT--')
    print ('The designer of this product is not held liable for this product recycling/erasing parts of your system')
    print ('If anything happens and your device is disabled it is due to your instalation and you not reading our instalation instructions')
    print ('In any case, the instructions would be inculded as a text file in the email we sent you')
    print ('Thank You')


def assist ():
    print ("Hi there, I'm lemon assist and I'm here to assist you!")
    
    while (True):
        
        assist = input ('/|~')

        if (assist == "I'm bored"):
            print ("I can't help it, go get something useful to do")
            print ("here's a suggestion: stop pestering me")

        elif (assist == "die"):
            print ("Why don't you try it?")

        elif (assist == "tell me a joke"):
            print ('when you woke the lemon assist robot up what did he say?')
            print ('you are sour to me')

        elif (assist == "do my math for me"):
            print ('Why should I care about your math?')
            print ('do it yourself')

        elif (assist == "what's the weather outside?"):
            print ('go outside and see')

        else:
            print ("That's Intresting")

    

while (True):
    
    cmdlist = input ('>>>')


    if (cmdlist == 'print'):
        write = input ('Print?')
        print (write)

    elif (cmdlist == 'math'):

        import time
        
        print ('1 for dividing, 2 for adding, 3 for subtracting, 4 for mutiplying and 5 for finding a common denominator')
        cmdlist1 = input ('Please Enter What You Want To Do: ')

        if (cmdlist1 == '1'):
            divida =  int (input ('ok enter the first number:'))
            dividb =  int (input ('all right, enter the second number:'))
            print (divida / dividb)
            time.sleep(4)
            
        elif (cmdlist1 == '2'):
            adda =  int (input ('ok enter the first number:'))
            addb =  int (input ('all right, enter the second number:'))
            print (adda + addb)
            time.sleep(4)

        elif (cmdlist1 == '3'):
            subtracta =  int (input ('ok enter the first number:'))
            subtractb =  int (input ('all right, enter the second number:'))
            print (subtracta - subtractb)
            time.sleep(4)

        elif (cmdlist1 == '4'):
            multiplya =  int (input ('ok enter the first number:'))
            multiplyb =  int (input ('all right, enter the second number:'))
            print (multiplya * multiplyb)
            time.sleep(4)

        elif (cmdlist1 == '5'):

            def compute_lcm(x, y):

               if x > y:
                   greater = x
               else:
                   greater = y

               while(True):
                   if((greater % x == 0) and (greater % y == 0)):
                       yee = greater
                       break
                   greater += 1

               return yee
               
            denominator = int (input ('Please enter a first number:'))
            denominator2 = int (input ('Please enter a second number:'))
            print("The Lowest Common Denominator. is", compute_lcm(denominator, denominator2))


        else:
            print ("Bruh, That's Not Even At Option ツ")


    elif (cmdlist == 'time'):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time Is", current_time)



    elif (cmdlist == 'help'):
          help()


    elif (cmdlist == 'lemon'):
        import webbrowser

        webbrowser.open('https://sites.google.com/view/lemonhome/home')  # Go to example.com



    elif (cmdlist == 'rickroll'):
        import webbrowser
        webbrowser.open('https://www.youtube.com/watch?v=dGeEuyG_DIc')

    
    elif (cmdlist == 'hangman'):
        
        import random
        import string

        WORDLIST_FILENAME = "words.txt"

        def load_words():
            """
            Returns a list of valid words. Words are strings of lowercase letters.
    
            Depending on the size of the word list, this function may
            take a while to finish.
            """
            print("Loading word list from file...")
            inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
            line = inFile.readline()
    # wordlist: list of strings

    #wordlist = string.split(line)
            wordlist = line.split()
            
            print(len(wordlist), "words loaded.")
            return wordlist

        def choose_word(wordlist):
            """
            wordlist (list): list of words (strings)

            Returns a word from wordlist at random
            """
            return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
        wordlist = load_words()

# your code begins here!

        def partial_word(chossenword, guessed_letters):
            """
            Return the secret_word in user-visible format, with underscores used
            to replace characters that have not yet been guessed.
            """

            result = ''
    
            for X in chossenword:

                if (X not in guessed_letters):
                    result = result + '_'

                else:
                    result = result + chossenword[len (result)]
                    print ('')

                if (result == chossenword):
                    print ('you win!')
                    break
    
            return result

        guessed_letters = ('')
        print ('')      
        print ('Welcome To The Game Hangman!')
        chossenword = choose_word(wordlist)
        finalnumber = len (chossenword)
        print ('I am thinking of a word that is ' + str (finalnumber) + ' letters long')
        avalibleletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        print ('avalible letters: ' +  str (avalibleletters))
        partial_words = ''
        num = finalnumber


        guesses = 8

        
        while (True):
            print (partial_word(chossenword, guessed_letters))
            print ('you have ' + str (guesses) + ' guesses left!')
            inputguess = input ('Please enter a guess: ')
            guesses = guesses - 1
            print ('-----------')

        
            if (inputguess not in avalibleletters):
                if (inputguess == 'tellmeaboutit'):
                    print (chossenword)
                else:
                    break
                print ('You have entered the same letter twice or entered something else. Please guess again')
                guesses = guesses + 1
                print (partial_word(chossenword, guessed_letters))
               
            else:
                avalibleletters.remove (inputguess)
                inputguessstr = str (inputguess)
                guessed_letters = guessed_letters + (inputguessstr)

            if (inputguess in chossenword):
               print ('good guess!')
       
            elif (inputguess not in chossenword):
                print ('oops! that is not my letter!')
                print ('')
                
        
            print ('You have ' + str (guesses) + ' guesses left!')

            if (guesses <=0):
                print ('You ran out of guesses!')
                break

        print ('')    
        print ('the word is: ' + chossenword)
        print ('')
        print ('good game!')
        print ('wanna try again?')


    elif (cmdlist == 'credit'):
        print ('Main Programer: yongn')


    elif (cmdlist == 'calculator'):
        import subprocess
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')


    elif (cmdlist == 'note'):
        import subprocess
        subprocess.Popen('C:\\Windows\\System32\\write.exe')


    elif (cmdlist == 'uqm'):
        import os
        import subprocess
        ##subprocess.Popen([r"C:\Program Files (x86)\The Ur-Quan Masters\uqm.exe"])
        ##os.system('')
        ##subprocess.run("C:\Program Files (x86)\The Ur-Quan Master\uqm.bat")
        ##subprocess.run (path)
        ##os.chidir(path)
        ##os.system("uqm.bat")

        print ('The Uqm Command Is Current Under Repair, Please Come Back Some Other Time')
        
    elif (cmdlist == 'bounce'):
        from tkinter import *
        import random
        import time

        tk = Tk()
        tk.title("Bounce - The Best Game In The World!")
        tk.resizable(0, 0)
        tk.wm_attributes("-topmost", 1)
        canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
        canvas.pack()
        tk.update()

        class Ball:
            def __init__(self, canvas, paddle, color):
                self.canvas = canvas
                self.paddle = paddle
                self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
                self.canvas.move(self.id, 245, 100)
                starts = [-3, -2, -1, 1, 2, 3]
                random.shuffle(starts)
                self.x = starts[0]
                self.y = -3
                self.canvas_height = self.canvas.winfo_height()
                self.canvas_width = self.canvas.winfo_width()
                self.hit_bottom = False
                
            def draw(self):
                self.canvas.move(self.id, self.x, self.y)
                pos = self.canvas.coords(self.id)
                if pos[1] <= 0:
                    self.y = 3
                if self.hit_paddle(pos) == True:
                    self.y = -3
                if pos[3] >= self.canvas_height:
                    self.hit_bottom = True
                    exit()
                if pos[0] <= 0:
                    self.x = 3
                if pos[2] >= self.canvas_width:
                    self.x = -3
                    
            def hit_paddle(self, pos):
                paddle_pos = self.canvas.coords(self.paddle.id)
                if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                    if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                        return True
                return False

        class Paddle:
            def __init__(self, canvas, color):
                self.canvas = canvas
                self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
                self.canvas.move(self.id, 200, 300)
                self.x = 0
                self.canvas_width = self.canvas.winfo_width()
                self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
                self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
                
            def turn_left(self, evt):
                self.x = -4
                
            def turn_right(self, evt):
                self.x = 4
                
            def draw(self):
                self.canvas.move(self.id, self.x, 0)
                pos = self.canvas.coords(self.id)
                if pos[0] <= 0:
                    self.x = 0
                elif pos[2] >= self.canvas_width:
                    self.x = 0
             
        paddle = Paddle(canvas, 'red')
        ball = Ball(canvas, paddle, 'green')

        while 1:
            if ball.hit_bottom == False:
                ball.draw()
                paddle.draw()
            tk.update_idletasks()
            tk.update()
            time.sleep(0.02)


    elif (cmdlist == 'maze'):
        from tkinter import *
        import random
        import time

        class Game:
            def __init__(self):
                self.tk = Tk()
                self.tk.title("Mr. Stick Man Races for the Exit")
                self.tk.resizable(0, 0)
                self.tk.wm_attributes("-topmost", 1)
                self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
                self.canvas.pack()
                self.tk.update()
                self.canvas_height = 500
                self.canvas_width = 500
                self.bg = PhotoImage(file=r"background.gif")
                w = self.bg.width()
                h = self.bg.height()
                for x in range(0, 5):
                    for y in range(0, 5):
                        self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
                self.sprites = []
                self.running = True

            def mainloop(self):
                while 1:
                    if self.running == True:
                        for sprite in self.sprites:
                            sprite.move()
                    self.tk.update_idletasks()
                    self.tk.update()
                    time.sleep(0.01)

        class Coords:
            def __init__(self, x1=0, y1=0, x2=0, y2=0):
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2

        def within_x(co1, co2):
            if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
                    or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
                    or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
                    or (co2.x2 > co1.x1 and co2.x2 < co1.x1):
                return True
            else:
                return False

        def within_y(co1, co2):
            if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
                    or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
                    or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
                    or (co2.y2 > co1.y1 and co2.y2 < co1.y1):
                return True
            else:
                return False

        def collided_left(co1, co2):
            if within_y(co1, co2):
                if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
                    return True
            return False

        def collided_right(co1, co2):
            if within_y(co1, co2):
                if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
                    return True
            return False

        def collided_top(co1, co2):
            if within_x(co1, co2):
                if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
                    return True
            return False

        def collided_bottom(y, co1, co2):
            if within_x(co1, co2):
                y_calc = co1.y2 + y
                if y_calc >= co2.y1 and y_calc <= co2.y2:
                    return True
            return False

        class Sprite:
            def __init__(self, game):
                self.game = game
                self.endgame = False
                self.coordinates = None
            def move(self):
                pass
            def coords(self):
                return self.coordinates

        class PlatformSprite(Sprite):
            def __init__(self, game, photo_image, x, y, width, height):
                Sprite.__init__(self, game)
                self.photo_image = photo_image
                self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
                self.coordinates = Coords(x, y, x + width, y + height)

        class StickFigureSprite(Sprite):
            def __init__(self, game):
                Sprite.__init__(self, game)
                self.images_left = [
                    PhotoImage(file=r"figure-L1.gif"),
                    PhotoImage(file=r"figure-L2.gif"),
                    PhotoImage(file=r"figure-L3.gif"),
                ]
                self.images_right = [
                    PhotoImage(file=r"figure-R1.gif"),
                    PhotoImage(file=r"figure-R2.gif"),
                    PhotoImage(file=r"figure-R3.gif"),
                ]
                self.image = game.canvas.create_image(200, 470, image=self.images_left[0], anchor='nw')
                self.x = -2
                self.y = 0
                self.current_image = 0
                self.current_image_add = 1
                self.jump_count = 0
                self.last_time = time.time()
                self.coordinates = Coords()
                game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
                game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
                game.canvas.bind_all('<space>', self.jump)
                game.canvas.bind_all('<Up>', self.jump)
                game.canvas.bind_all('<A>' or '<a>', self.turn_left)
                game.canvas.bind_all('<D>'or '<d>', self.turn_right)
                game.canvas.bind_all('<a>' or '<a>', self.turn_left)
                game.canvas.bind_all('<d>'or '<d>', self.turn_right)

            def turn_left(self, evt):
                if self.y == 0:
                    self.x = -2

            def turn_right(self, evt):
                if self.y == 0:
                    self.x = 2

            def jump(self, evt):
                if self.y == 0:
                    self.y = -4
                    self.jump_count = 0
                    
            def animate(self):
                if self.x != 0 and self.y == 0:
                    if time.time() - self.last_time > 0.1:
                        self.last_time = time.time()
                        self.current_image += self.current_image_add
                        if self.current_image >= 2:
                            self.current_image_add = -1
                        if self.current_image <= 0:
                            self.current_image_add = 1
                if self.x < 0:
                    if self.y != 0:
                        self.game.canvas.itemconfig(self.image, image=self.images_left[2])
                    else:
                        self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])
                elif self.x > 0:
                    if self.y != 0:
                        self.game.canvas.itemconfig(self.image, image=self.images_right[2])
                    else:
                        self.game.canvas.itemconfig(self.image, image=self.images_right[self.current_image])

            def coords(self):
                xy = list(self.game.canvas.coords(self.image))
                self.coordinates.x1 = xy[0]
                self.coordinates.y1 = xy[1]
                self.coordinates.x2 = xy[0] + 27
                self.coordinates.y2 = xy[1] + 30
                return self.coordinates
                
            def move(self):
                self.animate()
                if self.y < 0:
                    self.jump_count += 1
                    if self.jump_count > 20:
                        self.y = 4
                if self.y > 0:
                    self.jump_count -= 1
                    
                co = self.coords()
                left = True
                right = True
                top = True
                bottom = True
                falling = True
                
                if self.y > 0 and co.y2 >= self.game.canvas_height:
                    self.y = 0
                    bottom = False
                elif self.y < 0 and co.y1 <= 0:
                    self.y = 0
                    top = False

                if self.x > 0 and co.x2 >= self.game.canvas_width:
                    self.x = 0
                    right = False
                elif self.x < 0 and co.x1 <= 0:
                    self.x = 0
                    left = False

                for sprite in self.game.sprites:
                    if sprite == self:
                        continue
                    sprite_co = sprite.coords()
                    if top and self.y < 0 and collided_top(co, sprite_co):
                        self.y = -self.y
                        top = False
                        
                    if bottom and self.y > 0 and collided_bottom(self.y, co, sprite_co):
                        self.y = sprite_co.y1 - co.y2
                        if self.y < 0:
                            self.y = 0
                        bottom = False
                        top = False

                    if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and collided_bottom(1, co, sprite_co):
                        falling = False
                        
                    if left and self.x < 0 and collided_left(co, sprite_co):
                        self.x = 0
                        left = False
                        if sprite.endgame:
                            self.game.running = False

                    if right and self.x > 0 and collided_right(co, sprite_co):
                        self.x = 0
                        right = False
                        if sprite.endgame:
                            self.game.running = False
                    
                if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
                    self.y = 4
                
                self.game.canvas.move(self.image, self.x, self.y)

        class DoorSprite(Sprite):
            def __init__(self, game, photo_image, x, y, width, height):
                Sprite.__init__(self, game)
                self.photo_image = photo_image
                self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
                self.coordinates = Coords(x, y, x + (width / 2), y + height)
                self.endgame = True


        g = Game()
        platform1 = PlatformSprite(g, PhotoImage(file=r"platform1.gif"), 0, 480, 100, 10)
        platform2 = PlatformSprite(g, PhotoImage(file=r"platform1.gif"), 150, 440, 100, 10)
        platform3 = PlatformSprite(g, PhotoImage(file=r"platform1.gif"), 300, 400, 100, 10)
        platform4 = PlatformSprite(g, PhotoImage(file=r"platform1.gif"), 300, 160, 100, 10)
        platform5 = PlatformSprite(g, PhotoImage(file=r"platform2.gif"), 175, 350, 66, 10)
        platform6 = PlatformSprite(g, PhotoImage(file=r"platform2.gif"), 50, 300, 66, 10)
        platform7 = PlatformSprite(g, PhotoImage(file=r"platform2.gif"), 170, 120, 66, 10)
        platform8 = PlatformSprite(g, PhotoImage(file=r"platform2.gif"), 45, 60, 66, 10)
        platform9 = PlatformSprite(g, PhotoImage(file=r"platform3.gif"), 170, 250, 32, 10)
        platform10 = PlatformSprite(g, PhotoImage(file=r"platform3.gif"), 230, 200, 32, 10)
        g.sprites.append(platform1)
        g.sprites.append(platform2)
        g.sprites.append(platform3)
        g.sprites.append(platform4)
        g.sprites.append(platform5)
        g.sprites.append(platform6)
        g.sprites.append(platform7)
        g.sprites.append(platform8)
        g.sprites.append(platform9)
        g.sprites.append(platform10)
        door = DoorSprite(g, PhotoImage(file=r"door1.gif"), 45, 30, 40, 35)
        g.sprites.append(door)
        sf = StickFigureSprite(g)
        g.sprites.append(sf)
        g.mainloop()

    elif cmdlist == 'fibonacci':
        fibonaccinum = int (input ('How Many Fibonacci Numbers Do You Want To Generate?'))

        n1 = 1
        n2 = 1
        counter = 0

        if (fibonaccinum <= 0):
            print ('please enter a number that is NOT 0')

        elif (fibonaccinum == 1):
            print (n1)

        else:
            while counter < fibonaccinum:
                print (n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                counter += 1


    elif (cmdlist == 'cauculate intrest'):
        outstandingbalance = float(input ('Enter the outstanding balance on your credit card:'))
        annualinterstrate = float(input('Enter the annual credit card interest rate as a decimal:'))
        minimummonthlypaymentrate = float(input ('Enter the minimum monthly payment rate as a decimal:'))

        ##print ('Month: 1')
        ##print ('minimum monthly payment: $',str(outstandingbalance*annualinterstrate))
        ##print ('principle paid: $ ',str(minimummonthlypaymentrate-annualinterstrate))
        ##print ('Remaining Balance:$: ' ,str(outstandingbalance-Principlepaid))


        #int(month = 1)
        month = 1


        while (month <= 12):
            print(month)

            ## Calculation
            ## Minimum monthly payment = Minimum monthly payment rate x Balance (Minimum monthly payment gets split into interest paid and principal paid)

            minMonthlyPayment = outstandingbalance * minimummonthlypaymentrate
            print ('minimum monthly payment: $',str(minMonthlyPayment))


            ## Interest Paid = Annual interest rate / 12 months x Balance
            interestPaid = annualinterstrate/12 * outstandingbalance

            ## Principal paid = Minimum monthly payment – Interest paid 
            print ('principle paid: $ ',str(minMonthlyPayment - interestPaid))


            ## Remaining balance = Balance – Principal paid
            outstandingbalance = outstandingbalance - minMonthlyPayment
            print(outstandingbalance)
            
            
            month = month + 1



        #print ('RESULT')

    elif (cmdlist == 'disclamer'):
        disclaim()
    

    elif (cmdlist == 'exit'):
        exit()

    elif cmdlist == 'lemon assist':
        assist()


    elif (cmdlist == 'break'):
        print ('farewell')
        break


    else:
        print ("Bruh, That's Not Even At Option ツ")
