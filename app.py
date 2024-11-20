import cv2
from PIL import Image
import logging
import numpy as np
from ultralytics import YOLO

# Configure logging settings
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load the YOLO model
try:
    yolo = YOLO("model/yolo11n.pt")  # Replace 'yolo11n.pt' with the required model version
    logging.info("YOLO model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading YOLO model: {e}")
    exit(1)

def get_colors(cls_num):
    """
    Generates a unique RGB color based on the class number.

    Args:
        cls_num (int): The class number to generate a color for.

    Returns:
        tuple: A tuple representing the RGB color.
    """
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = cls_num % len(base_colors)
    increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
    
    color = [
        (base_colors[color_index][i] +
         increments[color_index][i] * (cls_num // len(base_colors)) % 256)
        for i in range(3)
    ]
    return tuple(color)

def apply_nms(boxes, scores, iou_threshold=0.5):
    """
    Applies Non-Maximum Suppression (NMS) to filter overlapping bounding boxes.

    Args:
        boxes (list): List of bounding boxes in [x, y, w, h] format.
        scores (list): Confidence scores for each bounding box.
        iou_threshold (float): Intersection over Union (IoU) threshold for NMS.

    Returns:
        list: Indices of the selected boxes after applying NMS.
    """
    indices = cv2.dnn.NMSBoxes(boxes, scores, score_threshold=0.4, nms_threshold=iou_threshold)
    if indices is not None and len(indices) > 0:
        return indices.flatten().tolist()
    return []

# Initialize video capture (0 for webcam, or provide a video file path)
# capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Uncomment for webcam input
capture = cv2.VideoCapture("video/sample_video.mp4")  # Use a video file

if not capture.isOpened():
    logging.error("Error: Unable to open video source.")
    exit(1)

logging.info("Video capture started.")

# Main loop for video processing
while True:
    ret, frame = capture.read()
    
    if not ret:
        logging.warning("Failed to capture frame. Exiting.")
        break
    
    # Resize the frame for processing
    frame = cv2.resize(frame, (1020, 600))

    # Perform object detection
    results = list(yolo.track(frame, stream=True))  # Convert generator to list

    # Prepare data for Non-Maximum Suppression (NMS)
    boxes, scores, classes = [], [], []
    for result in results:
        for box in result.boxes:
            if box.conf[0] > 0.4:  # Confidence threshold
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Extract bounding box coordinates
                boxes.append([x1, y1, x2 - x1, y2 - y1])  # Format as [x, y, w, h]
                scores.append(float(box.conf[0]))  # Convert confidence to float
                classes.append(int(box.cls[0]))  # Convert class index to int

    # Filter overlapping boxes using NMS
    selected_indices = apply_nms(boxes, scores)

    # Draw bounding boxes and labels on the frame
    for i in selected_indices:
        x, y, w, h = boxes[i]
        class_id = classes[i]
        class_name = result.names[class_id]  # Get class name
        color = get_colors(class_id)
        accuracy = np.round(scores[i] * 100, 2)  # Calculate accuracy percentage

        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        
        # Draw label with confidence score
        cv2.putText(
            frame,
            f"{class_name} {accuracy}%",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0 .5,
            color,
            2,
        )

    # Display the frame with detections
    cv2.imshow("YOLO Object Detection", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        logging.info("Exiting.")
        break

# Release video resources and close all OpenCV windows
capture.release()
cv2.destroyAllWindows()
logging.info("Video capture released, and all windows closed.")