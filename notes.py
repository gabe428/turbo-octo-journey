after using npm init in commandline to create your package.json and the index.html:

1. installing node module lite-server for testing
    npm install lite-server

2. add to package.json "start": "npm run lite"
this is configuring a command for npm when npm start is entered into the -
    command line it will do action "npm run lite"
    furthermore lite is definded as "lite": "lite-server"

3. Bootstrap: In order to use bootstrap, you must have popper and jquery
    when attempting to npm install boostrap you will get an error
    that the dependents are not installed, you must install them in the
    order of jquery > popper > Bootstrap

4. In the index.html you specify the css stylesheet using "stylesheet"
    and href to specify the path to "stylesheet"
    note: the same specificications need to be made for jquery, popper,
    and bootstrap in the respective orders, this is done right below the
    footer in index.html

5. 
