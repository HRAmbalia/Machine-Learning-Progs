import glob

def merge_text_files(text_files, output_file):
    i = 0
    with open(output_file, "w") as output_file:
        for text_file in text_files:
            print(i)
            with open(text_file, "r") as input_file:
                text = input_file.read()
                output_file.write(text)
                output_file.write("\n")
            i = i+1

if __name__ == "__main__":
    text_files = glob.glob("*.txt")
    print(text_files)
    output_file = "negative_text.txt"

    merge_text_files(text_files, output_file)
