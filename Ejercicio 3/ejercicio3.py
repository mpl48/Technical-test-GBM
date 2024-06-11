def min_jumps(x):
    k = 0
    position = 0
    # Incrementamos k mientras la posición actual más el salto no alcanza o supera a x
    while position < x:
        k += 1
        position += k
    # Si nos pasamos del punto, ajustamos con saltos hacia atrás
    while (position - x) % 2 != 0:
        k += 1
        position += k
    return k

def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        cases = int(file.readline().strip())
        results = []
        for _ in range(cases):
            x = int(file.readline().strip())
            results.append(min_jumps(x))
    
    with open(output_filename, 'w') as file:
        for result in results:
            file.write(str(result) + '\n')

def main(inputs, output_folder):
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for input_file in inputs:
        output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_file))[0]}_output.txt")
        process_file(input_file, output_file)

if __name__ == "__main__":
    input_files = ["input1.txt", "input2.txt", "input3.txt", "input4.txt", "input5.txt"]
    main(input_files, "output")

