# -*- coding: utf-8 -*-
import csv

with open('datasetatoms.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    total_time_with_atoms = 0
    entries_count_with_atoms = 0

    total_time_without_atoms = 0
    entries_count_without_atoms = 0

    number_finished_with_atom_faster = 0

    data = []
    for row in csv_reader:
        data.append(row)

    for row in data:
        if line_count == 0:
            line_count += 1
        else:
            minutes = row[9]
            technique = row[6]

            if technique == 'With Atom':
                total_time_with_atoms += float(minutes)
                entries_count_with_atoms += 1
            else:
                total_time_without_atoms += float(minutes)
                entries_count_without_atoms += 1

    total_time_medium_with_atoms = total_time_with_atoms / entries_count_with_atoms
    total_time_medium_without_atoms = total_time_without_atoms / entries_count_without_atoms

    print("Total time medium with atoms = %d minutes" % (total_time_medium_with_atoms))
    print("Total time medium without atoms = %d minutes" % (total_time_medium_without_atoms))


    relative_difference_between_total_time = total_time_medium_with_atoms = 100

    decrease = total_time_medium_with_atoms - total_time_medium_without_atoms
    decrease = (decrease / total_time_medium_with_atoms) * 100
    print("Diferença percentual %f" % decrease)

    grouped_by_participant = {}
    for row in data[1:]:
        dict_key = "%d%d" % (int(row[1]), int(row[2]),)
        if dict_key not in grouped_by_participant:
            grouped_by_participant[dict_key] = {}

        grouped_by_participant[dict_key][row[6]] = float(row[9])

    number_finished_with_atom_faster_time_difference = 0
    for key, participant in grouped_by_participant.items():
        if participant['Without Atom'] > participant['With Atom']:
            number_finished_with_atom_faster += 1
            print("%f %f" % (participant['Without Atom'], participant['With Atom']))
            print("%f" % (participant['Without Atom'] - participant['With Atom']))
            number_finished_with_atom_faster_time_difference += (participant['Without Atom'] - participant['With Atom'])


    print("Number of users which finished with atoms faster than without atoms = %f" % (number_finished_with_atom_faster))
    print("Number of users which finished with atoms faster than without atoms medium = %f" % (number_finished_with_atom_faster_time_difference / number_finished_with_atom_faster))

    print(number_finished_with_atom_faster_time_difference)
    # print(f"Total time with atoms {total_time_with_atoms} minutes")
