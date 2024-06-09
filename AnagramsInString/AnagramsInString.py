

def findAnagrams(s,p):
   if len(s) < 1 and len(p) < 1:
       return 0

   index = 0
   result = []

   while(index <= (len(s) - len(p))):
       tempString = s[index:(index + len(p))]
       temp = p

       for i in range(0,len(tempString)):
           temp = temp.replace(tempString[i],'',1)
       
       if len(temp) == 0:
           result.append(index)
       index +=  1

   return result



if __name__ == '__main__':
      print(findAnagrams("baa","aa"))
