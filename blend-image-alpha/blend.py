import numpy as np
import cv2

def blend_transparent(background_image:np.ndarray, overlay_image: np.ndarray, alpha: float, left_x: int, left_y: int):
    """
    :param background_image: 배경으로 사용할 이미지
    :param overlay_image: 겹쳐서 사용할 이미지
    :param alpha: 투명도
    :param left_x: 겹칠 이미지의 시작 위치
    :param left_y: 겹칠 이미지의 시작 위치
    :return:
    """
    overlay_region = background_image[left_y:left_y + overlay_image.shape[0], left_x:left_x + overlay_image.shape[1]]
    cropped_overlay = overlay_image[0:overlay_region.shape[0], 0:overlay_region.shape[1]]
    cv2.addWeighted(cropped_overlay, alpha, overlay_image, 1 - alpha, 0)

    mask = np.all(overlay_image == 0, axis=2)

    blended_region = cv2.addWeighted(overlay_region, 1 - alpha, overlay_image, alpha, 0)

    background_image[left_y:left_y + overlay_image.shape[0], left_x:left_x + overlay_image.shape[1]] = blended_region

    background_image[left_y:left_y + overlay_image.shape[0], left_x:left_x + overlay_image.shape[1]][mask] = overlay_image[mask]

    cv2.imshow('Image', background_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return background_image

if __name__ == '__main__':
    alpha = 0.5  # alpha 값이 낮을 수록 투명도 증가
    background_img = cv2.imread('test.png')
    overlay = cv2.imread('overlay.jpg', cv2.IMREAD_UNCHANGED)
    blend_transparent(background_img, overlay, alpha, 100, 100)
