class BulletBox:
    def __init__(self, capacity, bulletCount):
        self.capacity = 10
        self.bulletCount = bulletCount


class Gun:

    def __init__(self, bulletBox):
        self.bulletBox = bulletBox

    def loadBullet(self, bullets):
        if self.bulletBox.bulletCount + bullets >= self.bulletBox.capacity:
            self.bulletBox.bulletCount = self.bulletBox.capacity
        else:
            self.bulletBox.bulletCount += bullets

    def shoot(self):
        if self.bulletBox.bulletCount <= 0:
            print("no bullet")
        else:
            self.bulletBox.bulletCount -= 1
            print("remain {} bullets".format(self.bulletBox.bulletCount))


class Person:

    def __init__(self, gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()


bullet = BulletBox(10, 5)
gun = Gun(bullet)
per = Person(gun)
for i in range(1, 7):
    per.fire()

gun.loadBullet(3)
per.fire()
