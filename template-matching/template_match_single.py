"""
minMaxLoc()을 사용한 템플릿 매칭
-> 이미지 안에 템플릿 하나만 있는 경우 + 템플릿이 무조건 존재하는 것이 보장 되는 경우에 사용
(임계값을 사용하지 않기 때문에 배경이미지에 템플릿이 없어도 검출처리 될 수 있음)

그리고 아래 방식들은 컬러 이미지를 사용하기 때문에 뚜렷한 이미지가 아니면 오검출 가능성이 높음
-> 따라서 성능을 높이고 싶다면 그레이 스케일로 변경하여 사용
"""

import cv2

# Load the main image and the template
main_image = cv2.imread('big.png') # 전체 이미지
template = cv2.imread('small.png') # 템플릿 이미지

# Get the width and height of the template
template_height, template_width = template.shape[:2]


# 원하는 사진에 따라 테스트해보고 결정하기
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    # Create a copy of the main image to draw rectangles on
    main_image_copy = main_image.copy()
    print(method)

    # Apply template matching
    result = cv2.matchTemplate(main_image, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Determine the top-left corner of the matched region
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    # Draw a rectangle around the matched region
    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
    cv2.rectangle(main_image_copy, top_left, bottom_right, (0, 255, 0), 2)

    # Display the results
    cv2.imshow('Matching Result', main_image_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
