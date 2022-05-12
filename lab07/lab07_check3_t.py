#checkpoint 1
def parse_line(sentence):
    new_sent = sentence.split("/")
    if len(new_sent) < 4:
        return None
    else:
        if (new_sent[-1]).isdigit() and (new_sent[-2]).isdigit() and (new_sent[-3]).isdigit():           
            news = "/".join(new_sent[0: len(new_sent) -3])
            news_later = [int(new_sent[-3]), int(new_sent[-2]), int(new_sent[-1]), news]
            return news_later
        else:
            return None

#checkpoint 2:
def get_line(fname, parno, lineno): 
    paragraphs = [[]] 
    num_pars = 0
    
    new_paragraph = False

    
    with open(fname, encoding="utf8") as f:
        for line in f:
            if line[0] == '\n' and new_paragraph == False:
                new_paragraph = True
                num_pars += 1
                paragraphs.append([])
            elif line[0] == '\n':
                continue
            else:
                new_paragraph = False
                paragraphs[num_pars].append(line.rstrip())
            
    return paragraphs[parno-1][lineno-1]
            

#chefckpoint 3
def build_python_program():
    python_program_lines = []
    
    fileno = input("Please enter a starting file numer ==> ")
    parno = int(input("Please enter a starting paragraph number ==> "))
    lineno = int(input("Please enter a starting line number ==> "))

    filename = fileno + ".txt"

    line = get_line(filename, parno, lineno)
    parsed_line = parse_line(line)
        
    reached_end = False
    while not reached_end:
        python_program_lines.append(parsed_line[-1])
        
        next_fileno = str(parsed_line[0]) + '.txt'
        next_parno = parsed_line[1]
        next_lineno = parsed_line[2]

        line = get_line(next_fileno, next_parno, next_lineno)
        parsed_line = parse_line(line)
        
        if parsed_line[-1] == "END":
            reached_end = True
    
    print(python_program_lines)
    
    with open("output.py",'w') as f:
        for item in python_program_lines:
            f.write(item+'\n')


build_python_program()


