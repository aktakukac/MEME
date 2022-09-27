"""Module for creating a meme."""
from msilib.schema import Error
from PIL import Image, ImageFont, ImageDraw
import os
from random import randint


class MemeEngine:
    """Module for creating a meme."""

    def __init__(self, output_dir: str):
        """
        Create a new meme engine.

        param img_dir: path to save the memes
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Generate a new meme.

        param img_path: path to the image
        param text: text of the meme
        param author: author of the meme
        param width: width of the image
        return: path to the created meme
        """
        allowed_extensions = ['jpg', 'png']

        ext = img_path.split('.')[-1].lower()

        if ext not in allowed_extensions:
            raise ValueError(f'file type with extension {ext} not valid')

        if width > 500:
            raise ValueError(f'image cannot be bigger than 500px')

        with Image.open(img_path) as im:

            im = self.image_resize(im, width)

            im = self.image_text(im, text, author)

            filename = f'meme_{randint(1, 10000)}.{ext}'
            img_outpath = os.path.join(self.output_dir, filename)

            im.save(img_outpath)

        return img_outpath

    @staticmethod
    def image_resize(im: Image.Image, width: int) -> Image.Image:
        """
        Resize images with a static method with original aspect ratio.

        param im: PIL image object
        param width: new width

        return: resized PIL image object
        """
        original_width = im.size[0]
        original_height = im.size[1]
        aspect_ratio = original_width / original_height
        height = int(round(width / aspect_ratio))
        im = im.resize((width, height))
        return im

    def image_text(self, im: Image.Image, quote: str, author: str,
                   quote_fnt: str = './_data/Fonts/OpenSans-Regular.ttf',
                   qoute_fnt_size: int = 30,
                   author_fnt: str = './_data/Fonts/OpenSans-Regular.ttf',
                   author_fnt_size: int = 20) -> Image.Image:
        """
        Add a quote to an image at random location.

        param im: PIL image object
        param quote: quote text
        param author: author text
        param quote_fnt: quote font type
        param quote_fnt_size: quote font size
        param author_fnt: author font type
        param author_fnt_size: author font size

        return: resized PIL image object
        """
        fnt_q = ImageFont.truetype(quote_fnt, qoute_fnt_size)
        fnt_a = ImageFont.truetype(author_fnt, author_fnt_size)

        draw = ImageDraw.Draw(im)

        quote_lenght = int(draw.textlength(quote, font=fnt_q))

        quote_x = randint(20, im.size[0] - quote_lenght)
        quote_y = randint(20, im.size[1] - (2 * qoute_fnt_size + 10))

        author_x = quote_x
        author_y = quote_y + qoute_fnt_size + 10

        draw.text((quote_x, quote_y), quote, font=fnt_q)
        draw.text((author_x, author_y), author, font=fnt_a)

        return im
