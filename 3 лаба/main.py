from PIL import Image, ImageDraw

# Пустой желтый фон.
im = Image.new('RGB', (5000, 5000), (0, 187, 51))
draw = ImageDraw.Draw(im)

# ракета
draw.rectangle((300, 100, 500, 200), fill='blue')
draw.rectangle((100, 50, 300, 250), fill='red')
draw.polygon(((500, 100), (500, 200), (700, 150)), fill="yellow")
draw.polygon(((100, 0), (100, 50), (200, 50)), fill="yellow")
draw.polygon(((100, 300), (200, 250), (100, 250)), fill="grey")

# много ракет
lvl = 500
for i in range(4):
    draw.rectangle((300, 100 + lvl, 500, 200 + lvl), fill='blue')
    draw.rectangle((100, 50 + lvl, 300, 250 + lvl), fill='red')
    draw.polygon(((500, 100 + lvl), (500, 200 + lvl), (700, 150 + lvl)), fill="yellow")
    draw.polygon(((100, 0 + lvl), (100, 50 + lvl), (200, 50 + lvl)), fill="yellow")
    draw.polygon(((100, 300 + lvl), (200, 250 + lvl), (100, 250 + lvl)), fill="grey")
    lvl += 500

# космическая ракета

tr1 = [(1500, 600), (1500, 700), (1700, 650)]
x0 = sum(x for x, _ in tr1) / 3
y0 = sum(y for _, y in tr1) / 3
rotated_tr1 = [(int((x - x0) * 0 - (y - y0) * 1 + x0), int((x - x0) * 1 + (y - y0) * 0 + y0)) for x, y in tr1]
draw.polygon(rotated_tr1, fill='yellow')

tr2 = ((1100, 500), (1100, 550), (1200, 550))
x0 = sum(x for x, _ in tr2) / 3
y0 = sum(y for _, y in tr2) / 3
rotated_tr2 = [(int((x - x0) * 0 - (y - y0) * 1 + x0), int((x - x0) * 1 + (y - y0) * 0 + y0)) for x, y in tr2]
draw.polygon(rotated_tr2, fill='yellow')

tr3 = ((1100, 800), (1200, 750), (1100, 750))
x0 = sum(x for x, _ in tr3) / 3
y0 = sum(y for _, y in tr3) / 3
rotated_tr3 = [(int((x - x0) * 0 - (y - y0) * 1 + x0), int((x - x0) * 1 + (y - y0) * 0 + y0)) for x, y in tr3]
draw.polygon(rotated_tr3, fill='grey')

pr1 = [(1300, 600), (1500, 700)]
x0 = (pr1[0][0] + pr1[1][0]) / 2
y0 = (pr1[0][1] + pr1[1][1]) / 2
rotated_pr1 = [
    (int((x - x0) * 0 - (y - y0) * 1 + x0), int((x - x0) * 1 + (y - y0) * 0 + y0))
    for x, y in pr1
]
draw.polygon(rotated_pr1, fill='blue')

pr2 = [(1100, 550), (1300, 750)]
x0 = (pr2[0][0] + pr2[1][0]) / 2
y0 = (pr2[0][1] + pr2[1][1]) / 2
rotated_pr2 = [
    (int((x - x0) * 0 - (y - y0) * 1 + x0), int((x - x0) * 1 + (y - y0) * 0 + y0))
    for x, y in pr2
]
draw.polygon(rotated_pr2, fill='red')



im.save('result.jpg', quality=95)

