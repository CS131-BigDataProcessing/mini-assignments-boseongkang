#!/usr/bin/env nextflow

params {
    input_str = 'Hello World'
}

process allCaps {
    input:
    val input_str from params.input_str

    output:
    val result into uppercase_output

    script:
    """
    echo ${input_str^^}
    """
}

