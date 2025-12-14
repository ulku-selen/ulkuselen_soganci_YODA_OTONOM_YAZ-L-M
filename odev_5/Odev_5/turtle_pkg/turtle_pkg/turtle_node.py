import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleNode(Node):
    def __init__(self):
        super().__init__('turtle_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Turtle node baslatildi')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 1.5
        msg.angular.z = 0.5
        self.publisher_.publish(msg)
        self.get_logger().info('Twist mesaji gonderildi')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
