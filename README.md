### How to run preseq_plateau.py

Input BAM file is a sorted BAM

First, run the Preseq analysis (https://github.com/smithlabcode/preseq)

```preseq lc_extrap -B -o <sampleid>_yield_estimates.txt <bam-input> -v```

```python3 preseq_plateau.py -f <sampleid>_yield_estimates.txt```

### How to run calculate.awk

Input BAM file is a deduplicated and indel-realigned BAM

```samtools view -q 20 <bam-input> | awk '{print length($10)}' | awk -f calculate.awk```

Outputs minimum, maximum, median and mean readlengths

https://github.com/samtools/samtools
