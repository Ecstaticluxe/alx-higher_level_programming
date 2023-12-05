#!/usr/bin/python3
'''Contains myInt class'''


class MyInt(int):
    '''MyInt is a rebel that has operands'''

    def __eq__(self, other):
        """Overrides the == operator."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Overrides the != operator."""
        return not super().__ne__(other)
