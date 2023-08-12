import cv2
import numpy
import numpy as np


def get_match_top_left(big,small,threshold=0.1)\
        -> list[tuple[int,int,int,int]]:
    """

    :param big: 배경 이미지
    :param small: 검출할 템플릿 이미지
    :param threshold:  # 현재 코드에서는 임계점을 낮춰야 정확성이 올라감 (왜냐면 "차이"를 보는 것이므로 차이가 적어야 정답)
    :return: 템플릿 매칭에서 나온 tl,br 좌표
    """
    template_width = small.shape[1]
    template_height = small.shape[0]
    result = cv2.matchTemplate(small_color, big_color, cv2.TM_SQDIFF_NORMED)
    locations = np.where(result <= threshold)
    answer: list[tuple[int,int,int,int]] = []
    for loc in zip(*locations[::-1]):
        top_left = loc
        bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
        answer.append((top_left[0],top_left[1],bottom_right[0],bottom_right[1]))
    return answer

def draw_and_show(background: numpy.ndarray, answer_list):
    for ans in answer_list:
        cv2.rectangle(background, (ans[0],ans[1]),(ans[2],ans[3]), (0, 255, 0), 2)


if __name__ == '__main__':
    big_color = cv2.imread("big.png")
    small_color = cv2.imread("small.png")
    threshold = 0.1
    lst = get_match_top_left(big_color,small_color,threshold)
    
    draw_and_show(big_color,lst)
    cv2.imshow('Matching Result', big_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
