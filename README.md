## ML Project

 ## Configuring GIT
-> User config = git config --global user.email "prakarsh.tewari@gmail.com"
-> Commit Readme.md file = git commit -m(message) "First Commit"
-> To sync this repository to git = git remote add origin https://github.com/Prakarsh23/Mlproject.git
-> Push data from origin to the Main = git push -u(--set-upstream) origin main
-> To sync local repository use git pull

-> -v (Verbose : Verbose mode in Git is a setting that provides additional information about the operations that Git is performing. This can be useful for debugging purposes or for simply getting a better understanding of what Git is doing.)

-> -u (sets the default remote branch for the current local branch.
Any future git pull command (with the current local branch checked-out),
will attempt to bring in commits from the <remote-branch> into the current local branch)

-> .gitignore file is a text file that tells Git which files and folders to ignore. It is placed in the root directory of a repository and contains a list of patterns that Git uses to ignore files.

## Setting up Setup.py
-> This file is used to build the entire project as a package & deploy it
-> -e . automatically triggers the setup.py file to run whenever a new package gets added to requirements.txt
-> git add . will add all the files onto git

## Project Structure

-> Creating a Components folder to store different modules like data ingestion & data transformation


## DataIngestion

-> python -m src.components.data_ingestion Used this to run the data ingestion file

-> The -m flag in Python stands for the “module name.” When you pass the -m flag followed by a module name to the Python interpreter, it will locate the module and execute its content as the __main__ module. This allows you to run a module directly from the command line.

## Data Transformation

-> Replaced StandardScaler with StandardScaler(with_mean = false)


