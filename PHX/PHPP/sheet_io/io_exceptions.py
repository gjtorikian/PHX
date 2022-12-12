# -*- coding: utf-8 -*-
# -*- Python Version: 3.7 -*-

"""Exceptions used by the IO classes."""


class FindSectionMarkerException(Exception):
    def __init__(self, search_string, _sheet_name, _col_letter):
        """Raises when the IO controller cannot find the reference marker in a column."""
        self.msg = (
            f"\n\tError: Cannot find the the marker: '{search_string}' "
            f"in the worksheet '{_sheet_name}' column '{_col_letter}'?"
        )
        super().__init__(self.msg)


class PerReferenceAreaException(Exception):
    def __init__(self, _sheet_name, _search_address):
        """Raises when the PER reference area (TFA / Footprint) is missing."""
        self.msg = (
            f"\n\tError: Cannot find the the reference area on '{_sheet_name}' "
            f"worksheet at location '{_search_address}'?"
        )
        super().__init__(self.msg)
