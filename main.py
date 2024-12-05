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
    
    # Calcul de la luminance (luminosité perçue)
    luminance = (0.2989 * r + 0.5870 * g + 0.1140 * b)

    # Si la couleur est sombre (luminance faible)
    if luminance < 128:
        if r > g and r > b:
            return bcolors.RED  # Rouge sombre
        elif g > r and g > b:
            return bcolors.GREEN  # Vert sombre
        elif b > r and b > g:
            return bcolors.BLUE  # Bleu sombre
        elif r == g == b:  # Gris foncé (proche du noir)
            return bcolors.BLACK  # Noir foncé
        else:
            return bcolors.MAGENTA  # Magenta foncé pour des cas intermédiaires

    # Si la couleur est claire (luminance élevée)
    elif luminance < 240:
        if r > g and r > b:
            return bcolors.LIGHT_RED  # Rouge clair
        elif g > r and g > b:
            return bcolors.LIGHT_GREEN  # Vert clair
        elif b > r and b > g:
            return bcolors.LIGHT_BLUE  # Bleu clair
        elif r == g and g == b:  # Gris clair (proche du blanc)
            return bcolors.LIGHT_WHITE  # Blanc
        elif r > b and r > g:
            return bcolors.YELLOW  # Jaune clair
        elif g > b and g > r:
            return bcolors.CYAN  # Cyan clair
        elif b > r and b > g:
            return bcolors.MAGENTA  # Magenta clair
        else:
            return bcolors.LIGHT_WHITE  # Cas par défaut (blanc)
    return bcolors.WHITE  # Par défaut



def grayscale_image(image):
    print(image.convert("L"))
    return image.convert("L")

def pixel_to_ascii(pixel_value, use_color=False):
    color_index = pixel_value // 25  # 255 / len(ASCII_CHARS) = 25
    ascii_char = ASCII_CHARS[color_index]

    if use_color:
        text_color = bcolors.RED if color_index % 2 == 0 else bcolors.GREEN
        
        return f"{text_color}{ascii_char}{bcolors.RESET}"
    else:
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

    for pixel_value in list(imageRGB.getdata()):
        color_str += getRGB(pixel_value)

    for pixel_value in list(image.getdata()):
        ascii_str += pixel_to_ascii(pixel_value, use_color)

    img_width = image.width
    ascii_str_len = len(ascii_str)
    print(type(ascii_str))
    ascii_str = [x + y for x, y in zip(color_str,ascii_str)]
    ascii_str = "".join(ascii_str)
    ascii_str = [ascii_str[index:index+img_width] for index in range(0, ascii_str_len, img_width )]
    print(type(ascii_str))

    ascii_str = "\n".join(ascii_str)
    
    return ascii_str

def print_ascii_image(ascii_str):
    print(ascii_str)

def main():
    image_path = input("Entrez le chemin de l'image à convertir : ")
    new_width = int(input("Entrez la largeur souhaitée pour l'image ASCII (par défaut 100) : ") or 100)

    use_color = input("Voulez-vous afficher l'image en couleur (y/n) ? ").lower() == 'y'

    ascii_image = image_to_ascii(image_path, new_width, use_color)
    print("\033[0;95mtest")
    print_ascii_image(ascii_image)

if __name__ == "__main__":
    main()
