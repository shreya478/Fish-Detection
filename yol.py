from ultralytics import YOLO

# Create and train a new YOLOv8 model
model = YOLO("yolov8n.pt")  # You can also try yolov8s.pt for better accuracy

# Train
model.train(data=r"C:\Users\ADMIN\Desktop\TMRT\Fish Detection 1.v2i.yolov5pytorch\data.yaml", epochs=30, imgsz=640)
