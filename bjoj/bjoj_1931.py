def max_meetings(meetings):
    meetings.sort(key=lambda x: x[1])

    count = 0
    end_time = 0

    for meeting in meetings:
        start, end = meeting
        if start >= end_time:
            end_time = end
            count += 1

    return count

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

print(max_meetings(meetings))
