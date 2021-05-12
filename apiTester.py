import requests

# leader board
lb = [
    'http://leaderboard-join.us-east-1.elasticbeanstalk.com/join',
    'http://ecleader-load.us-east-1.elasticbeanstalk.com/load',
    'http://ecleaderupdate.us-east-1.elasticbeanstalk.com/update',
    'http://leaderboard-join.us-east-1.elasticbeanstalk.com/leave',
    'https://lbload.temporal.echelonfit.com/leaderboard',
    'https://lbbeta1.temporal.echelonfit.com/api/pnjoin',
    'https://lbbeta1.temporal.echelonfit.com/api/leave',
    'https://lbbeta1.temporal.echelonfit.com/api/stat',
    'https://lbbeta1.temporal.echelonfit.com/api/ui',
    'https://lbbeta1.temporal.echelonfit.com/api/get',
    'https://lbbeta1.temporal.echelonfit.com/api/gettotals',
    'https://lbbeta1.temporal.echelonfit.com/api/getbadges',
    'https://lbbeta1.temporal.echelonfit.com/api/getpreviousclass',
    'https://lbbeta1.temporal.echelonfit.com/api/getclass',
    'https://lbbeta1.temporal.echelonfit.com/api/delete',
    'https://hydra.temporal.echelonfit.com/v1/router/queue']
# medianet
mn = [
    'https://medianet.echelonfit.com/api/playlists/get/',
    'https://medianet.echelonfit.com/api/stream/getsong']
# commcerial progress
cp = [
    'https://commercial.echelonfit.com/api/app/ride/create',
    'https://commercial.echelonfit.com/api/app/ride/update',
    'https://commercial.echelonfit.com/api/app/ride/end']
# URL for API
v1 = [
    'https://api.echelonfit.com/v1/api/',
    'https://api.echelonfit.com/v1/',
    'https://api.echelonfit.com/v1/api/favorites/',
    'https://api.echelonfit.com/v1/api/friends/',
    'https://api.echelonfit.com/v1/live/day/',
    'https://api.echelonfit.com/v1/live/',
    'https://api.echelonfit.com/v1/api/notifications/',
    'https://api.echelonfit.com/v1/api/ondemand/',
    'https://api.echelonfit.com/v1/ondemand/',
    'https://api.echelonfit.com/v1/api/addplan/',
    'https://api.echelonfit.com/v1/api/schedule/get',
    'https://api.echelonfit.com/v1/api/workout/',
    'https://api.echelonfit.com/v1/api/user/product/',
    'https://api.echelonfit.com/v1/programs/',
    'https://ex5sapi.echelonfit.com/billing/',
    'https://api.echelonfit.com/v1/ex5s/firmware/new',
    'https://api.echelonfit.com/v1/ex5s/update',
    'https://api.echelonfit.com/v1/appversion/add',
    'https://api.echelonfit.com/v1/family/',
    'https://api.echelonfit.com/v1/user/',
    'https://api.echelonfit.com/v1/user/leaderboard/preferences',
    'https://api.echelonfit.com/v1/user/leaderboard/preferences/old/city',
    'https://api.echelonfit.com/v1/user/leaderboard/preferences/old/status',
    'https://api.echelonfit.com/v1/user/nickname',
    'https://api.echelonfit.com/v1/preferences/',
    'https://beaconfarm.co/api/activityByEmailHash',
    'https://api.echelonfit.com/v1/filters/new/list',
    'https://api.echelonfit.com/v1/user/metrics',
    'https://api.echelonfit.com/v1/configuration/buttons']
# update user info
ui = [
    'https://api.echelonfit.com/v1/user/nickname',
    'https://api.echelonfit.com/v1/user/image']

api = [lb, mn, cp, v1, ui]
x = 0

if __name__ == "__main__":
    for apis in range(len(api)):
        for urls in range(len(api[apis])):
            x += 1
            url = api[apis][urls]
            response = requests.get(url)
            code = response.status_code
            print(x, ': ', url)
            print(code)
            if code == 200:
                print(response.text)
            elif code in (400, 401, 403):
                print('!!!!!-NOT AUTHORIZED-!!!!!')
            elif code in (500, 501, 502, 503, 504):
                print('!!!!!-SERVER ERROR-!!!!!')
            elif code == 404:
                print('~~~~~-Theres Nothing Here-~~~~~')
            else:
                print(response.text)
            print('......................................................\n')
