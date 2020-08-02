#!/usr/bin/env zsh
# -*- coding: utf-8 -*-
    # shellcheck shell=bash
    # shellcheck source=/dev/null
    # shellcheck disable=2128

#? ############################# skeptycal.com
#? binit - create symbolic links to [FILE(s)] in the current user's ~/bin folder
# using GNU coreutils: <https://www.gnu.org/software/coreutils/>

# import standard script modules, if available
. $(which ssm) >/dev/null 2>&1

BASH_SOURCE="${0}"
SCRIPT_NAME="${BASH_SOURCE##*/}"
SCRIPT_PATH="${BASH_SOURCE%/*}"

VERSION='1.1.2'

# list of cli arguments passed, including FILES to link
ARGS=( ${@:1} )

echo() {
    printf '%s\n' $@
}

# if no files are given, echo usage information and exit
if [ -z "$ARGS" ]; then
    echo "${CANARY:-}${BOLD:-}${SCRIPT_NAME}${RESET:-} version ${BLUE:-}${VERSION}${RESET:-}"
    echo "  Create symbolic links for ${GO:-}FILE(s)${RESET:-} in ${BLUE:-}~/bin${RESET:-}"
    echo "  ${MAIN:-}Usage: ${CANARY:-}${SCRIPT_NAME} ${GO:-}FILES(s)${RESET:-}"
    return 1
fi

link_scripts() {
    # prefer hard links; backups performed for files that are overwritten
    # remove extensions for sh and py files ... personal preference

    if [ "$1" ]; then
        TMP_ARGS=( ${@:1} )
    else
        TMP_ARGS=$ARGS
    fi

    for arg in $TMP_ARGS; do
        src=$(realpath $arg)
        if [ -r $src ]; then
            chmod a+x $src

            tgt=${src##*/}
            tgt=${tgt%.sh*}
            tgt=${tgt%.py*}
            tgt=${tgt%.php*}
            tgt=~/bin/$tgt


            ln -bv $src $tgt

            # if hardlink didn't work, try symbolic link
            if ! [ -r $tgt ]; then
                ln -sbv $src $tgt
            fi


        else
            exit "${arg} (${src}) is not readable."
        fi
    done
}


# make sure binit is setup first!
if ! type binit &> /dev/null; then
    echo "Setting up binit for the first time."
    BINIT_FILE=$(find . -type f -name binit.sh -print | tail -n 1)
    if [ -z $BINIT_FILE ]; then # may be long running! Hope we never see this...
        BINIT_FILE=$(find ~ -type f -name binit.sh -print | tail -n 1)
    fi
    link_scripts $(realpath $BINIT_FILE)
fi

link_scripts $@

# $SHELL -l
