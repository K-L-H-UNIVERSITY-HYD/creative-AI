import cv2
effiel_tower_img = cv2.imread("./images/effiel_tower.jpg")
mars_img = cv2.imread("./images/mars.jpg")


final_img = cv2.add(effiel_tower_img, mars_img)


cv2.imshow("creative AI", final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()