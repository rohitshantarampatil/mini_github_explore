import requests 
import sys
import json
from termcolor import colored
## AUTHOR :- ROHIT PATIL
#Token


TOKEN = "<Your Github Access Token here>"
headers = {'Authorization':"Token "+TOKEN,'Accept':'application/vnd.github.cloak-preview'}

'''
Getting the repositories using github search API
'''
def getrepos(company,n,m):
    repos=[]
    repo_min = []
    numpages = None

    
    if n<100:
        try:
            url = f"https://api.github.com/search/repositories?q=org:{company}&page=1&per_page={n}&sort=forks"
            repo=requests.get(url,headers=headers).json()
            repos.append(repo)
        except :
            pass
    else:
        numpages = n//100+1

        for i in range(numpages):
            try:
                url = f"https://api.github.com/search/repositories?q=org:{company}&page={i}&per_page=100&sort=forks"
                repo=requests.get(url,headers=headers).json()
                repos.append(repo)
            except Execption as e:
                pass
    print("Received repositories")
    ## Extractiong Repo name and forks
    for i in repos:
        for j in i['items']:
            repo_min.append({"full_name":j['full_name'],'forks':j['forks']})
    repo_min = repo_min[:n]

    commits = []
    for repo in repo_min:
        commit = getcommits(repo,m)
        commits.append(commit)

    return repo_min,commits

    
'''
Getting Commits from each repo
'''
def getcommits(repo,m):
    commits = None
    repo_name = repo['full_name']
    committees = []
    try:
        url = f"https://api.github.com/repos/{repo_name}/stats/contributors"
        commits=requests.get(url,headers=headers).json()
        print("Received commits for ",repo['full_name'])
    except:
        pass
    for c in commits:
        committees.append({'user':c['author']['login'],'total_commits':c['total']})
    
    committees.sort(key = lambda x:x['total_commits'],reverse=True)
    return committees[:m]



if __name__ == "__main__":
    while True:
        print('\n')
        print(colored("################################################################",'green'))
        print('Welcome to github explore mini by Rohit Patil')
        print('instructions: ')
        print('1) Please enter input in following format')
        print('   <organization> <n> <m>')
        print('   e.g : google 10 4')
        print('2) write 0 to exit')


        inp = input().split()

        if inp[0]=='0':
            print("Thank you")
            break

        org,n,m = inp[0],int(inp[1]),int(inp[2])
        print('Please wait while we receive data')
        try:
            result=getrepos(org,n,m)
            repo_min,commits = result[0],result[1]
            for i,repo in enumerate(repo_min):
                print(" \n "+str(i+1)+". Repository name : ",colored(repo['full_name'],'cyan')," Number of forks: ",str(repo['forks']))
                print('Top m committees')
                for user in commits[i]:
                    print("    username: ",colored(user['user'],'yellow'),', number of commits: ',colored(user['total_commits'],'yellow') )
        except:
            print(colored('Error'),"Please check your input")
        print(colored("################################################################",'green'))
