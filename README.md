# Image to PDF Converter 🖼️➡️📄

Welcome to the Image to PDF Converter! This Python console application allows you to effortlessly convert a directory of images into a single PDF file, with each image fitting perfectly on its own page. This tool is perfect for organizing scanned documents or creating PDF albums from your image collections. 📚✨

## Features ✨

- **Easy Conversion**: Convert all supported image files in a directory to a PDF with a single command.
- **Supported Formats**: Automatically detects and converts images with the following extensions:
  - `.jpg`
  - `.jpeg`
  - `.png`
  - `.bmp`
- **One Image Per Page**: Each image is resized to fit on its own page in the PDF.
- **Simple to Use**: Just provide the path to the directory containing your images.

## Installation 💻

1. **Clone the Repository**
   ```bash
   git clone https://github.com/loudsheep/PDFFromImages.git
   cd PDFFromImages
   ```
   
2. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🚀

1. **Run the Application**

   Run the console application with the following command:

   ```bash
   python main.py
   ```

2. **Enter the Directory Path**

   When prompted, enter the path to the directory containing your images:

   ```
   Enter path: /path/to/your/images
   ```

3. **Get Your PDF**

   The application will generate a PDF file named `generated.pdf` in the same directory as your script.

## Example 🛠️

For a directory `/images` containing 5 images:
- `image1.jpg`
- `image2.png`
- `image3.bmp`
- `image4.jpeg`
- `image5.jpg`

Running the script will create `generated.pdf`, a 5-page PDF with each image on a separate page.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Enjoy seamless image-to-PDF conversion! If you have any questions or issues, feel free to open an issue in the repository. Contributions are welcome! 🤝
