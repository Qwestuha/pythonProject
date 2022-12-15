
enemy = {
        'loc_x': 70,
        'loc_y': 50,
        'color': 'green',
        'health': 100,
        'name': 'Mudillo',
        'image':['image1.jpg', 'image2.jpg' , 'image3.jpg']

}

all_enemis = []

all_enemis.append(enemy)


for x in range(0,10):
        all_enemis.append(enemy.copy())


for ena in all_enemis:
        print(ena)


all_enemis[5]['health']= 30
all_enemis[8]['name'] = 'Kozel'
all_enemis[2]['loc_x'] += 10
print('----------------------')
for ena in all_enemis:
        print(ena)