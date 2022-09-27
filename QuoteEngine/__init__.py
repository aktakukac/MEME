"""
Initiation of the QuoteEngine module.

Ingestors are implementation for different file types
"""

from .IngestorCSV import IngestorCSV
from .IngestorPDF import IngestorPDF
from .IngestorDOCX import IngestorDOCX
from .IngestorTXT import IngestorTXT
from .Ingestor import Ingestor
from .QuoteModel import Quote
