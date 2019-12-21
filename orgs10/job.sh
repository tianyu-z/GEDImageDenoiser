#!/bin/bash
#

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:p1080:1
#SBATCH --time=80:00:00
#SBATCH --mem=50GB
#SBATCH --job-name=gowri
#SBATCH --mail-type=END
#SBATCH --mail-user=sga297@nyu.edu
#SBATCH --output=gowri.out



source ../../py3.6.3/bin/activate
python -u train.py>>log.txt
