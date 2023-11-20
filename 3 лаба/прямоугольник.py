from PIL import Image, ImageDraw

image = Image.new('RGB', (1000, 1000), 'white')
draw = ImageDraw.Draw(image)

rectangle = [(300, 100), (500, 200)]

draw.rectangle(rectangle, fill='black')

x0 = (rectangle[0][0] + rectangle[1][0]) / 2
y0 = (rectangle[0][1] + rectangle[1][1]) / 2

rotated_rectangle = [
    (int((x - x0) * 0 - (y - y0) * 1 + x0), int((x - x0) * 1 + (y - y0) * 0 + y0))
    for x, y in rectangle
]

draw.polygon(rotated_rectangle, fill='yellow')

image.save('прямоугольникк.png')

