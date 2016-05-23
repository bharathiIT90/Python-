"""homework_5_solution_module.py - gets a
file as input and performs operations on it
"""


def AskForFileName():
    """Will ask for the user a file name and returns the name
to the main program
    """

    name = raw_input('Enter the filename: ')

    return name

def ReadFileContents(file_name):
    """Gets the file name as arguement and opens the file
to read the contents of the file to a handle
    """
    
    try:
        f_hand = open(file_name)
        all_file_contents = f_hand.read()
        print 'File opened successfully'
        return all_file_contents
    
    except IOError:
        print 'File cannot be opened'

def BuildHeadList(all_file_contents):
    """Gets all_file_contents as arguement and creates a
new list called the head_list
    """
    
    head_list=[]
    new_list=[]
    new_list = all_file_contents.split('\n')
    for item in new_list:
        if item.startswith('ATOM'):
            break
        else:
            #item = item.rstrip()
            head_list.append(item)
    return head_list

def BuildAtomList(all_file_contents):
    """Gets all file_contents as arguement
and creates a new list called atom_list
    """

    atom_list = []
    new_list = []
    new_list = all_file_contents.split('\n')
    for item in new_list:
        if item.startswith('ATOM'):
            item = item.rstrip()
            atom_list.append(item)
    return atom_list

def BuildTailList(all_file_contents):
    """Gets all file_contents as arguement
and creates a new list called tail_list
    """
    
    a = None
    tail_list = []
    new_list = []
    new_list = all_file_contents.split('\n')
    for index,item in enumerate(new_list):
        if item.startswith('TER'):
            a = index

    for ind,item in enumerate(new_list):
        if (ind>=a):
            item = item.rstrip()
            tail_list.append(item)
        else:
            continue
    return tail_list           
                             
    
def WriteNewFile(head_list,atom_list,tail_list):
    """Gets the head_list,atom_list and tail_list as arguements
and write the content to an output file
    """

    last_list = head_list + atom_list+tail_list

    hand_f1 = open('output.txt','w')
    
    for item in last_list:
        hand_f1.write(item)
        hand_f1.write('\n')
    

if __name__ == '__main__':
    AskForFileName()
    

    
    

    
    
    
