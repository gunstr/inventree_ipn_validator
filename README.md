# IPNValidator

A plugin validating the combination of IPN and Revision uniqueness

## Installation

### InvenTree Plugin Manager

... todo ...

### Command Line 

To install manually via the command line, with the venv activated run the following command:

```bash
pip install git+https://github.com/gunstr/inventree_ipn_validator.git
```

## Configuration

Set the 'PART_ALLOW_DUPLICATE_IPN' to true for the core system and enable the plugin. There are currently no settings for the plugin itself.

## Usage

In the core functionality if 'PART_ALLOW_DUPLICATE_IPN' is set to true there is no validation of the IPN and if it is set to false the IPN always has to be unique.

This plugin allows having some parts without revision requiring unique IPN and others where the same IPN could have different revisions. When the plugin is enabled it will validate that the combination of IPN and revision is always unique.
