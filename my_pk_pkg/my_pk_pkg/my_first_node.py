import rclpy #ros 2^nin python ile konuşmasını sağlar
from rclpy.node import Node# sınıfı içeri alır


def main(args=None):
    rclpy.init(args=args)
    node = Node("py_test")
    node.get_logger().info("Hello world")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__": # direk çalıştırıldıysa  çağırılır import edildiysßße çağırılmaz
    main()