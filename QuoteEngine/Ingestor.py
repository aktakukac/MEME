"""
Ingestor capable of ingesting multiple filetypes.

Ingestors are implementation for different file types
"""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import Quote
from .IngestorCSV import IngestorCSV
from .IngestorDOCX import IngestorDOCX
from .IngestorTXT import IngestorTXT
from .IngestorPDF import IngestorPDF


class Ingestor(IngestorInterface):
    """
    Ingestor class object capable of ingesting multiple filetypes.

    Ingestors strategic objects are implementation for different file types
    """

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """
        Parse file and return a list of quote objects.

        args: path to files
        returns: a list of quotes
        """
        ingestors = [IngestorCSV, IngestorTXT, IngestorDOCX, IngestorPDF]

        for ingestor in ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise ValueError(
            f'incorrect extension: {cls.get_ext(path)}'
        )
