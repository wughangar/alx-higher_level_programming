#!/bin/bash
# script that posts key pair values
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
