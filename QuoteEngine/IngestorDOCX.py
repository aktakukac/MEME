"""
DOCX Ingestor capable of ingesting .docx extension files.

Feeds into Ingestor
"""
from typing import List
import docx

from .QuoteModel import Quote
from .IngestorInterface import IngestorInterface


class IngestorDOCX(IngestorInterface):
    """
    DOCX Ingestor class object capable of ingesting .csv extension files.

    Feeds into Ingestor
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """
        Parse file and return a list of quote objects.

        args: path to files
        returns: a list of quotes
        """
        cls.path_response(path)

        quotes = []

        doc = docx.Document(path)
        for parag in doc.paragraphs:
            if len(parag.text) > 0:
                quote_body = parag.text.split('-')[0]
                quote_author = parag.text.split('-')[1]
                quote = Quote(quote_body.strip(), quote_author.strip())
                quotes.append(quote)
        return quotes
