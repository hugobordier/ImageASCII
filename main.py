from PIL import Image
from bcolors import bcolors

ASCII_CHARS = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / (2 * width)  # Times 2 because an ASCII character is twice as tall
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def getRGB(rgb):
    r, g, b = rgb
    luminance = 0.2989 * r + 0.5870 * g + 0.1140 * b

    if luminance < 150:
        if r > g and r > b:
            return bcolors.YELLOW
        elif g > r and g > b:
            return bcolors.GREEN
        elif b > r and b > g:
            return bcolors.BLUE
        elif abs(r - g) < 10 and abs(g - b) < 10:
            return bcolors.BLACK
        else:
            return bcolors.MAGENTA
    elif luminance < 230:
        if r > 200 and g > 200 and b < 100:
            return bcolors.LIGHT_YELLOW
        elif g > 200 and b > 200 and r < 100:
            return bcolors.CYAN
        elif b > 200 and r > 200 and g < 100:
            return bcolors.MAGENTA
        elif r > g and r > b:
            return bcolors.LIGHT_RED
        elif g > r and g > b:
            return bcolors.LIGHT_GREEN
        elif b > r and b > g:
            return bcolors.LIGHT_BLUE
        elif abs(r - g) < 10 and abs(g - b) < 10:
            return bcolors.LIGHT_WHITE
    return bcolors.WHITE




def grayscale_image(image):
    return image.convert("L")

def pixel_to_ascii(pixel_value, use_color=False):
    color_index = pixel_value // 25  # 255 / len(ASCII_CHARS) = 25
    ascii_char = ASCII_CHARS[color_index]

    
    return ascii_char

def image_to_ascii(image_path, new_width=100, use_color=False):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    
    image = resize_image(image, new_width)
    imageRGB = image
    image = grayscale_image(image)

    ascii_str = ""
    color_str = ""

    if use_color:
        color_str = [getRGB(pixel_value) for pixel_value in list(imageRGB.getdata())]
    ascii_str = [pixel_to_ascii(pixel_value, use_color) for pixel_value in list(image.getdata())]

    img_width = image.width
    ascii_str_len = len(ascii_str)
    if use_color:
        ascii_str = [x + y for x, y in zip(color_str,ascii_str)]
    ascii_str = ["".join(ascii_str[index:index + img_width]) for index in range(0, ascii_str_len, img_width)]

    ascii_str = "\n".join(ascii_str)
    
    return ascii_str

def print_ascii_image(ascii_str):
    print(ascii_str)

def main():
    image_path = "assets/" + input("Entrez le chemin de l'image à convertir : ")
    new_width = int(input("Entrez la largeur souhaitée pour l'image ASCII (par défaut 100) : ") or 100)

    use_color = input("Voulez-vous afficher l'image en couleur (y/n) ? ").lower() == 'y'

    ascii_image = image_to_ascii(image_path, new_width, use_color)
    print_ascii_image(ascii_image)

if __name__ == "__main__":
    main()
