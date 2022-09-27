"""
CSV Ingestor capable of ingesting .csv extension files.

Feeds into Ingestor
"""
from typing import List
import pandas as pd

from .QuoteModel import Quote
from .IngestorInterface import IngestorInterface


class IngestorCSV(IngestorInterface):
    """
    CSV Ingestor class object capable of ingesting .csv extension files.

    Feeds into Ingestor
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """
        Parse file and return a list of quote objects.

        args: path to files
        returns: a list of quotes
        """
        cls.path_response(path)

        quotes = []

        dt = pd.read_csv(path)

        for index, row in dt.iterrows():
            quote = Quote(row['body'], row['author'])
            quotes.append(quote)

        return quotes
