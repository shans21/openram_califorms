# Define the general SRAM parameters
word_size = 8
num_words = 1024
tech_name = "scn4m_subm"

# Define the L1 and L2 Califorms metadata storage
l1_line_size = 64
l1_metadata_size = 8
l1_total_line_size = l1_line_size + l1_metadata_size

l2_line_size = 64
l2_metadata_size = 1
l2_total_line_size = l2_line_size + (l2_metadata_size // 8)
