"""
Quote class holds the data specific for qoutes.

Attributes: body, author
"""


class Quote:
    """
    Quote class hold the data specific for qoutes.

    Attributes: body, author
    """

    def __init__(self, body, author):
        """
        Initiate the objects.

        Initiate with body and author
        """
        self.body = body.strip('"')
        self.author = author

    def __str__(self):
        """
        Represent the objects.

        String form with body and author
        """
        return f'"{self.body}" - {self.author}'
