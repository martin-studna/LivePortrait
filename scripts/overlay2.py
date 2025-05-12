import cv2

cap1 = cv2.VideoCapture("5part.mp4")
cap2 = cv2.VideoCapture("animations/kešner--5part_driving_right_.mp4")
cap3 = cv2.VideoCapture("animations/miloš--5part_driving_left_.mp4")

cap1.set(cv2.CAP_PROP_FPS, 30)
cap2.set(cv2.CAP_PROP_FPS, 30)
cap3.set(cv2.CAP_PROP_FPS, 30)


# Define crop position and size
x1 = 1507  # top-right x
y1 = 697  # top-right y
w1 = 320  # width of cropped area
h1 = 240  # height of cropped area

x2 = 1920 - 1507 - 320  # top-left x
y2 = 697  # top-left y
w2 = 320  # width of cropped area
h2 = 240  # height of cropped area

writer = cv2.VideoWriter("5part_overlay.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (1920, 1080))


while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()

    if not ret1 or not ret2 or not ret3:
        break


    frame2 = cv2.resize(frame2, (w1, h1))
    frame3 = cv2.resize(frame3, (w2, h2))

    frame1[y1:y1+h1 + 30, x1:x1+w1] = 0
    frame1[y2:y2+h2 + 30, x2:x2+w2] = 0
    frame1[y1:y1+h1, x1:x1+w1] = frame2
    frame1[y2:y2+h2, x2:x2+w2] = frame3

    cv2.putText(frame1, "player1", (x1, y1 + h1 + 22), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame1, "player2", (x2, y2 + h2 + 22), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    writer.write(frame1)
    cv2.imshow("frame1", frame1)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

writer.release()
cv2.destroyAllWindows()
