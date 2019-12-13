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
                                                'profile': contributor['url']
                                                }
        self.contributors = contributors

    def no_of_primers(self):
        primers = []
        for ii in self.total_topics:
            res = self.sh.get_primers(ii)
            if isinstance(res, dict):
                for vals in res:
                    primers += vals
            else:
                primers += res
        self.total_primers = primers
        print(self.total_topics)

    def get_last_updated(self):
        url = 'https://api.github.com/repos/Devyanshu/primer'
        temp = urlopen(url).read()
        last_updated = json.loads(temp.decode('utf-8'))['updated_at']   
        last_updated = datetime.strptime(last_updated, '%Y-%m-%dT%H:%M:%SZ')
        today = datetime.now().date()
        ld = last_updated.date()
        if ld == today :
            self.last_updated = 'today'
        else:
            days = ld - today
            days = days.days
            if days == 1:
                self.last_updated = '1 day ago'
            else:
                self.last_updated = '{} days ago'.format(days)
        
if __name__ == '__main__':
    stats = Stats()
    stats.get_last_updated()