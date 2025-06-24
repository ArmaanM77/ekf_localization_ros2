import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

class EKFNode(Node):
    def __init__(self):
        super().__init__('ekf_node')
        self.get_logger().info('EKFNode initialized')
        # Subscribe to ground speed
        self.create_subscription(
            TwistStamped,
            '/optical_speed_sensor',
            self.speed_cb,
            10)
        self.last_time = self.get_clock().now()

    def speed_cb(self, msg: TwistStamped):
        now = self.get_clock().now()
        dt = (now - self.last_time).nanoseconds * 1e-9
        self.last_time = now
        v = msg.twist.linear.x
        self.get_logger().info(f'[Predict Test] dt={dt:.3f}s, v={v:.2f} m/s')

def main(args=None):
    rclpy.init(args=args)
    node = EKFNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
