word_size = 23
num_words = 32
num_banks = 1

num_rw_ports = 0
num_r_ports = 1
num_w_ports = 1

tech_name = "freepdk45"
nominal_corner_only = True
process_corners = ["TT"]
supply_voltages = [1.0]
temperatures = [25]

route_supplies = False
check_lvsdrc = False
analytical_delay = True

output_name = "sram_{0}rw{1}r{2}w_{3}_{4}_{5}".format(num_rw_ports,
                                                        num_r_ports,
                                                        num_w_ports,
                                                        word_size,
                                                        num_words,
                                                        tech_name)
output_path = "out_files/{}".format(output_name)
