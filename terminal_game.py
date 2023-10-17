import random
coins = 0
helmet = False
chestpiece = False
leggings = False
boots = False
sword = False 
HP_player = 100
HP_npc =100
moves = ['Attack', 'Block', 'Heal']
def arena(coins, helmet, chestpiece, leggings, boots, sword, HP_player, HP_npc):
    if helmet == True:
        HP_player = HP_player + 5
    if chestpiece == True:
        HP_player = HP_player + 15
    if leggings == True:
        HP_player = HP_player + 10
    if boots == True:
        HP_player = HP_player + 5
    print ("In the arena you can fight NPC's to earn coins, with those coins you can buy things like armor to make you battle's easyer.")
    ready = str(input('Are you ready for a 1V1? (Type Yes when ready): '))
    if ready == 'Yes':
        print(3)
        print(2)
        print(1)
        print('Fight')
        while HP_player > 0 and HP_npc > 0:
            npc_move = moves[random.randint (0,2)]

            print ('----------------------------------------------------------------------------------------------------------------------------------------------------')
            print (f'You have {HP_player}HP points left and the NPC has {HP_npc}HP points left')
            Player_move = str(input('It is your turn what action would you want to do?(Block, Heal, Attack): '))
            attack_damage = random.randint (10, 15)
            if Player_move == 'Heal':
                HP_player = HP_player + 5
            elif Player_move == 'Attack':
                HP_npc = HP_npc - attack_damage
                if sword == True:
                    HP_npc = HP_npc - 5
            elif Player_move == 'Block' and npc_move == 'Attack':
                HP_player = HP_player + 10
            attack_damage = random.randint (10, 15)
            if npc_move == 'Heal':
                HP_npc = HP_npc + 5
            elif npc_move == 'Attack':
                HP_player = HP_player - attack_damage
            elif npc_move == 'Block' and Player_move == 'Attack':
                HP_npc = HP_npc + 10
            if HP_player == 0:
                print ('You have died!')
            elif HP_npc <= 0:
                print ('Victory!')
                coins = int (coins + 10)
                return coins
            
def armory(coins, helmet, chestpiece, leggings, boots):
    Buy = str(input('What do you want to buy?(Helmet-10 Coins, Chestpiece-30 Coins, Leggings-20 Coins, Boots-10 Coins)'))
    if Buy == 'Helmet' and coins >= 10:
        helmet = True
        coins = coins - 10
        print ('You now have a Helmet')
    elif Buy == 'Chestpiece' and coins >= 30:
        chestpiece = True
        coins = coins - 30
        print ('You now have a Cheestpiece')
    elif Buy == 'Leggings' and coins >= 20:
        leggings = True
        coins = coins - 20
        print ('You now have Leggings')
    elif Buy == 'Boots' and coins >= 10:
        boots = True
        coins = coins - 10
        print ('You now have Boots')
    else:
        print ('You cant buy this!')
    return coins, helmet, chestpiece, leggings, boots

def Waponsmith(sword, coins):
    Wapon = str(input('What wapon do you want to buy?(Sword-30 Coins): '))
    if Wapon == 'Sword' and coins >= 30:
        sword = True
        coins = coins - 30
        print ('You now have a Sword')
    else:
        print ("You can't buy this!")
    return sword, coins

while True:
    Input = str(input('Where would you like to go?(Arena, Armory, Waponsmith ): '))
    if Input =='Arena':
        coins = arena(coins, helmet, chestpiece, leggings, boots, sword, HP_player, HP_npc)
    elif Input == 'Armory':
        output = armory(coins, helmet, chestpiece, leggings, boots)
        coins = output[0]
        helmet = output[1]
        chestpiece = [2]
        leggings = [3]
        boots = [4]
    elif Input == 'Waponsmith':
        output_waponsmith = Waponsmith(sword, coins)
        sword = output_waponsmith[0]
        coins = output_waponsmith[1]
    else:
        print ("You can't go here!(Check if you spelled the area correctly with capital letters)")

