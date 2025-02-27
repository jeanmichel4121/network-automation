#!/bin/bash


usage() {
    echo "$0"
    echo ""
    echo "Usage : convert all functions to lower case"
    echo "-------------------------------------------"
    echo ""
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
        FILE=$1
        DIRECTORY=$2
        FORCE=$3

        if [ $FORCE -eq 0 ]
        then
            for LINE in $(cat ${FILE} | grep -o -E "  *def  *[^(][^(]*\(" | sed -e "s|  *| |g" -e "s| def ||g" -e "s|(||g")
            do
                LOWER=$(echo ${LINE,,})

                #./replace_string.sh -o "::${LINE}" -n "::${LOWER}" -d "${DIRECTORY}" -g "\.py" -r "NetLogFilter|__init__"
                #./replace_string.sh -o "${LINE}(" -n "${LOWER}(" -d "${DIRECTORY}" -g "\.py" -r "NetLogFilter|__init__"
                ./replace_string.sh -o "${LINE}" -n "${LOWER}" -d "${DIRECTORY}" -g "\.py" -r "NetLogFilter|__init__"
            done 
        else
            for LINE in $(cat ${FILE} | grep -o -E "  *def  *[^(][^(]*\(" | sed -e "s|  *| |g" -e "s| def ||g" -e "s|(||g")
            do
                LOWER=$(echo ${LINE,,})

                #./replace_string.sh -o "::${LINE}" -n "::${LOWER}" -d "${DIRECTORY}" -g "\.py" -r "NetLogFilter|__init__" -f
                #./replace_string.sh -o "${LINE}(" -n "${LOWER}(" -d "${DIRECTORY}" -g "\.py" -r "NetLogFilter|__init__" -f
                ./replace_string.sh -o "${LINE}" -n "${LOWER}" -d "${DIRECTORY}" -g "\.py" -r "NetLogFilter|__init__" -f
            done 
        fi

    
    else
        echo "bad usage fct replace"
    fi
}


options=$(getopt -l "directory:,grep:,reverse:,force,help" -o "d:g:r:fh" -a -- "$@")
eval set -- "$options"

FORCE=0
DIRECTORY=""
GREP="."
REVERSE="^$"
while true; do
    case ${1} in
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
if [ ! -z ${DIRECTORY} ]
then
    for FILE in $(find ${DIRECTORY} -type f | grep -E "${GREP}" | grep -v -E "${REVERSE}")
    do
        replace ${FILE} ${DIRECTORY} ${FORCE}
    done
    echo ""
else

    echo "$0"
    echo ""

    if [ -z ${DIRECTORY} ]
    then
        echo "-d, --directory is not set"
    fi
    echo ""
fi

