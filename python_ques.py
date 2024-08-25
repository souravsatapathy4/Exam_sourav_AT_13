                                             '''python_block'''
#1.What is decorator , write a decorator?
'''A decorator is itself a function that takes another function as an argument 
and returns a new function that adds some kind of behavior to the original function.'''
#Example
def decore(is_prime):
    def is_even(n):
        if n%2==0:
            return f'{n}is a even number'
        return is_even
    return is_prime

@decore

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(3000))
#2. What is lambda expression, write a lambda expression?
'''A lambda expression in Python is a  anonymous function defined with the lambda keyword.
 lambda functions can have any number of arguments but only one expression.'''
add = lambda a,b : a+b

print(add(10,20))

#3. WAF, S = ‘Hello everyone’, count the occurrence of each char, return those
#repetitive character , without using any inbuilt function.

S = 'Hello everyone'

char_count = {}

for c in S:
    if c in char_count:
        char_count[c] += 1
    else:
        char_count[c] = 1

repetitive_chars = []
for char in char_count:
    if char_count[char] > 1:
        repetitive_chars.append(char)

print(repetitive_chars)
#4.WAF , Reverse a string words.
#> Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function

def reverse_words(input_string):
    words = []
    length = len(input_string)
    space = " "
    start = 0
    for i in range(length):
        if input_string[i] == space:
            words.append(input_string[start:i])
            start = i + 1
        elif i == length - 1:
            words.append(input_string[start:i + 1])
    reversed_string = ""
    for i in range(len(words) - 1, -1, -1):
        reversed_string += words[i]
        if i != 0:
            reversed_string += space

    return reversed_string


#6.Sort a list integer element without using inbuilt function?
li = [20,45,65,85,10,24]

def sort(li):
    n = len(li)
    for i in range(n):
        for j in range(0, n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

li = [20, 45, 65, 85, 10, 24]
sorted_list = sort(li)
print(sorted_list)

#7. Li = [1,2,3,4], Li2 = [10,20,30]
#Result = {1:10,2:20,3:30}
#Take a two list a parameter, return dictionary, look like above result.

def create_dict(list1, list2):
    result = {}
    i = 0
    while i < len(list1) and i < len(list2):
        result[list1[i]] = list2[i]
        i += 1
    return result

list1 = [1, 2, 3]
list2 = [10, 20, 30]

result = create_dict(list1, list2)
print(result)

#9 What is exception handling , how handel the exception in python , explain with each block
'''Exception handling is a way to manage errors and unexpected situations that occur during the execution of a program.'''


#try block: This is where you write the code that you want to test for exceptions. If an error occurs in this block, Python will jump to the except block.
try:
    '''code'''
    result = 10 / 0
#except block:in this block we can raise exception
except ZeroDivisionError:
    print("You can't divide by zero!")

#finally block: this block will execute anyway if error will there or its not there
finally:
    # Code that runs no matter what
    print("Execution completed.")

#10. Difference between Moudle and Packages
'''Modules are single files containing Python code.
Packages are directories containing multiple modules and init file'''

#11. Difference between List vs tuple vs set vs dictionary?
'''list: 1.written with in [],The list allows duplicate elements ,Example: [1, 2, 3, 4, 5]
tuple:1.written with in (),Tuple allows duplicate elements,Example: (1, 2, 3, 4, 5)
set:1.written with in {},The Set will not allow duplicate elements,Example: {1, 2, 3, 4, 5}
dict:1.written with in {},The dictionary doesn’t allow duplicate keys.,{1: “a”, 2: “b”, 3: “c”, 4: “d”, 5: “e”}'''

#12. What is Garbage Collection?
'''The process of finding and deleting objects which are no longer in use'''
a=2
a=3
print(a)
'''here is a example where first a value is 2 and its printing 2 but when we assign a=3 then the first value becomes garbage'''




#13.What is list comprehension , write code in list comprehension?
'''its is a way to create a new list in a sigle line of code'''

pall_list=[i for i in range(1,501)if str(i)==str(i)[::-1]]
print(pall_list)

#15.Explain break, continue, pass with code?
#break
'''The break statement in Python is used to terminate the loop'''
for  loop:
    '''statement(s)'''
    if condition:
        break
     '''statement'''
#continue
'''instead of terminating the loop, it forces to execute the next iteration of the loop'''
for loop:
    '''statement'''
    if condition:
        continue
    '''statement'''
#pass
'''The pass statement in Python is used when a statement is required but you do not want any command or code to execute.'''

s = "sourav"
for i in s:
    pass



                                                '''selenium'''
#1What is webdriver?
'''WebDriver is a tool used in Selenium for automating web applications.
It provides a way to control web browsers programmatically. With WebDriver, you can simulate user interactions such 
as clicking buttons, entering text into forms, and navigating through web page'''
#2How to handel selective dropdown, write a snippet for it?
'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
Select(driver.find_element(By.TAG_NAME,'select')).select_by_visible_text('Option2')'''

#3. How to handel auto suggestive dropdown, write a snippet for it.?
'''from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"autocomplete").send_keys("ind")
list_country = driver.find_elements(By.XPATH,"//ul/li[@class='ui-menu-item']")
for country in list_country:
    if country.text == "india":
        print(country.text)
        country.click()
        break'''
#4How to handel multiple windows and back to current window?
''' we can click on linktext so it will open new window and we can use indexing window method to switch between windows
we can use driver.switch_to.window(driver.window_handles[1]) method 
to switch to new window . there we can perform our task by finding elements then to switch back to our default windows 
we can use driver.switch_to.window(driver.window_handles[0]) '''

#6.Explain the wait mechanism, write syntax and snippet for it.
'''In Selenium WebDriver, waiting mechanisms are used to handle the timing issues
that can occur when web elements are dynamically loaded or when their states change'''
'''implicity wait :These are used to set a default waiting time for all elements
  driver.implicitly_wait(time)
'''
'''explicity wait:These are used to wait for a specific condition to occur before proceeding
 from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, timeout)
element = wait.until(EC.condition(locator))
'''
#7.How to handle dynamic web element.
'''by using explicity wait we can handle dynamic web element'''
#8.How many locators in selenium
'''there are 8 types of locator in selenium , Ex: ID,Class,tag_name,xpath,css_selector,link_text,partial_link_text,name'''
#9In web table want to fetch 3rd Column , 3rd row data, write a xpath for it.
'''//table//tr[3]//td[3]'''
#10
'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get(" https://www.nseindia.com/")
hover_element = driver.find_element(By.XPATH,"(//li/a[@id='link_2'])[1]")
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
driver.find_element(By.XPATH,"//a[contains(text(),'Pre-Open Market')]").click()
prev_close=driver.find_element((By.XPATH,"//tbody/tr[2]/td[3]"))
print(prev_close.text)'''

                                              '''Unix'''
#1.Copy a file one directory to another directory
'''cp source file Destination'''
#3difference between chown vs chmod?
'''chown is used to change the ownership of files and directories.
   chmod is used to change the file permissions (read, write, and execute) for files and directories.'''
#4In a directory a find a file name abc.txt?
'''find [directory] -name [filename]'''
#6How to list directories in Unix?
'''ls -d */'''

                                               '''Sql'''
#1.Explain about the DML,DDL,TCL,DQL commands
'''DDL commands are used to define and modify the structure of database objects like tables, indexes, and schemas.

   DML commands are used to manipulate and manage data within database objects. These commands allow for the insertion, updating, and deletion of records.
    
   TCL commands manage transactions in a database, ensuring data integrity and consistency. Transactions are sequences of operations performed as a single logical unit.
    
   DQL: Retrieves data from the database (primarily SELECT). '''
#2.What is join, explain about the all joins?
'''INNER JOIN: Matches rows from both tables.
LEFT JOIN: All rows from the left table and matching rows from the right table.
RIGHT JOIN: All rows from the right table and matching rows from the left table.
FULL JOIN: All rows from both tables, with NULLs where there is no match.
CROSS JOIN: Cartesian product of both tables.
SELF JOIN: Joins a table with itself.'''
#3Difference between Joins vs Subquery?
'''Joins are typically used to combine data from multiple tables into a single result set and are generally more efficient.
Subqueries are used to perform operations based on the results of other queries and are useful for complex filtering 
and computation but can be less efficient, especially if correlated.'''



