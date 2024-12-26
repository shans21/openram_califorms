#!/bin/sh
source /home/sh4471/workplace/OpenRAM/miniconda/bin/activate
/home/sh4471/workplace/OpenRAM/miniconda/bin/klayout -b -r freepdk45.lylvs -rd input=example_config_freepdk45.gds -rd report=example_config_freepdk45.lvs.report -rd schematic=example_config_freepdk45.sp -rd target_netlist=example_config_freepdk45.spice -rd connect_supplies=1
conda deactivate
