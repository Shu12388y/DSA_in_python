#!bin/bash

git status
git add .
echo "Enter your message"
read message
git commit -m "$message"
git push
echo "done !!!!"