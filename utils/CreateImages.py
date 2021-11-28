import cv2
import numpy as np

data = np.load("../data/training_data.npy", allow_pickle=True)
targets = np.load("../data/target_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

count_nth = 0
count_a = 0
count_s = 0
count_d = 0
count_w = 0
count_laser = 0

for data in holder_list:
    # print(data[1])
    if data[1] == 'none':
        count_nth += 1
        cv2.imwrite(f"../data/Nothing/H7-nothing{count_nth}.png", data[0]) 
    elif data[1] == 'A':
        count_a += 1
        cv2.imwrite(f"../data/A/H7-a{count_a}.png", data[0]) 
    elif data[1] == 'S':
        count_s += 1
        cv2.imwrite(f"../data/S/H7-s{count_s}.png", data[0]) 
    elif data[1] == 'D':
        count_d += 1
        cv2.imwrite(f"../data/D/H7-d{count_d}.png", data[0]) 
    elif data[1] == 'W':
        count_w += 1
        cv2.imwrite(f"../data/W/H7-w{count_w}.png", data[0]) 
    elif data[1] == ' ':
        count_laser += 1
        cv2.imwrite(f"../data/Space/H7-laser{count_laser}.png", data[0]) 