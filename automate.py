import os

def generate_sram_config(word_size, num_words):
    config = f"""
word_size = {word_size}
num_words = {num_words}

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

output_name = "sram_{{0}}rw{{1}}r{{2}}w_{{3}}_{{4}}_{{5}}".format(num_rw_ports,
                                                        num_r_ports,
                                                        num_w_ports,
                                                        word_size,
                                                        num_words,
                                                        tech_name)
output_path = "out_files/{{}}".format(output_name)
"""
    return config.strip()

def main():
    word_size = 32
    num_words_list = [128, 256, 512, 1024, 2048]  # Add or modify this list as needed
    output_dir = "sram_configs"
    command_list = []

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for num_words in num_words_list:
        config_content = generate_sram_config(word_size, num_words)
        filename = f"sram_config_{word_size}_{num_words}.py"
        file_path = os.path.join(output_dir, filename)

        with open(file_path, "w") as f:
            f.write(config_content)

        command = f"python3 /home/sh4471/workplace/OpenRAM/compiler/../sram_compiler.py {filename} -v"
        command_list.append(command)

        print(f"Generated: {file_path}")

        # Write filenames to a text file
        command_list_path = os.path.join(output_dir, "sram_compiler_commands.txt")
        with open(command_list_path, "w") as f:
            for command in command_list:
                f.write(f"{command}\n")

        print(f"\nCompiler commands saved to: {command_list_path}")

if __name__ == "__main__":
    main()

