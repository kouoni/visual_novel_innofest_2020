########--RENPY INIITIALISE--############
init:
    #To scale the background to fit the game size, 1280 x 720
    image white = im.Scale("white.jpg", 1280, 720)

    #Another world: On an island
    image bg beach = im.Scale("bg beach.jpg", 1280, 720)
    image bg cave = im.Scale("bg cave.jpg", 1280, 720)
    image bg forest = im.Scale("bg forest.jpg", 1280, 720)

    #Another world: In the apopcalypse
    image bg destroyedcity = im.Scale("bg destroyedcity.jpg", 1280, 720)
    image bg shop = im.Scale("bg shop.jpg", 1280, 720)
    image bg hideout = im.Scale("bg hideout.jpg", 1280, 720)

    #Another world: Time travel to a medieval fantasy
    image bg castlefaraway = im.Scale("bg castlefaraway.jpg", 1280, 720)
    image bg fantasyforest = im.Scale("bg fantasyforest.jpg", 1280, 720)
    image bg town = im.Scale("bg town.jpg", 1280, 720)

    #Another world: Space background with spaceship heading toward another planet
    image bg space = im.Scale("bg space.png", 1280, 720)
    image emergency = im.Scale("emergencybuttonlarge.jpeg", 1280, 720)
    image electrical = im.Scale("electrical.png", 1280, 720)
    image taskundone = im.Scale("wires_disconnected.jpg", 1280, 720)
    image taskdone = im.Scale("wires_connected.jpg", 1280, 720)
    image bg admin = im.Scale("bg admin.png",1280,720)
    image bg logs = im.Scale("bg logs.jpg",1280, 720)
    image bg oxygen = im.Scale("bg oxygen.png", 1280 , 720)
    image bg planet = im.Scale("bg planet.jpg", 1280, 720)
    image bg win = im.Scale("bg victoryroyale.png", 1280, 720)

########--PYTHON INITIALISE--##########
init python:
    me = Character("[name]") #Your character's name
    #a = Character("Your friend's name")
    Crewmate1 = Character("Crewmate 1")
    Crewmate2 = Character("Crewmate 2")
    Crewmate3 = Character("Crewmate 3")

###########--TRANSFORMATIONS--################
transform center:
    xalign 0.5 yalign 1.0

transform left:
    xalign 0.1 yalign 1.0

transform leftleft:
    xalign 0.01 yalign 1.0

transform right:
    xalign 0.80 yalign 1.0

transform rightright:
    xalign 0.99 yalign 1.0
