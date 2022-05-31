import cv2 as cv

folha = cv.imread("folha_ teste.jpeg")

folha_red = cv.resize(folha, (224,224),interpolation=cv.INTER_AREA)

cv.imshow("original",folha)
cv.imshow("redimensionada",folha_red)
cv.waitKey(0)
cv.destroyAllWindows()

