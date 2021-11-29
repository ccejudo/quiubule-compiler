from quiubule_parser import parser, memory
import json

def quiubule(input_file):
    # Read the input file
    with open(input_file, "r") as f:
        data = f.read()
        
    # Parse the input file
    parser.parse(data)
    print("Tabla de símbolos: ", json.dumps(memory, indent=1))
    

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: %s <input file>" % sys.argv[0])
        sys.exit(1)

    quiubule(sys.argv[1])