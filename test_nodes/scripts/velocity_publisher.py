from matplotlib.pyplot import cla
from sympy import Float
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray


class VelocityPublisher(Node):
    def __init__(self):
        super().__init__("velocity_publisher")
        self.publisher_ = self.create_publisher(Float64MultiArray,"/velocity_controller/commands",10)
        self.timer_period = 2.0
        self.timer = self.create_timer(self.timer_period,self.timer_callback)
        self.i = 0
        self.dir = 1
        
    def timer_callback(self):
        msg =  Float64MultiArray()
        if self.i%2 == 0:
            if self.dir == 1:
                msg.data = [1000.0]
            else:
                msg.data = [-1000.0]
            self.dir = self.dir ^ 1
        else:
            msg.data = [0.0]
        self.i = self.i + 1
        self.publisher_.publish(msg)
        
        
        
def main(args=None):
    rclpy.init(args=args)
    vel_pub = VelocityPublisher()
    rclpy.spin(vel_pub)
    ter_msg = Float64MultiArray()
    ter_msg.data = [0.0]
    vel_pub.publisher_.publish(ter_msg)
    vel_pub.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
        