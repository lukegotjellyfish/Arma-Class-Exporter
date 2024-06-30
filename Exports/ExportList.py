# -*- coding: utf-8 -*-
import csv
import os


class ExportList:
    def __init__(self, mod, _list, cwd, csv_file=None, backup_folders=None):
        if backup_folders is None:
            backup_folders = []
        self.list = _list
        self.csv_file = csv_file
        self.mod = mod
        self.cwd = cwd
        self.backup_folders = backup_folders
        self.export_to_csv = False
        self.csv_writer = None
        self.scope = None
        self.csvHeader = None
        self.armour = None
        self.weapon = None
        self.vehicle_weapon = None

        # Init Values
        self.fov = 0.75  # Default Arma 3 FOV
        self.fov_round_digits = 3

        # Weapon Values
        self.hit_ranges = [100, 200, 300, 400, 500, 1000, 1500, 2000]

        # Armour Values
        self.armour_hitpoints = ["head", "neck", "chest", "body", "diaphragm", "abdomen"]
        self.armour_parameters = ["armor", "passthrough", "simulation"]

        # Other formatting values
        self.hit_formatting = 3
        self.hit_values_formatting = 3
        self.submunition_hit_values_formatting = 3
        self.dispersion_formatting = 7
        self.air_friction_formatting = 8
        self.rpm_formatting = 2
        self.penetration_formatting = 2
        self.submunition_penetration_formatting = 2
        self.disable_print = False

    def set_hit_ranges(self, hit_ranges):
        self.hit_ranges = hit_ranges

    def set_fov(self, fov, fov_round_digits):
        self.fov = fov
        self.fov_round_digits = fov_round_digits

    def set_number_formatting(self,
                              hit_formatting=3, hit_values_formatting=3, submunition_hit_values_formatting=3,
                              dispersion_formatting=7, air_friction_formatting=8, rpm_formatting=2,
                              penetration_formatting=2, submunition_penetration_formatting=2):
        self.hit_formatting = hit_formatting
        self.hit_values_formatting = hit_values_formatting
        self.submunition_hit_values_formatting = submunition_hit_values_formatting
        self.dispersion_formatting = dispersion_formatting
        self.air_friction_formatting = air_friction_formatting
        self.rpm_formatting = rpm_formatting
        self.penetration_formatting = penetration_formatting
        self.submunition_penetration_formatting = submunition_penetration_formatting

    def check_file_exists(self, name, _type):
        for folder in [*[self.mod], *self.backup_folders]:
            # If weapon dict file exists
            for configType in _type:
                if os.path.isfile(f"{self.cwd}/SQF-Class-Exports/{folder}/{configType}/{name}.py"):
                    return [folder, configType]
        print(
            f"\33[31m{name} could not be found in {[*[self.mod], *self.backup_folders]} with configType(s) {_type}\33[0m")
        return False

    def export_list(self, _type, write_to_csv=True):
        self.export_to_csv = (self.csv_file != "") or (write_to_csv == True)
        if self.export_to_csv:
            self.csv_file.truncate(0)
            self.csv_writer = csv.writer(self.csv_file, delimiter=',')

        if _type == "Weapon":
            # Import relevant class
            from ParseExports import ArmaWeaponClass

            if self.export_to_csv:
                self.csvHeader = [
                    "Name",  # Weapon Name
                    "Cartridge",  # Ammo Name
                    "Capacity",  # Magazine Capacity
                    "Damage",  # Shot Damage @ Initspeed
                    "Warhead",
                    "Fire Modes",  # Unique firemodes
                    "RPM",  # |- RPM for each firemode
                    "Dispersion",  # |- Dispersion for each firemode
                    "Time To Live",  # TimeToLive for fired shot
                    "Initial Speed",  # Shot initial speed
                    # Shot typical speed (damage falloff)
                    "Typical Speed",
                    "weaponInitialSpeed",  # initspeed modifier/override from weapon
                    # Shot air resistance (deceleration)
                    "Air Resistance",
                    # Shot penetration (against RHA/Concrete/Meat)
                    "RHA Penetration",
                    # Shot penetration (against RHA/Concrete/Meat)
                    "Concrete Penetration",
                    # Shot penetration (against RHA/Concrete/Meat)
                    "Meat Penetration",
                ]
                for x in range(len(self.hit_ranges)):
                    self.csvHeader.append(f"Damage at {self.hit_ranges[x]}m")
                self.csvHeader.extend(
                    ["Weapon Class", "Magazine Class", "Weapon Scope", "Magazine Scope", "Weapon Mass", "Magazine Mass", "Mass per Ammo", "Caliber"])
                self.csv_writer.writerow(self.csvHeader)
            for loadout in self.list:
                weapon_folder = self.check_file_exists(loadout[0], ["Weapons"])
                if weapon_folder:
                    magazine_folder = self.check_file_exists(loadout[1], ["Magazines"])
                    if magazine_folder:
                        self.weapon = ArmaWeaponClass(weapon_folder[0], magazine_folder[0], loadout[0], loadout[1],
                                                      self.hit_formatting, self.hit_values_formatting,
                                                      self.submunition_hit_values_formatting,
                                                      self.dispersion_formatting, self.air_friction_formatting,
                                                      self.rpm_formatting, self.penetration_formatting,
                                                      self.submunition_penetration_formatting, self.hit_ranges)
                        self.weapon.get_firearm_stats()

                        # If triggerTime is the lowest time possible, in almost all cases it will be the
                        # submunitions dealing damage
                        if self.weapon.submunition_trigger_time == 0.0001:
                            self.weapon.replace_normal_with_submunition_values()
                        self.weapon.set_csv_export()

                        if not self.disable_print:
                            self.weapon.print_stats()
                        if self.export_to_csv:
                            self.csv_writer.writerow(self.weapon.csv_export)
        elif _type == "Scope":
            # Import relevant class
            from ParseExports import ArmaScopeClass

            self.csvHeader = [
                "Name",
                "Scope Class",
                "Scope Mode 1",
                "Magnification Min",
                "Magnification Max",
                "Zero Min",
                "Zero Max",
                "Scope Mode 2",
                "Magnification Min",
                "Magnification Max",
                "Zero Min",
                "Zero Max",
                "Scope Mode 3",
                "Magnification Min",
                "Magnification Max",
                "Zero Min",
                "Zero Max",
                "Scope Mode 4",
                "Magnification Min",
                "Magnification Max",
                "Zero Min",
                "Zero Max",
                "Scope Mode 5",
                "Magnification Min",
                "Magnification Max",
                "Zero Min",
                "Zero Max",
            ]
            self.csv_writer.writerow(self.csvHeader)
            for _scope in self.list:
                scope_folder = self.check_file_exists(_scope, ["Weapons"])
                if scope_folder:
                    self.scope = ArmaScopeClass(scope_folder[0], _scope, self.fov, self.fov_round_digits)

                    is_scope = self.scope.get_scope_stats()
                    if is_scope:
                        if not self.disable_print:
                            self.scope.print_stats()
                        if (self.csv_file != "") and (write_to_csv == True):
                            self.scope.set_csv_export()
                            self.csv_writer.writerow(self.scope.csv_export)
        elif (_type == "Vehicle") or (_type == "Launcher"):  # Vehicle
            # Import relevant class
            from ParseExports import ArmaVehicleWeaponClass
            if self.export_to_csv:
                self.csvHeader = [
                    "Name",  # Weapon Name
                    "Cartridge",  # Ammo Name
                    "Capacity",  # Magazine Capacity
                    "Damage",  # Shot Damage @ Initspeed
                    "Indirect Damage",  # Shot Damage within range Indirect Range
                    # Range where Indrect Damage is applied without a multiplier
                    "Indirect Range",
                    "Submunition Damage",  #
                    "Submunition Indirect Damage",  #
                    "Submunition Indirect Range",  #
                    "Submunition",  #
                    "Sub-Submunition",  #
                    "Submunition Cone",  #
                    "Warhead",  #
                    "Submunition Warhead",
                    "Fire Modes",  # Unique Firemodes
                    "RPM",  # |- RPM for each firemode
                    "Dispersion",  # |- Dispersion for each firemode
                    "Time To Live",  # TimeToLive for fired shot
                    "Initial Speed",  # Shot initial speed
                    # Shot typical speed (damage falloff)
                    "Typical Speed",
                    "weaponInitialSpeed",  # initspeed modifier/override from weapon
                    # Shot air resistance (deceleration)
                    "Air Resistance",
                    "Side Air Resistance",  #
                    "Control Range",  #
                    "RHS Guide Mode",  #
                    "RHS Saclos",
                    "RHS Ballistic Mode",
                    "RHA Penetration (mm)",
                    "Concrete Penetration (mm)",
                    "Meat Penetration (mm)",
                    "Submunition RHA Penetration (mm)",
                    "Submunition Concrete Penetration (mm)",
                    "Submunition Meat Penetration (mm)",
                    "Thrust",  #
                    "Thrust Time",  #
                    "Max speed",  #
                    "Manoeuvrability",  #
                    "Track Oversteer",  #
                    "Track Lead",  #
                    "Control Cone",  #
                    "Flight Profiles",  #
                ]
                for x in range(len(self.hit_ranges)):
                    self.csvHeader.append(f"Damage at {self.hit_ranges[x]}m")
                self.csvHeader.extend(
                    ["Weapon Class", "Magazine Class", "Weapon Scope", "Magazine Scope", "Caliber", "Submunition Caliber", "Sub-submunition Caliber"])
                self.csv_writer.writerow(self.csvHeader)
            for loadout in self.list:
                # TODO Add feature to detect/pass argument specifying
                # a loadout as using the first submunition as the ammo,
                # like with the yakbu, gau8 or m1001 for the mk19
                # These weapons+magazines fire a CfgAmmo that almost immediately
                # splits up to form the actual munition that deals damage
                # m1001 has 0 hit on Ammo, submunitionHit totals at 224(56*4)
                # This will also should be indicated somehow on the CSV export
                weapon_folder = self.check_file_exists(loadout[0], ["Weapons"])
                if weapon_folder:
                    magazine_folder = self.check_file_exists(loadout[1], ["Magazines"])
                    if magazine_folder:
                        self.vehicle_weapon = ArmaVehicleWeaponClass(weapon_folder[0], magazine_folder[0], loadout[0],
                                                                     loadout[1],
                                                                     self.hit_formatting, self.hit_values_formatting,
                                                                     self.submunition_hit_values_formatting,
                                                                     self.dispersion_formatting,
                                                                     self.air_friction_formatting,
                                                                     self.rpm_formatting, self.penetration_formatting,
                                                                     self.submunition_penetration_formatting,
                                                                     self.hit_ranges)
                        self.vehicle_weapon.get_weapon_stats()
                        self.vehicle_weapon.set_csv_export()
                        if not self.disable_print:
                            self.vehicle_weapon.print_stats()
                        if (self.csv_file != "") and (write_to_csv == True):
                            self.csv_writer.writerow(
                                self.vehicle_weapon.csv_export)
                        else:
                            print(
                                f"Did not add (nocsvFile) {loadout[0]} - {loadout[1]}")

                        # if (loadout[0] == "rhs_weap_ags30"):
                        #     self.vehicleWeapon.printAllVariables()
                        #     input()
        elif _type == "Armour":
            # Import relevant class
            from ParseExports import ArmaArmourClass
            if self.export_to_csv:
                self.csvHeader = [
                    "Name",
                    "Mass", ]
                for x in self.armour_hitpoints:
                    for c in self.armour_parameters:
                        self.csvHeader.extend([f"{x.title()} {c.title()}"])
                self.csvHeader.extend([
                    "AllowedSlots",
                    "II_GeneralMacro",
                    "ModelSides",
                    "IIType",
                    "AllowedFacewear",
                    "_GeneralMacro",
                    "DescriptionShort",
                    "Type",
                    "Access",
                    "Value"
                ])
            self.csv_writer.writerow(self.csvHeader)

            #new
            for armour in self.list:
                armour_folder = self.check_file_exists(armour, ["Weapons", "Glasses"])
                if armour_folder:
                    self.armour = ArmaArmourClass(armour_folder[0], armour_folder[1], armour)
                    self.armour.armour_hitpoints = self.armour_hitpoints
                    self.armour.armour_parameters = self.armour_parameters
                    self.armour.get_armour_stats()
                    if not self.disable_print:
                        self.armour.print_stats()
                    if (self.csv_file != "") and (write_to_csv == True):
                        self.armour.set_csv_export()
                        self.csv_writer.writerow(self.armour.csv_export)

        else:
            print(f"{_type} not in [Weapon,Scope,Vehicle,Armour]")
            pass
