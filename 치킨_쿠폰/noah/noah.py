def solution(chicken):
    answer = 0
    coupon = 0

    while(chicken != 0):
        free_chicken = chicken // 10
        answer += free_chicken
        coupon += chicken % 10
        if (coupon >= 10):
            answer += coupon // 10
            coupon = coupon % 10
        chicken = free_chicken
    return answer


