import rclpy #ros 2^nin python ile konuşmasını sağlar
from rclpy.node import Node# sınıfı içeri alır

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter = 0
        self.get_logger().info("Hello world")
        self.create_timer(1.0, self.timer_callback) 

    def timer_callback(self):
        self.get_logger().info("Hello" + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__": # direk çalıştırıldıysa  çağırılır import edildiysßße çağırılmaz
    main()