import homework_5_solution_module as hw5sm

def DifferenceTwoFiles(file_1,file_2):
    diff_list=[]
    f_1 = open(file_1,'r')
    f_2 = open(file_2,'r')

    f1_str = f_1.read()
    f2_str = f_2.read()

    f1_list = f1_str.split()
    f2_list = f2_str.split()

    for i in f1_list:
        if i in f2_list:
            continue
        else:
            diff_list.append(i)
            continue
    f_1.close()
    f_2.close()

    print 'The number of differences between the files is:',len(diff_list)

def Run():
    file_name = hw5sm.AskForFileName()
    all_file_contents = hw5sm.ReadFileContents(file_name)
    head_list = hw5sm.BuildHeadList(all_file_contents)
    atom_list = hw5sm.BuildAtomList(all_file_contents)
    tail_list = hw5sm.BuildTailList(all_file_contents)
    hw5sm.WriteNewFile(head_list,atom_list,tail_list)

    file_1 = raw_input('Enter the input file')
    file_2 = raw_input('Enter the output file')

    DifferenceTwoFiles(file_1,file_2)
                       
Run()
