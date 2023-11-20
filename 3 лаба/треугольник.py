from PIL import Image, ImageDraw

image = Image.new('RGB', (400, 400), 'white')
draw = ImageDraw.Draw(image)

triangle = [(200, 100), (100, 300), (300, 300)]

draw.polygon(triangle, fill='black')

x0 = sum(x for x, _ in triangle) / 3
y0 = sum(y for _, y in triangle) / 3

rotated_triangle = [(int((x - x0) * 0 - (y - y0) * 1 + x0), int((x - x0) * 1 + (y - y0) * 0 + y0)) for x, y in triangle]

draw.polygon(rotated_triangle, fill='yellow')

image.save('треугольникк.png')