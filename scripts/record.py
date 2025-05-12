#!/usr/bin/env python3

import multiprocessing
import cv2



video_name = "5part.mp4"
record_name = "5part_driving.mp4"


def record_video(args):
    cap = cv2.VideoCapture(0)
    ref_video = cv2.VideoCapture(video_name)
    frame_count = int(ref_video.get(cv2.CAP_PROP_FRAME_COUNT))
    if not cap.isOpened():
        print("Error: Could not open video device.")
        args["closed"] = True
        exit()


    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(record_name, fourcc, ref_video.get(cv2.CAP_PROP_FPS), (width, height))

    args["recording"] = True
    while args["frame_count1"] < frame_count:
        ret, frame = cap.read()

        if not ret:
            args["closed"] = True
            break

        out.write(frame)
        args["frame_count1"] += 1
        print(f"Recorded {args['frame_count1']} frames")
        cv2.imshow('record', frame)

        cv2.waitKey(1)
        if args["closed"]:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def play_video(args):

    cap2 = cv2.VideoCapture(video_name)


    if not cap2.isOpened():
        print("Error: Could not open video device.")
        args["closed"] = True
        exit()

    while not args["recording"]:
        pass

    # Position the window on the right side of the screen
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.moveWindow('frame', 800, 0)  # x=800, y=0 positions it on the right side
    frame_count = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Playing {frame_count} frames")
    while args["frame_count2"] < frame_count:

        if args["frame_count2"] > args["frame_count1"]:
            continue

        ret, frame = cap2.read()

        if not ret:
            args["closed"] = True
            break



        args["frame_count2"] += 1
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            args["closed"] = True
            break

    cap2.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    with multiprocessing.Manager() as manager:
        args = manager.dict()
        args["closed"] = False
        args["recording"] = False
        args["frame_count1"] = 0
        args["frame_count2"] = 0
        process = multiprocessing.Process(target=record_video, args=(args,))
        process2 = multiprocessing.Process(target=play_video, args=(args,))

        process.start()
        process2.start()

        process.join()
        process2.join()
