import cv2
cap = cv2.VideoCapture("C:\\Users\\saran\\OneDrive\\Desktop\\CV programs\\car.3gpp")
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
current_frame = total_frames - 1
while current_frame >= 0:
    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video in Reverse', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    current_frame -= 1
cap.release()

