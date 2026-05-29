from classes import Weapon, Armor, Hero, Enemy, Room, Dungeon, Trader, Healing


sword = Weapon("Меч", 7, 10)
pistol = Weapon("Desert_Eagle", 12, 15)
shotgun = Weapon("Remington_911", 18, 20)
batarang = Weapon("Batarang", 35, 50)
stick = Weapon("Stick", 4, 1)
bone = Weapon("Bone", 5, 3)
arms = Weapon("Arms", 5, 0)
bottle = Weapon("Bottle", 7, 3)
wolf_claws = Weapon("Wolf_claws", 7, 6)
bear_claws = Weapon("Bear_claws", 9, 9)
heal_box = Healing("Heal_Box", 70, 40)
bandage = Healing("Bandage", 15, 9)
music = Weapon("Music", 40, 200000)
pennyroyal_tea = Healing("Pennyroyal_tea", 30, 20)


clothes_armor = Armor("Clothes_armor", 1, 2)
lether_armor = Armor("Lether_armor", 2, 3)
iron_armor = Armor("Iron_armor", 6, 12)
diamond_armor = Armor("diamond_armor", 13, 22)
bulletproof_armor = Armor("Bulletproof_armor", 30, 40)
very_super_bulletproof_armor = Armor("Very_super_bulletproof_armor", 200, 100)
wolf_fur = Armor("Wolf_fur", 2, 4)
bear_fur = Armor("Bear_fur", 5, 7)
costume = Armor("Costume", 1, 8)
music_armor = Armor("Music_Armor", 30, 1000000)

#joker = Enemy("Joker", 50, 100000, pistol, bulletproof_armor, "Enemy", 80)
#batman = Hero("Bruce_Wayne", 100, 9000000000, batarang, very_super_bulletproof_armor)
player = Hero("Steve", 100, 100000000000000000000000000000000, stick, lether_armor)
skeleton = Enemy("Skeleton", 30, 5, bone, clothes_armor, "Enemy", 6)
goblin = Enemy("Goblin", 35, 10, sword, lether_armor, "Enemy", 8)
zombie = Enemy("Zombie", 20, 4, stick, clothes_armor, "Enemy", 4)
bandit = Enemy("Bandit", 40, 15, pistol, iron_armor, "Enemy", 10)
evil_brother1 = Enemy("Evil_brother1", 35, 10, arms, clothes_armor, "Enemy", 7)
evil_brother2 = Enemy("Evil_brother2", 30, 15, arms, clothes_armor, "Enemy", 8)
drunk_man1 = Enemy("Drunk_man1", 30, 12, bottle, clothes_armor, "Enemy", 6)
drunk_man2 = Enemy("Drunk_man2", 24, 15, bottle, clothes_armor, "Enemy", 7)
drunk_man3 = Enemy("Drunk_man3", 30, 17, bottle, clothes_armor, "Enemy", 8)
wolf1 = Enemy("Wolf1", 22, 4, wolf_claws, wolf_fur, "Enemy", 7)
wolf2 = Enemy("Wolf2", 26, 6, wolf_claws, wolf_fur, "Enemy", 6)
wolf3 = Enemy("Wolf3", 24, 5, wolf_claws, wolf_fur, "Enemy", 8)
gangster1 = Enemy("Gangster1", 40, 22, pistol, iron_armor, "Enemy", 9)
gangster2 = Enemy("Gangster2", 42, 25, pistol, costume, "Enemy", 8)
gangster3 = Enemy("Gangster3", 44, 23, pistol, costume, "Enemy", 7)
bear1 = Enemy("Bear1", 40, 6, bear_claws, bear_fur, "Enemy", 8)
bear2 = Enemy("Bear2", 35, 5, bear_claws, bear_fur, "Enemy", 7)
Boss = Enemy("Teen_Spirit", 100, 120000, music, music_armor, "Enemy", 6)


room1 = Room("Skeleton_room", [skeleton])
room2 = Room("Goblin_room", [goblin])
room3 = Room("Zombies_room", [zombie])
room4 = Room("Bandit_room", [bandit])
room5 = Room("Evil_Brothers_Room", [evil_brother1, evil_brother2])
room6 = Room("Drunk_Men_Room", [drunk_man1, drunk_man2, drunk_man3])
room7 = Room("Wolves_Room", [wolf1, wolf2, wolf3])
room8 = Room("Gangsta_Room", [gangster1, gangster2, gangster3])
room9 = Room("Two_Bears_Room", [bear1,bear2])
room10 = Room("Boss_Room", [Boss])


goods = [sword, pistol, stick, bone, batarang, lether_armor, iron_armor, diamond_armor, bulletproof_armor, shotgun, heal_box, bandage, pennyroyal_tea, very_super_bulletproof_armor]
trader = Trader("Mystery", goods, 1000)

dungeon_rooms = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10]
dungeon1 = Dungeon("Simple_Dungeon", dungeon_rooms, player, trader)
dungeon1.dungeon_manager()


