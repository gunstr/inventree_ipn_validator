"""A plugin validating the combination of IPN and Revision uniqueness"""

from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, ValidationMixin
from part.models import Part

from django.core.exceptions import ValidationError

from . import PLUGIN_VERSION


class IPNValidator(SettingsMixin, ValidationMixin, InvenTreePlugin):

    """IPNValidator - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "IPN Validator"
    NAME = "IPNValidator"
    SLUG = "ipn-validator"
    DESCRIPTION = "A plugin validating the combination of IPN and Revision uniqueness"
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "gunstr"
    WEBSITE = "https://github.com/gunstr/inventree_ipn_validator"
    LICENSE = "MIT"

    # Optionally specify supported InvenTree versions
    # MIN_VERSION = '0.18.0'
    # MAX_VERSION = '2.0.0'

    
    
    
    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/settings/
    # SETTINGS = {
    #     # Define your plugin settings here...
    #     'CUSTOM_VALUE': {
    #         'name': 'Custom Value',
    #         'description': 'A custom value',
    #         'validator': int,
    #         'default': 42,
    #     }
    # }

    def validate_part_ipn(self, ipn: str, part):
        """Validate part IPN

        The combination ipn and part.revision has to be unique.
        """
        
        if Part.objects.exclude(pk=part.pk).filter(revision=part.revision, IPN=ipn).exists(): 
             raise ValidationError("Part with this IPN and Revision already exists.") 