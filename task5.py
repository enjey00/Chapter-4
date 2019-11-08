class Soldier:
    def __init__(self, name, gun_type):
        self.name = name
        self.gun_type = gun_type
        print(name, 'has an', gun_type)

class Gun:
    def __init__(self, name, gun_type):
        Soldier.__init__(self, name, gun_type)
        self.bullets = 7
        print('Gun is loaded:', self.bullets, 'bullets')

    def fire_bullets(self):
        self.bullets = 0
        print('Gun has been fired:', self.bullets, 'bullets')

    def reload_bullets(self, bullets):
        self.bullets += bullets
        print('Gun has been reload:', self.bullets, 'bullets')

class Act_of_shooting(Gun):
    def __init__(self, name, gun_type):
        Gun.__init__(self, name, gun_type)

soldier = Act_of_shooting('Ryan', 'AK47')
soldier.fire_bullets()
soldier.reload_bullets(7)
soldier.fire_bullets()
soldier.reload_bullets(7)
soldier.fire_bullets()