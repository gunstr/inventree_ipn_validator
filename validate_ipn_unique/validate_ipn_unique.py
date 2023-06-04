"""Plugin which validates IPN and Revision uniqueness"""

from django.core.exceptions import ValidationError

from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, ValidationMixin

from part.models import Part # This is an internal InvenTree API, not guaranteed to be stable.


class IpnValidationMixin(SettingsMixin, ValidationMixin, InvenTreePlugin):
    """A sample plugin class for demonstrating custom validation functions.

    Simple of examples of custom validator code.
    """

    NAME = "ValidateUniqueIPN"
    SLUG = "ipn_validator"
    TITLE = "IPN Validator Plugin"
    DESCRIPTION = "Validates that IP + Revision is unique"
    VERSION = "0.1"
    AUTHOR = "Gunnar Strömme"

    def validate_part_ipn(self, ipn: str, part):
        """Validate part IPN

        The combination ipn and part.revision has to be unique.
        """
        
        if Part.objects.exclude(pk=part.pk).filter(revision=part.revision, IPN=ipn).exists(): 
             raise ValidationError("Part with this IPN and Revision already exists.") 