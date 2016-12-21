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
        [[1408, 1408, 1409, 1410, 1411],
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
        [[1344, 1344, 1345, 1346, 1347],
        [1348, 1349, 1350, 1351, 1352, 1353],
        [1354, 1355, 1356, 1357, 1358, 1359],
        [1360, 1361, 1362, 1363, 1364, 1365],
        [1367, 1368, 1369, 1370, 1371, 1372],
        [1373, 1374, 1375, 1376, 1377, 1378],
        [1379, 1380, 1381, 1382, 1383, 1384]
        # Next 6 go here
        ],

        # Left side, row 3, first 7 pixels
        [[1280, 1280, 1281, 1282, 1283],
        [1284, 1285, 1286, 1287, 1288, 1289],
        [1290, 1291, 1292, 1293, 1294, 1295],
        [1296, 1297, 1298, 1299, 1300, 1301],
        [1303, 1304, 1305, 1306, 1307, 1308],
        [1309, 1310, 1311, 1312, 1313, 1314],
        [1315, 1316, 1317, 1318, 1319, 1320]
        # Next 6 go here
        ],

        # right side row 0, first 7 pixels
        # [[
        # # Next 6 go here
        # ],

        [[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22],
        [23, 24, 25, 26, 27, 28],
        [29, 30, 31, 32, 33, 34]]
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

api = ScreenApi()
for r in range(12):
    for c in range(13):
        screen = [[(0,0,0) for x in range(13)] for y in range(12)]
        screen[r][c] = (255,255,255)
        # print(screen)
        api.draw(screen)
        i = raw_input()
        # time.sleep(.5)

        # import pdb; pdb.set_trace()
