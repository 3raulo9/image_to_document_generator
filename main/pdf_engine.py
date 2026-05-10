import os
from PIL import Image

class PDFEngine:
    @staticmethod
    def convert_images_to_pdf(file_paths, output_path):
        """Processes images and merges them into a single PDF."""
        if not file_paths:
            return False, "No images provided."

        try:
            image_list = []
            for path in file_paths:
                img = Image.open(path)
                # Convert to RGB (required for PDF saving as PNGs often have Alpha)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                image_list.append(img)

            if image_list:
                image_list[0].save(
                    output_path,
                    save_all=True,
                    append_images=image_list[1:]
                )
                return True, "Success"
        except Exception as e:
            return False, str(e)