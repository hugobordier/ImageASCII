from PIL import Image
from bcolors import bcolors

# Liste de caractères ASCII à utiliser
ASCII_CHARS = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]

# Fonction pour redimensionner l'image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / (2 * width)  # Times 2 because an ASCII character is twice as tall
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Fonction pour convertir l'image en niveaux de gris
def grayscale_image(image):
    return image.convert("L")

# Fonction pour mapper les pixels en caractères ASCII avec ou sans couleur
def pixel_to_ascii(pixel_value, use_color=False, use_background=False):
    # Choisir la couleur en fonction de la luminosité
    color_index = pixel_value // 25  # 255 / len(ASCII_CHARS) = 25
    ascii_char = ASCII_CHARS[color_index]

    if use_color:
        # Choisir la couleur de texte et de fond
        text_color = bcolors.RED if color_index % 2 == 0 else bcolors.GREEN
        background_color = bcolors.BACK_BLACK if use_background else bcolors.RESET
        
        # Appliquer la couleur et le fond (si nécessaire)
        return f"{text_color}{background_color}{ascii_char}{bcolors.RESET}"
    else:
        return ascii_char

# Fonction principale pour convertir l'image en ASCII avec option de couleur
def image_to_ascii(image_path, new_width=100, use_color=False, use_background=False):
    try:
        # Ouvrir l'image
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    
    # Redimensionner et convertir l'image en niveaux de gris
    image = resize_image(image, new_width)
    image = grayscale_image(image)

    # Créer une chaîne pour l'ASCII avec ou sans couleur
    ascii_str = ""
    for pixel_value in list(image.getdata()):
        print(pixel_value)
        ascii_str += pixel_to_ascii(pixel_value, use_color, use_background)

    # Diviser la chaîne en lignes pour correspondre à l'image
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_str = [ascii_str[index:index+img_width] for index in range(0, ascii_str_len, img_width)]

    # Joindre les lignes avec des retours à la ligne
    ascii_str = "\n".join(ascii_str)
    
    return ascii_str

# Fonction pour afficher l'ASCII dans la console
def print_ascii_image(ascii_str):
    print(ascii_str)

# Fonction principale
def main():
    image_path = input("Entrez le chemin de l'image à convertir : ")
    new_width = int(input("Entrez la largeur souhaitée pour l'image ASCII (par défaut 100) : ") or 100)

    use_color = input("Voulez-vous afficher l'image en couleur (y/n) ? ").lower() == 'y'
    use_background = input("Voulez-vous ajouter des fonds (y/n) ? ").lower() == 'y'

    ascii_image = image_to_ascii(image_path, new_width, use_color, use_background)
    # print_ascii_image(ascii_image)

if __name__ == "__main__":
    main()
