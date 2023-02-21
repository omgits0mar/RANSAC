# RANSAC Algorithm and Panoramic Image Stitching

This repository contains an implementation of the RANSAC (Random Sample Consensus) algorithm from scratch, as well as a panoramic image stitching feature that takes two or more images as input, calculates the matches between the images, scores the similarity score, and finally outputs a panoramic image and whether the images are similar or not.

## RANSAC Algorithm

The RANSAC algorithm is an iterative method used to estimate parameters of a mathematical model from a set of observed data that contains outliers. This implementation of RANSAC can be used for a variety of applications, such as image processing and computer vision.

## Panoramic Image Stitching

The panoramic image stitching feature takes two or more images as input, calculates the matches between the images using feature detection and extraction algorithms such as SIFT, SURF, or ORB, scores the similarity score using RANSAC, and outputs a panoramic image. The output image will be a stitched version of the input images that seamlessly blends them together.

## Acknowledgements

The implementation of the RANSAC algorithm is based on the work of Martin Fischler and Robert Bolles, and the panoramic image stitching feature is based on the work of Matthew Brown and David G. Lowe.

## References

- [Fischler, M. A., & Bolles, R. C. (1981). "Random sample consensus: A paradigm for model fitting with applications to image analysis and automated cartography." Communications of the ACM, 24(6), 381-395.](https://dl.acm.org/doi/10.1145/358669.358692)
- [Brown, M., & Lowe, D. G. (2007). "Automatic panoramic image stitching using invariant features." International Journal of Computer Vision, 74(1), 59-73.](https://link.springer.com/article/10.1007/s11263-006-0002-3)
