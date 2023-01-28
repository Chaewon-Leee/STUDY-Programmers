def solution(chicken):
  total_service_chicken = 0
  coupons = chicken

  while coupons >= 10:
    order_chicken = coupons//10
    total_service_chicken += order_chicken
    coupons = coupons%10 + order_chicken

  return total_service_chicken

print(solution(100))