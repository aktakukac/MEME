"""
TXT Ingestor capable of ingesting .txt extension files.

Feeds into Ingestor
"""
from typing import List

from .QuoteModel import Quote
from .IngestorInterface import IngestorInterface


class IngestorTXT(IngestorInterface):
    """
    TXT Ingestor class object capable of ingesting .txt extension files.

    Feeds into Ingestor
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """
        Parse file and return a list of quote objects.

        args: path to files
        returns: a list of quotes
        """
        cls.path_response(path)

        quotes = []

        with open(path) as f:
            for line in f.readlines():
                if len(line) > 0:
                    quote_body = line.split('-')[0]
                    quote_author = line.split('-')[1]
                    quote = Quote(quote_body.strip(), quote_author.strip())
                    quotes.append(quote)
        return quotes
