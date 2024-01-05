# Coffee Machine Simulation


## Jorge Mateos Ortega - Cardiff (UK)


## Video Demo: <https://youtu.be/OWGlX5fiUoQ>


## Description:

This Python program simulates a basic coffee machine, allowing users to insert coins, choose a coffee, and receive change. The coffee machine has a set of predefined coffees and accepts different coin denominations in pound sterling. It also has an internal system that takes ingredients to make the coffees and accumulates the money introduced.


## Features

- **take_coin**: Users can insert coins of various denominations.

- **validate_coin**: The coffee machine can check if the coin is valid.

- **choose_coffee**: Users can choose from a selection of predefined coffees (available in the "MENU" section).

- **check_credit**: The program checks if the user has enough credit to purchase the chosen coffee.

- **check_ingredients**: It verifies if there are sufficient coffee grains and milk for the chosen coffee.

- **fill_ingredients**: If ingredients are low, the machine can be refilled.

- **give_change**: The machine returns the user's change.

- **convert_to_coins**: The program converts the change into a combination of coins.

- **make_coffee**: If there's enough credit and ingredients, the coffee machine dispenses the chosen coffee.

- **main**: Our main function gives you an example of the functionality of the Coffee_machine class.




## Getting Started

**1. Navigate to the project directory:**

    cd project


**2. Install requirements:**

    pip install -r requirements.txt


**3. Run the coffee machine simulation:**

    python project.py


**4. Follow the on-screen instructions to insert coins, choose a coffee, and interact with the coffee machine.**


## Usage

- **Insert coin**: Enter "**i**" and provide the coin value.

    - When entering the coin value it will accept valid sterling coins (with or without the "**£**")


- **Choose coffee**: Enter "**c**" and select a coffee.

    - The range of coffees available is in the "MENU" section


- **Exit**: Enter "**e**" to exit the program.



## MENU

- **latte**.................................*£1.00*

- **cortado**..........................*£0.75*

- **espresso**.........................*£0.50*

- **double espresso**........*£0.85*


## Developer's thoughts

When facing the idea of creating a virtual vending coffee machine our main objective was to create the full user experience. We wanted you to be able to insert coins one by one (We don't accept cards, we're very sorry!) and choose your coffee. The idea was also to be able to feel the pain when the machine has run out ingredients (but don't panic, our main functions refills them automatically so you don't have to call maintenance!). Also, don't try to trick our machine! We only accept pound sterling, I'm afraid. But you will have your change optimally given to you, so no more rattling of unnecessary cash in your pocket!

When doing that, we realised that we couldn't miss the chance to create different models of coffee machines in the future, so why not make it a class? By doing that, we have a robust coffee machine class that can be the future of coffee machines!

We wanted to make the class simple, so if you want to change the menu and/or the coins accepted (maybe you have a note receiver as well?) you only have to change it at the top! Every function in the class calls the menu and the coins if needed, so the modding is simple!

We had problems related to floating-point precission in our calculations. First, we thought about changing everything to integers hoping it would solve the problem, but it didn't. Because of that we had to use the decimal library of python, that managed to help us solve that issue... or so we thought, because it kept failing when giving very little change. In the end we went back to using integers but this time helping us with the round() function, that converts the value to the nearest integer, solving the problem we encountered.


## Copyright

This program has been made for educational purposes and has been created from scratch. Therefore I give my permission to anybody that wants to use this with the intention of making a delicious coffee!
The program uses ASCII art that has not been created directly, all rights go to:

**Morfina** - *Coffee mug*

The coffee machine was taken from codegolf.stackexchange.com but the artist wasn't included, and has been modified to include our brand "COFI"




## Future updates

- **Back-end functionality**

    - Individual ingredient filling system.

    - Bank collection system.

- **Menu update**

    - Including our favourite flavours:
        - mokka
        - capuccino
        - vanilla latte.
