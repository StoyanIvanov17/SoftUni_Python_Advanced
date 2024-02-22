from collections import deque

food = deque(map(int, input().split(', ')))
stamina = deque(map(int, input().split(', ')))

day = 1

all_peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

peaks_conquered = []


while True:
    if len(peaks_conquered) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

    if day > 7 or not food or not stamina:
        print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')
        break

    current_food = food.pop()
    current_stamina = stamina.popleft()
    result = current_food + current_stamina

    current_peak = all_peaks.popleft()

    if result >= current_peak[1]:
        peaks_conquered.append(current_peak[0])
    else:
        all_peaks.appendleft(current_peak)

    day += 1

if peaks_conquered:
    print('Conquered peaks:')
    for peak in peaks_conquered:
        print(peak)