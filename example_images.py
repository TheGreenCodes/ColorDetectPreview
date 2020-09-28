from colordetect import ColorDetect

user_image = ColorDetect('media/random_balls.jpg')

user_image.get_color_count()

# write color count
user_image.write_color_count()

user_image.save_image('media', 'processed.jpg')