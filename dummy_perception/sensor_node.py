import rclpy           # The "Standard Library" for ROS 2
from rclpy.node import Node

class DriverlessSensor(Node):
    def __init__(self):
        # This gives the node a name in the system
        super().__init__('driverless_sensor_node')
        
        # Create a timer that runs every 1 second
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Sensor Node has started! Watching for cones...')

    def timer_callback(self):
        # This is where the "logic" happens
        # For now, we are just pretending to see a cone
        self.get_logger().info('PERCEPTION: I see a BLUE CONE at 5 meters.')

def main(args=None):
    rclpy.init(args=args)      # Initialize ROS 2
    node = DriverlessSensor()  # Create the node
    rclpy.spin(node)           # Keep the node running
    rclpy.shutdown()           # Shutdown when finished

if __name__ == '__main__':
    main()