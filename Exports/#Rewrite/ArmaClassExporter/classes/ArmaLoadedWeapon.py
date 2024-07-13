import math

from ArmaWeapon import ArmaWeapon
from ArmaMagazine import ArmaMagazine
import sys

sys.path.append('..')
import EvalParam


class ArmaLoadedWeapon:
    def __init__(self, weapon_class_name: str, weapon_class_path: str,
                 magazine_class_name: str, magazine_class_path: str):
        """
        Class to inherit for Loaded weapon types.

        Parameters:
            weapon_class_name (str): The class name of the weapon
            weapon_class_path (str): The absolute file path to the weapon dict
            magazine_class_name (str): The class name of the magazine
            magazine_class_path (str): The absolute file path to the magazine dict
        """
        #
        self.magazine = None
        self.weapon = ArmaWeapon(weapon_class_name, weapon_class_path)
        self.set_magazine(magazine_class_name, magazine_class_path)

    def set_magazine(self, magazine_class_name, magazine_class_path):
        self.magazine = ArmaMagazine(magazine_class_name, magazine_class_path)
        self.process_loadout()

    def process_loadout(self):
        """
        weapon init speed rules:
        initspeed = >0: use weapon initspeed
        initspeed = <0: use abs(weapon initspeed) * magazine initspeed
        initspeed = 0: use magazine initspeed
        """
        if self.weapon.init_speed > 0:
            self.init_speed = self.weapon.init_speed
        elif self.weapon.init_speed < 0:
            self.init_speed = abs(self.weapon.init_speed) * self.magazine.init_speed
        else:
            self.init_speed = self.weapon.init_speed

        # Player weapon if scope_arsenal != 0 (should be None/2/1)

    def get_projectile_speed(self, target_range: int = 0) -> float:
        try:
            estimated_speed = self.init_speed * (1 / math.exp(abs(self.magazine.ammo.air_resistance) * target_range))
        except OverflowError:
            estimated_speed = 0
        return estimated_speed

    def get_hit(self, target_range: int = 0) -> float:
        """
        Calculate the hit value for a loaded weapon.

        Parameters:
            target_range (int): The target range in meters

        Returns:
            hit (float): The hit value
        """
        # if range is 0, point blank, use found init_speed
        # else calculate the speed of the projectile
        if target_range == 0:
            speed = self.init_speed
        else:
            speed = self.get_projectile_speed(target_range)

        # If the ammo is purely kinetic
        if self.magazine.ammo.explosive == 0:
            # Kinetic Damage is x1 at typical speed and scales linearly.
            # 10/20 would be x2 damage, 10/10 would be x1 damage, 5/10 would be x0.5 damage
            hit = (speed / self.magazine.ammo.typical_speed) * self.magazine.ammo.hit
        elif self.magazine.ammo.explosive == 1:
            # Explosive damage is irrespective of speed
            hit = self.magazine.ammo.hit
        else:
            """
            Calculate both Kinetic Damage and Explosive Damage
            Damage is calculated like so:
            
            explosive = 0.6 (for example)
            kinetic coeff will be 0.4 (1-0.6)
            
            find kinetic damage and multiply by kinetic coeff, same for explosive damage:
             hit * explosive
            
            Then get the sum of both
            """
            hit = ((((speed / self.magazine.ammo.typical_speed) * self.magazine.ammo.hit) * (
                        1 - self.magazine.ammo.explosive)) +
                   (self.magazine.ammo.explosive * self.magazine.ammo.hit))
        if self.magazine.ammo.indirect_hit is not None:
            hit += self.magazine.ammo.indirect_hit

        return hit
