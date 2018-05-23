from faker import Factory
import json
from math import floor

    # functions to generate random values
from random import expovariate, normalvariate, choice, randint, random, shuffle

    # Constants for Stores model
MIN_CHANNELS = 1
MAX_CHANNELS = 7
WORKSPACES = ('CS6660', 'CS6820',
              'CS6020', 'CS4245',
              'CS6240', 'CS3240', 
              'CS6500', 'CS3424',
              'CS6125', 'CS6020', 
              'CS6425', 'CS4820',
              'CS6480', 'CS4500', 
              'CS6400', 'CS6340',
              'CS6150', 'CS6780',
              'CS6000', 'CS4580',
              'CS3860', 'CS6790')
STATUSES = ('active',
                'In a meeting',
                'On holiday',
                'Commuting',
                'Out sick',
                'Working remotely'
                )

APPS = ('dropbox',
            'vote',
            'google drive',
            'twitter',
            'giphy',
            'box',
            'kyber')
NUMS = (1,2,3,4) #for choosing number of workspaces
NUMS_C = (4,5,6,7) #for choosing number of channels



# Constants to manage values in documents to generate
MIN_CATEGORIES = 1
MAX_CATEGORIES = 3    
MIN_POSTS = 0
MAX_POSTS = 500


NO_POSTS = 0.05
REVIEWS_LAMBDA = 3  # for exponential distribution

# Faker random value generator
generator = Factory.create()

# dict to save used store names
used_emails = []


# Output files
slack_file = None

class slack(object):
    def __init__(self, uname, email, status, workspaces, channels, apps, posts):
        self.uname = uname
        self.email = email
        self.status = status
        self.workspaces = workspaces
        self.channels = channels
        self.apps = apps
        self.posts = posts

    def __str__(self):
        '''
        Return JSON string for entire store document,
        compatible with mongoimport
        '''
        slackdict = {}
        slackdict["uname"] = self.uname
        slackdict["email"] = self.email
        slackdict["status"] = self.status
        slackdict["workspaces"] = self.workspaces
        slackdict["channels"] = self.channels
        slackdict["apps"] = self.apps
        slackdict["posts"] = self.posts
        return json.dumps(slackdict)



def gen_channels():
    '''
    Generate channels names
    '''
    used_channels = []
    channels = []
    prefixes = ('project', 'assignment', 'group-study', 'general', 'random')
    suffixes = ("1", "'2", "3", "4", "5","6","7","8")
    num_channels = choice(NUMS_C)
    for i in range(num_channels):
        channel = choice(prefixes) + choice(suffixes)
        while channel in used_channels:
            channel = choice(prefixes) + choice(suffixes)
        channels.append(channel)
        used_channels.append(channel)
    return channels


def gen_status():
    '''
    Generate status of a user
    '''
    return choice(STATUSES)

def gen_workspaces():
    '''
    Generate workspace accessed by a user
    '''
    used_workspaces = []

    workspaces = []
    
    num_workspaces = choice(NUMS)
    
    for i in range(num_workspaces):
        workspace = choice(WORKSPACES)
        while workspace in used_workspaces:
            workspace = choice(WORKSPACES)
        workspaces.append(workspace)
        used_workspaces.append(workspace)
    return workspaces


def gen_single_post():
    '''
    Generate a single post
    '''
    post = generator.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        # While the "lorem" generator can produce appropriate sizes
        # of text, the amount of text gets a bit overwhelming,
        # and it's in Latin
    post_date = generator.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
    post_date = post_date.isoformat()
    post_date = post_date + "Z"
    return {"post":post, "post_date":post_date}

def gen_email():
    email = generator.safe_email()    
    while email in used_emails:
        email = generator.safe_email()
    used_emails.append(email) 
    return email

def gen_posts():
    '''
    Generate list of reviews
    '''
    if random() < NO_POSTS:
        return []   # no reviews
    num_posts = int(expovariate(REVIEWS_LAMBDA)*MAX_POSTS)
    if num_posts > MAX_POSTS:
        num_posts = MAX_POSTS
    posts = []
    for post_index in range(num_posts):
        posts.append(gen_single_post())
    return posts



def generate_single_user():
    ''' 
    Generate fields for one store
    '''    
    new_user = slack(generator.name(),
                           gen_email(),
                           gen_status(),
                           gen_workspaces(),
                           gen_channels(),
                           choice(APPS),
                           gen_posts())
    slack_file.write(str(new_user) + '\n')
    return new_user

def generate_slack_users(num_users):
    '''
    Generate store records
    '''
    for user_index in range(num_users):
        generate_single_user()
    slack_file.close()

if __name__ == '__main__':
    import sys
    slack_file = open('slack.json', 'w')
    generate_slack_users(10000)


