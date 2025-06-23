#!/bin/bash
#SBATCH --job-name=cleaner
#SBATCH --account=rhenderson
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=20:00:00
#SBATCH --output=cleaner.log

source ~/miniconda3/etc/profile.d/conda.sh
conda activate audio_env
python3 /home/u6/kathleencosta/independentstudy/cleaner.py
