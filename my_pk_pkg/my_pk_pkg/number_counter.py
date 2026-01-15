import rclpy 
from rclpy.node import Node# sınıfı içeri alır
from example_interfaces.msg import Int64
from example_interfaces.srv import Setbool

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("Number_Counter")
        self.counter = 0
        self.number_count_publisher = self.create_publisher(Int64,"number_topic",10)
        self.number_subscriber_ = self.create_subscription(Int64,"number_topic",self.callback_number,10)
        self.reset_counter_service_ = self.create_service(Setbool,"reset_counter",self.callback_reset_counter)
        self.get_logger().info("Number Counter Node has been starter")

    def callback_number(self,msg):
        self.counter += msg.data
        new_msg = Int64()
        new_msg.data = self.counter
        self.number_count_publisher.publish(new_msg)

    def callback_reset_counter(self,request:Setbool.Request, response: Setbool.Response):
        if request.data:
            self.counter = 0
            response.success = True
            response.message = "Counter has been reset"
        else:
            response.success = False
            response.message = "Counter has not been reset"

        return response
def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()