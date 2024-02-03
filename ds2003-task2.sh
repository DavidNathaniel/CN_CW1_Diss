#!/bin/bash
# Usage: ./line_count.sh <file>
# -----------------------------------------------------------------------------
# Link filedescriptor 10 with stdin
exec 10<&0
# stdin replaced with a file supplied as a first argument
exec < $1

#initialise encrypted file, and substring of decrypted message
encFile=$2
decText=""
encryptedMessage="Our shared secret word is:"
#for each word in plaintext file (separated by line)
while read LINE
    do
    wordLen=${#LINE} #make sure we aren't operating on any words longer more than 16 characters
    if [ $wordLen -lt 17 ];
        then
        echo "Attempting decryption with word: $LINE"
        
        for n in {0..9} # append each number ranging from 0-9 to the word to create a possible pasword.
        do
            password="$LINE$n"
            #decrypt the message with oppenssl statement using the $password I just created
            decText=$(openssl enc -d -aes-128-cbc -in $encFile -nosalt -pass pass:"$password" 2>/dev/null) #2>/dev/null  should send errors to null file (cleaning up cli)
            
            if [[ "$decText" == *"$encryptedMessage"* ]]; #check if the decryption was successful (containing the sub string)
            then
                #display decrypted message and successful password
                echo "Decryption successful with password: $password"
                echo "$decText"
                echo "$decText" > "output.txt" #place the decrypted text (including found shared secret word) into output file
                exit
            fi
        done
    fi
done
#$SHELL #to keep shell open after finished running task - so can read final output
# and close filedescriptor 10
exec 0<&10 10<&-
