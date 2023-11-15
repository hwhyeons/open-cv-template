"""
트랙바로 임계값 조절해가면서 이미지 컨투어
"""

import cv2

# 초기 이미지 로드
image = cv2.imread('image.png',0) # gray scale read

# 윈도우 이름 설정
window_name = 'Contour Detection'  

# 초기 임계값 설정
initial_threshold = 0


# 트랙바 이벤트 처리 함수
def on_trackbar(val):
    # 이미지 복사
    img_copy = image.copy()

    # 임계값 설정
    _, thresh = cv2.threshold(img_copy, val, 255, cv2.THRESH_BINARY)

    # 컨투어 찾기
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 이미지에 컨투어 그리기
    result = cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)

    # 결과 이미지 출력
    # cv2.imshow(window_name, result)
    cv2.imshow(window_name,thresh)


# 윈도우 생성
cv2.namedWindow(window_name)

# 트랙바 생성
cv2.createTrackbar('Threshold', window_name, initial_threshold, 255, on_trackbar)

# 초기 컨투어 찾기
on_trackbar(initial_threshold)
cv2.waitKey(0)

