@echo off

set newRepoName=%1
set repoDesc=%2
set envPick=%3
set gitUsername=%4
set projectPath=%5

cd %projectPath%%newRepoName%
echo %repoDesc%>readme.txt
git init
git remote add origin https://github.com/%gitUsername%/%newRepoName%
git add .
git commit -m "first commit"
git push -u origin master
echo All done!

IF %envPick%==v (
    start devenv
)
IF %envPick%==c (
    code .
)
IF %envPick%==j (
    echo "intelliJ support coming soon"
)