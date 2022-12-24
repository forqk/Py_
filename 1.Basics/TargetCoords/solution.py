shot_count = int(input())

summ_ = 0;

for i in range(0, shot_count):
    x, y = map(float, input().split())
    dist = (x**2 + y**2) ** 0.5

    if(dist <= 10):
        summ_ += 10 - int(dist)
            

print(int(summ_))
    