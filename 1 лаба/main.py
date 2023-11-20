from PIL import Image, ImageDraw


def main():
    img1 = Image.open("photo1.jpg")
    img1 = img1.convert(mode="1")
    img1 = img1.transpose(Image.FLIP_TOP_BOTTOM)
    img1.show()

    img2 = Image.open("photo2.jpg")
    img2 = img2.resize((img2.width // 3, img2.height // 3))
    img22 = ImageDraw.Draw(img2)
    img22.rectangle((0, 0, img2.width-1, img2.height-1))
    img2.show()

    img3 = Image.open("photo3.jpg").convert("RGB")
    width = img3.width
    height = img3.height
    for i in range(width):
        for j in range(height):
            r, g, b = img3.getpixel((i, j))
            if r == 0 and g == 146 and b == 71:
                img3.putpixel((i, j), (0, 0, 0))
    img3.show()


main()