import argparse
from PIL import Image, ImageOps

def add_image_in_frame(base_image_path, overlay_image_path, output_image_path):
    # Öffne die Basisbilddatei
    base_image = Image.open(base_image_path)
    
    # Öffne die Overlay-Bilddatei
    overlay_image = Image.open(overlay_image_path)
    
    # Berechne die Größe des Overlays (40% der Basisbildgröße)
    overlay_width = int(base_image.width * 0.40)
    overlay_height = int(overlay_image.height * (overlay_width / overlay_image.width))
    overlay_image = overlay_image.resize((overlay_width, overlay_height), Image.Resampling.LANCZOS)
    
    # Füge einen Rahmen zum Overlay-Bild hinzu
    border_size = 10  # Breite des Rahmens
    overlay_image_with_border = ImageOps.expand(overlay_image, border=border_size, fill='red')
    
    # Berechne die Position, an der das Overlay-Bild platziert werden soll (rechts oben)
    position = (base_image.width - overlay_image_with_border.width - border_size, border_size)
    
    # Kombiniere die Bilder
    base_image.paste(overlay_image_with_border, position)
    
    # Speichere das resultierende Bild
    base_image.save(output_image_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add an overlay image to a base image with a frame.')
    parser.add_argument('base_image', help='Path to the base image')
    parser.add_argument('overlay_image', help='Path to the overlay image')
    parser.add_argument('output_image', help='Path to save the output image')

    args = parser.parse_args()

    add_image_in_frame(args.base_image, args.overlay_image, args.output_image)
