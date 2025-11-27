import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request, response):
    if request.name == "浅沼陸斗":
        response.age = 46
    else:
        response.age = 255
    return response

def main():
    rclpy.init()
    node = Node("talker")
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)

if __name__ == "__main__":
    main()
