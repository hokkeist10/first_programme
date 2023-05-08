import sys
import random
import itertools
import numpy as np
import cv2 as cv

MAP_FILE = 'cape_python.png'
SA1_CORNERS = (130, 265, 180, 315)
SA2_CORNERS = (80, 255, 130, 305)
SA3_CORNERS = (105, 205, 155, 255)

class Search:

    def __init__(self, name):
        self.name = name
        self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
        if self.img is None:
            print(f'Could you load map file {MAP_FILE}', file=sys.stderr)
            sys.exit()

        self.area_actual = 0
        self.sailor_actual = [0, 0]

        self.sa1 = self.img[SA1_CORNERS[1] : SA1_CORNERS[3],
                            SA1_CORNERS[0] : SA1_CORNERS[2]
                            ]
        self.sa2 = self.img[SA2_CORNERS[1] : SA2_CORNERS[3],
                            SA2_CORNERS[0] : SA2_CORNERS[2]
                            ]
        self.sa3 = self.img[SA3_CORNERS[1]: SA3_CORNERS[3],
                            SA3_CORNERS[0]: SA3_CORNERS[2]
                            ]
        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.5

        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0

        def draw_map(self, last_known):
            cv.line(self.img, (20, 370), (70, 370), (0, 0, 0), 2)
            cv.putText(self.img, '0', (8, 370), cv.FONT_HERSION_PLAIN, 1, (0, 0, 0))
            cv.putText(self.img, '50 Nautical Miles', (8, 370), cv.FONT_HERSION_PLAIN, 1, (0, 0, 0))

            cv.rectangle(self.img, (SA1_CORNERS[1], SA1_CORNERS[3]),
                         (SA1_CORNERS[0], SA1_CORNERS[2]), (0, 0, 0), 1)
            cv.putText(self.img, '1', (SA1_CORNERS[0] + 3, SA1_CORNERS[1] + 15),
                       cv.FONT_HERSION_PLAIN, 1, 0)
            cv.rectangle(self.img, (SA2_CORNERS[1], SA2_CORNERS[3]),
                         (SA2_CORNERS[0], SA2_CORNERS[2]), (0, 0, 0), 1)
            cv.putText(self.img, '1', (SA2_CORNERS[0] + 3, SA2_CORNERS[1] + 15),
                       cv.FONT_HERSION_PLAIN, 1, 0)
            cv.rectangle(self.img, (SA3_CORNERS[1], SA3_CORNERS[3]),
                         (SA3_CORNERS[0], SA3_CORNERS[2]), (0, 0, 0), 1)
            cv.putText(self.img, '1', (SA3_CORNERS[0] + 3, SA3_CORNERS[1] + 15),
                       cv.FONT_HERSION_PLAIN, 1, 0)

            cv.putText(self.img, '+', (last_known), cv.FONT_HERSION_PLAIN, 1, (0, 0, 255))
            cv.putText(self.img, '+ = Last Known Position', cv.FONT_HERSION_PLAIN, 1, (0, 0, 255))
            cv.putText(self.img, '* = Actual Position', cv.FONT_HERSION_PLAIN, 1, (255, 0, 0))

            cv.imshow('Search Area', self.img)
            cv.moveWindow('Search Area', 750, 10)
            cv.waitKey(500)

