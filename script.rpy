
#############--GAME BEGINS HERE--##############

label start:
    scene black
    "Choose your colour"
    menu:
        "Blue": #Choose a blue character
            show blue at center
            $ crimson = False
        "Red": #Choose a red character
            show red at center
            $ crimson = True
    "So this will be your character."
    "What is your character's name?"
    hide blue
    hide red
    python:
        name = renpy.input("Input name.")
        if not name:#Default name if no input
            name = "Impo5t0r"
    "So your character's name is [name]? How interesting."
    "Alright let's start!"
    jump scene0

label scene0:
    scene bg space #starwars style intro
    with dissolve
    play sound 'audio/Imperial March.mp3'
    "The Earth is dying. You, [name], are part of the special team sent to set up outposts and colonise Pax as the last hope of humanity. As your crew ventures into the new world of space exploration, disaster strikes…"
    jump emergenscene
#emergenscene transition scene
label emergenscene:
    scene emergency
    with vpunch
    play sound 'audio/alarm_emergencymeeting.wav'
    "Hold on, what's this?"
    jump scene1
#scene1 dialogue w crewmates
label scene1:

    scene bg admin #include name of meeting rm bg
    if crimson:
        #If red was chosen
        show crewmate_1 at left
        with easeinleft
        Crewmate1  "Crewmate 4 was just found dead at electrical."
        show crewmate_2flip at center
        with easeinright
        Crewmate2 "What!?"
        show crewmate_3flip at right
        with easeinright
        Crewmate3 "How!?"
        Crewmate1 "I have no idea, I was just fixing some wires when I noticed their bodies there. I don’t think it was an accident, there were visibly man-made wounds."

        hide crewmate_1
        show crewmate_1flip at center
        with easeinleft
        show red at leftleft
        with easeinleft

        me "How could something like this happen?"
        Crewmate2 "We’ve got to find out who did this!"
        Crewmate3 "But we still have tasks to complete."
        me "Alright, then we have no choice but to stay alert while doing our tasks. Report any clues you find, or any suspicious activity immediately. Watch your backs everyone!"
        hide crewmate_1flip
        hide crewmate_2flip
        hide crewmate_3flip
        hide red

    else:
        #If blue was chosen
        show crewmate_1 at left
        with easeinleft
        Crewmate1  "Crewmate 4 was just found dead at electrical."
        show crewmate_2flip at center
        with easeinright
        Crewmate2 "What!?"
        show crewmate_3flip at right
        with easeinright
        Crewmate3 "How!?"
        Crewmate1 "I have no idea, I was just fixing some wires when I noticed their bodies there. I don’t think it was an accident, there were visibly man-made wounds."

        hide crewmate_1
        show crewmate_1flip at center
        with easeinleft
        show blue at leftleft
        with easeinleft

        me "How could something like this happen?"
        Crewmate2 "We’ve got to find out who did this!"
        Crewmate3 "But we still have tasks to complete."
        me "Alright, then we have no choice but to stay alert while doing our tasks. Report any clues you find, or any suspicious activity immediately. Watch your backs everyone!"
        hide crewmate_1flip
        hide crewmate_2flip
        hide crewmate_3flip
        hide blue

    menu: #choice of where to go, electrical or admin
        "Go to Electrical":
            jump scene2
        "Go to Admin":
            jump scene3
#scene2 electrical
label scene2:
    scene electrical
    with dissolve
    "You enter the cold and messy confines of the electrical room. Chills run down your spine, and your intuition tells you to get out of here as soon as possible. The feng shui here is terrible."
    menu: #choice of investigation or tasks
        "Investigate crime scene":
            jump scene2a
        "Do tasks":
            jump scene2b

label scene2a:
    scene electrical #chose investigate, automatically follow up with tasks
    with fade
    "You notice that there are blood stains on the floor next to the vent. Upon closer inspection, you find a white glove lodged deep in the grilles of the vent."
    scene electrical
    "Doing tasks next..."
    jump scene2bno

label scene2bno:
    scene taskundone #complete tasks, move to next scene (2d)
    "Task in progress"
    scene taskdone
    with fade
    "You have completed your task successfully. The current task progress is at 75 percent."
    jump scene2d

label scene2b:
    scene taskundone #chose tasks, automatically follow up with investigation
    "Task in progress"
    scene taskdone
    with fade
    "You have completed your task successfully. The current task progress is at 75 percent."
    "Investigating next..."
    jump scene2ano

label scene2ano:
    scene electrical #complete investigation, move to next scene (2d)
    with fade
    "You notice that there are blood stains on the floor next to the vent. Upon closer inspection, you find a white glove lodged deep in the grilles of the vent..."
    jump scene2d

#not the most elegant solution...try if/else next time

label scene2d:
    scene electrical
    with dissolve
    if crimson: #character displayed here
        show red at leftleft
        with easeinleft
    else:
        show blue at leftleft
        with easeinleft
    play sound 'audio/Walking-Down-Metal-Stairs.mp3'
    me "Who's there"
    show crewmate_1 at center
    with easeinright
    show crewmate_3 at rightright
    with easeinright
    hide crewmate_1
    show crewmate_1flip at center
    Crewmate1  "Calm down, it's just us."
    me "I don’t know if I can trust anyone after crewmate 4 was murdered just like that"
    hide crewmate_3
    show crewmate_3flip at rightright
    Crewmate2 "Well, it’s unfortunate but we need to move on. We need to stay on track and focus on our mission."
    hide crewmate_1flip
    hide crewmate_3flip
    me "Crewmate 3 sure is taking long to upload his data… Never mind, I’m overthinking things. I need to finish my tasks in admin."
    jump emergenscene2
#emergenscene transition scene
label emergenscene2:
    scene emergency
    with vpunch
    play sound 'audio/alarm_emergencymeeting.wav'
    jump scene4
#scene3 electrical
label scene3:
    scene bg admin
    "You enter the dark admin room. Inside you see Crewmate 3 doing his task. There is also a log to check who is in the vicinity of the murder scene."
    menu: #choice of investigation or tasks again
        "Check Logs":
            jump scene3a
        "Do Task":
            jump scene3b

label scene3a:
    scene bg logs
    "The log shows that you, Crewmate 1, and Crewmate 3 was near the murder scene when the body was discovered. You also notice that there is a significant gap in time between Crewmate 1 entering electrical, and the calling of the emergency meeting."
    "Doing Tasks Next"
    jump scene3bno

label scene3bno:
    scene bg oxygen
    "You have completed your task successfully. The current task progress is at 75 percent."
    jump scene3d

label scene3b:
    scene bg oxygen
    "You have completed your task successfully. The current task progress is at 75 percent."
    "Checking Logs Next"
    jump scene3ano

label scene3ano:
    scene bg logs
    "The log shows that you, Crewmate 1, and Crewmate 3 was near the murder scene when the body was discovered. You also notice that there is a significant gap in time between Crewmate 1 entering electrical, and the calling of the emergency meeting."
    jump scene3d

label scene3d:
    scene bg oxygen
    if crimson: #character displayed here
        show red at center
        with easeinright
        play sound 'audio/Walking-Down-Metal-Stairs.mp3'
        "You suddenly feel an icy cold hand touching your shoulder. Alarmed, you immediately shove the person away."
        show crewmate_3flip at right
        with easeinright
        Crewmate3 "Woah, don't be so tense. It's just me."
        me "There is clearly a killer among us! You should really stop sneaking around and surprising people."
        show crewmate_1 at left
        with easeinleft
        hide red
        show red_flip at center
        Crewmate1 "Hey guys, have you all finished your tasks? I'm done with mine."
        Crewmate3 "I just need to do the upload and I should be done!"
        me "I almost finished mine as well. Just need to connect some wires in electrical."
        Crewmate3 "Huh, that's odd. We should be finishing up our tasks and yet the progress is still around 75 percent. We should check on crewmate 2."
        me "I’ll head to electrical first and meet you guys later."
        hide red_flip
        hide crewmate_1
        hide crewmate_3flip
    else:
        show blue at center
        with easeinright
        play sound 'audio/Walking-Down-Metal-Stairs.mp3'
        "You suddenly feel an icy cold hand touching your shoulder. Alarmed, you immediately shove the person away."
        show crewmate_3flip at right
        with easeinright
        Crewmate3 "Woah, don't be so tense. It's just me."
        me "There is clearly a killer among us! You should really stop sneaking around and surprising people."
        show crewmate_1 at left
        with easeinleft
        hide blue
        show blue_flip at center
        Crewmate1 "Hey guys, have you all finished your tasks? I'm done with mine."
        Crewmate3 "I just need to do the upload and I should be done!"
        me "I almost finished mine as well. Just need to connect some wires in electrical."
        Crewmate3 "Huh, that's odd. We should be finishing up our tasks and yet the progress is still around 75 percent. We should check on crewmate 2."
        me "I’ll head to electrical first and meet you guys later."
        hide blue_flip
        hide crewmate_1
        hide crewmate_3flip
    jump emergenscene2

default cmone = False

label scene4:
    scene bg admin
    if crimson:
        show red at leftleft
    else:
        show blue at leftleft
    show crewmate_1flip at center
    show crewmate_3flip at right
    me "What?!"
    Crewmate1 "I’m telling you, I found Crewmate 2 lying in storage, right between electrical and admin. It must have been you, Crewmate 3! I saw you faking your upload task. How could you do this?"
    Crewmate3 "What?! It's not me! Are you trying to push the blame on me?! You were the last person who saw crewmate 2 AND the one who reported the first body!"

    "They start accusing each other. Your vote can seal the fate of one of them."

    menu: #choose who to die
        "Crewmate 1":
            $ cmone = True
            jump scene4a
        "Crewmate 3":
            $ cmone = False
            jump scene4a


label scene4a:
    scene bg admin
    if crimson:
        show red at leftleft
    else:
        show blue at leftleft
    show crewmate_1flip at center
    show crewmate_3flip at right
    if cmone:
        Crewmate1 "You’re making a huge mistake! Don’t do this!"
        hide blue
        hide red
        hide crewmate_1flip
        hide crewmate_3flip
        jump scene4b
    else:
        Crewmate3 "You’re making a huge mistake! Don’t do this!"
        hide blue
        hide red
        hide crewmate_1flip
        hide crewmate_3flip
        jump scene4b


label scene4b:
    show bg space
    play sound 'audio/door_open.wav'
    play sound 'audio/door_close.wav'
    if cmone:
        "Crewmate 1 is thrown out of the spaceship and order is restored once more… Or has it? As you near Pax , you contemplate what had happened"
        jump scene4c
    else:
        "Crewmate 3 is thrown out of the spaceship and order is restored once more… Or has it? As you near Pax , you contemplate what had happened"
        jump scene4c

label scene4c:
    show bg planet

    if crimson:
        show red at leftleft
    else:
        show blue at leftleft

    me "Did we make the right decision? … I’m getting a terrible headache, I’m going to… pass… out..."
    jump scene4d

label scene4d: #sike
    show bg admin
    if cmone:
        show crewmate_3_dead at center
        play music 'audio/alarm_emergencymeeting.wav' fadeout 1.0
        "You open your eyes and see blood in your hands. Your hands tremble, and as you look up, you see the corpse of the last crewmate in front of you."
        play music 'audio/Imperial March.mp3' fadein 1.0
        hide crewmate_3_dead
        me "... I knew… I knew it all along… "
        hide red
        hide blue

    else:
        show crewmate_1_dead at center
        play music 'audio/alarm_emergencymeeting.wav' fadeout 1.0
        "You open your eyes and see blood in your hands. Your hands tremble, and as you look up, you see the corpse of the last crewmate in front of you."
        play music 'audio/Imperial March.mp3' fadein 1.0
        hide crewmate_1_dead
        me "... I knew… I knew it all along… "
        hide red
        hide blue
    jump scenefinal

label scenefinal:
    show bg victoryroyale
    with fade
    if crimson:
        show red at center
    else:
        show blue at center
    "Congratulations, you have won"
return
#end of game, thanks for playing!!
