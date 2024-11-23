# 🖼️ Object Detection App using yolo11n

📖 Description
---------------

This repository contains an Object Detection App built using yolo11n, a state-of-the-art object detection model. The app achieves an impressive accuracy of **99.63%** 🎯 and includes functionalities for detecting and recognizing objects such as 🐾 animals, 🐦 birds, 👤 humans, 🚗 transport, and more. It supports real-time object detection through a live webcam feed 📷.it’s the perfect resource for developers and researchers looking to enhance their projects with advanced detection capabilities. 🚀📊

📁 Repository Structure
-----------------------
    ├── model/ 
    │       └── yolo11n.pt          # yolo11n model file 
    ├── video/ 
    │       └── sample_video.mp4    # Sample video for testing the application 
    ├── app.py                      # Main application file 
    ├── requirements.txt            # List of required libraries and dependencies


 ✨ Features
-------------

- 🧠 **yolo11n Model:** Utilizes the latest yolo11n model for high-accuracy object detection.
- 🎥 **Real-Time Detection:** Detects and recognizes objects from a live webcam feed.
- 📜 **Logging:** Comprehensive logging for better understanding and debugging.
- 📝 **Code Documentation:** Clear and concise comments to ensure readability and understanding of the code.

🛠️ Installation
----------------

1. Clone the repository:
   ```bash
   git clone https://github.com/MohammadAshmir786/Object_Detection_with_YOLO.git
   cd Object_Detection_with_YOLO
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the `yolo11n.pt` model file is located in the `model` directory.

4. Place your sample video file in the `video` directory if you wish to test with custom videos.

## 🚀 Usage

1.  **Run the Application:**
    ```bas
    python app.py
    ```

2.  The application will start detecting objects in real-time using the webcam.

3.  Optionally, test the model using the sample video provided in the `video` directory.

📂 File Details
----------------

### 1\. `app.py` 📜

The main application script. Features include:

-   **Live webcam object detection.**
-   **Sample video testing.**
-   **Detailed logging for debugging.**
-   **Inline comments to explain the workflow.**

### 2\. `requirements.txt` 📋

A list of libraries and dependencies required to run the application. Install them using:

```bash
pip install -r requirements.txt
```

### 3\. `model/yolo11n.pt` 🧠

The yolo11n model file used for object detection.

### 4\. `video/sample_video.mp4` 🎞️

A sample video file containing various objects such as 🐾 animals, 🐦 birds, 👤 humans, and 🚗 transport for testing purposes.

🛡️ Requirements
----------------

Ensure you have the following installed:

-   🐍 Python 3.7 or higher
-   📦 Libraries listed in `requirements.txt`

📊 Example Output
-----------------

When running `app.py`, the application will:

1.  Use yolo11n for object detection.
2.  Display real-time webcam footage with bounding boxes and labels around detected objects.
3.  Log the detection details for review and debugging.

🤝 Contributing
---------------

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

📜 License
----------

This project is licensed under the MIT License. See the [LICENSE](https://github.com/MohammadAshmir786/Object_Detection_with_YOLO/blob/main/LICENSE) file for details.

💡 Acknowledgments
------------------

-   [YOLO Algorithm](https://github.com/ultralytics/ultralytics) - for the yolo11n model.
-   [Ultralytics](https://docs.ultralytics.com/models/yolo11/) - for the yolo11n model documentation.

🔧 Troubleshooting
------------------

If you encounter issues while running the application, consider the following steps:

1.  **Verify Dependencies:** Ensure all required libraries are installed correctly by running:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Model File Check:** Confirm that the `yolo11n.pt` model file is located in the `model` directory.

3.  **Webcam Issues:** Ensure your webcam is functioning properly and accessible by Python.

4.  **Logging:** Use the logs generated during the application's runtime to identify errors and debug the program.

5.  **Python Version:** Ensure you are using Python 3.7 or higher.

🌟 Future Enhancements
----------------------

Planned improvements for the app include:

-   Adding support for additional object categories.
-   Enhancing the GUI for better user interaction.
-   Integrating support for GPU acceleration for faster processing.
-   Providing a feature for saving detection results as video or image files.

📞 Contact
----------

For any questions or feedback, feel free to contact:

-   **Author:** Mohammad Ashmir Abbasi
-   **Email:** moashmir7003@gmail.com
-   **Social:** Connect with me for professional networking click 👉 <a href="https://www.linkedin.com/in/mohammad-ashmir-abbasi/" target="_blank"> <img src='https://github.com/user-attachments/assets/11bbd489-2246-4fe6-92c6-7ce271289482' width='60' height=15/></a>👈



📅 Changelog
------------

### v1.0.0

-   Initial release with YOLOv11n integration.
-   Support for real-time webcam detection.
-   Sample video testing included.
-   Logging and documentation added for clarity.

* * * * *

<h3 align="center">
  Thank you for using the Object Detection App with YOLO11n! 😊
</h3>
