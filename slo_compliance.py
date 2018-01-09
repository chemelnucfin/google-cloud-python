from collections import namedtuple
from datetime import datetime
from datetime import date
from datetime import timedelta

import re
import requests

from bs4 import BeautifulSoup


today = date.today()
language = 'python'
google_cloud = 'https://github.com/GoogleCloudPlatform/google-cloud-{}/'
github_url = google_cloud.format(language)
url_pattern = re.compile('%([0-9a-fA-F]{2})', re.M)
no = '-'
Types = namedtuple('Label',
                   ['bug', 'feature', 'question', 'cleanup', 'process'])
types = Types('label:"type: bug" ',
              'label:"type: feature request" ',
              'label:"type: question" ',
              'label:"type: cleanup" ',
              'label:"type: process" ')
no_assignee = '"no: assignee" '
Priority = namedtuple('Priority', ['p0', 'p1', 'p2'])
priority = Priority('label:"priority: p0" ',
                    'label:"priority: p1" ',
                    'label:"priority: p2" ')


def updated(days):
    return 'updated:<={}'.format(today-timedelta(days))


def created(days):
    return 'created:<={}'.format(today-timedelta(days))


def unquote(url):
    return url_pattern.sub(lambda m: chr(int(m.group(1), 16)), url)


def query(url, params, name):
    r = requests.get(url, params=params)
    soup = BeautifulSoup(r.text, 'html.parser')
    number = int(soup
                 .find('a', class_='btn-link selected')
                 .contents[2]
                 .strip()[:-5])
    if number == 0:
        return
    items = soup.find_all('span', class_='opened-by')
    # if number > 0:
    #     print(r.url)
    #     print(name, number)
    #     print([int(item.contents[0].strip().split('\n')[0][1:]) for item in items])

    print(unquote(r.url.replace(github_url, '')))
    print(name, number)
    print([int(item.contents[0].strip().split('\n')[0][1:]) for item in items])
    print("") 

issues = {'issues_with_no_type': (no+types.bug
                                  + no+types.feature
                                  + no+types.question
                                  + no+types.cleanup
                                  + no+types.process),
          'questions_with_no_assignee': types.question + 'no:assignee ',
          'bugs_with_no_assignee': types.bug + 'no:assignee ',
          'issues_with_no_assignee': 'no:assignee ',
          'bugs_with_no_priority': (types.bug
                                    + no+priority.p0
                                    + no+priority.p1
                                    + no+priority.p2),
          'bugs_with_priority_p0': types.bug + priority.p0,
          'bugs_with_priority_p1': types.bug + priority.p1,
          'bugs_with_priority_p2': types.bug + priority.p2,
          'questions_over_response_slo': (types.question
                                          + updated(5)),
          'p0_bugs_over_response_slo': (types.bug
                                        + priority.p0
                                        + updated(1)),
          'p0_bugs_over_closure_slo': (types.bug
                                       + priority.p0
                                       + created(5)),
          'p1_bugs_over_response_slo': (types.bug
                                        + priority.p1
                                        + updated(5)),
          'p1_bugs_over_closure_slo': (types.bug
                                       + priority.p1
                                       + created(42)),
          'p2_bugs_over_response_slo': (types.bug
                                        + priority.p2
                                        + updated(120)),
          'p2_bugs_over_closure_slo': (types.bug
                                       + priority.p2
                                       + created(120)),
          'feature_requests_over_response_slo': (types.feature
                                                 + updated(120)),
          'feature_requests_over_closure_slo': (types.feature
                                                + created(120)),
          'cleanup_over_response_slo': (types.cleanup
                                        + updated(120)),
          'cleanup_over_closure_slo': (types.cleanup
                                       + created(120)),
          'issues_over_six_months': created(182),
          'issues_over_a_year': created(365)}


pull_requests = {'pull_requests_with_no_type': (no+types.bug
                                                + no+types.feature
                                                + no+types.question
                                                + no+types.cleanup
                                                + no+types.process),
                 'pull_requests_over_response_slo': updated(2),
                 'pull_requests_over_closure_slo': created(5),
                 'pull_requests_over_six_months': created(182),
                 'pull_requests_over_a_year': created(365)}


for issue in issues:
    if not issues[issue]:
        continue
    params = {'q': 'is:open is:issue ' + issues[issue]}
    url = github_url + 'issues?'
    try:
        query(url, params, issue)
    except AttributeError:
        import pdb
        pdb.set_trace()


for pull_request in pull_requests:
    if not pull_requests[pull_request]:
        continue
    params = {'q': 'is:open is:pr ' + pull_requests[pull_request]}
    url = github_url + 'pulls?'
    query(url, params, pull_request)

print(datetime.now())
