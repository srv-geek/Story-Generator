import random  # random module is imported as to select the items randomly from the argument/passed list in choice method.

while True:  # this loop runs for the choices taken as input from the user for different options for story generation.
    print('Enter numeric choice (e.g. 1,2,3....):')
    print("1. Plot story\n2. Imagination\n3. Pokemon Battle story\n4.EXIT")
    choice = input()  # The choice entered by user is stored in choice variable

    # This block will print a plot story with the three input characters the name of the protagonist, his female friend and a male friend.
    if (
            choice == '1'):  # This checks whether the input choice is 2 (to print the random plot story as per the defined choices). the input is read as string 2, not converted into numeric, as only just to make an intended choice is the current objective.
        he = input("Enter the male character: ")
        she = input("Female friend name (eg veronica): ")
        his_father = input("Male friend name (eg John, wilson max): ")

        # Following section declares some lists/sequences of words. One word from every sequence will be chosen randomly during story generation process.
        word1 = ['Once', 'A year ago', 'Last month']
        word2 = ['older', 'young', 'in his school', 'in his college', 'teenager']
        word3 = ['florida', 'north carolina', 'hawaii', 'alberta', 'bighorn river', 'outer banks']
        word4 = ['in a fishing boat', 'in a fishing yatch']
        word5 = ['dolphin', 'alaskan salmon', 'cod', 'herring', 'mahi mmahi', 'perch', 'sardines']
        word6 = ['beautiful cars', 'four vehilars']
        word7 = ['jaguar', 'marcedes benz', 'porsche', 'maserati gran', 'nissan gt', 'lamborghini', 'buggati']

        # This section defines the assignment of random words, chosen from the above defined lists (using choice method from random random module imported), into variables
        w1 = random.choice(word1)
        w2 = random.choice(word2)
        w3 = random.choice(word3)
        w4 = random.choice(word4)
        w5 = random.choice(word5)
        w6 = random.choice(word6)
        w7 = random.choice(word7)

        # This section defines the template that is used to print the plot story .
        sentence = [
            'word1', 'when', 'he', 'was', 'word2', ',', 'he', 'and', 'she', 'had gone to', 'word3', ',',
            'They went out', 'word4', 'to the glittering waters of the great Gulf Stream.',
            'she', 'threw a half-smoked cigarette into the water as she reeled in a brightly',
            'colored fish that would fade to gray' 'in moments.',

            'It was a', 'word5', ',he said.',

            'she', 'said,',
            'I have never fished in my life.',
            'I would never fish', 'as they call them', 'word5', 'but they’re not the mammals.',
            'They are pretty,', 'and though', 'People, they put them in sandwiches,', 'Use them in sandwiches.',

            'I can’t remember', 'word3', 'very well,', 'he admitted.',

            '"Good", she said', 'It was a foolish thing to do,', 'going off to', 'word3', '—', 'word3',
            'of all places.',

            'she', 'word6',
            'Before she met', 'his_father', '(which was when he appeared as well',
            'he thought, but before he was visible)',
            'she had one from the sixties that she cherished—a', 'word7', '. She still had the manual for it.',
            'A large book with a hard black cover.',
            'Everything about the car was described and illustrated in',
            'great detail. he particularly liked the wiring diagrams. but there was no picture of the actual car.'
        ]

        # Following conditions are set in such a way that whenever a particular word occurs in the defined template, it is replaced by the defined random words and inputs of user.
        for item in sentence:
            if item == 'he':
                sentence[sentence.index(item)] = he
            elif item == 'she':
                sentence[sentence.index(item)] = she
            elif item == 'his_father':
                sentence[sentence.index(item)] = his_father
            elif item == 'word1':
                sentence[sentence.index(item)] = w1
            elif item == 'word2':
                sentence[sentence.index(item)] = w2
            elif item == 'word3':
                sentence[sentence.index(item)] = w3
            elif item == 'word4':
                sentence[sentence.index(item)] = w4
            elif item == 'word5':
                sentence[sentence.index(item)] = w5
            elif item == 'word6':
                sentence[sentence.index(item)] = w6
            elif item == 'word7':
                sentence[sentence.index(item)] = w7

            else:
                continue

        # This section prints the story as per the defined template.
        story = " ".join(item for item in sentence)
        print(story)

    #
    elif (
            choice == '2'):  # This checks whether the input choice is 1 (to print the random Imagination type story as per the defined choices).
        # Three inputs are taken from the user: the name of the enemy that is the self's enemy in the story, the name of self's father, and the adjective for the enemy showing his behaviour at particular moment
        enemy = input("Enter the name of the enemy.(e.g.chihuahua, border collie, wolf):")
        father = input("Enter the  name of the father (e.g. John, Mr.Pickles,Hairyface,Willy Wonka,Steve,Bob):")
        enemyadj = input("Enter the adjective for enemy (e.g. grimy, muddy, awful, grotesque, hideous,adorable, cute):")

        # Following section declares some lists/sequences of words. One word from every sequence will be chosen randomly during story generation process.
        intro1 = "I was sitting on the edge of the rocky cliff beside my favourite tree."
        intro2 = "Alone in the searing desert, I was wondering why I was leaning against a cactus."
        intro3 = "Staring out my apartment window, I saw my reflection staring back at me."
        char1 = "As I looked out into the distance, I thought about my past and all of the drama in it."
        char2 = "I wondered if this was my destiny- trying to find happiness."
        char3 = "I pulled out the photo of my long lost mother and where on earth she could be."
        prob1 = "Suddenly I was covered from head to toe with darkness. I couldn't breathe or see. Everything went black..."
        prob2 = "All of a sudden a psychopathic " + enemy + " grinned at me,showing all his razor sharp teeth. Suddenly it started to claw at my face. From the loss of blood, I collapsed onto the tough ground..."
        prob3 = "I suddenly felt a sharp needle sink into my flesh. It was a tranquilizer. But before I knew it I started feeling really drowsy. Everything went black..."
        sol1 = "I forced my drowsy eyes open my eyes to see a bright light."
        sol2 = "I forced my drowsy eyes open to find myself on the back of a massive dragon and a man in front of me."
        sol3 = "I forced my drowsy eyes open to the sounds of a " + enemyadj + " " + enemy + " licking my face."
        end1 = "A man came to my side with a knife. It was my father!" + father + "!" "'Go to sleep young one...'"
        end2 = "It was difficult to keep my eyes open as I stuggled to breathe. "
        end3 = "Out of nowhere, a duck wearing a deerstalker looked me in the eye and pointed a gun at me. 'Quack.' And that was the last thing I heard..."

        # This step defines the templates' sequences for the story that has been chosen for the stories that are randomly printed during each run.
        intros = [intro1, intro2, intro3]
        characters = [char1, char2, char3]
        problems = [prob1, prob2, prob3]
        solutions = [sol1, sol2, sol3]
        endings = [end1, end2, end3]

        # This section prints the story based on the random choices selected from the sequence of templates defined in above section.
        print(random.choice(intros)),
        print(random.choice(characters)),
        print(random.choice(problems)),
        print(random.choice(solutions)),
        print(random.choice(endings))


    elif (choice == '3'):  # This checks whether the input choice is 3 (to print the Pokemon battle random stories as per the defined choices).
        # This type of story takes 5 inputs from the user:
        # The type of the pokemon, the name of the pokemon, the enemy of the pokemon, the adjective for the pokemon showing the bahavior, and the scene for the pokemon battle. also some suggestions are given to the user to enter.
        pokemon = input(
            "Enter the type of Pokemon (e.g. Wailord, Wobbufet,Solosis, Eevee, Aegislash, Leafeon, Beldum, Arceus):")
        name = input(
            "Enter the name of Pokemon (e.g. MegaBoy, LemurMan, Chris, Airman, Ash Ketchum, Wally, Bob, Bianca, Tieno):")
        enemy = input(
            "Enter the enemy of Pokemon (e.g. N, Maxie, Archie, Lysandre, Xerosic, AZ, Jessie,James, Giovanni, Silver, Shelly, Tabhitha):")
        sceneryadj = input(
            "Enter the adjective about the battle scene (e.g. rumbling, shaking, secret, extremely squeaky, surprising, scary, thorny):")
        adjpkmn = input(
            "Enter the type of Pokemon (e.g. terrifying, thrashing, undefeatable, timid, award winning, shiny, dangerous, glamourous):")

        # in this step two mood choices are randomly selected to generate the new story every time.
        mood = random.choice(["serious", "playful"])
        if mood == "serious":
            adj = ["ferocious", "serious", "untrustworthy"]
        elif mood == "playful":
            adj = ["lively", "cheerful", "spirited"]

        # Following section declares some lists/sequences of words. One word from every sequence will be chosen randomly during story generation process.
        intro1 = "I, " + name + ", was standing in front of the mysterious trainer..."
        intro2 = "I, " + name + ", walked through the " + sceneryadj + " place leading to the pokemon stadium."
        intro3 = "My opponent was standing opposite me."
        char1 = "I threw my " + adjpkmn + " " + pokemon + " at the trainer, " + enemy + ", and attacked."
        char2 = "I summoned my " + adjpkmn + " " + pokemon + " to attack the trainer, " + enemy + "."
        char3 = "I Threw my pokeball and out came my " + adjpkmn + " " + pokemon + ", than it suddenly attacked the trainer, " + enemy + "."
        prob1 = "The " + random.choice(adj) + " opponent used the most effective move in the book!!!"
        prob2 = "But the " + random.choice(adj) + " opponent was a dash more energetic and slashed at my Pokemon."
        prob3 = "The " + random.choice(adj) + " opponent used the strongest dragon type move 'Draco Meteor'!"
        sol1 = "However, my Pokemon had a special ability, it made me immune to all of the opponents attacks."
        sol2 = "My Pokemon was quite fragile, luckily it was holding an oran berry so it healed itself and than i shouted a command."
        sol3 = "Luckily, the opponent had terrible accuracy and missed me."
        end1 = "I couldn't believe my eyes!!! The opponents Pokemon returned to its pokeball, weary and tired. It fainted."
        end2 = "The oppenent was on it's last breath and finally it fainted."
        end3 = "I could not believe my eyes, I had just defeated a terribly strong Pokemon!"

        # This step defines the templates' sequences for the story that has been chosen for the stories that are randomly printed during each run.
        intros = [intro1, intro2, intro3]
        characters = [char1, char2, char3]
        problems = [prob1, prob2, prob3]
        solutions = [sol1, sol2, sol3]
        ends = [end1, end2, end3]

        # This section prints the story based on the random choices selected from the sequence of templates defined in above section.
        print(random.choice(intros) + random.choice(characters) + random.choice(problems) + random.choice(solutions) + random.choice(ends))
        

        # this section print the end part when you have done .
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Thank you for reading our random generated Pokemon battle story.")

    # this section gives the choice when you want to exit from the generator.
    elif (choice == '4'):
        print("you are exited!")
        break
    else:#if user enter anything diffrent from choice, he\she will got a text to enter a valid choice.
        print("Please enter a valid choice!")
