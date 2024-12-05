from PIL import Image
from bcolors import bcolors

ASCII_CHARS = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / (2 * width)  # Times 2 because an ASCII character is twice as tall
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def pixel_to_ascii(pixel_value, use_color=False, use_background=False):
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
    image = grayscale_image(image)

    ascii_str = ""
    for pixel_value in list(image.getdata()):
        ascii_str += pixel_to_ascii(pixel_value, use_color)

    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_str = [ascii_str[index:index+img_width] for index in range(0, ascii_str_len, img_width)]

    ascii_str = "\n".join(ascii_str)
    
    return ascii_str

def print_ascii_image(ascii_str):
    print(ascii_str)

def main():
    image_path = input("Entrez le chemin de l'image à convertir : ")
    new_width = int(input("Entrez la largeur souhaitée pour l'image ASCII (par défaut 100) : ") or 100)

    use_color = input("Voulez-vous afficher l'image en couleur (y/n) ? ").lower() == 'y'

    ascii_image = image_to_ascii(image_path, new_width, use_color)
    print_ascii_image(ascii_image)

if __name__ == "__main__":
    main()
