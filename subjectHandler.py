import os

class SubjectHandler():
    def __init__(self):
        self.subjects = []
        self.filter_non_subject()

    def filter_non_subject(self):
        all_files = os.listdir()
        default = ['static', 'templates', 'pr_env', '.vscode', '__pycache__'] # remove pr_env & .vscode later
        for ii in all_files:
            if os.path.isdir(ii) and ii not in default:
                # print(ii)
                self.subjects.append(ii)

    def get_primers(self, subject):
        topics = os.listdir(subject)
        print(topics)
        primers = []
        for i in topics:
            name, extension = i.split('.')
            if name!="README" and extension == 'md':
                primers.append(name)
        return primers



if __name__ == "__main__":
    sh = SubjectHandler()
    print(sh.subjects)
    print(sh.get_primers('Python'))