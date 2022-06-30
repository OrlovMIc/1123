s=str(input())
n=len(s)
for i in range(0,int(n/2)):
    if s[i]>s[n-1-i]:
       s=s[:n-1-i]+s[i]+s[n-i:]
    elif s[i]<s[n-1-i]:
       k=1
       while s[n-1-i-k]=='9':
         s=s[:n-1-k-i]+'0'+s[n-k-i:]
         k=k+1 
       s=s[:n-1-k-i]+str(int(s[n-1-k-i])+1)+s[n-k-i:]
       s=s[:n-1-i]+s[i]+s[n-i:] 
print(s)
