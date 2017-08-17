Last login: Thu Aug 17 11:35:59 on ttys000
luoyuhuadeAir:~ luoyuhua$ python3 ex01.py
/Library/Frameworks/Python.framework/Versions/3.6/Resources/Python.app/Contents/MacOS/Python: can't open file 'ex01.py': [Errno 2] No such file or directory
luoyuhuadeAir:~ luoyuhua$ cd documents
luoyuhuadeAir:documents luoyuhua$ cd py104
luoyuhuadeAir:py104 luoyuhua$ ls
0w1				ex11.py
0w1.py				ex12.py
0w10.py				ex13.py
copied.txt			ex14.py
e09.py				ex15.py
ex01.py				ex15_sample.txt
ex02.py				ex16.py
ex03.py				ex17.py
ex04.py				ex18.py
ex05.py				ex19.py
ex051.py			ex20.py
ex06.py				ex21.py
ex07.py				test.txt
ex08.py				终端存储的输出
ex09.py				终端存储的输出20170814
ex10.py				终端存储的输出ex03
ex11-14
luoyuhuadeAir:py104 luoyuhua$ python3 ex01.py
Hello World!
Hello Again
I like typing this.
This is fun.
Yay! Printing.
I'd much rather you 'not'.
I"said" do not touch this .
luoyuhuadeAir:py104 luoyuhua$ python3 ex02.py
I could have code like this.
This will run.
luoyuhuadeAir:py104 luoyuhua$ python3 ex03.py
I will now count my ckickens:
hens 30.0
roosters 97
Now I will count the eggs:
6.75
Is it true that 3 + 2 < 5 - 7?
False
what is 3 + 2?  5
what is 5 - 7?  -2
oh, that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
luoyuhuadeAir:py104 luoyuhua$ python3 ex04.py
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We can transport 120.0 people today
We have 90 to carpool today.
We need to put about  3.0 in each car.
luoyuhuadeAir:py104 luoyuhua$ python3 ex05.py
let's talk about Zed A Shaw.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got blue eyes and Brown hair.
His teeth are usually white depending on the coffee.
If I add 35, 74, and 180 I get 289.
luoyuhuadeAir:py104 luoyuhua$ python3 ex06.py
There are 10 types of people.
Those who know binary and those who don't.
I said: 'There are 10 types of people.'.
I also said: 'Those who know binary and those who don't.'.
Isn't that joke so funny?! False
This is the left side of ...a string with a right side.
luoyuhuadeAir:py104 luoyuhua$ python3 ex07.py
Mary had little lamb.
Its fleece was white as snow.
And everywhere that Mary went.
..........
cheese Burger
luoyuhuadeAir:py104 luoyuhua$ python3 ex08.py
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing," 'So I said goodnight.'
luoyuhuadeAir:py104 luoyuhua$ python3 ex09.py
  File "ex09.py", line 10
    There's something going on here.
                                   ^
SyntaxError: EOL while scanning string literal
luoyuhuadeAir:py104 luoyuhua$ python3 ex09.py
Here are the days: Mon Tue Wed Thu Fri Sat Sun
Here are the months: Jan
Feb
Mar
Apr
May
Jun
Ju1
Aug


There's something going on here.

With the three double-quotes.

We'll be able to type as much as we like.

Even 4 lines if we want, or 5, or 6.


luoyuhuadeAir:py104 luoyuhua$ python3 ex10.py
	I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
	* cat food
	* Fishies
	* catnip
	* Grass


luoyuhuadeAir:py104 luoyuhua$ python3 ex11.py
How old are you?35
How tall are you?6'
How much do you weigh180lbs
So, you're '35' old, "6'" tall and '180lbs' heavy.
luoyuhuadeAir:py104 luoyuhua$ 
luoyuhuadeAir:py104 luoyuhua$ python3 ex12.py
How old are you?35
How tall are you?6'2"
How much do you weigh?180lbs
so,you're '35' old, '6\'2"' tall and '180lbs' heavy.
luoyuhuadeAir:py104 luoyuhua$ python3 ex13.py first 2nd 3rd
The script is called: ex13.py
Your first variable is: first
Your second variable is: 2nd
your third variable is: 3rd
luoyuhuadeAir:py104 luoyuhua$ python3 ex13.py cheese apples bread
The script is called: ex13.py
Your first variable is: cheese
Your second variable is: apples
your third variable is: bread
luoyuhuadeAir:py104 luoyuhua$ python3 ex14.py Zed
Hi Zed, I'm the ex14.py script.
I'd like to ask you a few questions.
Do you like me Zed?
>yes
where do you live Zed?
>America
what kind of computer do you have?
>Mac

Alright, so you said 'yes' about liking me .
You live in 'America' . Not sure where that is .
And you have a 'Mac' computer . Nice .

luoyuhuadeAir:py104 luoyuhua$ python3 ex15.py ex15_sample.txt
Here's your file 'ex15_sample.txt':

This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

Type the filename again:
>ex15.sample.txt
Traceback (most recent call last):
  File "ex15.py", line 11, in <module>
    txt_again = open(file_again)
FileNotFoundError: [Errno 2] No such file or directory: 'ex15.sample.txt'
luoyuhuadeAir:py104 luoyuhua$ python3 ex15.py ex15_sample.txt
Here's your file 'ex15_sample.txt':

This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

Type the filename again:
>
Traceback (most recent call last):
  File "ex15.py", line 11, in <module>
    txt_again = open(file_again)
FileNotFoundError: [Errno 2] No such file or directory: ''
luoyuhuadeAir:py104 luoyuhua$ python3 ex15.py ex15_sample.txt
Here's your file 'ex15_sample.txt':

This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

Type the filename again:
>ex15_sample.txt

This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

luoyuhuadeAir:py104 luoyuhua$ python3 ex16.py test.txt
We're going to erase 'test.txt'.
If you don't want that, hit CTRL-C(^C).
If you do want that, hit RETURN.
?
Opening the file...
Truncating the file. Goodbye!
Now I'm going to ask you for three lines.
line 1: To all the people out there.
line 2: I say I don't like my hair.
line 3: I need to shave it off.
I'm going to write these to the file.
And finally, we close it.
luoyuhuadeAir:py104 luoyuhua$ python3 ex17.py test.txt copied.txt
Copying from test.txt to copied.txt
The input file is 81 bytes long
Does the output file exist? True
Ready,hit RETURN to continue, CTRL-C to abort.
Alright, all done.
luoyuhuadeAir:py104 luoyuhua$ cat copied.txt
To all the people out there.
I say I don't like my hair.
I need to shave it off.
luoyuhuadeAir:py104 luoyuhua$ python3 ex18.py
arg1: 'Zed', arg2: 'Shaw'
arg1: 'Zed', arg2: 'Shaw'
arg1: 'First!' 
I got nothin'.
luoyuhuadeAir:py104 luoyuhua$ python3 ex19.py
We can just give the function numbers directly:
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket.

OR, we can use variables from our script:
You have 10 cheeses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can even do math inside too:
You have 30 cheeses!
You have 11 boxes of crackers!
Man that's enough for a party!
Get a blanket.

And we can combine the two, variables and math:
You have 110 cheeses!
You have 1050 boxes of crackers!
Man that's enough for a party!
Get a blanket.

luoyuhuadeAir:py104 luoyuhua$ python3 ex20.py test.txt
First let's print the whole file:

['To all the people out there.\n', "I say I don't like my hair.\n", 'I need to shave it off.\n']
Now let's rewind, kind of like a tape.
Let's print three lines:
1 To all the people out there.

2 I say I don't like my hair.

3 I need to shave it off.

luoyuhuadeAir:py104 luoyuhua$ python3 ex21.py
Let's do some math with just functions!
ADDING 30 + 5
SUBTRVTING 78 -4
MULTIPLYING 90 * 2
DIVIDING 100 / 2
Age:35, Height:74, Weight:180, IQ:50
Here is a puzzle.
DIVIDING 50 / 2
MULTIPLYING 180 * 25
SUBTRVTING 74 -4500
ADDING 35 + -4426
That becomes: -4391.0 can you do it by hand?
luoyuhuadeAir:py104 luoyuhua$ 
