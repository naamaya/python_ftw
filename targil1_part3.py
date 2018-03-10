#subject1=Math, subject2=History
subj1_all_students={'jack':[80,85],'naama':[100,100],'mattan':[99,95],'garua':[60,63],'may':[80,82]}
subj2_all_students={'jack':[75,95],'naama':[90,99],'mattan':[85,95],'garua':[55,70]}

def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """

    keys = list(subj2_all_students.keys())[:]
    keys[len(keys):]=list(subj1_all_students.keys())[:]
    #remove students with only one grade and remove duplicate student names
    for element in range(len(keys)):
        if keys.count(keys[element])==1:
            keys.remove(keys[element])
    keys=list(set(keys))

    best_subject=dict()

    for student in range(len(keys)):
        if max(subj2_all_students[keys[student]]) > max(subj1_all_students[keys[student]]):
            best_subject[keys[student]]='History'
        else:
            best_subject[keys[student]] = 'Math'

    return (best_subject)

