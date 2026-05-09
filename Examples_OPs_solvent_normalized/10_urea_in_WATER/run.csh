#!/bin/csh
### Job name
#BSUB -J water_u10
### Number of cores
#BSUB -n 16
### Wallclock time
#BSUB -W 95:00
### Request specific queue (uncomment to use)
#BSUB -q santiso
### Request all cores on same node
#BSUB -R "span[hosts=1]"
### Request 2 8-core processors
#BSUB -R "select[oc]"
### Standard output file
#BSUB -o o.%J
### Standard error file
#BSUB -e e.%J

module load amber

grep -m 1 ‘model name’ /proc/cpuinfo
cat /etc/redhat-release

mpiexec sander.MPI -O -i min0.in -o min0.out -p simbox.prmtop -c simbox.inpcrd -r min0.ncrst -x min0.mdcrd -inf min0.mdinfo -ref simbox.inpcrd

mpiexec sander.MPI -O -i min.in -p simbox.prmtop -c min0.ncrst -r min.ncrst -o min.out -x min.mdcrd -inf min.mdinfo
$AMBERHOME/bin/ambpdb -p simbox.prmtop -c min.ncrst > min.pdb

mpiexec sander.MPI -O -i heat.in -o heat.out -p simbox.prmtop -c min.ncrst -r heat.ncrst -x heat.nc -ref min.ncrst

mpiexec sander.MPI -O -i equil.in -o equil.out -p simbox.prmtop -c heat.ncrst -r equil.ncrst -x equil.nc -inf equil.mdinfo
$AMBERHOME/bin/ambpdb -p simbox.prmtop -c equil.ncrst > equil.pdb

echo "DONE"
