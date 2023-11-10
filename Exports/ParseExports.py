# -*- coding: utf-8 -*-
import contextlib
import importlib.util
import math
import os
import ast  #string values for integer config parameters that require eval :'c
import operator as op #https://stackoverflow.com/a/9558001
from decimal import Decimal
from json import dumps

# Some mod authors like using string values for int config parameters that 
#  require the game to evaluate the expressions to get a number
#  this is not good for numerical operations.
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

def eval_expr(expr):
    return eval_(ast.parse(expr, mode='eval').body)

def eval_(node):
    if isinstance(node, ast.Num): # <number>
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)

os.system("")
cred = '\33[31m'
cgreen = '\33[32m'
cyellow = '\33[33m'
cviolet = '\33[35m'
ccyan = '\33[36m'
cgrey = '\33[90m'
cred2 = '\33[91m'
cgreen2 = '\33[92m'
cyellow2 = '\33[93m'
cblue2 = '\33[94m'
cviolet2 = '\33[95m'
ccyan2 = '\33[96m'
cwhite = '\33[96m'
cbold = '\33[1m'
cend = '\33[0m'


class ExportProperties:
    csv_export = []


class ArmaSharedProperties(ExportProperties):
    # Shared variables
    display_name = ""  # https://community.bistudio.com/wiki/BIS_fnc_displayName
    item_info_mass = 0
    item_info_hitpoints_protection_info = {}
    item_info_allowed_slots = []
    item_info_general_macro = ""
    item_info_model_sides = []
    item_info_type = 0
    model = ""

    def get_display_name(self, _module):
        with contextlib.suppress(KeyError):
            self.display_name = _module.d["displayname"]

    def get_item_info_type(self, _module):
        with contextlib.suppress(KeyError):
            self.item_info_type = _module.d["iteminfo"]["type"]

    def get_item_info_mass(self, _module):
        with contextlib.suppress(KeyError):
            self.item_info_mass = _module.d["iteminfo"]["mass"]

    def get_item_info_hitpoints_protection_info(self, _module):
        with contextlib.suppress(KeyError):
            self.item_info_hitpoints_protection_info = _module.d["iteminfo"]["hitpointsprotectioninfo"]

    def get_item_info_allowed_slots(self, _module):
        with contextlib.suppress(KeyError):
            self.item_info_allowed_slots = _module.d["iteminfo"]["allowedslots"]

    def get_item_info_general_macro(self, _module):
        with contextlib.suppress(KeyError):
            self.item_info_general_macro = _module.d["iteminfo"]["_generalmacro"]

    def get_item_info_model_sides(self, _module):
        with contextlib.suppress(KeyError):
            self.item_info_model_sides = _module.d["iteminfo"]["modelsides"]

    def get_model(self, _module):
        with contextlib.suppress(KeyError):
            self.model = _module.d["model"]


class ArmaWeaponSharedProperties(ArmaSharedProperties):
    def __init__(self, weapon_mod, magazine_mod, weapon, mag,
                 hit_formatting, hit_values_formatting, submunition_hit_values_formatting,
                 dispersion_formatting, air_friction_formatting, rpm_formatting,
                 penetration_formatting, submunition_penetration_formatting, hit_ranges):
        # Get script directory for dict path
        cwd = os.getcwd()

        # Import weapon dict
        spec = importlib.util.spec_from_file_location(weapon,
                                                      f"{cwd}/SQF-Class-Exports/{weapon_mod}/Weapons/{weapon}.py")
        self.weapon_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.weapon_module)

        # Import magazine dict
        spec = importlib.util.spec_from_file_location(mag, f"{cwd}/SQF-Class-Exports/{magazine_mod}/Magazines/{mag}.py")
        self.magazine_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.magazine_module)
        # Find if magazine has an ammo defined
        if self.magazine_module.d["ammo"] == "":
            self.ammo_flag = False
        else:
            self.ammo_flag = True

        # Class Properties
        self.weapon_class = weapon
        self.magazine_class = mag

        # General Parameters
        self.cartridge = ""  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#cartridge
        self.capacity = 0  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#cartridge
        self.hit = 0  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#hit
        self.explosive_hit = 0
        self.kinetic_hit = 0
        self.indirect_hit = 0  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#indirectHit
        self.indirect_hit_range = 0  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#indirectHitRange
        self.weap_initial_speed = 0  # https://community.bistudio.com/wiki/CfgWeapons_Config_Reference#initSpeed.3D0
        self.initial_speed = 0  # https://community.bistudio.com/wiki/CfgMagazines_Config_Reference#initSpeed.3D900
        self.typical_speed = 0  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#typicalSpeed
        self.init_greater_than_typical_speed = 0
        self.fire_modes = []  # https://community.bistudio.com/wiki/CfgWeapons_Config_Reference#modes.5B.5D.3D_.7B.22this.22.7D
        self.rpm = []  # https://community.bistudio.com/wiki/CfgWeapons_Config_Reference#reloadTime.3D1.0
        self.dispersion = []  # https://community.bistudio.com/wiki/CfgWeapons_Config_Reference#dispersion.3D0.002
        self.time_to_live = []  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#timeToLive
        self.airFriction = 0  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#airFriction
        self.side_air_friction = 0  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#sideAirFriction
        self.caliber = 0  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#caliber
        self.penetration = ["0", "0", "0"]  #
        self.hit_ranges = hit_ranges  #
        self.hit_values = []  #
        self.cm_immunity = 0
        self.thrust = 0
        self.thrust_time = 0
        self.max_speed = 0
        self.control_range = 0
        self.track_oversteer = 0
        self.track_lead = 0
        self.lock_type = 0
        self.manual_control = 0
        self.maneuvrability = 0
        self.weapon_lock_system = ""
        self.eventhandlers = {}
        self.flight_profiles = []
        self.can_lock = 0
        self.ir_lock = 0
        self.missile_manual_control_cone = 0
        self.fuze_distance = 0
        self.explosive = 0
        self.missile_lock_cone = 0
        self.missile_keep_locked_cone = 0
        self.missile_lock_max_distance = 0
        self.missile_lock_max_speed = 0
        self.warhead = ""
        self.rhs_guide_mode = ""
        self.rhs_saclos = 0
        self.rhs_ballistic_mode = 0
        self.weapon_mass = 0
        self.magazine_mass = 0

        # Flags
        self.missile_use_max_speed = 0
        self.has_submunition = 0  # 0|1|2 - no submunitions|one submunition|multiple submunitions

        # Submunition variables
        self.submunitions = []  #
        self.submunitions_names = []
        self.submunitions_submunitions = []  # The submunitions in a submunition
        self.submunitions_submunitions_names = []
        self.submunition_spawn_chance = []  # Variable to store the % chance to spawn the specific submunition when there are 2 or more
        self.submunition_hit = []  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#hit
        self.submunition_explosive_hit = []  #
        self.submunition_explosive = []
        self.submunition_indirect_hit = []  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#indirectHit
        self.submunition_indirect_hit_range = []  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#indirectHitRange
        self.submunition_initial_speed = []  # https://community.bistudio.com/wiki/CfgMagazines_Config_Reference#initSpeed.3D900
        self.submunition_typical_speed = []  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#typicalSpeed
        self.submunition_caliber = []  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#caliber
        self.submunition_submunition_caliber = []
        self.submunition_penetration = [["0", "0", "0"]]  #
        self.submunition_parent_speed_coef = []  # submunitionParentSpeedCoef https://community.bistudio.com/wiki/Arma_3:_Weapon_Config_Guidelines#Ammo_changes_on_fly_and_on_hit
        self.submunition_trigger_on_impact = 0  # triggerOnImpact            https://community.bistudio.com/wiki/Arma_3:_Weapon_Config_Guidelines#Ammo_changes_on_fly_and_on_hit
        self.submunition_delete_parent_when_triggered = 0  # deleteParentWhenTriggered  https://community.bistudio.com/wiki/Arma_3:_Weapon_Config_Guidelines#Ammo_changes_on_fly_and_on_hit
        self.submunition_trigger_speed_coef = [0,
                                               0]  # triggerSpeedCoef           https://community.bistudio.com/wiki/Arma_3:_Weapon_Config_Guidelines#Ammo_changes_on_fly_and_on_hit
        self.submunition_trigger_speed_coef_flag = True
        self.submunition_trigger_speed_coef = [0,0]  # triggerSpeedCoef           https://community.bistudio.com/wiki/Arma_3:_Weapon_Config_Guidelines#Ammo_changes_on_fly_and_on_hit
        self.submunition_shot_count = 1  # submunitionConeType        https://community.bistudio.com/wiki/Arma_3:_Weapon_Config_Guidelines#Ammo_changes_on_fly_and_on_hit
        self.submunition_trigger_time = 0  #
        self.submunition_time_to_live = []  #
        self.submunition_air_friction = []  # https://community.bistudio.com/wiki/CfgAmmo_Config_Reference#airFriction
        self.submunition_side_air_friction = []  #
        self.submunition_hit_values = []  #
        self.submunition_initial_offset = []  #
        self.submunition_warhead = ""
        self.submunition_cone = ""
        self.submunition_cone_angle = 0

        # Formatting
        self.hit_formatting = hit_formatting
        self.hit_values_formatting = hit_values_formatting
        self.submunition_hit_values_formatting = submunition_hit_values_formatting
        self.dispersion_formatting = dispersion_formatting
        self.air_friction_formatting = air_friction_formatting
        self.rpm_formatting = rpm_formatting
        self.penetration_formatting = penetration_formatting
        self.submunition_penetration_formatting = submunition_penetration_formatting

    def get_weapon_mass(self):
        try:
            self.weapon_mass = self.weapon_module.d["weaponslotsinfo"]["mass"]
        except KeyError:
            pass

    def get_magazine_mass(self):
        try:
            self.magazine_mass = self.magazine_module.d["mass"]
            # If mass is a string to be evaluated to a float
            if isinstance(self.magazine_mass, str):
                # Evalute string after replacing comma with a .
                self.magazine_mass = eval_expr(self.magazine_mass.replace(",", "."))
        except KeyError:
            pass

    def get_cartridge(self):
        try:
            self.cartridge = self.magazine_module.d["displaynameshort"]
            if self.cartridge == "":
                # Field is empty so use _dictAmmoName
                raise KeyError
        except KeyError:
            self.cartridge = self.magazine_module.d["ammo"]["_dictAmmoName"]

    def get_time_to_live(self):
        # Time to live of the first CfgAmmo spanwed
        self.time_to_live = self.magazine_module.d["ammo"]["timetolive"]

        # Time to live of the submunition(s)
        if self.has_submunition != 0:
            self.submunition_penetration = []  # Remove default [[0,0,0]] value
            for sub in self.submunitions:
                self.submunition_time_to_live.append(self.magazine_module.d["ammo"][sub]["timetolive"])

    def get_submunition_values(self):

        # Submunition parameters not tied to a specific submunition:
        try:
            self.submunition_delete_parent_when_triggered = self.magazine_module.d["ammo"]["deleteparentwhentriggered"]
        except KeyError:
            pass  # Not present, default value will be used instead
        try:
            self.submunition_trigger_speed_coef = self.magazine_module.d["ammo"]["triggerspeedcoef"]
            if isinstance(self.submunition_trigger_speed_coef, int) or isinstance(self.submunition_trigger_speed_coef, float):
                self.submunition_trigger_speed_coef_flag = False
        except KeyError:
            pass  # Not present, default value will be used instead
        try:
            self.submunition_cone_angle = self.magazine_module.d["ammo"]["submunitionconeangle"]
        except KeyError:
            pass  # :DDD
        # Submunition-specific parameters

        for x, sub in enumerate(self.submunitions):
            try:
                self.submunition_parent_speed_coef.append(self.magazine_module.d["ammo"]["submunitionparentspeedcoef"])
            except KeyError:
                pass  # Not present, default value will be used instead
            try:
                sub_initial_speed = self.magazine_module.d["ammo"]["submunitioninitspeed"]

                if sub_initial_speed == 0:
                    if self.submunition_parent_speed_coef[x] > 0:
                        sub_initial_speed = self.initial_speed * self.submunition_parent_speed_coef[x]

                self.submunition_initial_speed.append(sub_initial_speed)
            except KeyError:
                # NOTE submunitionInitSpeed method when using submunitionTriggerSpeedCoef
                # No submunitionInitSpeed value, we have to calculate it instead
                # Using the lowest multiplier from the range - possibly make it in between the two
                #  multipliers from submunitionTriggerSpeedCoef?
                # Current method gives ensures submunition performs at or above calculated speed
                self.submunition_initial_speed.append(self.submunition_trigger_speed_coef[0] * self.initial_speed)
                if self.submunition_trigger_speed_coef_flag:
                    print(f"{self.submunition_trigger_speed_coef} | {self.submunition_trigger_speed_coef_flag}")
                    self.submunition_initial_speed.append(self.submunition_trigger_speed_coef[0] * self.initial_speed)
                else:
                    self.submunition_initial_speed.append(self.submunition_trigger_speed_coef * self.initial_speed)
                pass  # Not present, default value will be used instead
            try:
                self.submunition_typical_speed.append(self.magazine_module.d["ammo"][sub]["typicalspeed"])
            except KeyError:
                pass  # Not present, default value will be used instead

    def get_speeds(self):
        self.weap_initial_speed = self.weapon_module.d["initspeed"]
        self.initial_speed = self.magazine_module.d["initspeed"]
        self.typical_speed = self.magazine_module.d["ammo"]["typicalspeed"]
        self.max_speed = self.magazine_module.d["ammo"]["maxspeed"]
        if self.weap_initial_speed != 0:
            if self.weap_initial_speed < 0:
                self.initial_speed = abs(self.initial_speed * self.weap_initial_speed)
            else:
                self.initial_speed = self.weap_initial_speed
        # Missiles
        if self.initial_speed == 0:
            self.missile_use_max_speed = 1
        if self.has_submunition > 0:
            # Structure is list of dicts: [submunitionammo] or [submunitionammo1,submunitionammo2,...]
            self.get_submunition_values()

    def get_hit(self):
        self.explosive = self.magazine_module.d["ammo"]["explosive"]
        self.max_speed = self.magazine_module.d["ammo"]["maxspeed"]
        self.hit = self.magazine_module.d["ammo"]["hit"]
        self.explosive_hit = self.hit * self.explosive
        self.init_greater_than_typical_speed = (self.initial_speed >= self.typical_speed)

        if self.magazine_module.d["ammo"]["simulation"] not in ["shotMissile", "shotRocket"]:
            if self.explosive == 1:
                self.hit = self.explosive_hit
            elif self.explosive == 0:
                if self.init_greater_than_typical_speed is not True:
                    self.hit = self.hit * (self.initial_speed / self.typical_speed)
                    # print(f"{self.displayName}\nhit({self.hit}) = {self.kineticHit} + {self.explosiveHit}")
            else:
                if self.init_greater_than_typical_speed is not True:
                    self.kinetic_hit = (self.hit - self.explosive_hit) * (self.initial_speed / self.typical_speed)
                else:
                    self.kinetic_hit = self.hit - self.explosive_hit

            if (self.kinetic_hit > 0) or (self.explosive_hit > 0):
                # print(f"{self.displayName}\nhit({self.hit}) = {self.kineticHit} + {self.explosiveHit}")
                self.hit = self.kinetic_hit + self.explosive_hit

        self.indirect_hit = self.magazine_module.d["ammo"]["indirecthit"]
        self.indirect_hit_range = self.magazine_module.d["ammo"]["indirecthitrange"]
        self.caliber = self.magazine_module.d["ammo"]["caliber"]
        # TODO Evaluate these expressions in SQF export, instead of here, if possible
        if isinstance(self.caliber, str):
            self.caliber = eval_expr(self.caliber)
        self.penetration = [('{:.' + str(self.penetration_formatting) + 'f}').format(
            (Decimal(self.initial_speed * self.caliber * 0.015))).zfill(5),
                            ('{:.' + str(self.penetration_formatting) + 'f}').format(
                                (Decimal(self.initial_speed * self.caliber * 0.080))).zfill(5),
                            ('{:.' + str(self.penetration_formatting) + 'f}').format(
                                (Decimal(self.initial_speed * self.caliber * 0.250))).zfill(5)]
        if self.has_submunition > 0:  # Else we have one or more submunitions
            # Find the number of submunitions created
            try:
                self.submunition_shot_count = self.magazine_module.d["ammo"]["submunitionconetype"][1]

                # If it's a list, it's a custom submunitionconetype and the number of entires is the number of submunitions
                if isinstance(self.submunition_shot_count, list):
                    self.submunition_shot_count = len(self.submunition_shot_count[0])
            except KeyError:
                pass  # There is only one submunition created

            for x, sub in enumerate(self.submunitions):
                self.submunition_explosive.append(self.magazine_module.d["ammo"][sub]["explosive"])
                self.submunition_hit.append(self.magazine_module.d["ammo"][sub]["hit"])
                self.submunition_indirect_hit.append(self.magazine_module.d["ammo"][sub]["indirecthit"])
                if self.has_submunition == 1:
                    # If there is only one type of submunition we know that
                    #  every submunitionShot will be that CfgAmmo and can therefore
                    #  multiply the hit value by the number of submunitions spawned to get the damage
                    #print(f"{self.submunition_hit[x]} * {self.submunition_shot_count}")
                    self.submunition_hit[x] = self.submunition_hit[x] * self.submunition_shot_count

                    self.submunition_indirect_hit[x] = self.submunition_indirect_hit[x] * self.submunition_shot_count
                    self.submunition_spawn_chance.append(1)  # Only one CfgAmmo in self.submunitions
                else:  # If there are 2+ submunitions, get the chance to spawn them
                    self.submunition_spawn_chance.append(self.magazine_module.d["ammo"][sub]["_dictAmmoChance"])
                self.submunition_indirect_hit_range.append(self.magazine_module.d["ammo"][sub]["indirecthitrange"])
                self.submunition_caliber.append(self.magazine_module.d["ammo"][sub]["caliber"])
                self.submunition_penetration.append(
                    [(f"{{:.{self.submunition_penetration_formatting}f}}").format(
                        (Decimal(self.submunition_initial_speed[x] * self.submunition_caliber[x] * 0.015))).zfill(5),
                     (f"{{:.{self.submunition_penetration_formatting}f}}").format(
                         (Decimal(self.submunition_initial_speed[x] * self.submunition_caliber[x] * 0.080))).zfill(5),
                     (f"{{:.{self.submunition_penetration_formatting}f}}").format(
                         (Decimal(self.submunition_initial_speed[x] * self.submunition_caliber[x] * 0.250))).zfill(5)]
                )

    def get_capacity(self):
        self.capacity = self.magazine_module.d["count"]

    def get_fire_modes(self):  # [Fire mode, RPM, Dispersion]
        print(f"get_fire_modes {self.weapon_class}")
        fire_modes = self.weapon_module.d["modes"]
        fire_modes = [x.lower() for x in fire_modes]

        # Validate firemodes
        for mode in fire_modes:
            try:
                self.weapon_module.d[mode]["showtoplayer"]
            except KeyError:
                #Remove invalid firemodes
                fire_modes.remove(mode)

        # TODO Redo this mess
        if fire_modes != ["this"]:
            for mode in fire_modes:
                if self.weapon_module.d[mode]["showtoplayer"] == 1:
                    try:
                        rpm = str(round(60 / self.weapon_module.d[mode]["reloadtime"], self.rpm_formatting)).zfill(6)
                        try:
                            rpm = str(round(60 / self.weapon_module.d[mode]["reloadtime"], self.rpm_formatting)).zfill(6)
                        except TypeError:
                            rpm = str(round(60 / eval_expr(self.weapon_module.d[mode]["reloadtime"]), self.rpm_formatting)).zfill(6)
                        # If a unique rpm for the firemode, add it to the list
                        self.fire_modes.append(mode)
                        self.rpm.append(rpm)
                        dispersion = self.weapon_module.d[mode]["dispersion"]
                        try:
                            self.dispersion.append((f"{{:.{self.dispersion_formatting}f}}").format(dispersion))
                        except ValueError:  # Value is a string to eval eg "0.005*25"
                            self.dispersion.append((f"{{:.{self.dispersion_formatting}f}}").format(eval(dispersion)))
                            self.dispersion.append((f"{{:.{self.dispersion_formatting}f}}").format(eval_expr(dispersion)))
                    except KeyError:
                        print(f"KeyError: {self.weapon_class}|{self.magazine_class}|{mode}")
                        pass
        else:
            try:
                rpm = str(round(60 / self.weapon_module.d["reloadtime"], self.rpm_formatting)).zfill(6)
            except (KeyError, ZeroDivisionError):
            except (KeyError, ZeroDivisionError) as e:
                rpm = 0
            self.fire_modes.append("this")
            self.rpm.append(rpm)
            dispersion = self.weapon_module.d["dispersion"]
            try:
                self.dispersion.append((f"{{:.{self.dispersion_formatting}f}}").format(dispersion))
            except ValueError:  # Value is a string to eval eg "0.005*25"
                self.dispersion.append((f"{{:.{self.dispersion_formatting}f}}").format(eval(dispersion)))
                self.dispersion.append((f"{{:.{self.dispersion_formatting}f}}").format(eval_expr(dispersion)))

        if all(item == self.rpm[0] for item in self.rpm):
            self.rpm = self.rpm[0]
        if all(item == self.dispersion[0] for item in self.dispersion):
            self.dispersion = self.dispersion[0]
        if self.rpm != []:
            if all(item == self.rpm[0] for item in self.rpm):
                self.rpm = self.rpm[0] # self.rpm[0] FIXME list index out of range
            if all(item == self.dispersion[0] for item in self.dispersion):
                self.dispersion = self.dispersion[0]
        else:
            #No mode with an applicable reloadtime, use main weapon parameter value
            self.rpm = self.weapon_module.d["reloadtime"]

    def get_air_frictions(self):
        self.airFriction = abs(self.magazine_module.d["ammo"]["airfriction"])
        self.side_air_friction = abs(self.magazine_module.d["ammo"]["sideairfriction"])

        if self.has_submunition != 0:
            for sub in self.submunitions:
                self.submunition_air_friction.append(abs(self.magazine_module.d["ammo"][sub]["airfriction"]))
                self.submunition_side_air_friction.append(abs(self.magazine_module.d["ammo"][sub]["sideairfriction"]))

    def get_submunition_cone(self):
        try:
            self.submunition_cone = self.magazine_module.d["ammo"]["submunitionconetype"][0]
        except KeyError:
            pass

    def get_warheads(self):
        if self.has_submunition == 0:
            try:
                self.warhead = self.magazine_module.d["ammo"]["warheadname"]
            except KeyError:
                pass
        else:
            for submunition in self.submunitions:
                try:
                    self.submunition_warhead += self.magazine_module.d["ammo"][submunition]["warheadname"]
                except KeyError:
                    continue
                if (self.has_submunition > 1) and (submunition != self.submunitions[-1]):
                    self.submunition_warhead += "|"

    def get_control_range(self):
        self.control_range = self.magazine_module.d["ammo"]["maxcontrolrange"]

    def get_rhs_modes(self):
        try:
            self.rhs_guide_mode = self.magazine_module.d["ammo"]["rhs_guidemode"]
        except KeyError:
            pass
        try:
            self.rhs_saclos = self.magazine_module.d["ammo"]["rhs_saclos"]
        except KeyError:
            pass
        try:
            self.rhs_ballistic_mode = self.magazine_module.d["ammo"]["rhs_ballisticmode"]
        except KeyError:
            pass

    def get_missile_params(self):
        try:
            self.thrust = self.magazine_module.d["ammo"]["thrust"]
        except KeyError:
            pass
        try:
            self.thrust_time = self.magazine_module.d["ammo"]["thrusttime"]
        except KeyError:
            pass
        try:
            self.maneuvrability = self.magazine_module.d["ammo"]["maneuvrability"]
        except KeyError:
            pass
        try:
            self.track_oversteer = self.magazine_module.d["ammo"]["trackoversteer"]
        except KeyError:
            pass
        try:
            self.track_lead = self.magazine_module.d["ammo"]["tracklead"]
        except KeyError:
            pass
        try:
            self.missile_manual_control_cone = self.magazine_module.d["ammo"]["missilemanualcontrolcone"]
        except KeyError:
            pass
        try:
            self.flight_profiles = self.magazine_module.d["ammo"]["flightprofiles"]
        except KeyError:
            pass

    def get_submunition_initial_offset(self):
        try:
            self.submunition_initial_offset = self.magazine_module.d["ammo"]["submunitioninitialoffset"]
        except KeyError:
            pass

    def get_estimate_speed(self, distance=200):
        try:
            estimated_speed = self.initial_speed * (1 / math.exp(abs(self.airFriction) * distance))
        except OverflowError:
            estimated_speed = 0
        return estimated_speed

    def get_hit_at_ranges(self):
        # TODO Redo this mess
        if self.explosive == 0:
            for distance in self.hit_ranges:
                estimated_speed = self.get_estimate_speed(distance)
                # str(distance).zfill(4) + ": " + (round(estSpeed, 2)).zfill(6) + " - Hit: " + '{:.3f}'.format(round(damage * (estSpeed/typicalSpeed),3)) + "\n"
                if estimated_speed != 0:
                    hit_value = self.hit
                    if estimated_speed < self.typical_speed:
                        hit_value = hit_value * (estimated_speed / self.typical_speed)
                    self.hit_values.append(
                        (f"{{:.{self.hit_values_formatting}f}}").format(round(hit_value, self.hit_values_formatting)))

                else:
                    self.hit_values.append("n/a")
        elif self.explosive == 1:
            for distance in self.hit_ranges:
                self.hit_values.append(
                    ('{:.' + str(self.hit_values_formatting) + 'f}').format(round(self.explosive_hit)))
        else:
            for distance in self.hit_ranges:
                estimated_speed = self.get_estimate_speed(distance)

                kinetic_hit_value = self.kinetic_hit
                if estimated_speed < self.typical_speed:
                    kinetic_hit_value = kinetic_hit_value * (estimated_speed / self.typical_speed)
                self.hit_values.append((f"{{:.{self.hit_values_formatting}f}}").format(
                    round(self.explosive_hit + kinetic_hit_value, self.hit_values_formatting)))

        if self.has_submunition != 0:
            for x, sub in enumerate(self.submunitions):
                submunition_hit_values = []
                for distance in self.hit_ranges:
                    estimated_speed = self.get_estimate_speed(distance)
                    if estimated_speed != 0:
                        submunition_hit_values.append((f"{{:.{self.submunition_hit_values_formatting}f}}").format(
                            round(self.submunition_hit[x] * (estimated_speed / self.submunition_typical_speed[x]),
                                  self.submunition_hit_values_formatting)))
                    else:
                        submunition_hit_values.append(0.000)
                self.submunition_hit_values.append(submunition_hit_values)

    def replace_normal_with_submunition_values(self):
        # To use when there is one submunition type that "replaces" the original shot
        self.hit = self.submunition_hit[0]
        self.dispersion = self.submunition_cone_angle
        self.time_to_live = self.submunition_time_to_live[0]
        self.initial_speed = self.submunition_initial_speed[0]
        self.typical_speed = self.submunition_typical_speed[0]
        self.airFriction = self.submunition_air_friction[0]
        self.penetration = self.submunition_penetration[0]
        self.hit_values = self.submunition_hit_values[0]
        self.caliber = self.submunition_caliber[0]

    def get_submunition_submunition_caliber(self):
        for submunition in self.submunitions:
            try:
                self.submunition_submunition_caliber.append(
                    self.magazine_module.d["ammo"][submunition]["submunitionammo"]["caliber"])  #
            except (TypeError, IndexError):
                self.submunition_submunition_caliber.append(0)

    @staticmethod
    def get_nested_value(class_dict, path):
        nested_value = None
        for key in path:
            nested_value = class_dict[key]
            class_dict = nested_value
        return nested_value


class ArmaWeaponClass(ArmaWeaponSharedProperties):
    def __init__(self, weapon_mod, magazine_mod, weapon, mag,
                 hit_formatting, hit_values_formatting, submunition_hit_values_formatting,
                 dispersion_formatting, air_friction_formatting, rpm_formatting,
                 penetration_formatting, submunition_penetration_formatting, hit_ranges):
        super().__init__(weapon_mod, magazine_mod, weapon, mag,
                         hit_formatting, hit_values_formatting, submunition_hit_values_formatting,
                         dispersion_formatting, air_friction_formatting, rpm_formatting,
                         penetration_formatting, submunition_penetration_formatting, hit_ranges)

        # Determine if the projectile has submunitions here
        try:
            # Check to see if there is one submunition
            submunition_check = self.magazine_module.d["ammo"]["submunitionammo"]
            if submunition_check:
                self.submunitions.append("submunitionammo")
                self.submunitions_names.append(self.magazine_module.d["ammo"]["submunitionammo"]["_dictAmmoName"])
                self.has_submunition = 1
        except KeyError:
            try:
                for i in range(1, 10):
                    submunition_var = f"submunitionammo{i}"
                    submunition_check = self.magazine_module.d["ammo"][submunition_var]
                    if submunition_check != "":
                        self.submunitions.append(submunition_var)
                        self.submunitions_names.append(self.magazine_module.d["ammo"][submunition_var]["_dictAmmoName"])
                        self.has_submunition = 2
            except KeyError:
                pass  # There is no submunitions named submunitionammoX
        # Determine if the projectile's submunitions have Submunitions
        for submunition in self.submunitions:
            try:
                self.submunitions_submunitions.append(
                    self.magazine_module.d["ammo"][submunition]["submunitionammo"]["_dictAmmoName"])
                self.submunitions_submunitions_names.append(
                    self.magazine_module.d["ammo"][submunition]["submunitionammo"]["_dictAmmoName"])
            except (KeyError, TypeError):
                pass
        if self.has_submunition == 1:
            # Find when submunitions are deployed:
            #  On impact? Just after fired?
            try:
                self.submunition_trigger_on_impact = self.magazine_module.d["ammo"]["triggeronimpact"]
            except KeyError:
                pass  # No triggeronimpact set, retain default 0 value
            try:
                self.submunition_trigger_time = self.magazine_module.d["ammo"]["triggertime"]
            except KeyError:
                pass  # No triggertime set, retain default 0 value

    def get_firearm_stats(self, display_name=1, cartridge=1, time_to_live=1,
                          capacity=1, speeds=1, air_frictions=1, hit=1,
                          hit_at_ranges=1, fire_modes=1, weapon_mass=1,
                          magazine_mass=1):
        if display_name == 1:
            self.get_display_name(self.weapon_module)
        if cartridge == 1:
            self.get_cartridge()
        if time_to_live == 1:
            self.get_time_to_live()
        if capacity == 1:
            self.get_capacity()
        if speeds == 1:
            self.get_speeds()
        if air_frictions == 1:
            self.get_air_frictions()
        if hit == 1:
            self.get_hit()
        if hit_at_ranges == 1:
            self.get_hit_at_ranges()
        if fire_modes == 1:
            self.get_fire_modes()
        if weapon_mass == 1:
            self.get_weapon_mass()
        if magazine_mass == 1:
            self.get_magazine_mass()

    def set_csv_export(self):
        # TODO use optional exports from getFireamStats
        # do this for ArmaVehicleWeaponCLass.set_csv_export too
        #  Created variable self.get_firearm_statsParameters for this
        self.airFriction = (f"{{:.{self.air_friction_formatting}f}}").format(self.airFriction)
        self.csv_export = [self.display_name, self.cartridge, self.capacity,
                           (f"{{:.{self.hit_formatting}f}}").format(self.hit),
                           '|'.join(self.fire_modes), self.rpm, self.dispersion, self.time_to_live,
                           self.initial_speed, self.typical_speed, self.weap_initial_speed,
                           self.airFriction, self.penetration[0], self.penetration[1], self.penetration[2]]
        self.csv_export.extend(self.hit_values)
        self.csv_export.extend([self.weapon_class, self.magazine_class, self.weapon_mass, self.magazine_mass, round(self.magazine_mass/self.capacity, self.hit_formatting), self.caliber])

    def print_stats(self):
        h_vz_fill = len(str(self.hit_values[0]))
        h_rz_fill = len(str(self.hit_ranges[-1]))

        print_string = (f"{ccyan}                  Name: {cend}{cgreen}{self.display_name}{cend}\n" +
                        f"{ccyan}             Cartridge: {cend}{cgreen}{self.cartridge}{cend}\n" +
                        f"{cred}              Capacity: {cend}{cviolet}{self.capacity}{cend}\n" +
                        f"{cred}                Damage: {cend}{cviolet}{self.hit}{cend}\n" +
                        f"{ccyan}            Fire Modes: {cend}{cyellow}{self.fire_modes}{cend}\n" +
                        f"{ccyan}                   RPM: {cend}{cyellow}{self.rpm}{cend}\n" +
                        f"{ccyan}            Dispersion: {cend}{cyellow}{self.dispersion}{cend}\n" +
                        f"{cred}         Initial Speed: {cend}{cviolet}{self.initial_speed}{cend}\n" +
                        f"{cred}         Typical Speed: {cend}{cviolet}{self.typical_speed}{cend}\n" +
                        f"{cred}        Air Resistance: {cend}{cviolet}{self.airFriction}{cend}\n" +
                        f"{cred}       RHA Penetration: {cend}{cgreen}{self.penetration[0]}{cend}\n" +
                        f"{cred}  Concrete Penetration: {cend}{cgreen}{self.penetration[1]}{cend}\n" +
                        f"{cred}      Meat Penetration: {cend}{cgreen}{self.penetration[2]}{cend}\n" +
                        f"{cred}            Ballistics: {cend}{cgreen}\n" +
                        f"            {str(self.hit_values[0]).zfill(h_vz_fill)} @ {str(self.hit_ranges[0]).zfill(h_rz_fill)}m\n" +
                        f"            {str(self.hit_values[1]).zfill(h_vz_fill)} @ {str(self.hit_ranges[1]).zfill(h_rz_fill)}m\n" +
                        f"            {str(self.hit_values[2]).zfill(h_vz_fill)} @ {str(self.hit_ranges[2]).zfill(h_rz_fill)}m\n" +
                        f"            {str(self.hit_values[3]).zfill(h_vz_fill)} @ {str(self.hit_ranges[3]).zfill(h_rz_fill)}m\n" +
                        f"            {str(self.hit_values[4]).zfill(h_vz_fill)} @ {str(self.hit_ranges[4]).zfill(h_rz_fill)}m\n" +
                        f"            {str(self.hit_values[5]).zfill(h_vz_fill)} @ {str(self.hit_ranges[5]).zfill(h_rz_fill)}m\n" +
                        f"            {str(self.hit_values[6]).zfill(h_vz_fill)} @ {str(self.hit_ranges[6]).zfill(h_rz_fill)}m\n" +
                        f"            {str(self.hit_values[7]).zfill(h_vz_fill)} @ {str(self.hit_ranges[7]).zfill(h_rz_fill)}m{cend}\n" +
                        f"{ccyan}        Weapon Class: {cend}{cgreen}{self.weapon_class}{cend}\n" +
                        f"{cred}      Magazine Class: {cend}{cgreen}{self.magazine_class}{cend}\n" +
                        f"{cred}             Caliber: {cend}{cviolet}{self.caliber}{cend}\n")
        if self.has_submunition > 0:
            print_string += (
                    f"{cred}                            Submunitions:{cend}{cyellow}{self.submunitions_names}{cend}\n" +
                    f"{cred}               Submunitions Submunitions:{cend}{cyellow}{self.submunitions_submunitions_names}{cend}\n" +
                    f"{cred}               Submunition Spawn Chances:{cend}{cyellow}{self.submunition_spawn_chance}{cend}\n" +
                    f"{cred}                         Submunition Hit:{cend}{cyellow}{self.submunition_hit}{cend}\n" +
                    f"{cred}                Submunition Indirect Hit:{cend}{cyellow}{self.submunition_indirect_hit}{cend}\n" +
                    f"{cred}          Submunition Indirect Hit Range:{cend}{cyellow}{self.submunition_indirect_hit_range}{cend}\n" +
                    f"{cred}               Submunition Initial Speed:{cend}{cyellow}{self.submunition_initial_speed}{cend}\n" +
                    f"{cred}               Submunition Typical Speed:{cend}{cyellow}{self.submunition_typical_speed}{cend}\n" +
                    f"{cred}                     Submunition Caliber:{cend}{cyellow}{self.submunition_caliber}{cend}\n" +
                    f"{cred}                 Submunition Penetration:{cend}{cyellow}{self.submunition_penetration}{cend}\n" +
                    f"{cred}           Submunition Parent Speed Coef:{cend}{cyellow}{self.submunition_parent_speed_coef}{cend}\n" +
                    f"{cred}           Submunition Trigger On Impact:{cend}{cyellow}{self.submunition_trigger_on_impact}{cend}\n" +
                    f"{cred}Submunition Delete Parent When Triggered:{cend}{cyellow}{self.submunition_delete_parent_when_triggered}{cend}\n" +
                    f"{cred}          Submunition Trigger Speed Coef:{cend}{cyellow}{self.submunition_trigger_speed_coef}{cend}\n" +
                    f"{cred}                       Submunition Count:{cend}{cyellow}{self.submunition_shot_count}{cend}\n" +
                    f"{cred}                Submunition Trigger Time:{cend}{cyellow}{self.submunition_trigger_time}{cend}\n" +
                    f"{cred}                Submunition Time To Live:{cend}{cyellow}{self.submunition_time_to_live}{cend}\n" +
                    f"{cred}                Submunition Air Friction:{cend}{cyellow}{self.submunition_air_friction}{cend}\n" +
                    f"{cred}        Submunition Turning Air Friction:{cend}{cyellow}{self.submunition_side_air_friction}{cend}\n" +
                    f"{cred}         Submunition Hit at Given Ranges:{cend}{cyellow}{self.submunition_hit_values}{cend}\n")
        print_string += "----------------------------------------------------------------------------------"
        print(print_string)


class ArmaScopeClass(ArmaSharedProperties):
    def __init__(self, mod, scope, fov, fov_round_digits):
        # Get script directory for dict path
        cwd = os.getcwd()
        # Import scope dict
        spec = importlib.util.spec_from_file_location(scope, f"{cwd}/SQF-Class-Exports/{mod}/Weapons/{scope}.py")
        self.scopeModule = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.scopeModule)

        # Class Properties
        self.scopeClass = scope
        self.playerFov = fov
        self.fov_round_digits = fov_round_digits

        # Init variables
        self.scopeType = 201
        self.optics_modes = []
        self.optics_mode_settings = []

    def get_scope_modes(self):
        try:
            self.optics_modes = list(self.scopeModule.d["iteminfo"]["opticsmodes"].keys())
        except KeyError:
            pass

    def get_scope_mode_parameter(self, mode, param):
        try:
            return self.scopeModule.d["iteminfo"]["opticsmodes"][mode][param]
        except KeyError:
            return None

    def get_scope_mode_settings(self):
        self.optics_mode_settings = {}
        magnification_list = []
        for mode in self.optics_modes:
            _discreteFov = self.get_scope_mode_parameter(mode, "discretefov")
            if _discreteFov is not None:
                magnification_list = []
                for _fov in _discreteFov:
                    if type(_fov) is str:
                        split_fov = _fov.split("/")
                        split_divide = Decimal(split_fov[0]) / Decimal(split_fov[1])
                        magnification = Decimal(self.playerFov) / split_divide
                    else:
                        magnification = Decimal(self.playerFov) / Decimal(_fov)
                    magnification_list.append(float(round(magnification, self.fov_round_digits)))

            self.optics_mode_settings[mode] = (
                {
                    "magnificationList": magnification_list,
                    "opticsid": self.get_scope_mode_parameter(mode, "opticsid"),
                    "usemodeloptics": self.get_scope_mode_parameter(mode, "usemodeloptics"),
                    "opticsppeffects": self.get_scope_mode_parameter(mode, "opticsppeffects"),
                    "discretedistance": self.get_scope_mode_parameter(mode, "discretedistance"),
                    "discretedistanceinitindex": self.get_scope_mode_parameter(mode, "discretedistanceinitindex"),
                    "opticszoommax": self.get_scope_mode_parameter(mode, "opticszoommax"),
                    "opticszoommin": self.get_scope_mode_parameter(mode, "opticszoommin"),
                    "opticszoominit": self.get_scope_mode_parameter(mode, "opticszoominit"),
                    "memorypointcamera": self.get_scope_mode_parameter(mode, "memorypointcamera"),
                    "discretefov": _discreteFov,
                    "discreteinitindex": self.get_scope_mode_parameter(mode, "discreteinitindex"),
                    "modeloptics": self.get_scope_mode_parameter(mode, "modeloptics"),  # Crosshair
                    "visionmode": self.get_scope_mode_parameter(mode, "visionmode"),
                    "opticsflare": self.get_scope_mode_parameter(mode, "opticsflare"),
                    "opticsdisableperipherialvision": self.get_scope_mode_parameter(mode,
                                                                                    "opticsdisableperipherialvision"),
                    # Black around scope when in use
                    "distancezoommin": self.get_scope_mode_parameter(mode, "distancezoommin"),
                    "distancezoommax": self.get_scope_mode_parameter(mode, "distancezoommax"),
                }
            )

    def get_scope_stats(self, display_name=1, optics_modes=1, optics_mode_settings=1):
        # TODO Apply this functionality to the other get_x_stats methods
        self.get_item_info_type(self.scopeModule)
        if self.item_info_type == self.scopeType:
            if display_name == 1:
                self.get_display_name(self.scopeModule)
            if optics_modes == 1:
                self.get_scope_modes()
            if optics_mode_settings == 1:
                self.get_scope_mode_settings()
            return True
        else:
            return False

    def print_stats(self):
        print(f"{ccyan}          Scope Name: {cend}{cyellow}{self.display_name}{cend}\n" +
              f"{ccyan}         Scope Class: {cend}{cyellow}{self.scopeClass}{cend}\n" +
              f"{ccyan}        Optics Modes: {cend}{cgreen}{self.optics_modes}{cend}\n" +
              f"{ccyan}Optics Mode Settings: {cend}{cgreen}\n" +
              f"{dumps(self.optics_mode_settings, sort_keys=False, indent=4)}{cend}\n" +
              "--------------------------------------------")
        # "\n".join(map(str, self.opticsModeSettings[0]))

    def set_csv_export(self):
        self.csv_export = [self.display_name, self.scopeClass,
                           self.optics_modes, self.optics_mode_settings]


class ArmaVehicleWeaponClass(ArmaWeaponClass):
    def __init__(self, weapon_mod, magazine_mod, weapon, mag,
                 hit_formatting, hit_values_formatting, submunition_hit_values_formatting,
                 dispersion_formatting, air_friction_formatting, rpm_formatting,
                 penetration_formatting, submunition_penetration_formatting, hit_ranges):
        # ArmaWeaponClass.__init__(self,mod,weapon,mag,hitRanges)
        super().__init__(weapon_mod, magazine_mod, weapon, mag,
                         hit_formatting, hit_values_formatting, submunition_hit_values_formatting,
                         dispersion_formatting, air_friction_formatting, rpm_formatting,
                         penetration_formatting, submunition_penetration_formatting, hit_ranges)

    def get_weapon_stats(self):
        self.get_display_name(self.weapon_module)
        self.get_cartridge()
        self.get_weapon_mass()
        self.get_time_to_live()
        self.get_capacity()
        self.get_speeds()
        self.get_air_frictions()
        self.get_hit()
        self.get_hit_at_ranges()
        self.get_fire_modes()

        if self.has_submunition != 0:
            self.get_submunition_initial_offset()
            self.get_submunition_cone()
            self.get_submunition_submunition_caliber()
        self.get_warheads()
        self.get_control_range()
        self.get_rhs_modes()
        self.get_missile_params()

    def set_csv_export(self):
        # TODO use optional exports from getFireamStats
        self.airFriction = (f"{{:.{self.air_friction_formatting}f}}").format(self.airFriction)
        self.csv_export = [
            self.display_name,
            self.cartridge,
            self.capacity,
            (f"{{:.{self.hit_formatting}f}}").format(self.hit),
            self.indirect_hit,
            self.indirect_hit_range,
            self.submunition_hit,
            self.submunition_indirect_hit,
            self.submunition_indirect_hit_range,
            self.submunitions_names,
            self.submunitions_submunitions,
            self.submunition_cone,
            self.warhead,
            self.submunition_warhead,
            '|'.join(self.fire_modes),
            self.rpm,
            self.dispersion,
            self.time_to_live,
            self.initial_speed,
            self.typical_speed,
            self.weap_initial_speed,
            self.airFriction,
            self.side_air_friction,
            self.control_range,
            self.rhs_guide_mode,
            self.rhs_saclos,
            self.rhs_ballistic_mode,
            self.penetration[0],
            self.penetration[1],
            self.penetration[2],
            self.submunition_penetration[0][0],
            self.submunition_penetration[0][1],
            self.submunition_penetration[0][2],
            self.thrust,
            self.thrust_time,
            self.max_speed,
            self.maneuvrability,
            self.track_oversteer,
            self.track_lead,
            self.missile_manual_control_cone,
            self.flight_profiles,
        ]
        self.csv_export.extend(self.hit_values)
        self.csv_export.extend([self.weapon_class, self.magazine_class, self.caliber,
                                self.submunition_caliber, self.submunition_submunition_caliber])

    def print_all_variables(self):
        # regex =.*[^\n]
        print(
            f"                        display_name = {self.display_name}\n" +
            f"                        weapon_class = {self.weapon_class}\n" +
            f"                      magazine_class = {self.magazine_class}\n" +
            f"                          csv_export = {self.csv_export}\n" +
            f"                           cartridge = {self.cartridge}\n" +
            f"                            capacity = {self.capacity}\n" +
            f"                                 hit = {self.hit}\n" +
            f"                        explosiveHit = {self.explosive_hit}\n" +
            f"                          kineticHit = {self.kinetic_hit}\n" +
            f"                         indirectHit = {self.indirect_hit}\n" +
            f"                    indirectHitRange = {self.indirect_hit_range}\n" +
            f"                    weapInitialSpeed = {self.weap_initial_speed}\n" +
            f"                        initialSpeed = {self.initial_speed}\n" +
            f"                        typicalSpeed = {self.typical_speed}\n" +
            f"                           fireModes = {self.fire_modes}\n" +
            f"                                 rpm = {self.rpm}\n" +
            f"                          dispersion = {self.dispersion}\n" +
            f"                          timeToLive = {self.time_to_live}\n" +
            f"                         airFriction = {self.airFriction}\n" +
            f"                     sideAirFriction = {self.side_air_friction}\n" +
            f"                             caliber = {self.caliber}\n" +
            f"                         penetration = {self.penetration}\n" +
            f"                           hitRanges = {self.hit_ranges}\n" +
            f"                           hitValues = {self.hit_values}\n" +
            f"                          cmImmunity = {self.cm_immunity}\n" +
            f"                              thrust = {self.thrust}\n" +
            f"                          thrustTime = {self.thrust_time}\n" +
            f"                            maxSpeed = {self.max_speed}\n" +
            f"                        controlRange = {self.control_range}\n" +
            f"                      trackOversteer = {self.track_oversteer}\n" +
            f"                           trackLead = {self.track_lead}\n" +
            f"                            lockType = {self.lock_type}\n" +
            f"                       manualControl = {self.manual_control}\n" +
            f"                      maneuvrability = {self.maneuvrability}\n" +
            f"                    weaponlocksystem = {self.weapon_lock_system}\n" +
            f"                       eventhandlers = {self.eventhandlers}\n" +
            f"                      flightProfiles = {self.flight_profiles}\n" +
            f"                             canLock = {self.can_lock}\n" +
            f"                              irLock = {self.ir_lock}\n" +
            f"            missileManualControlCone = {self.missile_manual_control_cone}\n" +
            f"                        fuseDistance = {self.fuze_distance}\n" +
            f"                           explosive = {self.explosive}\n" +
            f"                     missileLockCone = {self.missile_lock_cone}\n" +
            f"               missileKeepLockedCone = {self.missile_keep_locked_cone}\n" +
            f"              missileLockMaxDistance = {self.missile_lock_max_distance}\n" +
            f"                 missileLockMaxSpeed = {self.missile_lock_max_speed}\n" +
            f"                             warhead = {self.warhead}\n" +
            f"                        rhsGuideMode = {self.rhs_guide_mode}\n" +
            f"                           rhsSaclos = {self.rhs_saclos}\n" +
            f"                    rhsBallisticMode = {self.rhs_ballistic_mode}\n" +
            f"                  missileUseMaxSpeed = {self.missile_use_max_speed}\n" +
            f"                      hasSubmunition = {self.has_submunition}\n" +
            f"                        submunitions = {self.submunitions}\n" +
            f"                   submunitionsNames = {self.submunitions_names}\n" +
            f"            submunitionsSubmunitions = {self.submunitions_submunitions}\n" +
            f"              submunitionSpawnChance = {self.submunition_spawn_chance}\n" +
            f"                      submunitionHit = {self.submunition_hit}\n" +
            f"             submunitionExplosiveHit = {self.submunition_explosive_hit}\n" +
            f"                submunitionExplosive = {self.submunition_explosive}\n" +
            f"              submunitionIndirectHit = {self.submunition_indirect_hit}\n" +
            f"         submunitionIndirectHitRange = {self.submunition_indirect_hit_range}\n" +
            f"             submunitionInitialSpeed = {self.submunition_initial_speed}\n" +
            f"             submunitionTypicalSpeed = {self.submunition_typical_speed}\n" +
            f"                  submunitionCaliber = {self.submunition_caliber}\n" +
            f"       submunitionSubmunitionCaliber = {self.submunition_submunition_caliber}\n" +
            f"              submunitionPenetration = {self.submunition_penetration}\n" +
            f"          submunitionParentSpeedCoef = {self.submunition_parent_speed_coef}\n" +
            f"          submunitionTriggerOnImpact = {self.submunition_trigger_on_impact}\n" +
            f"submunitionDeleteParentWhenTriggered = {self.submunition_delete_parent_when_triggered}\n" +
            f"         submunitionTriggerSpeedCoef = {self.submunition_trigger_speed_coef}\n" +
            f"                submunitionShotCount = {self.submunition_shot_count}\n" +
            f"              submunitionTriggerTime = {self.submunition_trigger_time}\n" +
            f"               submunitionTimeToLive = {self.submunition_time_to_live}\n" +
            f"              submunitionAirFriction = {self.submunition_air_friction}\n" +
            f"          submunitionSideAirFriction = {self.submunition_side_air_friction}\n" +
            f"                submunitionHitValues = {self.submunition_hit_values}\n" +
            f"            submunitionInitialOffset = {self.submunition_initial_offset}\n" +
            f"                  submunitionWarhead = {self.submunition_warhead}\n" +
            f"                     submunitionCone = {self.submunition_cone}\n"
        )


class ArmaArmourClass(ArmaSharedProperties):
    def __init__(self, armour_mod, config_type, armour):
        # Get script directory for dict path
        cwd = os.getcwd()

        # Import armour dict
        spec = importlib.util.spec_from_file_location(armour,
                                                      f"{cwd}/SQF-Class-Exports/{armour_mod}/{config_type}/{armour}.py")
        self.armour_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.armour_module)

        # Init variables
        self.loadout_title = ""
        self.allowed_facewear = []
        self.general_macro = ""
        self.description_short = ""
        self.type = 0
        self.access = 0
        self.value = 0

        self.armourHitpoints = []
        self.armourParameters = []

    def get_general_macro(self):
        try:
            self.general_macro = self.armour_module.d["_generalmacro"]
        except KeyError:
            pass

    def get_description_short(self):
        try:
            self.description_short = self.armour_module.d["descriptionshort"]
        except KeyError:
            pass

    def get_type(self):
        try:
            self.type = self.armour_module.d["type"]
        except KeyError:
            pass

    def get_access(self):
        try:
            self.access = self.armour_module.d["access"]
        except KeyError:
            pass

    def get_value(self):
        try:
            self.value = self.armour_module.d["value"]
        except KeyError:
            pass

    def get_allowed_facewear(self):
        try:
            self.allowed_facewear = self.armour_module.d["allowedfacewear"]
        except KeyError:
            pass

    def get_armour_stats(self):
        self.get_display_name(self.armour_module)
        self.get_item_info_mass(self.armour_module)
        self.get_item_info_hitpoints_protection_info(self.armour_module)
        self.get_item_info_allowed_slots(self.armour_module)
        self.get_item_info_general_macro(self.armour_module)
        self.get_item_info_model_sides(self.armour_module)
        self.get_item_info_type(self.armour_module)
        self.get_allowed_facewear()
        self.get_general_macro()
        self.get_description_short()
        self.get_type()
        self.get_access()
        self.get_value()

    def set_csv_export(self):
        armour_values = []
        for partIndex, part in enumerate(self.armourHitpoints):
            armour_values.append([])
            for param in self.armourParameters:
                try:
                    param_value = self.item_info_hitpoints_protection_info[part][param]
                    try:
                        if type(param_value) is str:
                            if int(param_value[0]):
                                sum_value = 0
                                temp_string = ""
                                for char in param_value.replace(" ", "").replace("\t", ""):
                                    if char != "+":
                                        temp_string += char
                                    else:
                                        sum_value += int(temp_string)
                                        temp_string = ""
                                sum_value += int(temp_string)
                                param_value = sum_value
                    except ValueError:
                        pass
                    armour_values[partIndex].append(param_value)
                except KeyError:
                    armour_values[partIndex].append(0)

        self.csv_export = [
            self.loadout_title,
            self.display_name,
            self.item_info_mass, ]
        for x in armour_values:
            self.csv_export.extend(x)
        self.csv_export.extend([
            self.item_info_allowed_slots,
            self.item_info_general_macro,
            self.item_info_model_sides,
            self.item_info_type,
            self.allowed_facewear,
            self.general_macro,
            self.description_short,
            self.type,
            self.access,
            self.value,
        ])

    def print_stats(self):
        print((
            f"           LoadoutTitle: {self.loadout_title}\n"
            f"                   Name: {self.display_name}\n"
            f"                   Mass: {self.item_info_mass}\n"
            f"HitPointsProtectionInfo: {self.item_info_hitpoints_protection_info}\n"
            f"           AllowedSlots: {self.item_info_allowed_slots}\n"
            f"        II_GeneralMacro: {self.item_info_general_macro}\n"
            f"             ModelSides: {self.item_info_model_sides}\n"
            f"                 IIType: {self.item_info_type}\n"
            f"        AllowedFacewear: {self.allowed_facewear}\n"
            f"          _GeneralMacro: {self.general_macro}\n"
            f"       DescriptionShort: {self.description_short}\n"
            f"                   Type: {self.type}\n"
            f"                 Access: {self.access}\n"
            f"                  Value: {self.value}\n"
        ))


class ArmaSharedVehicleClass(ArmaSharedProperties):
    def __init__(self, config_mod, vehicle):
        # Get script directory for dict path
        cwd = os.getcwd()

        # Import vehicle dict
        spec = importlib.util.spec_from_file_location(vehicle,
                                                      f"{cwd}/SQF-Class-Exports/{config_mod}/Vehicles/{vehicle}.py")
        self.vehicleModule = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.vehicleModule)

        # TODO: Chkeck all paramaters aginst the wiki
        #  to check usefulness
        # Init variables
        self.max_speed = 0
        self.fuel_capacity = 0
        self.simulation = ""
        self.vehicle_class = ""
        self.crew = ""
        self.category = ""
        self.destr_type = ""
        self.driver_optics_model = ""
        self.get_in_radius = 0
        self.normal_speed_forward_coef = 0.0
        self.slowSpeedForwardCoef = 0.0

        self.gunnerHasFlares = 0
        self.enableManualFire = 0
        self.fuelConsumptionRate = 0.0
        self.cameraSmoothSpeed = 0
        self.allowTabLock = 0
        self.fireReistiance = 0
        self.cargeoCanEject = 0
        self.driverCanEject = 0

        # Wheels
        self.numberPhysicalWheels = 0
        self.wheelDamageThreshold = 0.0
        self.wheelDestroyThreshold = 0.0
        self.wheelDamageRadiusCoef = 0.0
        self.wheelDestroyRadiusCoef = 0.0

        # Water
        self.waterResistance = 0
        self.waterDamageEngine = 0.0
        self.maxFordingDepth = 0.0
        self.waterLeakiness = 0
        self.canFloat = 0
        self.waterLinearDampingCoefX = 0
        self.waterLinearDampingCoefY = 0
        self.waterAngularDampingCoef = 0

        self.armor = 0
        self.armorStructural = 0
        self.explosionShielding = 0
        self.crewExplosionProtection = 0
        self.minTotalDamageThreshold = 0.0
        self.mapSize = 0.0
        self.brakeIdleSpeed = 0.0
        self.waterReistanceCoef = 0.0
        self.dampingRateFullThrottle = 0.0
        self.epe_impulse_damage_coef = 0
        self.inside_coef = 0.0
        self.outside_sound_filter = 0
        self.turn_coef = 0
        self.crew_crash_protection = 0.0
        self.secondary_explosion = 0
        self.fuel_explosion_power = 0
        # TODO Look at BiWiki to see case of parameters
        self.enable_gps = 0

        self.night_vision = 0
        self.occlude_sounds_when_in = 0.0
        self.obstruct_sounds_when_in = 0.0
        self.cargo_compartments = []
        self.air_capacity = 0  # Determines the time the crew inside the ship can be below the surface before dying suffocated for lack of air
        self.min_g_force = 0.0
        self.max_g_force = 0
        self.g_force_shake_attenuation = 0.0

        self.accel_aid_force_coef = 0.0
        self.accel_aid_force_offset = 0.0
        self.accel_aid_force_spd = 0.0
        self.maximum_load = 0
        self.body_friction_coef = 0.0
        self.hull_damage_cause_explosion = 0

        # Init turret/driver/optics variables
        # Refer to List-Vehicles-That-Have-Given-Weapon.py
        self.weapons = []  # List of weapons for the driver/array of all turrets+driver?
        self.magazines = []  # List of weapons for the driver
        # NOTE Maybe use a class for all vehicle turrets as they are 
        #  universal across all vehicle types
        self.turrets = []  # List of dict paths?
        self.view_optics = {}  # Driver optics


class ArmaSharedGroundVehicleClass(ArmaSharedVehicleClass):
    def __init__(self, config_mod, vehicle):
        super().__init__(config_mod, vehicle)

        # Init Variables
        self.rhsDukeType = ""
        self.engineStartSpeed = 0.0
        self.gearbox = []
        self.torqueCurve = []
        self.peakTorque = 0
        self.engineMoi = 0
        self.enginePower = 0


class ArmaTankVehicleClass(ArmaSharedGroundVehicleClass):
    def __init__(self, config_mod, vehicle):
        # Pass to ArmaSharedVehicleClass for init
        super().__init__(config_mod, vehicle)

        # Init variables
        self.tankTurnForce = 0
        self.tankTurnForceAngMinSpd = 0.0
        self.tankTurnForceAngSpd = 0.0

        # Do other stuff


class ArmaHelicopterVehicleClass(ArmaSharedVehicleClass):
    def __init__(self, config_mod, vehicle):
        # Pass to ArmaSharedVehicleClass
        super().__init__(config_mod, vehicle)

        # init variables
        self.tail_blade_vertical = 0
        self.lift_force_coef = 0


class ArmaPlaneVehicleClass(ArmaSharedVehicleClass):
    def __init__(self, config_mod, vehicle):
        # Pass to ArmaSharedVehicleClass
        super().__init__(config_mod, vehicle)

        # Init variables
