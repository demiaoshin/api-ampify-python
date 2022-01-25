# Web API Parsing

Parsing a json that is stored on a website online.

### How I did it

I coded this solution in Python. It reads the JSON from the following website link: https://api.ampifymusic.com/packs 

I made use of the urllib python library to read the json file. The code that I used to do this
was acquired from this link: https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script

Then, I store the packs from the json in a variable called `songs`. 

From there, I looped through each song, went through each genre and stored it into another 
list to get the list of all the genres. In this loop, I made sure to get the songs that had the genre
"hip-hop" so that I could output that list as well.

I sorted the list ```genres``` and also applied the `set` function to the list, to remove duplicate genres.

The program outputs a list of all the genres and then a list of all the songs under the genre "hip-hop".

### How to run

Download the project and open the project in an IDE. Then run the ```main.py``` file from there.

