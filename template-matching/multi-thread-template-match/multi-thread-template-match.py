import random
import time
import cv2
import concurrent
from concurrent import futures

executor = concurrent.futures.ThreadPoolExecutor()
if __name__ == '__main__':
    background_image = cv2.imread("background image path")
    template_image_list: list = [load_all_images..]
    for _ in range(5): # executor에 처음 submit 하는 과정에서는 많은 시간 소요 -> 반복하면 속도가 크게 줄어듦
        futures = []
        time_start = time.time()
        for i in range(8):
            futures.append(executor.submit(cv2.matchTemplate,background_image, random.choice(template_image_list), cv2.TM_CCOEFF_NORMED))
        for i in range(8):
            a = (futures[i].result())
        print(f"소요 시간 : {time.time() - time_start}")
