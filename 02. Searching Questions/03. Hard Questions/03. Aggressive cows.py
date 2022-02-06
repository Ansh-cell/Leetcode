def maxDistance(position, m: int) -> int:
    start = 1
    end = max(position)
    answer = float('-inf')
    if m == 2:
        return end - 1
    elif m % 2 != 0 and end % 2 != 0:
        return (start + (end - start) // 2) - 1

    while start <= end:

        mid = start + (end - start) // 2
        total_step = 0
        number_balls = m
        all_balls_in_range = False
        for i in range(max(position)):
            if number_balls == 0:
                all_balls_in_range = True
                break
            else:
                if i == 0:
                    number_balls -= 1
                elif total_step + 1 == mid:
                    number_balls -= 1
                    total_step = 0
                else:
                    total_step += 1

        if number_balls == 0:
            all_balls_in_range = True
        if all_balls_in_range:
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1

    return answer


print(maxDistance([79,74,57,22], 4))
