import cv2
image_name = input("Enter the path to the image file: with image: ")
image = cv2.imread(image_name)
if image is None:
    print("Error: Could not read the image.")
    exit()


else:
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Greyscale Image", grey_image)
    output_name = input("Enter the path to save the greyscale image: ")
    cv2.imwrite(output_name, grey_image)

    print(f"Greyscale image saved as {output_name}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
