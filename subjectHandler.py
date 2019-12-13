import os

class SubjectHandler():
    def __init__(self):
        self.subjects = []
        self.filter_non_subject()

    def filter_non_subject(self):
        all_files = os.listdir()
        default = set(['static', 'templates', 'pr_env', '.vscode', '__pycache__', '.heroku']) # remove pr_env & .vscode later
        for ii in all_files:
            if os.path.isdir(ii) and ii not in default:
                # print(ii)
                self.subjects.append(ii)

    def get_primers(self, subject):
        topics = os.listdir(subject)
        # print(topics)
        primers = []
        for i in topics:
            if os.path.isdir(os.path.join(subject, i)):
                primers.append(self.get_sub_dirs(subject, i))
            if '.md' in i:
                name, _ = i.split('.')
                if name!="README":
                    primers.append(name)
        return primers

    def get_sub_dirs(self, maintopic, subtopic):
        path = os.path.join(maintopic, subtopic)
        topics = os.listdir(path)
        subprimers = []
        for i in topics:
            if '.md' in i:
                name, _ = i.split('.')
                if name!="README":
                    subprimers.append(name)
        return { subtopic : subprimers }


if __name__ == "__main__":
    sh = SubjectHandler()
    print(sh.subjects)
    print(sh.get_primers('Python'))