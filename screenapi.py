#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import opc, time

numLEDs = 512 * 3
MAP = [
        # Left side, row 0, first 7 pixels
        [[1472, 1472, 1473, 1474, 1475],
        [1476, 1477, 1478, 1479, 1480, 1481],
        [1482, 1483, 1484, 1485, 1486, 1487],
        [1488, 1489, 1490, 1491, 1492, 1493],
        [1495, 1496, 1497, 1498, 1499, 1500],
        [1501, 1502, 1503, 1504, 1505, 1506],
        [1507, 1508, 1509, 1510, 1511, 1512],
        # right side, row 0, next 6 pixels
        [1245, 1246, 1247, 1248, 1249, 1250],
        [1239, 1240, 1241, 1242, 1243, 1244],
        [1233, 1234, 1235, 1236, 1237],
        [1227, 1228, 1229, 1230, 1231],
        [1220, 1221, 1222, 1223, 1224, 1225],
        [1216, 1216, 1217, 1218, 1219]
        ],

        # Left side, row 1, first 7 pixels
        [[1408, 1409, 1410, 1411],
        [1412, 1413, 1414, 1415, 1416, 1417],
        [1418, 1419, 1420, 1421, 1422, 1423],
        [1424, 1425, 1426, 1427, 1428, 1429],
        [1431, 1432, 1433, 1434, 1435, 1436],
        [1437, 1438, 1439, 1440, 1441, 1442],
        [1443, 1444, 1445, 1446, 1447, 1448],
        # right side, row 1, next 6 pixels
        [1181, 1182, 1183, 1184, 1185, 1186],
        [1175, 1176, 1177, 1178, 1179, 1180],
        [1169, 1170, 1171, 1172, 1173],
        [1163, 1164, 1165, 1166, 1167],
        [1156, 1157, 1158, 1159, 1160, 1161],
        [1152, 1152, 1153, 1154, 1155]
        ],

        # Left side, row 2, first 7 pixels
        [[1344, 1345, 1346, 1347],
        [1348, 1349, 1350, 1351, 1352, 1353],
        [1354, 1355, 1356, 1357, 1358, 1359],
        [1360, 1361, 1362, 1363, 1364, 1365],
        [1367, 1368, 1369, 1370, 1371, 1372],
        [1373, 1374, 1375, 1376, 1377, 1378],
        [1379, 1380, 1381, 1382, 1383, 1384],
        # right side, row 2, next 6 pixels
        [1117, 1118, 1119, 1120, 1121, 1122],
        [1111, 1112, 1113, 1114, 1115, 1116],
        [1105, 1106, 1107, 1108, 1109],
        [1099, 1100, 1101, 1102, 1103],
        [1092, 1093, 1094, 1095, 1096, 1097],
        [1088, 1088, 1089, 1090, 1091]
        ],

        # Left side, row 3, first 7 pixels
        [[1280, 1281, 1282, 1283],
        [1284, 1285, 1286, 1287, 1288, 1289],
        [1290, 1291, 1292, 1293, 1294, 1295],
        [1296, 1297, 1298, 1299, 1300, 1301],
        [1303, 1304, 1305, 1306, 1307, 1308],
        [1309, 1310, 1311, 1312, 1313, 1314],
        [1315, 1316, 1317, 1318, 1319, 1320],
        # right side, row 2, next 6 pixels
        [1053, 1054, 1055, 1056, 1057, 1058],
        [1047, 1048, 1049, 1050, 1051, 1052],
        [1041, 1042, 1043, 1044, 1045],
        [1035, 1036, 1037, 1038, 1039],
        [1028, 1029, 1030, 1031, 1032, 1033],
        [1024, 1024, 1025, 1026, 1027]
        ],

        # Left side, row 4, first 7 pixels
        [[896, 897, 898, 899],
        [900, 901, 902, 903, 904, 905],
        [906, 907, 908, 909, 910, 911],
        [912, 913, 914, 915, 916, 917],
        [919, 920, 921, 922, 923, 924],
        [925, 926, 927, 928, 929, 930],
        [931, 932, 933, 934, 935, 936],
        # Next 6 go here
        [477, 478, 479, 480, 481, 482],
        [471, 472, 473, 474, 475, 476],
        [465, 466, 467, 468, 469, 470],
        [459, 460, 461, 462, 463, 464],
        [453, 454, 455, 456, 457, 458],
        [448, 449, 450, 451, 452],
        ],

        # Note that this one probably got
        # wired wrong, so it's out of order
        # Left side, row 5, first 7 pixels
        [[960, 961, 962, 963],
        [964, 965, 966, 967, 968, 969],
        [970, 971, 972, 973, 974, 975],
        [976, 977, 978, 979, 980, 981],
        [983, 984, 985, 986, 987, 988],
        [989, 990, 991, 992, 993, 994],
        [995, 996, 997, 998, 999, 1000],
        # Next 6 go here
        [413, 414, 415, 416, 417, 418],
        [407, 408, 409, 410, 411, 412],
        [401, 402, 403, 404, 405, 406],
        [395, 396, 397, 398, 399, 400],
        [389, 390, 391, 392, 393, 394],
        [384, 385, 386, 387, 388],
        ],

        # Left side, row 6, first 7 pixels
        [[832, 833, 834, 835],
        [836, 837, 838, 839, 840, 841],
        [842, 843, 844, 845, 846, 847],
        [848, 849, 850, 851, 852, 853],
        [855, 856, 857, 858, 859, 860],
        [861, 862, 863, 864, 865, 866],
        [867, 868, 869, 870, 871, 872],
        # Next 6 go here
        [349, 350, 351, 352, 353, 354],
        [343, 344, 345, 346, 347, 348],
        [337, 338, 339, 340, 341, 342],
        [331, 332, 333, 334, 335, 336],
        [325, 326, 327, 328, 329, 330],
        [320, 321, 322, 323, 324],
        ],

        # Left side, row 7, first 7 pixels
        [[768, 769, 770, 771],
        [772, 773, 774, 775, 776, 777],
        [778, 779, 780, 781, 782, 783],
        [784, 785, 786, 787, 788, 789],
        [791, 792, 793, 794, 795, 796],
        [797, 798, 799, 800, 801, 802],
        [803, 804, 805, 806, 807, 808],
        # Next 6 go here
        [285, 286, 287, 288, 289, 290],
        [279, 280, 281, 282, 283, 284],
        [273, 274, 275, 276, 277, 278],
        [267, 268, 269, 270, 271, 272],
        [261, 262, 263, 264, 265, 266],
        [256, 257, 258, 259, 260],
        ],

        # Left side, row 8, first 7 pixels
        [[704, 705, 706, 707],
        [708, 709, 710, 711, 712, 713],
        [714, 715, 716, 717, 718, 719],
        [720, 721, 722, 723, 724, 725],
        [727, 728, 729, 730, 731, 732],
        [733, 734, 735, 736, 737, 738],
        [739, 740, 741, 742, 743, 744],
        # Next 6 go here
        [221, 222, 223, 224, 225, 226],
        [215, 216, 217, 218, 219, 220],
        [209, 210, 211, 212, 213, 214],
        [203, 204, 205, 206, 207, 208],
        [197, 198, 199, 200, 201, 202],
        [192, 193, 194, 195, 196],
        ],

        # Left side, row 9, first 7 pixels
        [[640, 641, 642, 643],
        [644, 645, 646, 647, 648, 649],
        [650, 651, 652, 653, 654, 655],
        [656, 657, 658, 659, 660, 661],
        [663, 664, 665, 666, 667, 668],
        [669, 670, 671, 672, 673, 674],
        [675, 676, 677, 678, 679, 680],
        # Next 6 go here
        [157, 158, 159, 160, 161, 162],
        [151, 152, 153, 154, 155, 156],
        [145, 146, 147, 148, 149, 150],
        [139, 140, 141, 142, 143, 144],
        [133, 134, 135, 136, 137, 138],
        [128, 129, 130, 131, 132],
        ],

        # Left side, row 10, first 7 pixels
        [[576, 577, 578, 579],
        [580, 581, 582, 583, 584, 585],
        [586, 587, 588, 589, 590, 591],
        [592, 593, 594, 595, 596, 597],
        [599, 600, 601, 602, 603, 604],
        [605, 606, 607, 608, 609, 610],
        [611, 612, 613, 614, 615, 616],
        # Next 6 go here
        [93, 94, 95, 96, 97, 98],
        [87, 88, 89, 90, 91, 92],
        [81, 82, 83, 84, 85, 86],
        [75, 76, 77, 78, 79, 80],
        [69, 70, 71, 72, 73, 74],
        [64, 65, 66, 67, 68],
        ],

        # Left side, row 11, first 7 pixels
        [[512, 513, 514, 515],
        [516, 517, 518, 519, 520, 521],
        [522, 523, 524, 525, 526, 527],
        [528, 529, 530, 531, 532, 533],
        [535, 536, 537, 538, 539, 540],
        [541, 542, 543, 544, 545, 546],
        [547, 548, 549, 550, 551, 552],
        # Next 6 go here
        [29, 30, 31, 32, 33, 34],
        [23, 24, 25, 26, 27, 28],
        [17, 18, 19, 20, 21, 22],
        [11, 12, 13, 14, 15, 16],
        [5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4],
        ],
    ]



class ScreenApi:

    def __init__(self):
        self.client = opc.Client('localhost:7890')
        self.leds =[ (0,0,0) ] * numLEDs
        self.led_map = MAP

    def draw(self, pixels):
        for x in range(len(pixels)):
            for y in range(len(pixels[0])):
                try:
                    led_list = self.led_map[x][y]
                    if (pixels[x][y] != (0,0,0)):
                        print("led list is %s" % str(led_list))
                    for led in led_list:
                        self.leds[led] = pixels[x][y]
                except:
                    pass
        self.client.put_pixels(self.leds)

if __name__ == '__main__':
    api = ScreenApi()
    # time.sleep(20)
    # screen = [[(255,0,0) for x in range(13)] for y in range(12)]
    # api.draw(screen)
    # time.sleep(2)
    # screen = [[(0,0,0) for x in range(13)] for y in range(12)]
    # api.draw(screen)
    # time.sleep(2)
    for r in range(12):
        for c in range(13):
            screen = [[(0,0,0) for x in range(13)] for y in range(12)]
            screen[r][c] = (255,255,255)
            # print(screen)
            api.draw(screen)
            i = raw_input()
            # time.sleep(.04)

            # import pdb; pdb.set_trace()
