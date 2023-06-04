# inventree_ipn_validator

This is a plugin for [InvenTree](https://inventree.org/) that allows duplicated IPNs but only in combination with unique R-states.

## Installation

Copy the `validate_ipn_unique`folder to the local plugin directory `src/InvenTree/plugins/`, the plugin will then automatically be discovered (only this method has been tested). For more info about plugin installation see the [inventree plugin documentation](https://docs.inventree.org/en/latest/extend/plugins/install/). 

Set the PART_ALLOW_DUPLICATE_IPN to true for the core system and enable the plugin. There are no settings for the plugin itself.

## How it works

In the core functionality if PART_ALLOW_DUPLICATE_IPN is set to true there is no validation of the IPN and if it is set to false the IPN always has to be unique.

This plugin allows having some parts without revision requiring unique IPN and others where the same IPN could have different revisions. When the plugin is enabled it will validate that the combination of IPN and revision is always unique.
