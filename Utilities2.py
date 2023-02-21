import numpy as np
import cv2


def detectAndDescribe(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    descriptor = cv2.SIFT_create()  # cv2.xfeatures2d.SIFT_create()
    (kps, features) = descriptor.detectAndCompute(gray, None)
    kps = np.float32([kp.pt for kp in kps])
    return (kps, features)

def matchKeypoints(featuresA, featuresB, ratio):
    matcher = cv2.BFMatcher()
    rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
    matches = []
    for m in rawMatches:
        if (m[0].distance / m[1].distance) < ratio:
            matches.append(m)
    return matches

def mean_score(matches):
    sum = 0
    for kp in matches:
        sum += kp[0].distance
    avg = sum / len(matches)
    Matches = []
    for mt in matches:
        if mt[0].distance < avg:
            Matches.append((mt[0].queryIdx, mt[0].trainIdx))
    return Matches


def drawMatches(imageA, imageB, kpsA, kpsB, matches):
    # initialize the output visualization image
    (hA, wA) = imageA.shape[:2]
    (hB, wB) = imageB.shape[:2]
    vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
    vis[0:hA, 0:wA] = imageA
    vis[0:hB, wA:] = imageB
    for ((trainIdx, queryIdx)) in (matches):
        ptA = (int(kpsA[queryIdx][0]), int(kpsA[queryIdx][1]))
        ptB = (int(kpsB[trainIdx][0]) + wA, int(kpsB[trainIdx][1]))
        cv2.line(vis, ptA, ptB, (0, 255, 0), 1)
    # return the visualization
    return vis