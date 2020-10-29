from PIL import Image, ImageFont, ImageDraw
import os

class Poster:
    def __init__(
        self, bg_img=None, base_size=None, bg_color=('RGB',(255, 255, 255)) , img_name='img.png'
    ):
        if bg_img == None:
            mode, color = bg_color
            if base_size == None:
                base_size = (500,500) # default value
            self.bg_img = Image.new(mode, base_size, color)
        else:
            if base_size == None:
                self.bg_img = Image.open(bg_img)
                base_size = self.bg_img.size
            else:
                self.bg_img = Image.open(bg_img).resize(base_size)
        self.add_to_poster = ImageDraw.Draw(self.bg_img)
        self.base_size = base_size
        self.max_width, self.max_height = base_size
        self.img_name = img_name
        self.bg_img.save(self.img_name)

    def filter(self, rgb, opacity=100):
        opacity = int(250 * (opacity/100))
        r, g, b = rgb
        bg_filter = Image.new('RGBA', self.base_size, (r, g, b, opacity))
        self.bg_img.paste(bg_filter, (0, 0), bg_filter.convert('RGBA'))
        self.bg_img.save(self.img_name)

    def frame(self, fill=None, thickness=5, outline=None):
        self.add_to_poster.rectangle(
            [(0, 0), (self.max_width, self.max_height)], fill, outline, thickness)
        self.bg_img.save(self.img_name)

    def add_image(self, img_name, position, move=(0,0), resize=None, scale=None, crop=None):
        img = Image.open(img_name)
        if resize != None:
            img = img.resize(resize, Image.ANTIALIAS)  
        if isinstance(crop, tuple):
            left, top, img_width, img_height = crop
            img = img.crop((left, top, left+img_width, top+img_height)) 
        image_width, image_height = img.size

        if scale != None:
            if scale == 'fit':
                img = img.resize((self.max_width, self.max_height), Image.BICUBIC)
            elif scale == 'cover':
                img = img.resize((self.max_height*image_width//image_height, self.max_height), Image.BICUBIC)
            elif isinstance(scale, int):
                scale = scale if scale > 0 and scale <= 100 else 100
                img = img.resize((int(image_width*(scale/100)), int(image_height*(scale/100))), Image.BICUBIC)
            image_width, image_height = img.size

        positions = {
            'tl':(0,0),
            'tc':((self.max_width - image_width)//2, 0),
            'tr':(self.max_width - image_width, 0),
            'cl':(0,(self.max_height - image_height)//2),
            'cc':((self.max_width - image_width)//2,(self.max_height - image_height)//2),
            'cr':(self.max_width - image_width, (self.max_height - image_height)//2),
            'bl':(0, self.max_height - image_height),
            'bc':((self.max_width - image_width)//2, self.max_height - image_height),
            'br':(self.max_width - image_width, self.max_height - image_height),
        }
        X, Y = positions.get(position, position)
        x, y = move
        self.bg_img.paste(img, (X+x, Y+y), img.convert('RGBA'))
        self.bg_img.save(self.img_name)

    def text(
        self, text, position, text_size=30, move=(0,0), color=None, 
        textbox_width=200, font_style=None, align='left', spacing=4, stroke_width=0
    ):
        lines = []
        if font_style == None:
            try:
                font = ImageFont.truetype('arial.ttf', text_size)
            except:
                font = ImageFont.load_default()
        else:
            font = ImageFont.truetype(font_style, text_size)
        if font.getsize(text)[0] <= textbox_width:
            lines.append(text)
        else:
            words = text.split(' ')
            i = 0
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= textbox_width:
                    line = line + words[i] + " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        wrappedText = '\n'.join(lines)
        width, height = self.add_to_poster.multiline_textsize(wrappedText, font=font)
        positions = {
            'tl':(0,0),
            'tc':((self.max_width - width)//2, 0),
            'tr':(self.max_width, 0),
            'cl':(0,(self.max_height - height)//2),
            'cc':((self.max_width - width)//2,(self.max_height - height)//2),
            'cr':(self.max_width, (self.max_height - height)//2),
            'bl':(0, self.max_height - height),
            'bc':((self.max_width - width)//2, self.max_height - height),
            'br':(self.max_width - width, self.max_height - height),
        }
        X, Y = positions.get(position, position)
        x, y = move
        self.add_to_poster.multiline_text((X+x, Y+y), wrappedText, fill=color, font=font, align=align, spacing=spacing,  stroke_width=stroke_width)
        self.bg_img.save(self.img_name)

    def square(self, size=(200, 200), rgb=(255, 255, 255), opacity=100, position='tl', move=(0,0)):
        x, y = move
        r, g, b = rgb
        opacity = int(250 * (opacity/100))
        sq = Image.new('RGBA', size, (r, g, b, opacity))
        width, height = sq.size
        positions = {
            'tl':(0,0),
            'tc':((self.max_width - width)//2, 0),
            'tr':(self.max_width, 0),
            'cl':(0,(self.max_height - height)//2),
            'cc':((self.max_width - width)//2,(self.max_height - height)//2),
            'cr':(self.max_width, (self.max_height - height)//2),
            'bl':(0, self.max_height - height),
            'bc':((self.max_width - width)//2, self.max_height - height),
            'br':(self.max_width - width, self.max_height - height),
        }
        selected_position = positions.get(position, (0,0))
        cx, cy = selected_position
        self.bg_img.paste(sq, (cx+x, cy+y), sq)
        self.bg_img.save(self.img_name)

    @property
    def size(self):
        return (self.max_width, self.max_height)





