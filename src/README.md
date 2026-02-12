Additions:
Organized code into src/pages folder where all our logic is for each page.

Added home.py in src/pages for our main menu after we login.

Reasoning:
Makes our code easier to read and understand.

- Main.py will start up our program and will load our login/create account page.
  How this works:
  1. main.py calls start_auth_page which is where our users will login or create an account.
  2. After user logs in our home page will be called using the function home_menu in home.py
  3. User will then be able to select there option of Hydration, workout, zen, etc... Depending on the selection they will be able to navigate through our app using the function calls without starting and stopping program.
