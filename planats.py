import cv2

cv2.imread("C:/Users/maxwe/Downloads/PRO-104-Project-Image-main (1)/PRO-104-Project-Image-main/solar-system.jpg")
cv2.imshow("output", img)
cv2.waitKey(0)

cv2.putText(img,
            "Sun",
              (20,300),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255)
              )
cv2.putText(img,
            "Mercury",
              (30,300),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255)
              )
cv2.putText(img,
            "Venus",
              (40,300),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255)
              )
cv2.putText(img,
            "Earth",
              (50,300),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255)
              )
cv2.putText(img,
            "Mars",
              (60,300),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255)
              )
cv2.putText(img,
            "Jupiter",
              (70,300),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255)
              )
cv2.putText(img,
            "Saturn",
              (80,300),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255)
              )
cv2.putText(img,
            "Uranus",
              (90,300),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255)
              )
cv2.putText(img,
            "Neptune",
              (100,300),
              cv2.FONT_HERSHEY_COMPLEX,
              0.5,
              (255,255,255)
              )

cv2.imwrite("Solar_systemwithname.jpg", img)