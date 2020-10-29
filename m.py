from niceposter import Create

im = Create.Poster() 
im.add_image('sky.jpg', scale='cover', position='tr')
im.frame()
im.square(position='cc')
im.text('Hello, World!', color='black', position='cc')


