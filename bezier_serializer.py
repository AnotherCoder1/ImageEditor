from copy import deepcopy
from json import dump, loads
from vec2d import Vector2


json_control_points="""
        [
            {
            "Vector2": {
                "x": 888.6954345703125,
                "y": 477.718505859375
            }
        },
        {
            "Vector2": {
                "x": 876.3091430664063,
                "y": 554.936279296875
            }
        },
        {
            "Vector2": {
                "x": 793.6849975585938,
                "y": 541.320556640625
            }
        },
        {
            "Vector2": {
                "x": 796.4682006835938,
                "y": 478.5450744628906
            }
        }
        ]"""

bezier_control_points=loads(json_control_points)

controlPoints=[ Vector2(bezier_control_points[0]['Vector2']['x'], bezier_control_points[0]['Vector2']['y'] ), 
                Vector2(bezier_control_points[1]['Vector2']['x'], bezier_control_points[1]['Vector2']['y'] ),
                Vector2(bezier_control_points[2]['Vector2']['x'], bezier_control_points[2]['Vector2']['y'] ),
                Vector2(bezier_control_points[3]['Vector2']['x'], bezier_control_points[3]['Vector2']['y'] ),
                ]


bezier=[{ "Vector2": { "x": i.x, "y":i.y }} for i in controlPoints]

with open('bezierControlPoints.json', 'w') as file:
    dump(bezier, file, indent=4)
