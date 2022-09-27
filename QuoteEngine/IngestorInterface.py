"""
IngestorInterface for creating the abstract class.

Individual implementations are: CSV, DOCX, PDF and TXT Ingestors
"""
from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import Quote


class IngestorInterface(ABC):
    """
    IngestorInterface abstract class object.

    Individual implementations are: CSV, DOCX, PDF and TXT Ingestors
    """

    allowed_extensions = []

    @classmethod
    def get_ext(cls, path: str) -> str:
        """
        Get full path and return extension.

        args: path to files
        returns: extension
        """
        return path.split(".")[-1]

    @classmethod
    def path_response(cls, path: str) -> None:
        """
        Get full path and return error if incorrect file extension.

        args: path to files
        returns: (None) error message if incorrect file type
        """
        if not cls.can_ingest(path):
            raise ValueError(f'incorrect extension: {cls.get_ext(path)}')

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Get full path and return T/F for file extension.

        args: path to files
        returns: TRUE/FALSE
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        """
        Abstract method for populating a list of quote objects.

        Implemented in individual parsers
        args: path to files
        returns: List of Quote objects
        """
        pass
