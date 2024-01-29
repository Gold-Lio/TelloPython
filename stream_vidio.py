import cv2
from djitellopy import tello

def process_tello_vidio(drone):
    while True:
        frame = drone.get_frame_read().frame
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    drone.end()

def main():
    drone = tello.Tello()
    drone.connect()
    drone.streamon()
    process_tello_vidio(drone)

if __name__ == "__main__":
    main()