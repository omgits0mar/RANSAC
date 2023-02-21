import glob
import cv2
import numpy as np
import Utilities2

images_jpeg = glob.glob("images/*.jpeg")

images = glob.glob("images/*")

left_images = [img for img in images_jpeg if img.__contains__("_i")]
left_images.sort()
right_images = [img for img in images_jpeg if img.__contains__("_j")]
right_images.sort()
extra_images = [img for img in images_jpeg if img.__contains__("_z")]
right_images.sort()

png_idx = 0
i = 0
j = 0
dir = []

for img in images:
    if img.endswith("c.png"):
        dir.append(int((png_idx - 1) / 2))
    png_idx += 1
for left_img_path, right_img_path in zip(left_images, right_images):

    imageA = cv2.imread(right_img_path)
    imageB = cv2.imread(left_img_path)
    imageA = cv2.resize(imageA,(400,200))
    imageB = cv2.resize(imageB,(400,200))

    kpsA, featuresA = Utilities2.detectAndDescribe(imageA)
    kpsB, featuresB = Utilities2.detectAndDescribe(imageB)

    M = Utilities2.matchKeypoints(featuresA, featuresB, 0.72)
    M2 = Utilities2.mean_score(M)

    if(dir.__contains__(i)):
        img_extra = cv2.imread(dir[j])
        i += 1
        img_extra = cv2.resize(img_extra,(400,200))
        kpsC, featuresC = Utilities2.matchKeypoints(img_extra)

        M = Utilities2.matchKeypoints(featuresA, featuresC, 0.72)
        similarity = len(M) / min(len(kpsA), len(kpsB))
        print("Similarity Score of david law's : " + str(similarity))
        M = Utilities2.mean_score(M)

        M2 = Utilities2.matchKeypoints(featuresC, featuresB, 0.72)
        M2 = Utilities2.mean_score(M2)

        vis2 = Utilities2.drawMatches(imageA, img_extra, kpsC, kpsA, M2)
        vis3 = Utilities2.drawMatches(img_extra, imageB, kpsB, kpsC, M2)
        cv2.imshow("Keypoint Matches", vis2)
        cv2.imshow("Keypoint Matches", vis3)
        cv2.waitKey(0)

    vis = Utilities2.drawMatches(imageA, imageB, kpsB, kpsA, M2)
    cv2.imshow("Keypoint Matches", vis)
    cv2.waitKey(0)

    similarity = len(M2) / (min(len(kpsA), len(kpsB)))
    print("Similarity Score of mean : " + str(similarity))
    if similarity > 0.05:
        print("both are Similar")
    else:
        print("both aren't Similar")
    j += 1