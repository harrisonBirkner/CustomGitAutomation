@echo off

set newRepoName=%1

cd C:/
md %newRepoName%
cd %newRepoName%
echo %newRepoName%>readme.txt
git init
git remote add origin https://github.com/harrisonBirkner/%newRepoName%
git add .
git commit -m "first commit"
git push -u origin master
code .