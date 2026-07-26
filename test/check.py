data = []

with open('list.txt', 'r') as file:
    for line in file:
        data.append(line.strip())

st_data = []
with open('schemes with req.txt', 'r') as file:
    for line in file:
        st_data.append(line.strip())

# print(data)
# print(st_data)

for scheme in st_data:
    sc = scheme.split('-')[1]
    if sc not in data:
        print(sc)


# def missingNumber(nums) -> int:
#     t_sum = 0
#     max_sum = 0
#     for idx, num in enumerate(nums, start=1):
#         t_sum += num
#         max_sum += idx
#     return max_sum - t_sum
#
# print(missingNumber([2,1,3]))
