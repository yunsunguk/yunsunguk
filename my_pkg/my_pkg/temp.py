import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Sim_pub(Node):
    def __init__(self):
        super().__init__("simple_mpub")
        self.pub = self.create_publisher(str, 'message', 10)
        self.creat_timer(1, self.publisher)

    def publisher(self):
        msg = String()        
        msg.data = 'hellow'
        self.pub.publish(msg) 

def test():
    print('test')

def main():
    rclpy.init()
    node = Sim_pub()
    node.create_timer(1, test)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('keyboard interupt !')
    finally:
        node.destroy_node
        rclpy.shutdown()

if __name__ == '__main__':
    main()

