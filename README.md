# PyEngine

# About
PyEngine is my attempt at making a game engine using python. Most of what is in it you can probably just do with pygame, but I'm doing it anyway Initially, this was just for me to test out using classes and class methods, but then I decided to make a game engin out of it. I might not finish this, and I dont really think that will be to big of a deal, I mean, the whole purpose of this originally was to get better at using classes, and it fufulled its purpose.

# License
You are free to use this in any way you like. You can use this to do whatever you like, you can use parts of it as you wish, you can sell things using this. If you get into legal trouble over what you make with this, I am not liable or responsible in any way. The only condition is that I'd like it if you gave credit were it is deserved.

# Version
### PyEngine ver. 0.1.1: March 3rd, 2021
- Added Screen class
	- Added \__init__
	- Added show_img, basically a fancy blit
	- Added draw_rect, basically a fancy pygame.draw.rect
	- Added set_bg, fills background with a solid color and if so chosen displays an image

### PyEngine ver. 0.2.1: March 4th, 2021
- Added Mouse class
	- Added \__init__
	- Added show_cursor, displays the cursor img at the location of the cursor
- Added bug.txt
- Added docs.txt, for better, more indepth explination of how things work

### PyEngine ver. 0.2.2: March 5th, 2021
- Redid Mouse.show_cursor

### PyEngine ver. 0.2.3: March 6th, 2021
- Fixed Mouse.show_cursor

### PyEngine ver 0.3.1: March 7th, 2021
- Added Button class
	- Added \__init__
	- Added show_button
	- Added set_img
- For Mouse class
	- Added set_cursor

### PyEngine ver 0.4.1: March 8th, 2021
- Added Entity class
	- Added \__init__
	- Added show_entity
	- Added set_pos
	- Added set_dim
	- Added grav_effect
	- Added jump
- Added Platform class
	- Added \__init__

### PyEngine ver 0.4.2 March 9th, 2021
- Got Entity.collide1 working, kind of.

### PyEngine ver 0.4.3 March 10th, 2021
- Tweaked self.grav_effect/self.collide1

### PyEngine ver 0.5.1 March 11th, 2021
- Removed Entity.grav
- Removed Entity.grav_effect
- Removed Entity.jump
- Made the engine more top down than side scroll
