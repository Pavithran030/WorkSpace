# # n=int(input())
# # for i in range(n):
# #     for j in range(2,n):
# #         if i%j==0:
# #             break
# #         print(i,end=" ")

# def student_info(name, **kwargs):
#     print("Student Information:")
#     print("Name:", name)
#     if 'age' in kwargs:
#         print("Age:", kwargs['age'])
#     if 'grade' in kwargs:
#         print("Grade:", kwargs['grade'])
#     if 'school' in kwargs:
#         print("School:", kwargs['school'])

# # Example usage:
# student_info("Alice", age=15, grade=10, school="ABC High School")

def twoSum(nums,targets):
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = targets - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []
print(twoSum([2,7,11,15],9))