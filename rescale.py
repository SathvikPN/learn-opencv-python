import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    # Images, videos, Live Videos
    width = frame.shape[1] * scale
    height = frame.shape[0] * scale 
    dimension = (int(width),int(height))
    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    # Live videos 
    capture.set(3,width)
    capture.set(4,height)



def main():

    # Image 
    img = cv.imread('Photos/Saath.jpg')
    cv.imshow('Original_photo', img)

    img_resized = rescaleFrame(img,0.5) # Image Resize

    cv.imshow('Photo_Resized',img_resized)
    cv.waitKey(0)

    # Video
    capture = cv.VideoCapture('Videos/hurray.mp4')


    while True:
        isTrue, frame = capture.read()
        cv.imshow('Original_Video', frame)

        frame_resized = rescaleFrame(frame,0.7) # Resize every frame of video
        cv.imshow('Resized_video', frame_resized) 

        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()

if __name__=='__main__': # Won't execute this script when imported into another. But can borrow function definitions
    main()