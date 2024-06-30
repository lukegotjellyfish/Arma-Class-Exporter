from ExportProperties import ExportProperties

class Arma(ExportProperties):
    def __init__(self, _module_name, _module_path):
        """
        :param _module_name: dict/class name
        :param _module_path: complete file path to dict file
        """
        # Send the module details to the super class
        super().__init__(_module_name, _module_path)

        properties_mapping = {
            "display_name": "displayname",
            "model": "model",
            "scope": "scope",
            "eventhandlers": "eventhandlers",
            # "item_info_type": ["iteminfo", "type"],
            # "item_info_mass": ["iteminfo", "mass"],
            # "item_info_hitpoints_protection_info": ["iteminfo", "hitpointsprotectioninfo"],
            # "item_info_allowed_slots": ["iteminfo", "allowedslots"],
            # "item_info_general_macro": ["iteminfo", "_generalmacro"],
            # "item_info_model_sides": ["iteminfo", "modelsides"],
        }
        self.load_properties(properties_mapping)