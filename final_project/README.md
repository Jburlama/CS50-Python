# Top Places

#### Video Demo
https://youtu.be/VXLiQUHrdoY?si=r8RT33VF6XaKe6-J

https://github.com/user-attachments/assets/4a37ed6e-67da-40bc-ac88-5bc1e251de66


#### Description

Top Places is a Python script that uses Google Maps API to search the top places in a certain area based on ratings

##### Usage

In the command line execute the program by typing ```python3 project.py```.
You'll be prompted for what you are looking for, such as a bar, restaurant, museum, park, hotel ...
Then, you'll be prompted to tell the script where to search for what you are looking for. It can be any country, city, street address ...
At last, you'll be prompted for how many results you want to see.

After that, the program will output a grid, with the establishment names, ratings, and the address of the place. Order by rating

Another way of using the program is to pass the information directly in the command line, ```python3 project.py <what> <where> <how many>```
where the first parameter would be what you are looking for, the second where, and the third how many results you want to output. example
```python3 project.py restaurants Porto 5```, this would output the top 5 best rating restaurants in Porto


##### Improvements

At the current stage of the program, it assumes that the user will use the program correctly.
Future improvements would be error-checking more thoroughly, and making the program more robust against not valid inputs


##### Side notes

This program was made for educational purposes.
It uses the free trial key for the Google Maps API, and it has a duration of three months.
So the program will lose its functionality by the end of February 2025
