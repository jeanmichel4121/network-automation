#!/bin/bash


usage() {
    echo "$0"
    echo ""
    echo "Usage : convert old string with new string"
    echo "------------------------------------------"
    echo ""
    echo "-o, --old             define string search"
    echo "-n, --new             define string replace"
    echo "-d, --directory       define root directory"
    echo "-g, --grep            define value from grep -E on the root directory"
    echo "-r, --reverse         define value from grep -v -E on the root directory"
    echo "-f, --force           force the replace without commit asking"
    echo "-h, --help            help"
    echo ""
}


replace(){
    if [ $# -eq 3 ]
    then
        OLD=$1
        NEW=$2
        FILE=$3

        sed -i -e "s|${OLD}|${NEW}|g" ${FILE} 
    else
        echo "bad usage fct replace"
    fi
}




verify(){
    if [ $# -eq 3 ]
    then
        OLD=$1
        NEW=$2
        FILE=$3

        if [ $(diff -d ${FILE} <(cat ${FILE} | sed -e "s|${OLD}|${NEW}|g") | wc -l) -gt 0 ]
        then
            echo "${FILE}"
            VAR=""
            for I in $(seq 2 $(echo "${FILE}" | wc -c))
            do
                VAR=${VAR}"-"
            done
            echo ${VAR}


            diff -d ${FILE} <(cat ${FILE} | sed -e "s|${OLD}|${NEW}|g") | grep -E "^[0-9]|>|<" | sed -e "s|^[0-9]..*||g"
            echo ""
            COMMIT="var"
            while [ ${COMMIT} != "y" ] && [ ${COMMIT} != "n" ]
            do
                read -p  "would you commit ? (y/n) : " COMMIT
            done
            echo ""
            if [ ${COMMIT} == "y" ]
            then
                replace ${OLD} ${NEW} ${FILE}
            fi

         fi
    else
        echo "bad usage fct verify"
    fi
}



options=$(getopt -l "new:,old:,directory:,grep:,reverse:,force,help" -o "n:o:d:g:r:fh" -a -- "$@")
eval set -- "$options"

FORCE=0
OLD=""
NEW=""
DIRECTORY=""
GREP="."
REVERSE="^$"
while true; do
    case ${1} in
        -n|--new )
            if [ -z ${2} ]
            then
                echo '-n,--new is empty'
                exit 1
            else
                NEW=${2}
            fi
            ;;
        -o|--old )
            if [ -z ${2} ]
            then
                echo '-o,--old is empty'
                exit 1
            else
                OLD=${2}
            fi
            ;;
        -d|--directory )
            if [ -f ${2} ]
            then
                echo '-d,--directory is empty'
                exit 1
            else
                DIRECTORY=${2}
            fi
            ;;
        -g|--grep )
            if [ -z ${2} ]
            then
                echo '-g,--grep is empty'
                exit 1
            else
                GREP=${2}
            fi
            ;;
        -r|--reverse )
            if [ -z ${2} ]
            then
                echo '-r,--reverse is empty'
                exit 1
            else
                REVERSE=${2}
            fi
            ;;
        -h|--help )
            usage
            exit 1
            ;;
        -f|--force )
            FORCE=1
            ;;            
        --)
            shift
            break
            ;;
        esac
    shift
done

echo ""
if [ ! -z ${OLD} ] && [ ! -z ${NEW} ] && [ ! -z ${DIRECTORY} ]
then
    for FILE in $(find ${DIRECTORY} -type f | grep -E "${GREP}" | grep -v -E "${REVERSE}")
    do
        if [ ${FORCE} -eq 0 ]
        then
            verify ${OLD} ${NEW} ${FILE}
        else
            replace ${OLD} ${NEW} ${FILE}

        fi
    done
    echo ""
else

    echo "$0"
    echo ""

    if [ -z ${OLD} ]
    then
        echo "-o, --old is not set"
    fi
    if [ -z ${NEW} ]
    then
        echo "-n, --new is not set"
    fi
    if [ -z ${DIRECTORY} ]
    then
        echo "-d, --directory is not set"
    fi
    echo ""
fi

