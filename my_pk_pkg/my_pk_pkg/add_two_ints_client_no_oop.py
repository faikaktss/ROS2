import rclpy 
from rclpy.node import Node# sınıfı içeri alır
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_client_no_oop")

    client = node.create_client(AddTwoInts,"add_two_ints") #Müşteri yaratır
    while not client.wait_for_service(1.0):# Dükkan açıldımı diye bakar
        node.get_logger().info("Waiting for the service...")

    request = AddTwoInts.Request()
    request.a = 5
    request.b = 7

    future = client.call_async(request)
    rclpy.spin_until_future_complete(node,future)

    response = future.result()
    node.get_logger().info("Result: " + str(response.sum))

    rclpy.shutdown()

if __name__ == "__main__":
    main()