import os
from pathlib import Path


class ListOfRequests:
    def __init__(self, path):
        self.p = path
        self.lof = None
        self.elements = dict()

    def get_list_of_files(self):
        if self.p.is_dir():
            self.lof = os.listdir(self.p)

    def get_elements_from_all_files(self):
        for file in self.lof:
            # Get content per file
            with open(os.path.join(self.p, file), 'r') as f:
                f_content = f.readlines()
            f.close()

            # Separate content per type
            content_dict = dict()
            card_type = None
            for line in f_content:
                if line == '\t\n' or line == '\n':
                    continue
                elif 'Trainer:' in line:
                    card_type = 'Trainer'
                elif 'Pokemon:' in line:
                    card_type = 'Pokemon'
                elif 'Energy:' in line:
                    card_type = 'Energy'
                else:
                    l_elements = line.split(' ')
                    card_name = ' '.join(l_elements[1:-2]).replace(',', ' ') \
                        if 'Trainer' == card_type or 'Energy' == card_type \
                        else ' '.join(l_elements[1:]).replace(',', ' ')
                    card_name = card_name.replace('\t\n', "") if '\t\n' in card_name else card_name.replace('\n', "")
                    card_amnt = int(l_elements[0])

                    # Create types if required
                    if not self.elements.get(card_type, None):
                        self.elements[card_type] = {}

                    # Save card under its type
                    if self.elements[card_type].get(card_name, None):
                        self.elements[card_type][card_name] += card_amnt
                    else:
                        self.elements[card_type][card_name] = card_amnt


    def main(self):
        self.get_list_of_files()
        self.get_elements_from_all_files()


if __name__ == '__main__':
    # Pass the address where lists are stored
    obj = ListOfRequests(Path(f'C:\\Users\\familia\\Downloads\\poke_project'))
    obj.main()
    print(obj.elements)
