# # from collections import Counter
# # x=int(input())
# # s=[]
# # for i in range(1,x+1):
# #     k=int(input())
# #     s.append(k)
# # c=int(input())
# # d={}
# # for i in range(c):
# #     p,s1=map(int,input().split())
# #     if p in s:
# #         d[s1]=p
# # print(d)
# # print(Counter(d))
# # print(Counter(d).items())
# # print(sum(Counter(d).keys()))
# # print(Counter(d).values())


# s="babad"
# lst={}
# if len(s)<=2 and s==s[::-1]:
#     print(s)
# else:
#     for i in range(len(s)):
#         for j in range(i+1,len(s)):
#             lst[len(s[i:j])]=s[i:j]
#     lst[len(s)]=s
#     k=sorted(lst.keys(),reverse=True)
#     print(k)
#     print(lst)
#     for i in k:
#         m=lst[i]
#         print(m)
#         if m==m[::-1]:
#             print(m)
#             break

class Solution:
    def reverse(self, x: int) -> int:
        k=str(x)
        s1=""
        s2="-"
        if '-'in k:
            re=k[::-1]
            for i in range(len(re)-1):
                if re[i]!=0:
                    s2+=re[i]
            return int(s2)
        else:
            re=k[::-1]
            for i in re:
                if i!=0:
                    s1+=i
            return int(s1)
k=Solution()
print(k.reverse(-123))