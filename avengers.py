heroes = [
    'captainAmerica', 'ironMan', 'thor', 'hulk', 'drStange', 'blackPanther', 'blackWidow',
    'vision', 'scarletWitch', 'spiderman', 'wong', 'falcon', 'warMachine', 'rocket', 'groot',
    'drax', 'nebula', 'gamora', 'loki', 'heimdall'
]

stoneAcquired = []
gauntletFull = False
snap = 'notPossible'

places = [
    'asgardianShip', 'vormier', 'wakanda', 'titan', 'xandar', 'knowhere'
]

asgardianShip = 'asgardianShip'
vormier = 'vormier'
wakanda = 'wakanda'
titan = 'titan'
xandar = 'xandar'

war = True
while war:
    for event in pygame.event.get():
        if event.type == SNAP:
            print("End is near")
            war = False

    for place in places:
        if place == 'xandar':
            stoneAcquired.append('Powerne')

        if place == 'asgardianShip':
            heroes.remove('loki')
            heroes.remove('heimdall')
            stoneAcquired.append('Spacene')

        if place == 'knowhere':
            heroes.remove('collector')
            stoneAcquired.append('Realityne')

        if place == 'vormier':
            heroes.remove('gamora')
            stoneAcquired.append('Soulne')

        if place == 'titan':
            print("We are in the end game now")
            stoneAcquired.append('Timene')

        if place == 'wakanda':
            heroes.remove('vision')
            stoneAcquired.append('Mindne')
            gauntletFull = True
            snap = 'isPossible'
            if snap == 'isPossible':
                war = False

    pygame.update()

universePopulation = 1000
death.kill(universePopulation // 2)
print("Universe is balanced now")
pygame.quit()
sys.exit()

