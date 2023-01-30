def solution(chicken):
    total_chicken = 0
    while chicken >= 10:
        service_chicken = chicken // 10
        remain_coupon = service_chicken + chicken % 10
        total_chicken += service_chicken
        chicken = remain_coupon
    return total_chicken


chicken = 1081
print(solution(chicken))

# 쿠폰      서비스치킨  남은 쿠폰   총 남은 쿠폰    총 치킨
# 1081      108       1        109         108
# 109       10        9         19         118
# 19        1         9         10         119
# 10        1         0          0         120