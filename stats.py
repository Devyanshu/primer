from urllib.request import urlopen
import json
import os
from subjectHandler import SubjectHandler
from datetime import datetime

class Stats:

    def __init__(self):
        self.contributors = {}
        self.sh = SubjectHandler()       
        self.total_topics = self.sh.subjects
        self.total_primers = []
        self.last_updated = ''


    def get_contributors(self):
        url = 'https://api.github.com/repos/Devyanshu/primer/contributors'
        contributors_data = urlopen(url).read()
        contributors_data = json.loads(contributors_data.decode('utf-8'))
        contributors = {}
        for contributor in contributors_data:
            contributors[contributor['login']] = {
                                                'contributions':contributor['contributions'],
                                                'avatarUrl': contributor['avatar_url'],
                                                'profile': contributor['html_url'],
                                                'primers': 5 #TODO: Implement autogeneration of this
                                                }
        self.contributors = contributors

    def no_of_primers(self):
        primers = []
        temp = []
        for ii in self.total_topics:
            res = self.sh.get_primers(ii)
            temp += res
        for pr in temp:
            if isinstance(pr, dict):
                vals = [item for prs in list(pr.values()) for item in prs]
                primers += vals
            else:
                primers.append(pr)

        self.total_primers = primers

    def get_last_updated(self):
        url = 'https://api.github.com/repos/Devyanshu/primer'
        temp = urlopen(url).read()
        last_updated = json.loads(temp.decode('utf-8'))['updated_at']   
        last_updated = datetime.strptime(last_updated, '%Y-%m-%dT%H:%M:%SZ')
        print(last_updated)       
        today = datetime.utcnow().date()
        ld = last_updated.date()
        if ld == today :
            hrs = datetime.utcnow() - last_updated
            hrs = hrs.total_seconds() 
            temp = int(hrs//3600)
            if temp >=1:
                self.last_updated = '1 hour ago' if temp == 1 else '{} hours ago'.format(temp)
            else:
                temp = int(hrs//60)
                self.last_updated = 'just now'.format(temp) if temp <= 1 else '{} mins ago'.format(temp)
        else:
            days = today - ld
            days = days.days
            if days == 1:
                self.last_updated = 'yesterday'
            else:
                self.last_updated = '{} days ago'.format(days)
        
if __name__ == '__main__':
    stats = Stats()
    stats.get_last_updated()