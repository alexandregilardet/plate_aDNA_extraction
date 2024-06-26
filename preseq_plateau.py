#!/usr/bin/env python3
#original author Alexandre Gilardet @CPG Stockholm

#run Preseq on UPPMAX
#ml bioinfo-tools preseq/3.2
#for bam in *.sorted.bam; do sbatch -A naiss2024-5-54 -p core -n 8 -t 01:00:00 -J preseq --wrap="preseq lc_extrap -B -o ${bam%.bam}_yield_estimates.txt $bam -v"; done

import argparse
import sys

################################# Argparse ###################################
parser = argparse.ArgumentParser(
    description="""Extracts plateau value from Preseq output,
    run as a loop: for file in *yield_estimates.txt; do python3 preseq_plateau.py -f $file >> all_preseq.txt ; done""",
    epilog=f"Example of use: {sys.argv[0]} -f AG036M_1027_L4.sorted_yield_estimates.txt >> AG036M_preseq.txt",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument(
    "-f", "--file_preseq", type=str, required=True, help="output from Preseq lc_extrap eg. AG036M_1027_L4.sorted_yield_estimates.txt"
)

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()
##############################################################################

old_complexity = -111 #default

with open(args.file_preseq, "r") as f_in:
    ag = args.file_preseq.split('_')[0] #library id
    for line in f_in.readlines():
        if line.split("\t")[0] == "TOTAL_READS": #skip header
            pass
        else:
            new_complexity = line.split("\t")[1]
            diff = float(new_complexity) - float(old_complexity)
            if (diff < 400) and (old_complexity != -111): #plateau extracted when increase in between two consecutive values is less than 400
                plateau = new_complexity
                print(ag,plateau)
                break 
            else:
                old_complexity = new_complexity

