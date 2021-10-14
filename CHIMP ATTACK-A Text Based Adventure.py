import time


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


log = 0
flare = 0

required = ("\nUse only A, B, or C\n")



def intro():
    print("After a drunken night out with friends, you awaken the "
          "next morning in a thick, dank forest. Head spinning and "
          "fighting the urge to vomit, you stand and observe your new, "
          "unfamiliar setting. The peace quickly fades when you hear a "
          "rough grunt.As you turn around you see a wild big chimpanzee running towards your direction"
          " You will:")
    time.sleep(1)
    print("""  A. Grab a nearby rock and throw it at the chimp
  B. Lie down and play dead
  C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        print("\nHe knows you are not dead yet as you started screaming when he  gouged your eyes out. "
              "\n\nYou died in agony!")
    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()


def option_rock():
    print("\nThe chimp is wobbled but recovers very quickly. He starts to "
          "run at you again. Will you:")
    time.sleep(1)
    print("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print("\nYou decided to throw another rock, as if you could "
              "knock him out.You put all your power into it.The rock flew well over the "
              "chimps head. You missed. \n\nYou died in agony!")
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_rock()


def option_cave():
    print("\nYou were hesitant, since the cave was dark and "
          "ominous. Before you fully enter, you notice a Log that kind of resembles "
          "a bat.You cant quite tell how heavy it is.Do you try to pick it up? Y/N?")
    choice = input(">>> ")
    if choice in yes:
        log = 1
    else:
        log = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("""  A. Hide in silence
  B. Fight
  C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nReally? You're going to hide in the dark?He really cant see you"
              "but he can smell you DUMBASS"
              "You got nowhere to escape,...\n\nYou died in agony!")
    elif choice in answer_B:
        if log > 0:
            print("\nYou laid in wait. The Log was not that heavy and you could swing it at "
                  "the chimp, which was not amused by your toy at all. As the chimp stormed in "
                  "closer and closer to you, your heart starts to beat rapidly.Adrenaline settles in as the chimp "
                  "trys to jump on your face, you swung that shit and connect right on the chin"
                  "LUCKILY HES OUT COLD YOU KNOCKED HIM OUT. \n\nYou survived!")
        else:
            print("\nYou should have picked up that log. You're defenseless "
                  "as the chimp pulls out your testicles and toungue leaving you to bleed out \n\nYou died in agony!")
    elif choice in answer_C:
        print("As the chimp enters the dark cave, you sliently "
              "sneak out. You're several feet away, but the chimp turns "
              "around and sees you running.")
        option_run()
    else:
        print(required)
        option_cave()


def option_run():
    print("\nYou run as quickly as possible, but the chimp's "
          "speed is too great. You will:")
    time.sleep(1)
    print("""  A. Hide behind a boulder
  B. You choose to fight him instead
  C. Run towards an abandoned town""")
    choice = input(">>> ")
    if choice in answer_A:
        print("You're easily spotted.The animal shows no mercy "
              "\n\nYou died in agony!")
    elif choice in answer_B:
        print("\nYou're no match for the nasty chimp as the chimp mutilates your face and tears of your limbs and testes "
              "\n\nYou died in agony!")
    elif choice in answer_C:
        option_town()
    else:
        print(required)
        option_run()


def option_town():
    print("\nWhile frantically running, you notice a big "
          "log in the mud. You quickly reach down to pick it up, "
          "but realize its too heavy and wont be of much use.Your breahting heavy,as the chimp aproaches,"
          "you panic and hide inside an abondened house,you hear him following.You glance at a flare in a"
          "room that you can be trapped in.You remember you had a lighter in your pocket"
          "How lucky?Exactly how afraid of fire are chimps thought?Well you are you going for the flare? Y/N")
    choice = input(">>> ")
    if choice in yes:
        flare = 1
    else:
        flare = 0
    print("You hear its heavy footsteps and ready yourself for "
          "the nasty chimp.")
    time.sleep(1)
    if flare > 0:
        print("\nYou quickly light the flare out and point it at him but the chimp does not look worried "
              ".It keeps moving forward as you start to run around the room and scream as loud as you can"
              "As the chimp gets closer, you loose balance,hiting an old shelf which falls off making a crashing sound"
              "\n\nThe chimps had enough he got scared of the noise and ran away.You got lucky and you survived!")
    else:
        print("\nMaybe you should have went for the flare.You are neither stronger nor faster than a damn chimp "
              "\n\nYou died in agony!")


intro()
