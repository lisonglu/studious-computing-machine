#!/bin/bash

if [[ $(uname) == "Darwin" ]]; then
    readlink=greadlink
else 
    readlink=readlink 
fi

declare -rx PIPELINE_DIR=$(dirname $($readlink -f "$BASH_SOURCE"))
declare -rx ThisBin="${PIPELINE_DIR}"/bin
declare -x  PATH=${ThisBin}:${PATH}
declare -x  ConfigDir=${PIPELINE_DIR}/conf/

# load shell lib
if [[ ! -s ${PIPELINE_DIR}/ShellLib/activate ]]; then
    echo "cannot find Shell Lib, clone the repository with --recursive or run git submodule update --init --recursive"
    exit 1
fi

. ${PIPELINE_DIR}/ShellLib/activate || exit $?
. ${ThisBin}/const.sh

function usage {
    cat <<EOF

${HERE_FONT_COLOR_GREEN}Pipeline X ${HERE_FONT_STYLE_RESET}
${HERE_FONT_STYLE_BOLD}
Pipeline for ???? analysis done in Intellia Therapeutics internally.
Version: ${HERE_FONT_STYLE_RESET}${HERE_FONT_STYLE_UNDERLINE}${PipelineVersion}${HERE_FONT_STYLE_RESET}

It currently include the following modules:
${HERE_FONT_COLOR_YELLOW}
[version]
    Return the version of this pipeline
${HERE_FONT_COLOR_MAGENTA}
[module1]
    Analyze... 
${HERE_FONT_COLOR_RED}
[module2]
    Analyze...
${HERE_FONT_COLOR_BLUE}
[module3]
    Analyze ...
${HERE_FONT_STYLE_RESET}
EOF
}

# trigger usage
if [[ $# -lt 1 ]]; then usage && exit 1; fi

# invoke specific module
declare SubProgram=$(echo ${1} | tr '[A-Z]' '[a-z]')

case $SubProgram in
    module1|m1)
        shift && bash ${ThisBin}/run_module1.sh $@ 
        # TODO:                  ^^^^^^^^^^^^^^ update this
    ;;
    version|v)
        echo $PipelineVersion
    ;;
    *)
        echo "unrecognized option: ${SubProgram}"
        exit 1
    ;;
esac
