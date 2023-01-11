#!/usr/bin/python3
"""MyInt inherits from int
"""


class MyInt(int):
    """Invert:
             ==,
             !=.
    """

    def __eq__(self, value):
        """Overide the '==' operator
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """Overide the '!=' operator
        """
        return super().__eq__(value)
