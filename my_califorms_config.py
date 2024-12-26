import os
import sys

# Set the OPENRAM_HOME environment variable
OPENRAM_HOME = os.path.abspath(os.environ.get("OPENRAM_HOME", ""))
sys.path.append(OPENRAM_HOME)

import openram
openram.init_openram("my_califorms_config.py")

from openram import sram_config
from openram import sram
import tech

# Import the required OpenRAM modules
from base import design
from sram_factory import factory
import debug
import tech

# Define the general SRAM parameters
word_size = 8
num_words = 1024
tech_name = "mystic_tech"

# Define the L1 and L2 Califorms metadata storage
l1_line_size = 64
l1_metadata_size = 8
l1_total_line_size = l1_line_size + l1_metadata_size

l2_line_size = 64
l2_metadata_size = 1
l2_total_line_size = l2_line_size + (l2_metadata_size // 8)

# Define the SRAM macro and other parameters
sram = factory.create(module_type="sram",
                     word_size=word_size,
                     num_words=num_words,
                     num_banks=1,
                     name="my_sram",
                     column_size=l1_total_line_size,
                     num_terms=1)

s.save()
openram.end_openram()
