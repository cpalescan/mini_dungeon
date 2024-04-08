print("""
 
                                       ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
            ,---`_,888`  ,.''*''`-.,|,|/!,--,.&\|&\-,|&#:::::

""")
print("Welcome to the Doomed Castle.")
print("I challenge you to find the treasure!") 
print()
print()

##### entrance
enter = input("Do you dare to enter? (Y/N)\n")
if enter.lower() == "n":
  print("Yes. I knew you are not the chosen one. Go back home.")
else:
  import random
  print('''The old and dark castle sits in front of you, smelling like mold and dust and something... you can't quite name.
You pull the large door just enough for you to sneak into the darkness. The only companions you have are your sword and your    torch.''')
print(".")
print("...")
way = input('''Three dark paths open in front of you:
(1) - A small door to your right. Looks like it might lead to the cellar
(2) - A big corridor right in front of you. It looks huge and you can't quite tell how long it is.
(3) - An old door on your left.
Where do you go? 1, 2, or 3?''')

##### small door


if way == "1":
  print("""
        ______
     ,-' ;  ! `-.
    / :  !  :  . 
   |_ ;   __:  ;  |
   )| .  :)(.  !  |
   |"    (##)  _  |
   |  :  ;`'  (_) (
   |  :  :  .     |
   )_ !  ,  ;  ;  |
   || .  .  :  :  |
   |" .  |  :  .  |
   |mt-2_;----.___|
  """)
  print("The small door opens right into the Abyss.")
  abyss = random.randrange(20)
  print(abyss)
  if abyss < 12:
    print("Your step finds no floor and you march right into the Abyss. Such a short adventure for this unnamed hero.")
  else:
    print("With an impressive reaction, you manage to balance your weight just an instant before falling into the Abyss. You go back to the entrance and you wonder if it'd be better to go away, to check the corridor or to enter the other door.")
    run = input('''Do you:
    (1) - run away
    or
    (2) - go back at the entrance
    ?''')
    if run == "1":
      print("Yes... The wisest choice. Farewell adventurer.")
    else:
      way = input('''So, brave hero, which way? 
      (2) - corridor
      (3) - other door ''')
      
##### corridor

if way == "2":
  print("""
                                          ▒▒▓▓▓▓▒▒                                
                                        ▒▒▓▓▓▓▓▓▓▓░░                              
                                        ▓▓▓▓▓▓▒▒▒▒▓▓                              
                                      ░░▓▓▓▓▒▒░░░░▓▓                              
                                      ▓▓▓▓▓▓▓▓▒▒▒▒▓▓░░                  ▒▒▒▒░░    
                                      ██▓▓▓▓▒▒░░░░▓▓░░  ░░▓▓▓▓▓▓▒▒      ▓▓▓▓▓▓    
              ░░▒▒▒▒░░▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▓▓▒▒▓▓▓▓  
    ░░░░    ▓▓▓▓▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓██▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▒▒▓▓██▓▓▓▓████▒▒▓▓██▓▓▒▒░░    ██████▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒  ▒▒██▓▓██▓▓▓▓▓▓████▓▓▓▓
  ▓▓▓▓▓▓▓▓██▓▓██▓▓░░▒▒  ▒▒      ██▓▓▓▓██▓▓▓▓▓▓▓▓▓▓░░▒▒▓▓▓▓██  ▒▒▒▒██▓▓██▓▓▓▓▓▓▓▓██
  ▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▒▒          ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓    ░░▓▓  ▓▓▒▒  ▓▓░░
    ░░▒▒▒▒▒▒░░▓▓▓▓▓▓          ██▓▓▓▓▒▒▓▓▒▒▓▓▒▒▒▒▓▓▒▒▒▒░░░░░░▓▓▓▓    ▓▓  ▓▓░░  ▓▓▒▒
              ██▓▓▓▓        ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒░░░░░░▒▒▓▓        ▓▓    ░░▓▓
              ▓▓▓▓██          ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░░░▒▒▒▒▒▒░░░░▒▒▒▒        ▒▒    ░░▓▓
            ▒▒██▓▓▓▓▓▓  ░░░░▒▒▒▒▓▓▓▓▓▓▒▒▓▓▒▒░░░░▒▒░░▒▒▓▓░░░░▒▒                ░░  
              ██▓▓▓▓▓▓▓▓████▒▒▒▒▓▓▓▓██▒▒▓▓▒▒▒▒▒▒░░░░▓▓██▓▓▒▒▓▓                ▒▒  
              ██▓▓██▓▓▓▓██▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒▓▓                    
            ░░▓▓▓▓▓▓▓▓▒▒██▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░                  
              ▓▓██▓▓▒▒▒▒░░▓▓▓▓████▓▓██▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▒▒░░░░░░                  
              ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒████████▓▓▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒░░░░░░░░                
              ▒▒▓▓▓▓▒▒▒▒▓▓░░░░░░▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▒▒░░░░▒▒                
              ▒▒▓▓▒▒▒▒▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒▒░░░░▓▓                
              ▒▒▓▓░░▒▒░░░░░░░░▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓░░░░▓▓▒▒░░▒▒    ░░    ░░    
              ▓▓▒▒  ░░░░░░░░▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓████▒▒▓▓██░░░░  ▓▓▒▒▒▒                
              ▓▓▒▒  ░░░░░░░░▒▒▒▒██▓▓▒▒▓▓▒▒▒▒▓▓██▓▓▓▓▓▓░░░░░░▒▒░░░░░░              
              ▒▒    ░░░░░░▒▒░░▒▒▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒░░░░▓▓              
              ▒▒    ░░░░▒▒▒▒░░░░██▓▓▓▓▓▓▓▓██▓▓▒▒▒▒████▓▓░░▒▒▓▓▓▓▓▓▓▓              
                    ░░░░░░▒▒▒▒▓▓████████▓▓▓▓▓▓▒▒░░▓▓▒▒▓▓░░▒▒████▓▓▓▓░░            
                  ░░░░░░░░▒▒▒▒▓▓██▓▓██▓▓▓▓██▓▓▓▓░░▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓            
                  ░░░░░░░░▒▒▒▒▓▓▒▒▓▓▓▓██▓▓██▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓            
                ░░░░░░░░░░▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓████▓▓▒▒▒▒▓▓▓▓░░▒▒▓▓▓▓▓▓▓▓▓▓░░░░        
                ░░░░░░░░░░░░▒▒██▓▓▓▓▓▓██▓▓██████▒▒▓▓▓▓▓▓▒▒░░▓▓▓▓▒▒▒▒▓▓░░          
              ░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒▓▓▓▓████████▓▓▓▓▓▓▓▓▒▒░░░░▓▓▒▒▓▓░░▓▓          
              ░░░░░░░░░░▒▒░░▓▓██▒▒▓▓████▓▓██▓▓▓▓▓▓██▓▓▒▒▓▓▒▒░░▓▓▒▒▒▒▒▒            
            ░░░░░░▒▒░░▒▒░░▓▓▓▓██▒▒██▓▓██▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▒▒▓▓            
              ░░░░░░░░▒▒░░▓▓▓▓████▓▓██████████▓▓▓▓████▓▓██▒▒▒▒██▓▓▓▓▓▓░░          
              ░░░░▒▒▒▒▒▒░░▒▒▓▓▓▓██▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▒▒██▓▓▒▒▓▓            
              ░░░░▒▒░░░░▒▒▒▒▓▓████▓▓▓▓████████████▓▓██▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓            
          ░░░░░░░░▒▒░░▒▒░░▒▒▒▒██▓▓▓▓▓▓▓▓██████████████▓▓▒▒░░░░▓▓▓▓▓▓▓▓            
          ░░░░░░░░░░▒▒▒▒▒▒░░▒▒██▓▓██▒▒▒▒▓▓██▓▓██████▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░          
          ░░░░░░░░░░░░░░░░░░░░██▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░            
          ░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░  ░░              
            ░░░░  ░░░░░░░░░░░░░░▓▓▓▓░░▒▒▓▓▓▓▒▒░░░░▓▓▒▒░░▒▒▒▒░░                    
        ░░░░░░░░    ░░░░░░░░  ░░▒▒▓▓░░▒▒▒▒▒▒░░░░░░▓▓▒▒░░▒▒▒▒                      
            ░░░░░░░░  ░░      ░░░░▓▓▒▒▒▒▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒                      
              ░░░░░░            ░░░░▓▓▒▒▒▒▓▓░░░░░░░░▓▓▓▓▒▒▒▒                      
              ░░░░░░░░░░      ░░░░░░▓▓▓▓▓▓▓▓▒▒░░  ░░▓▓▒▒▒▒▒▒░░                    
              ░░░░░░            ░░░░▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▒▒░░▒▒▒▒                    
                ░░░░░░░░      ░░░░░░▓▓▓▓▓▓▒▒▓▓▒▒░░░░▓▓▒▒▒▒▒▒▓▓▒▒                  
                ░░░░        ░░    ░░████▓▓▓▓▓▓▓▓    ██▓▓▓▓▓▓▓▓▓▓                  
                ░░░░            ░░  ██▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓░░                
                ░░                ░░▓▓▓▓██▓▓▓▓░░      ▓▓▓▓▓▓▓▓▓▓▒▒                
                                    ██▓▓▓▓▓▓▓▓        ██▓▓▓▓▓▓▒▒▓▓                
                                    ██▓▓▓▓▓▓▓▓        ██▓▓▓▓▒▒▒▒▓▓▓▓              
                                    ██▓▓▓▓▓▓▓▓        ██▓▓▓▓▒▒▓▓▓▓▓▓              
                                    ██▓▓▓▓▓▓▓▓        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓              
                                  ▒▒██▓▓▓▓▓▓██        ▒▒██▓▓▓▓▓▓▓▓                
                                  ██▓▓▓▓▓▓████          ████▓▓████                
                                ▒▒██▓▓▓▓▓▓▓▓▓▓          ██▓▓▓▓▓▓▓▓                
                              ░░██████▓▓▓▓▓▓▓▓██        ▓▓▓▓▓▓▓▓▓▓▒▒              
                              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒        ████▓▓▓▓▓▓                
                          ▒▒▓▓▓▓▓▓▒▒▓▓▒▒▓▓  ░░          ██▓▓▓▓▓▓██░░              
                          ░░▓▓▓▓▒▒▒▒░░                  ██▓▓▓▓▓▓▓▓▒▒              
                              ░░                        ████▓▓▓▓▓▓▒▒              
                                                        ▓▓██▓▓▓▓▓▓▓▓              
                                                      ██▓▓▓▓▓▓▓▓████              
                                                        ▒▒▒▒▒▒██▓▓▒▒              
                                                      ▒▒▒▒▒▒▒▒▓▓░░                
                                                      ▒▒░░░░░░▓▓                  
                                                    ▓▓▒▒░░░░▒▒░░                  
                                                    ▓▓▒▒▒▒▓▓▒▒                    
  """)
  print(''' You hear something grunting in the dark. You keep walking. Slowly, Until the shy light of your torch brightens a humongous figure. A two headed giant, with a heavy club... still dripping blood. You draw your sword, ready to fight.''')
  fight = random.randrange(20)
  print(fight)
  if fight <= 1:
    print("The giant tries to hit you with his club. But he hits an old column instead. You hear a deep sound. The giant looks TERRIFIED. Right between the two (well, three?) of you, the Helldoor opens. There is no place to escape the ord of angry souls and demons that are now raising in front of you. Life itself is doomed.")
  elif fight < 10:
    print("You fought with honor. You'll be remembered")
  else:
    print("The fight is epic. Years of training and your shining will, make you defeat the horrendous creature. You search his corpse and you find a key. You put it into your pocket, you clean your sword and you start marching again through the empty corridor.")
    print("You search the entire castle to find out that the only living creature was that giant and the last door to check is the one at the entrance.")
    key = True
    way = "3"
    
###### left door

if way == "3" and key == True:
  print("""
        ______
     ,-' ;  ! `-.
    / :  !  :  . \
   |_ ;   __:  ;  |
   )| .  :)(.  !  |
   |"    (##)  _  |
   |  :  ;`'  (_) (
   |  :  :  .     |
   )_ !  ,  ;  ;  |
   || .  .  :  :  |
   |" .  |  :  .  |
   |mt-2_;----.___|
  """)
  door = input("""You look at the old door. It seems robust, but not stronger than you. The small key you have is way too small for this door. What do you do?
  (1) - You try to break it
  (2) - You've had to deal with enough doors for today. You leave it alone and go home.
  """)
  ####### SMASH
  if door == "1":
    open = random.randrange(20) + 5
    print(open)
    if open < 10:
      print("You smash the door, but loose balance and can't avoid the trap hole right behind it. This is the end of your adventure")
    else:
      print("You smash the door easily. Behind it you find an old chest in which your key fits well. The treasure you were looking for is now in your hands and your name will be legend.")
  if door == "2" and key == True:
      print("The moment you look away from the door, you realize that the entrance of the castle is not there anymore. You see your body growing more and more. When you turn your head on your shoulder you see another you... well... only another head. You try to speak, but the only thing that comes out of your mouth is a primitive growl. Welcome home.")
  elif door == "2":
    print("Another one who was not ready to be THE hero. Might you be forgotten.")
elif way == "3":
  print("""
        ______
     ,-' ;  ! `-.
    / :  !  :  . 
   |_ ;   __:  ;  |
   )| .  :)(.  !  |
   |"    (##)  _  |
   |  :  ;`'  (_) (
   |  :  :  .     |
   )_ !  ,  ;  ;  |
   || .  .  :  :  |
   |" .  |  :  .  |
   |mt-2_;----.___|
  """)
  door = input("""You look at the old door. It seems robust, but not stronger than you. What do you do?
  (1) - You try to break it
  (2) - You've had to deal with enough doors for today. You leave it alone and go home.
  """)
  ####### SMASH
  if door == "1":
    open = random.randrange(20)
    print(open)
    if open < 10:
      print("You smash the door, but loose balance and can't avoid the trap hole right behind it. This is the end of your adventure")
    else:
      print("You smash the door easily. Behind it you find an old chest. The treasure you were looking for is now in your hands and your name will be legend.")