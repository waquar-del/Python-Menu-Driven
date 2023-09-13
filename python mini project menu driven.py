#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while(True):
    print("WELCOME TO MENU-DRIVEN PROGRAM.\n")
    print("1.List\n2.Tuple\n3.String\n4.Dictionary\n5.Set\n6.Exit")
    ch=int(input("Enter a choice:"))
    if(ch==1):
        while(True):
            print("1.Definition of List\n2.To add elements in a list\n3.To delete elements from a list\n4.Exit.")
            ch1=int(input("Enter a choice:"))
            if(ch1==1):
                print("Definition of List: The list is a dynamic array, along with the linear sequence, and also provides several built-in functions to perform various operations on data stored in it")
                print("The data stored in the list is ordered. Python lists are mutable an can contain duplicate elements as each element is identified by a unique number or position as an index.")
            elif(ch1==2):
                while(True):
                    print("1.Single element\n2.Multiple element\n3.To add at a specific position\n4.Exit")
                    ch11=int(input("Enter a choice in list:"))
                    if(ch11==1):
                        l1=["mango","banana","orange",22]
                        print(l1)
                        b=input("Enter the element to add:")
                        l1.append(b)
                        print(l1)
                    elif(ch11==2):
                        l1=["mango","banana","orange",22]
                        print(l1)
                        l2=["tomato","potato",512,"Ginger"]
                        print(l2)
                        l1.extend(l2)
                        print(l1)
                    elif(ch11==3):
                        l1=["mango","banana","orange",22]
                        print(l1)
                        b1=int(input("Enter the element to add:"))
                        a=input("Enter position:")
                        l1.insert(a,b1)
                        print(l1)
                    else:
                        break
            elif(ch1==3):
                while(True):
                    print("1.To delete random element\n2.To delete element based on index\n3.To delete element based on value\n4.To clear the list\n5.To delete complete list\n6.Exit")
                    ch111=int(input("Enter a choice in list:"))
                    if(ch111==1):
                        l1=["mango","banana","orange",22]
                        print(l1)
                        l1.pop()
                        print(l1)
                    elif(ch111==2):
                        l1=["mango","banana","orange",22]
                        print(l1)
                        i=input("Enter index:")
                        l1.pop(i)
                        print(l1)
                    elif(ch111==3):
                        l1=["mango","banana","orange",22]
                        print(l1)
                        i=input("Enter value:")
                        l1.remove(i)
                        print(l1)
                    elif(ch111==4):
                        l1=["mango","banana","orange",22]
                        print(l1)
                        l1.clear()
                        print(l1)
                    elif(ch111==5):
                        l1=["mango","banana","orange",22]
                        print(l1)
                        del l1
                    else:
                        break
            else:
                break
    elif(ch==2):
        print("Definition of Tuple: A tuple represents a sequence of any objects seperated by commas and enclosed in parenthesis. A tuple is immutable which means it cannot be changed, and it is used to represent fixed collection of items.")
    elif(ch==3):
        print("Definition of String: A string is a data structure in python that represents a sequence of characters. Strings are used widely in many different applications, such as storing and manipulating text data, representing names, addresses and other types of data that can be represented as text.")
        print("String is an immutable datatype i.e. it's value cannot be updated.")
    elif(ch==4):
        while(True):
            print("1.Definition of Dictionary\n2.To add items in Dictionary\n3.To delete items from Dictionary\n4.Exit.")
            ch4=int(input("Enter a choice in dictionary:"))
            if(ch4==1):
                print("Definition of Dictionary: Python dictionary is one of the supported data types in python. It is an unordered collection of elements. The elements in dictionaries are stored as key-value pairs. Dictionaries are indexed by keys.")
            elif(ch4==2):
                while(True):
                    print("1.Single element\n2.Multiple element\n3.Exit")
                    ch41=input("Enter a choice which type you want:")
                    if(ch41==1):
                        d1={"Name":"john","Age":50}
                        print(d1)
                        d1["Address"]="washington"
                        print(d1)
                    elif(ch41==2):
                        d1={"Name":"john","Age":50}
                        print(d1)
                        d2={"Address":"washington","Occupation":"farmer"}
                        print(d2)
                        d1.update(d2)
                        print(d1)
                    else:
                        break
            elif(ch4==3):
                while(True):
                    print("1.To delete particular key value\n2.To clear the dictionary\n3.To delete entire dictionary\n4.Exit")
                    ch411=int(input("Enter a choice in dic:"))
                    if(ch411==1):
                        d1={"Name":"john","Age":50}
                        print(d1)
                        del d1["Name"]
                        print(d1)
                    elif(ch411==2):
                        d1={"Name":"john","Age":50}
                        print(d1)
                        d1.clear()
                        print(d1)
                    elif(ch411==3):
                        d1={"Name":"john","Age":50}
                        print(d1)
                        del d1
                    else:
                        break
            else:
                break
                        
    elif(ch==5):
        while(True):
            print("1.Definition of Set\n2.To add elements in a Set\n3.To delete elements from a Set\n4.Exit.")
            ch5=int(input("Enter a choice in set:"))
            if(ch5==1):
                print("Definition of Set: A set is an unordered collection datatype that is iterable, mutable and has no duplicate elements. The major advantage of using a set is that it has a highly optimized method for checking whether a specific element is contained in the set.")
            elif(ch5==2):
                while(True):
                    print("1.To add single elements\n2.To add multiple elements\n3.Exit")
                    ch51=int(input("Enter a choice which type you want:"))
                    if(ch51==1):
                        s1=set([11,120,130,140])
                        print(s1)
                        i=int(input("Enter element:"))
                        s1.add(i)
                        print(s1)
                    elif(ch51==2):
                        s1=set([11,120,130,140])
                        print(s1)
                        s2=set([150,160,170,180])
                        print(s2)
                        s1.update(s2)
                        print(s1)
                    else:
                        break
            elif(ch5==3):
                while(True):
                    print("1.To delete a random element\n2.To delete element using remove()\n3.To delete element using discard()\n4.To clear the set\n5.To delete the entire set\n6.Exit")
                    ch511=int(input("Enter a choice which type of deletion you want:"))
                    if(ch511==1):
                        s1=set([11,120,130,140])
                        print(s1)
                        s1.pop()
                        print(s1)
                    elif(ch511==2):
                        s1=set([11,120,130,140])
                        print(s1)
                        i=int(input("Enter the element to be removed:"))
                        s1.remove(i)
                        print(s1)
                    elif(ch511==3):
                        s1=set([11,120,130,140])
                        print(s1)
                        i=int(input("Enter the element to be discarded:"))
                        s1.discard(i)
                        print(s1)
                    elif(ch511==4):
                        s1=set([11,120,130,140])
                        print(s1)
                        s1.clear()
                        print(s1)
                    elif(ch511==5):
                        s1=set([11,120,130,140])
                        print(s1)
                        del s1
                    else:
                        break
            else:
                break
    else:
        break
print("PROGRAM TERMINATED.")


# In[ ]:




