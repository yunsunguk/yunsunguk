import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Sim_sub(Node):
    def __init__(self):
        super().__init__("m2sub")
        self.pub = self.create_subscription(String, 'message2', self.sub, 10)
        

    def sub(self, msg):
        self.get_logger().info(f'Received meassage2 : {msg.data}')

def test():
    print('test')



def main():
    rclpy.init()
    node = Sim_sub()
    # node.create_timer(1, test)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('keyboard interupt !')
    finally:
        node.destroy_node
        rclpy.shutdown()

if __name__ == '__main__':
    main()
