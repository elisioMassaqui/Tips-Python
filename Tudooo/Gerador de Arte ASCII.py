from PIL import Image

def image_to_ascii(image_path, width=100):
    chars = "@%#*+=-:. "
    image = Image.open(image_path)
    aspect_ratio = image.height / image.width
    new_height = int(aspect_ratio * width)
    image = image.resize((width, new_height))
    image = image.convert("L")  # Converte para escala de cinza
    
    pixels = image.getdata()
    ascii_str = ''.join([chars[pixel // 25] for pixel in pixels])
    ascii_str += "\n"

    img_width = image.width
    for i in range(0, len(ascii_str), img_width):
        ascii_str += ascii_str[i:i+img_width] + "\n"
    
    return ascii_str

if __name__ == '__main__':
    ascii_art = image_to_ascii('logo.png')
    print(ascii_art)
