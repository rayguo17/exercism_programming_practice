from pyparsing import line_start


def grep(pattern, flags, files):
    #need to open files by line
    #compare sub str in line
    #use flags to handle options
    #read flags first
    #print(pattern)
    #print(flags)
    #print(files)
    flagify = str(flags)
    flag_arr=flagify.split(' ')
    line_number = False
    name_of_file = False
    case_insensitive=False
    invert=False
    entire_line=False
    for flag in flag_arr:
        if flag=="-n":
            line_number=True
        if flag=="-l":
            name_of_file=True
        if flag=="-i":
            case_insensitive=True
        if flag=="-v":
            invert=True
        if flag=="-x":
            entire_line=True
    #now read files into list
    file_arr = {}
    for file in files:
        fo = open(file,"r")
        lines = fo.readlines()
        file_arr[file] = lines
    #print(file_arr)
    #start the matching process
    match_files= []
    match_lines = {}
    #inverse and entire_line decouple?
    def insert_files(match_files,file):
        if file in match_files:
            return match_files
        else :
            match_files.append(file)
            return match_files
    def insert_lines(file,line,index,match_lines):
        if not file in match_lines:
            match_lines[file] = []
        insert_str = ""
        if index !=0:
            insert_str = f"{index}:{line}"
        else:
            insert_str=f"{line}"
        match_lines[file].append(insert_str)
        
            
    #print(file_arr)
    for file in files:
        for i in range(len(file_arr[file])):
            line = file_arr[file][i]
            if case_insensitive:
                line = line.lower()
                pattern = pattern.lower()
            index=0
            line = line[0:-1]
            #print(line)
            #print(pattern)
            if line_number:
                index = i+1
            if entire_line:
                if invert:
                    if not line == pattern:
                        insert_files(match_files,file)
                        insert_lines(file,file_arr[file][i],index,match_lines)
                else:
                    if line == pattern:
                        insert_files(match_files,file)
                        insert_lines(file,file_arr[file][i],index,match_lines)
                
                        
            else:
                if invert:
                    if not pattern in line:
                        insert_files(match_files,file)
                        insert_lines(file,file_arr[file][i],index,match_lines)
                else:
                    if pattern in line:
                        insert_files(match_files,file)
                        insert_lines(file,file_arr[file][i],index,match_lines)
    
    #print(match_files)
    #print(match_lines)
    #shall we escape \n?
    def insert_result(result,line,file):
        line_str = ""
        if len(files)>1:
            line_str=f"{file}:{line}"
        else:
            line_str=line
        if result == """""":
            result = f"""{line_str}"""
        else:
            result = f"""{result}{line_str}"""
        return result
    def insert_file(result,file):
        file= file+"\n"
        if result == """""":
            result = f"""{file}"""
        else :
            result = f"""{result}{file}"""
        return result    
    result=""""""
    if name_of_file:
        for file in match_files:
            result = insert_file(result,file)
    else:
        for file in match_files:
            for line in match_lines[file]:
                result=insert_result(result,line,file)
    #print(result)
    return result
    

if __name__ == "__main__":
    files = ["iliad.txt"]
    pattern = "Illustrious into Ades premature"
    flags="-x -v"
    print(grep(pattern,flags,files))
    
