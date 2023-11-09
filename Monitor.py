#!/usr/bin/env python3

import cv2
import numpy as np
from config import rtsp_address, rtsp_port, rtsp_username, rtsp_password 
from datetime import datetime
from time import sleep 

# channels = { "front":"401", "deck":"301"}
channels = { "deck":"301"}

endpoint_template = f"rtsp://{rtsp_username}:{rtsp_password}@{rtsp_address}:{rtsp_port}/Streaming/Channels/"

print(endpoint_template)

def get_region_of_interest(frame, channel_name):
    # get the length and height of the original frame
    height, width, _ = frame.shape

    if(channel_name == 'front'):
        # 去掉两条马路
        relative_points = np.array([
            [0.39, 0],
            [0.39, 0.2],
            [0.6, 0.2],
            [0.6, 1],
            [1, 1],
            [1, 0]
        ])
    elif(channel_name == 'deck'):
        # 从房顶开始
        relative_points = np.array([
            [0.45, 0],
            [0.45, 0.6],
            [0.4, 1],
            [1,1],
            [1, 0]
        ])
    
    points = (relative_points * np.array([width, height])).astype(np.int32)

    mask = np.zeros((height, width), dtype=np.uint8)

    # Mask out the region of non-interest
    cv2.fillPoly(mask, [points], 1)
    frame_copy = np.copy(frame)
    frame_copy[mask == 1] = 0
    return frame_copy

def compare_region_of_interest(region_of_interest, previous_region_of_interest):
    # compare regions of interest
    diff = cv2.absdiff(region_of_interest, previous_region_of_interest)
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    diff_blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)

    _, thresh_bin = cv2.threshold(diff_blur, 20, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def getVideo(endpoint, channel_name):
    print("endpoint:", endpoint)
    vcap = cv2.VideoCapture(endpoint)
    ret, previous_frame = vcap.read()
    assert ret
    previous_region_of_interest = get_region_of_interest(previous_frame, channel_name)

    while vcap.isOpened():
        sleep(0.1)
        ret, frame = vcap.read()
        assert ret
        region_of_interest = get_region_of_interest(frame, channel_name)
        contours = compare_region_of_interest(region_of_interest, previous_region_of_interest)

        maxChangeSize = 0
        maxChangeContour = None
        # to draw the bounding box when motion is detected
        for contour in contours:
            changeSize = cv2.contourArea(contour)
            if changeSize > maxChangeSize:
                maxChangeSize = changeSize
                maxChangeContour = contour
            
        if maxChangeSize > 3000:
            # x, y, w, h = cv2.boundingRect(maxChangeContour)
            # print("Motion detected at", datetime.now())
            # print("x:", x, "y:", y, "w:", w, "h:", h)
            # # get this subframe
            # subframe = frame[y:y+h, x:x+w]
            
            # save it for investigation later, with the name of the channel and datetime
            datetimestr = datetime.now().strftime("%Y%m%d-%H%M%S")
            cv2.imwrite(f"./data/motions/{channel_name}/{datetimestr}.jpg", frame)

        cv2.imshow("Detecting Motion...", frame)
        previous_frame = frame
        previous_region_of_interest = region_of_interest

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

# loop all the channels
for ( channel_name, channel_id) in channels.items():
    print("channel_name:", channel_name)
    endpoint = endpoint_template + channel_id
    getVideo(endpoint, channel_name)


