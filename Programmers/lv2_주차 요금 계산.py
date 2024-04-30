def cal(basic_time, basic_fee, unit_time, unit_fee, time):
    if time <= basic_time:
        return basic_fee
    if (time - basic_time) % unit_time == 0:
        return basic_fee + ((time - basic_time) // unit_time) * unit_fee
    return basic_fee + (((time - basic_time) // unit_time) + 1) * unit_fee

def solution(fees, records):

    bt, bf, ut, uf = fees
    
    money = {}
    cum = {}
    parking = {}
    
    for i in records:
        time, car, move = i.split()
        money[car] = 0
        cum[car] = 0
        parking[car] = "abs"
    
    for i in records:
        time, car, move = i.split()
        h, m = map(int, time.split(":"))
        time = h * 60 + m
        if parking[car] == "abs":
            parking[car] = time
        else:
            cum[car] += (time - parking[car])
            parking[car] = "abs"

    for i in parking:
        if parking[i] != "abs":
            cum[i] += 1439 - parking[i]
    
    for i in money:
        money[i] = cal(bt, bf, ut, uf, cum[i])
    
    return [money[i] for i in sorted(list(money.keys()))]