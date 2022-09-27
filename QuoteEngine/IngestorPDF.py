"""
PDF Ingestor capable of ingesting .pdf extension files.

Feeds into Ingestor
"""
from typing import List
import subprocess
import os
from random import randint

from .QuoteModel import Quote
from .IngestorInterface import IngestorInterface


class IngestorPDF(IngestorInterface):
    """
    PDF Ingestor class object capable of ingesting .pdf extension files.

    Feeds into Ingestor
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """
        Parse file and return a list of quote objects.

        args: path to files
        returns: a list of quotes
        """
        cls.path_response(path)

        quotes = []

        tmp = f'{randint(0, 10000)}.txt'
        cmd = ['pdftotext', '-table', path, tmp]
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        with open(tmp) as f:
            for line in f.readlines():
                line = line.strip('\n').strip('\x0c')
                if len(line) > 0:
                    quote_body = line.split('-')[0]
                    quote_author = line.split('-')[1]
                    quote = Quote(quote_body.strip('" '), quote_author.strip())
                    quotes.append(quote)
        os.remove(tmp)
        return quotes
