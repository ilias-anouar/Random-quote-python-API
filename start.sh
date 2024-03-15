#!/bin/bash
function loading_icon() {
    counter=2
    while [ $counter -gt 0 ]; do
        # Frame #1
        printf "\r< Loading...▰▱▱▱▱▱▱"
        sleep 0.1
        # Frame #2
        printf "\r> Loading...▰▰▱▱▱▱▱"
        sleep 0.1
        # Frame #1
        printf "\r< Loading...▰▰▰▱▱▱▱"
        sleep 0.1
        # Frame #4
        printf "\r> Loading...▱▰▰▰▱▱▱"
        sleep 0.1
        # Frame #1
        printf "\r< Loading...▱▱▰▰▰▱▱"
        sleep 0.1
        # Frame #6
        printf "\r> Loading...▱▱▱▰▰▰▱"
        sleep 0.1
        # Frame #6
        printf "\r< Loading...▱▱▱▱▰▰▰"
        sleep 0.1
        # Frame #7
        printf "\r> Loading...▱▱▱▱▱▰▰"
        sleep 0.1
        # Frame #8
        printf "\r< Loading...▱▱▱▱▱▱▰"
        sleep 0.1
        # Frame #9
        printf "\r> Loading...▱▱▱▱▱▱▱"
        sleep 0.1
        # Frame #10
        printf "\r< Loading...▱▱▱▱▱▱▱"
        sleep 0.1
        # Frame #11
        printf "\r> Loading...▱▱▱▱▱▱▱"
        sleep 0.1
        # Frame #12
        printf "\r< Loading...▱▱▱▱▱▱▱"
        sleep 0.1
        counter=$((counter - 1))
        # printf $counter
    done
    printf "\r<---> Done...!!"
}

pip install fastapi

pip install "uvicorn[standard]" --user

npm install pm2 -g

echo
echo "     //--------------------------------------------------------------\\"
echo
echo "        #####  ##  ##  ####  ###### ######  ####   ######  #####  ##     "
echo "       ##   ## ##  ## ##  ##   ##   ##     #       ##  ## ##   ## ##     "
echo "       ##   ## ##  ## ##  ##   ##   ######  ###    ###### ######  ##     "
echo "       ##   ## ##  ## ##  ##   ##   ##         #   ##  ## ##      ##     "
echo "        ######  ####   ####    ##   ###### ####    ##  ## ##      ##     "
echo "             ##                                                       "
echo "     \\---------------------------------------------------------------//"
echo
echo "############################# ilias-anouar ####################################"
echo
echo "         ##################### quotes API ##########################"
echo

echo "Starting uvicorn server"
pm2 start main.py
echo "Enter the link to PM2.io :"
read link
$link