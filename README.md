<p align="center">
  <img src="https://raw.githubusercontent.com/amajai/niceposter/main/res/icon.png" width="180">
<p>

# Niceposter
  <p>
    <a href="https://github.com/python-pillow/Pillow">
      <img src="https://img.shields.io/badge/built%20with-Pillow-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
  </p>
A library that allows you to create your own image poster which you can use to share on social media. Implemented in Python using the PIL module.
</br>
<img src="https://raw.githubusercontent.com/amajai/niceposter/main/res/demo.gif">

## **Installation**
```elm
pip install niceposter
```
__Important:__ depending on your system, make sure to use `pip3` and `python3` instead.


**That's all! 🎉**   

>If you would like to install a specific version of Niceposter you may do so with:
>```elm
>pip install niceposter==0.1.1
>```
#### Using Niceposter

To start creating an image poster, you have to initialize it, like so: 
```python
from niceposter import Create

bg_image = Create.Poster() # default size of 500x500
```

Then use any one of the methods to make or add changes to an image. Examples:
```python
bg_image.add_image('cool-image.png', position='cc', scale=20)
bg_image.text('Interesting text!', position(50,50), color='red', align='center')
bg_image.frame(thickness=10)
bg_image.filter(rgb=(255,255,255), opacity=50)
```

#### Updating Niceposter
```elm
pip install niceposter -U
```
## Basic functions
[**In progress**]

## Features in progress
⬜ Add `add_shape` method option to provide variety of available shapes

⬜ Add image transformations options

⬜ Add image effects options

## Documentation
Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.


