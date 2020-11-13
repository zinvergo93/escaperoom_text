
run_game = False


def new_game():
    startgame = input(
        "Hello? Can you hear me? It's time to wake up (Yes/No)\n\t")

    run_game = True
    if startgame.lower() == "yes":
        while run_game == True:

            print("You wake up in a haze. Looking around you, you see a small, lit gas lamp on the desk across the room, but everything else is hard to make out in the dark room.\n")
            print("You stand up and stumble towards the desk. On it you see 6 worn photos. One of them is hard to make out, as it has a burn mark going through much of it, but you can see there's something written on the back that appeared to be a '6'.\n")
            flip_photo = input("Flip all photos? (Y/N)\n\t")

            if flip_photo.lower() == "y":
                photo_reveal = True
                while photo_reveal == True:
                    print("You flip each photo from left to right. Crudely painted in blood, each photo has a number. '3', '7', '0', '6', '1', '4'\n\n What could these numbers mean?")
                    print("You pick one up to scan it, try to correlate between photo and number, but suddenly one-by-one, each photo burst into flames. The one in your hand floats to the floor then vanishes into a thin dust of ash.\n")
                    print("3, 7, 0, 6, 1, 4...I can remember that. You look up and realized that through the combustion, the intensity of the flame in the lamp increased and illuminated the room")
                    print(
                        "To your left, you see a bed, to your right you see a wardrobe and a closet, and behind you there is a window.")

                    environment_choice_loop = True
                    while environment_choice_loop == True:
                        environment_choice = input(
                            "What would you like to inspect? (Bed, Wardrobe, Window)\n\t")

                        if environment_choice.lower() == "bed":
                            bed_choice_loop = True
                            while bed_choice_loop == True:
                                bed_choice = input(
                                    "Where do you want to look? (On top/underneath) 'Go Back' to go back'\n\t")
                                if bed_choice.lower() == "on top":
                                    print(
                                        "You inspect the bed and see some dusted, but neat, sheets. The last person in this room certainly tidied up before leaving...if they did.")

                                elif bed_choice.lower() == "underneath":
                                    print("You lower to one knee, lift the bedskirt and peak your head down to check underneath the bed. It's mostly vacant, however you notice a small metal box towards the foot of the bed. You grab it to inspect it. Whilst grabbing it you feel a chill flow through your fingers, then your forearm. Once it's revealed, you see a dial with room for 6 digits")
                                    print(
                                        "Written on top of the box is a warning: 'I had one chance...and I lost it'.")
                                    enter_password = input(
                                        "Would you like to try the passcode? (Y/N)\n\t")

                                    if enter_password.lower() == "y":
                                        passcode = input("Enter the code:\n\t")
                                        if passcode == '170634':
                                            print("The lock clicks open successfully and the lid loosens. Upon opening it you see writing on the inner lid reading 'Simply breathtaking'. Inside the box is a dried rose. Around its stem is a pair of wedding rings, and a clear photo of a beautiful woman with light-colored hair and bright eyes.")
                                            print("A click comes from behind you, inside of the closet. The door swings open, and reveals a greyed man in a black tuxedo, hanging from the rafter above with a belt around his neck. His body twists towards you, as his face brightens and his eyes become alive and look directly into yours. The belt loosens itself and he lands to the floor on his feet. He straightens himself and turns to reveal a door within the closet.")
                                            print("As it opens, a bright sunlight and smell of fresh air seep through the widening gap. The man looks at you, smiles and says 'We're free...', then steps into the sunlight. Following him you feel a comfort take over. You are indeed free, but what lies ahead?\n\n")

                                            finished_game = input(
                                                "Congratulations! You made it through the game. Would you like to play again? (Y/N)\n\t")

                                            if finished_game.lower() == 'y':
                                                run_game = False
                                                return new_game()
                                            elif finished_game.lower() == 'n':
                                                print('Thanks for playing!')
                                                run_game = False
                                        else:
                                            print("A meaty hand yanks you around and another grabs you by the neck. A large man with an grim, grey appearance stares at you with dark, lifeless eyes as he dangles your body far above the floor. He snarls and inhales sharply through his teeth, and jolts his frame to bring all strength to his hands. Slowly the room darkens, and your pulse slows to nothing. You died.")
                                            continue_game = input(
                                                "Continue? (Y/N)\n\t")
                                            if continue_game.lower() == "y":
                                                bed_choice_loop = True
                                            elif continue_game.lower() == "n":
                                                print("Better luck next time!")
                                                bed_choice_loop = False
                                                environment_choice_loop = False
                                                photo_reveal = False
                                                run_game = False
                                    elif enter_password.lower() == "n":
                                        bed_choice_loop = True

                                elif bed_choice.lower() == "go back":
                                    bed_choice_loop = False
                                    environment_choice_loop = True
                                else:
                                    print("That is not an available option")
                                    break

                        elif environment_choice.lower() == "wardrobe":
                            wardrobe_closet = input(
                                "Would you like to look in the wardrobe or check the closet? (Wardrobe/Closet) 'Go Back' to go back.\n\t")
                            if wardrobe_closet.lower() == "wardrobe":
                                print(
                                    "You open the cabinet doors and see four compartments and one drawer behind it.\n")
                                wardrobe_inspect_loop = True
                                while wardrobe_inspect_loop == True:
                                    wardrobe_inspect = input(
                                        "What would you like to look at? (Drawer/Compartments) 'Go Back' to go back.\n\t")
                                    if wardrobe_inspect.lower() == "drawer":
                                        print(
                                            "Inside the drawer, there was one shirt. A white button-up, with a note protruding from underneath.\n")
                                        read_note = input(
                                            "Read the note? (Y/N)\n\t")
                                        if read_note.lower() == 'y':
                                            print(
                                                "You pull up the note to see a passage scribbled in a faded ink. It reads:")
                                            print("London. The year of our Lord 1935, on a particularly warm day of the 20th of June. It's been exactly one year since I lost the love of my life, and three more days since I married her. I can no longer bare the pain without you.")
                                            print(
                                                "The note continued on the back:")
                                            print(
                                                "If you found this, I am gone. Please do not enter the closet. I have one more chance to find her, or else I will live the same day forever.\n\n")

                                        elif read_note.lower() == 'n':
                                            wardrobe_inspect_loop = True

                                        else:
                                            print(
                                                "That is not an available option")
                                    elif wardrobe_inspect.lower() == "compartments":
                                        print("Inside 3 of the compartments were stacks of folded clothing. The air smelled stale from the cloth having sat for so long in the wooden cabinet. In the upper-right cubby, you see an old pocket watch, a letter opener, a rolled up tie, and there appeared to be a wedding photo. Much like the others it was worn, and had also had a burn mark on it. You pull it out to inspect it and see on the back 'The only one for me'. You set it down.\n")
                                    elif wardrobe_inspect.lower() == "go back":
                                        wardrobe_inspect_loop = False
                                        environment_choice_loop = True
                                    else:
                                        print("That is not an available option")

                            elif wardrobe_closet.lower() == "closet":
                                print("You slowly approach the closet and reach for the doorknob. Upon touching it, the metal crumbles and falls to the floor. Immediately afterward, the closet door slams open where a tall, ghastly man stares at you, lowering his arm to rest. Before you have a moment to react, he bolts towards you at paranormal speed. A rush of cold and a cloud of matter envelops you, as your sight fades into nothing. You died.")
                                continue_game = input("Continue? (Y/N)\n\t")
                                if continue_game.lower() == "y":
                                    bed_choice_loop = True
                                elif continue_game.lower() == "n":
                                    print("Better luck next time!")
                                    bed_choice_loop = False
                                    environment_choice_loop = False
                                    photo_reveal = False
                                    run_game = False
                            else:
                                print("That is not an available option.")

                        elif environment_choice.lower() == "window":
                            print("The window is stuck shut, but out in the darkness you can faintly see a dirt road and the beginning of dense forestry. You look back at the lamp and back outside...'If I get out of here...you're coming with me.\n")
                            environment_choice_loop = True
                        else:
                            print("That is not an available option")
                            break

            elif flip_photo.lower() == "n":
                print("Suddenly a loud creak comes from behind you. A tall man with an ashened complexion towers over you. The stink of formaldehyde fills the room, and the temperature plummets to freezing. Slowly everything fades to black as the man's body expands and encapsuates yours. You died, please try again.")
                continue_game = input("Continue? (Y/N)\n\t")
                if continue_game.lower() == "y":
                    run_game = True
                elif continue_game.lower() == "n":
                    print("Better luck next time!")
                    run_game = False
    elif startgame.lower() == "no":
        print("Perhaps next time...")
        run_game = False

    else:
        print("I'll try again later...")
        run_game = False


new_game()
