# -*- coding: utf-8 -*-
import contextlib
import importlib.util
import math
import os
import rich
from decimal import Decimal
from json import dumps


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



class ArmaWeaponClass(ArmaWeaponSharedProperties):
    def __init__(self, weapon_mod, magazine_mod, weapon, mag,
                 hit_formatting, hit_values_formatting, submunition_hit_values_formatting,
                 dispersion_formatting, air_friction_formatting, rpm_formatting,
                 penetration_formatting, submunition_penetration_formatting, hit_ranges):
        super().__init__(weapon_mod, magazine_mod, weapon, mag,
                         hit_formatting, hit_values_formatting, submunition_hit_values_formatting,
                         dispersion_formatting, air_friction_formatting, rpm_formatting,
                         penetration_formatting, submunition_penetration_formatting, hit_ranges)

        # If the magazine has ammo
        if self.ammo_flag:
            # Determine if the projectile has submunitions here
            try:
                # Check to see if there is one submunition
                # print(f"weapon: {self.weapon_class}|{self.magazine_class}")
                submunition_check = self.magazine_module.d["ammo"]["submunitionammo"]
                if submunition_check:
                    self.submunitions.append("submunitionammo")
                    self.submunitions_names.append(self.magazine_module.d["ammo"]["submunitionammo"]["_dictAmmoName"])
                    self.has_submunition = 1
                self.get_warheads()
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
        if self.ammo_flag:
            if cartridge == 1:
                self.get_cartridge()
            if time_to_live == 1:
                self.get_time_to_live()
        if capacity == 1:
            self.get_capacity()
        if self.ammo_flag:
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
                           (f"{{:.{self.hit_formatting}f}}").format(self.hit),self.warhead,
                           '|'.join(self.fire_modes), self.rpm, self.dispersion, self.time_to_live,
                           self.initial_speed, self.typical_speed, self.weapon_initial_speed,
                           self.airFriction, self.penetration[0], self.penetration[1], self.penetration[2]]
        self.csv_export.extend(self.hit_values)
        try:
            shot_mass = round(self.magazine_mass / self.capacity, self.hit_formatting)
        except ZeroDivisionError:
            shot_mass = 0
        self.csv_export.extend([self.weapon_class, self.magazine_class, self.weapon_scope, self.magazine_scope, self.weapon_mass, self.magazine_mass, shot_mass, self.caliber])

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
            self.weapon_initial_speed,
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
        self.csv_export.extend([self.weapon_class, self.magazine_class, self.weapon_scope, self.magazine_scope, self.caliber,
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
            f"                    weapInitialSpeed = {self.weapon_initial_speed}\n" +
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
        self.allowed_facewear = []
        self.general_macro = ""
        self.description_short = ""
        self.type = 0
        self.access = 0
        self.value = 0

        self.armour_hitpoints = []
        self.armour_parameters = []

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
        for partIndex, part in enumerate(self.armour_hitpoints):
            armour_values.append([])
            for param in self.armour_parameters:
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
                    except ValueError as e:
                        # print(f"armour_values ValueError: {e}")
                        pass
                    armour_values[partIndex].append(param_value)
                except KeyError as e:
                    # print(f"armour_values KeyError: {e}")
                    armour_values[partIndex].append(0)
        # print(f"armour_values = {armour_values}")

        self.csv_export = [
            self.display_name,
            self.item_info_mass,
        ]
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
        spec = importlib.util.spec_from_file_location(vehicle,f"{cwd}/SQF-Class-Exports/{config_mod}/Vehicles/{vehicle}.py")
        self.vehicleModule = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.vehicleModule)

        # TODO: Check all paramaters aginst the wiki
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
