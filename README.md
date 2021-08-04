# Tier List Stocker

This is a homemade Tier List created to track the ranking I give to categories like hobbies, dreams, priorities, etc.

I chose to make this personal project so I can practice my coding skills and only get what I want, on my computer. I try to start with a simple implementation.

## Starting the (BE) service
The program has been written in Javascript, and you need it to 
## Using the FE GUI
The program is located into *gui* folder and the file to be run is *main.py*. 
As it is a python program, you need python installed on your computer to run it.
Here is the command to run it from the root of the project (tierliststocker):
`python gui/main.py`
There are 4 actions possible in the GUI:

* Select tierlist: The tierlist to read and write. Default one is *tierlist*.
* Get tierlist: Displays the selected tierlist, i.e. the items by rank.
* Add item to tier: Item an item in the tierlist by specifying its rank.
* Remove item: Remove an item from the tierlist.
### Gallery
![Menu](/screenshots/gui_menu.png)



## BE
* Do the move operation
* Handle all anormal cases in the requests 
* Handle the case where the request is garbage. Or let the API response be bad. To see.
* Handle better case of checking folder not found and file not found

## FE - GUI
* Allow to choose the tierlist. For now all is hardcoded to "tierlist" // OK
* Allow to chosse the DB location. Or save them in the user's home.
* Change item separator: instead of ",", choose something else like "|". 
* Inform in a simple text if we have success or error // OK
* Inform in a simple text if we have warning
* Handle errors, like DB down // OK
* Solve bug: response message overwriting over each other. Present when adding and deleting items
* Reingineer this big mqin_support class 
* Bug: When in the add item none is selected, display a message to select something 
* Think about a way to automate GUI testing. Like behavior testing 

## Hard
* Concurrency when writing to file