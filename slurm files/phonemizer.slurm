#!/bin/bash
#SBATCH --job-name=phonemizer
#SBATCH --account=rhenderson
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8GB
#SBATCH --time=5:00:00
#SBATCH --output=phonemizer.log

source ~/miniconda3/etc/profile.d/conda.sh
conda activate independentstudy
python3 /home/u6/kathleencosta/independentstudy/phonemizer.py
