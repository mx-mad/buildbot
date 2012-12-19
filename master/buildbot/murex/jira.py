import json
import httplib2

class JiraClient():
    def __init__(self, server, username=None, password=None):
        self.server = server
        self.username = username
        self.password = password
        self.base_url = "http://%s/rest/api/2" % server
        self.http = httplib2.Http( disable_ssl_certificate_validation=True)
        self.http.add_credentials(self.username, self.password)

    def request(self, path, verbose=False):
        req_url = "%s/%s" % (self.base_url, path)
        print "[jira] - request: %s" % req_url
        try:
            response, content = self.http.request(req_url, "GET", headers={'Content-Type' : 'application/json'})
        except Exception,ex:
            print "[jira] - exception: %s " % ex
            return
     
        if int(response.status) != 200:
            print "[jira] - bad status code: %s " % int(response.status)
            return

        try:
            data = json.loads(content)
        except:
            print "[jira] - bad data format: %s " % content
            return

        if verbose:
            print json.dumps(data, sort_keys=True, indent=4)
        data['tpks'] = [1452, 4556]
        return data

    def getProjects(self):
        print self.base

    def getIssue(self, issue):
        path = "issue/%s" % issue
        return self.request(path)

    # get issues
    def getIssues(self, assignee=None):
        path = "search?jql=assignee=%s" % assignee
        return self.request(path)

if __name__ == '__main__':
    jira = JiraClient('mxjira')
    print jira.getIssue("CI-42")