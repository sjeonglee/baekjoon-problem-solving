input_values = list(map(int, input().split(' ')))
p_yang = input_values[0]
p_who = input_values[1]
p_mix = input_values[2]
q_yang = input_values[3]
q_who = input_values[4]
q_mix = min(q_yang, q_who) * 2
q_left_yang = q_yang - q_mix / 2
q_left_who = q_who - q_mix / 2

p_criteria = p_yang if q_left_yang > 0 else p_who

if p_mix * 2 >= p_yang + p_who: # 반반 치킨 가격이 각각 사서 합치는 것보다 저렴한 경우
  price = p_yang * q_yang + p_who * q_who
elif p_mix * 2 <= p_criteria: # 반반 치킨 가격이 각각의 가격보다 저렴한 경우
  price = p_mix * max(q_yang, q_who) * 2
else:
  price = p_mix * q_mix + p_yang * q_left_yang + p_who * q_left_who

price = int(price)
print(price)