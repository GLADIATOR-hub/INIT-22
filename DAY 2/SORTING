def selsort(l1):
     n=len(l1)
     for i in range (0,n-1):
          small=l1[i]
          pos=i
          for j in range (i+1,n):
               if l1[j]<small:
                    small=l1[j]
                    pos=j
                    l1[i],l1[pos]=l1[pos],l1[i]
          print "\t","*after ",i+1,"iteration",l1


def bubsort(a):
     n=len(a)
     for i in range (0,n-1):
          for j in range (0,n-1-i):
               if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
          print "\t","* after ",i+1,"iteration",a


def inssort(a):
     n=len(a)
     for i in range (1,n):
          elt=a[i]
          j=i-1
          while a[j]>elt and j>=0:
               a[j+1]=a[j]
               j=j-1
          a[j+1]=elt
          print "\t"," * after ",i ,"iteration",a
          
while True:
     print "\t","*"*35
     print "\tTO SORT THE ELEMENTS IN A LIST"
     print "\t","*"*35
     print 
     print" \t1.) SELECTION SORTING"
     print" \t2.) BUBBLE SORTING"
     print" \t3.) INSERTION SORTING"
     print" \t4.) EXIT"
     print
     print "\t","*"*35

     n=input("\t=>enter your choice :- ")
     if n==1:
          print
          print "\tYOU HAVE SELECTED SELECTION SORT"
          print
          l1=input("\t#enter the list :-")
          selsort(l1)


     if n==2:
          print
          print "\tYOU HAVE SELECTED BUBBLE SORT"
          print
          a=input("\t#enter the list:-")
          bubsort(a)

     if n==3:
          print
          print "\tYOU HAVE SELECTED INSERTION SORT"
          print
          a=input("\t#enter the list:-")
          inssort(a)

     if n==4:
          print "\tYOU WANT TO EXIT THE LOOP"
          break
     print
     print "\t\t!!! THANK YOU !!!"
     print


