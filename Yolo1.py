from ultralytics import YOLO

model = YOLO(r"C:\Users\ADMIN\Desktop\TMRT\runs\detect\train\weights\best.pt")

results = model(r"C:\Users\ADMIN\Desktop\TMRT\task1vid1.mp4", save=True)

results[0].show()

