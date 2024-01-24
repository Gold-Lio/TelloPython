from djitellopy import tello

def basic_flight_routine(drone):

    drone.connect()
    drone.takeoff()
    drone.land()
    drone.end()

def main():
    drone = tello.Tello()
    basic_flight_routine(drone)

if __name__ == "__main__":
    main()