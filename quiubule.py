def idValidate(char, line):
    if not char.isalpha():
        print("Error in line %d: invalid ID declaration" % line)
        exit(1)

def quiubule(input_file):
    # Rules
    rules = ["D_ARREGLO", "D_STRUCT", "D_VAR", "D_FUNCION"]

    # Keywords
    keywords = {
        "juntitos" : 1, 
        "chafirete" : 2, 
        "coso" : 3, 
        "rifate" : 4,
        "chance" : 5,
        "chambea" : 6
    }

    # Variables dictionary
    variables = {}

    # State
    state = 0

    # Read the input file
    with open(input_file, "r") as f:
        lines = f.readlines()

    # Remove empty spaces
    lines = [line.strip() for line in lines]

    # Iterate over the characters in the input file
    for i in range(len(lines)):
        pointer = 0
        curr = ''
        while pointer < len(lines[i]):
            if lines[i][pointer] == "\n":
                break
            
            if state == 0:
                if lines[i][pointer] == ' ':
                    if curr in keywords:
                        state = keywords[curr]
                    curr = ''
                    pointer += 1
                    continue
                else:
                    curr += lines[i][pointer]
                    pointer += 1
                    continue
            
            if state == 1:
                print(rules[state - 1])
                idValidate(lines[i][pointer], i+1)
                state = 0
                continue

            if state == 2:
                print(rules[state - 1])
                idValidate(lines[i][pointer], i+1)
                state = 0
                continue

            if state == 3:
                print(rules[state - 1])
                idValidate(lines[i][pointer], i+1)
                state = 0
                continue

            if state == 4:
                print(rules[state - 1])
                idValidate(lines[i][pointer], i+1)
                state = 0
                continue
            

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: %s <input file>" % sys.argv[0])
        sys.exit(1)

    quiubule(sys.argv[1])