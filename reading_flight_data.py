import cv2
from djitellopy import tello

def get_orientation_data(drone):
    pitch = 'Pitch' + str(drone.get_pitch()) + '.'
    roll = 'Roll' + str(drone.get_roll()) + '.'
    yaw = 'Yaw' + str(drone.get_yaw()) + '.'
    vgx = 'Speed X' + str(drone.get_speed_x()) + 'm/s'
    vgy = 'Speed Y' + str(drone.get_speed_y()) + 'm/s'
    vgz = 'Speed Z' + str(drone.get_speed_z()) + 'm/s'
    agx = 'Acceleration X' + str(drone.get_acceleration_x()) + 'cm/s'
    agy = 'Acceleration Y' + str(drone.get_acceleration_y()) + 'cm/s'
    agz = 'Acceleration Z' + str(drone.get_acceleration_z()) + 'cm/s'
    print(
        pitch + "\n" + roll + "\n" + yaw + "\n" + vgx + "\n" + vgy + "\n" + vgz
        + "\n" + agx + "\n" + agy + "\n" + agz)

def get_status_data(drone):
    activeMotorTime = drone.get_flight_time()
    battery = drone.get_battery()
    height = drone.get_height()
    tof = drone.get_distance_tof()
    templ = drone.get_lowest_temperature()
    temph = drone.get_highest_temperature()
    avgtemp = drone.get_temperature()
    barometer = drone.get_barometer()
    return activeMotorTime, battery, height, tof, templ, temph, avgtemp, barometer

def process_tello_vidio(drone):

    while True:
        get_orientation_data(drone)
        frame = drone.get_frame_read().frame

        activeMotorTime, battery, height, tof, templ, temph, avgtemp, barometer = get_status_data(drone)

        cv2.putText(frame, 'Active Motor Time : ' + str(activeMotorTime) + 'Seconds', (10, 20),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 234, 255), 1, 2)

        cv2.putText(frame, 'Battery : ' + str(battery) + '%', (10, 45),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 234, 255), 1, 2)

        cv2.putText(frame, 'Height : ' + str(height) + 'cm', (10, 70),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 234, 255), 1, 2)

        cv2.putText(frame, 'tof : ' + str(tof) + 'cm', (10, 95),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 234, 255), 1, 2)

        cv2.putText(frame, 'templ : ' + str(templ) + 'Celsius', (10, 120),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 234, 255), 1, 2)

        cv2.putText(frame, 'temph : ' + str(temph) + 'Celsius', (10, 145),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 234, 255), 1, 2)

        cv2.putText(frame, 'Avg temp : ' + str(avgtemp) + 'Celsius', (10, 170),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 234, 255), 1, 2)

        cv2.putText(frame, 'Barometor : ' + str(barometer) + 'cm (abs height)', (10, 195),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 234, 255), 1, 2)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def main():
    drone = tello.Tello()
    drone.connect()
    drone.streamon()
    process_tello_vidio(drone)

if __name__ == "__main__":
    main()
