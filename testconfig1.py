word_size = 32
num_words = 2048

num_rw_ports = 1
num_r_ports = 0
num_w_ports = 0

tech_name = "freepdk45"
nominal_corner_only = False
process_corners = ["TT"]
supply_voltages = [1.0]
temperatures = [25]

#analytical_delay = False

output_name = "sram_{0}rw{1}r{2}w_{3}_{4}_{5}".format(num_rw_ports,
                                                      num_r_ports,
                                                      num_w_ports,
                                                      word_size,
                                                      num_words,
                                                      tech_name)
