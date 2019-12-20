# Write a program that test if two rectangles have a non-empty intersection. If the intersections is non-empty, return the rectangle formed by their intersection.

import sys

def calculate_iou(bbox1, bbox2):
    """Return the intersection bbox or None"""
    x1 = max(bbox1['x1'], bbox2['x1'])
    y1 = max(bbox1['y1'], bbox2['y1'])
    x2 = min(bbox1['x2'], bbox2['x2'])
    y2 = min(bbox1['y2'], bbox2['y2'])

    if (x2 - x1) < 0 or (y2 - y1) < 0:
        return None

    else:
        return {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}


if __name__ == '__main__':

    bbox1 = {}
    bbox2 = {}

    bbox1['x1'] = int(sys.argv[1])
    bbox1['y1'] = int(sys.argv[2])
    bbox1['x2'] = int(sys.argv[3])
    bbox1['y2'] = int(sys.argv[4])

    bbox2['x1'] = int(sys.argv[5])
    bbox2['y1'] = int(sys.argv[6])
    bbox2['x2'] = int(sys.argv[7])
    bbox2['y2'] = int(sys.argv[8])

    print(calculate_iou(bbox1, bbox2))
