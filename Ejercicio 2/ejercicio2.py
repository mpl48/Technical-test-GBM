import os

def parse_input(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    i = 0
    results = []

    while i < len(data):
        G, P = map(int, data[i].split())
        if G == 0 and P == 0:
            break
        i += 1

        races = []
        for _ in range(G):
            races.append(list(map(int, data[i].split())))
            i += 1

        S = int(data[i])
        i += 1

        scoring_systems = []
        for _ in range(S):
            scoring = list(map(int, data[i].split()))
            points = scoring[1:]
            scoring_systems.append(points)
            i += 1

        results.append((G, P, races, scoring_systems))
    return results

def calculate_points(G, P, races, scoring_system):
    points = [0] * P
    for race in races:
        for idx, position in enumerate(race):
            if position - 1 < len(scoring_system):
                points[idx] += scoring_system[position - 1]
    return points

def find_champions(points):
    max_points = max(points)
    champions = [i + 1 for i, point in enumerate(points) if point == max_points]
    return champions

def main(inputs, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for input_file in inputs:
        results = parse_input(input_file)
        output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_file))[0]}_output.txt")
        with open(output_file, 'w') as f:
            for G, P, races, scoring_systems in results:
                for scoring_system in scoring_systems:
                    points = calculate_points(G, P, races, scoring_system)
                    champions = find_champions(points)
                    f.write(" ".join(map(str, champions)) + "\n")

if __name__ == "__main__":
    input_files = ["input1.txt", "input2.txt", "input3.txt"]
    main(input_files, "output")
