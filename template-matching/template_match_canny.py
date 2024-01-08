import cv2
import numpy as np

"""
Canny Edge Detection을 이용한 템플릿 매칭
- matchTemplate방식을 cv2.TM_CCOEFF 대신 cv2.TM_CCOEFF_NORMED를 사용하면 THRESHOLD를 0~1사이로 조정 하기

"""

def match_template(background_image_path: str, template_image_path: str):
    THRESHOLD=20000000

    background_image= cv2.imread(background_image_path,cv2.IMREAD_GRAYSCALE)
    template_image= cv2.imread(template_image_path,cv2.IMREAD_GRAYSCALE)
    background_image = cv2.Canny(background_image, 50, 200)
    template_image= cv2.Canny(template_image, 50, 200)

    result = cv2.matchTemplate(background_image, template_image, cv2.TM_CCOEFF)
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

    if maxVal<=THRESHOLD:
        return None
    (tH, tW) = template_image.shape[:2]
    minx,miny,maxx,maxy=maxLoc[0],maxLoc[1],maxLoc[0] + tW, maxLoc[1] + tH

    clone = np.dstack([background_image, background_image, background_image])
    cv2.imshow('template',template_image)
    cv2.waitKey(0)
    cv2.rectangle(clone, (minx,miny),
                  (maxx, maxy), (0, 0, 255), 2)
    cv2.imshow('match',clone)
    cv2.waitKey(0)
