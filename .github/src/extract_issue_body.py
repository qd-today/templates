import base64
import json
import os
import time

with open('tpls_history.json', 'r', encoding='utf8') as f:
    hfile = json.loads(f.read())
issue_body = os.getenv('ISSUE_JSON','{}')
issue_json:dict = json.loads(issue_body)
repo_full_name = os.getenv('REPO_FULL_NAME','')
repo_default_branch = os.getenv('REPO_DEFAULT_BRANCH','')
if len(issue_json) > 0 and 'name' in issue_json and 'author' in issue_json and 'filename' in issue_json and 'har_content' in issue_json:
    commenturl = os.getenv('ISSUE_URL','')
    issue_json['name'] = issue_json['name'].replace(' ','_')
    issue_json['filename'] = issue_json['filename'].replace(' ','_')
    har_content = issue_json['har_content'].replace('```JSON','').replace('```','').strip()
    try:
        har_content = json.loads(har_content)
    except:
        os._exit(0)

    update = False
    if 'har' not in hfile or not isinstance(hfile['har'], dict):
        hfile['har'] = {}
    elif issue_json['name'] in hfile['har']:
        update = True
    else:
       for k,v in list(hfile['har'].items()):
            if v['commenturl'] == commenturl:
                hfile['har'][issue_json['name']] = v
                update = True
                hfile['har'].pop(k)
                break

    if not issue_json['filename']:
        issue_json['filename'] = issue_json['name'] + '.har'
    if not issue_json['filename'].endswith('.har'):
        issue_json['filename'] = issue_json['filename'] + '.har'
    if update and issue_json['filename'] != hfile['har'][issue_json['name']]['filename'] and os.path.exists(hfile['har'][issue_json['name']]['filename']):
        os.remove(hfile['har'][issue_json['name']]['filename'])

    content_jsonstring = json.dumps(har_content, indent=4, ensure_ascii=False)
    with open(issue_json['filename'], 'w', encoding='utf8') as f:
        f.write(content_jsonstring)

    har = {
        'name': issue_json['name'],
        'author': issue_json['author'],
        'url': 'https://raw.githubusercontent.com/'+ repo_full_name + '/' + repo_default_branch + '/' + issue_json['filename'],
        'update': update,
        'comments': issue_json.get('comments','').replace('\\r', '\r').replace('\\n', '\n').replace('\r','').replace('\n','<br>').strip(),
        'filename': issue_json['filename'],
        'content': base64.b64encode(content_jsonstring.encode('utf8')).decode('utf8'),
        'date': hfile['har'][issue_json['name']]['date'] if update else time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
        'version': hfile['har'][issue_json['name']]['version'] if update else time.strftime('%Y%m%d', time.localtime()),
        'commenturl': commenturl
    }

    # 判断更新后的hfile['har'][issue_json['name']]是否与原来的一致，如果一致则不更新
    if not hfile['har'].get(issue_json['name']):
        hfile['har'][issue_json['name']] = har
    elif update and hfile['har'][issue_json['name']] != har:
        hfile['har'][issue_json['name']] = har
        hfile['har'][issue_json['name']]['date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        hfile['har'][issue_json['name']]['version'] = time.strftime('%Y%m%d', time.localtime())

    with open('tpls_history.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(hfile, indent=4, ensure_ascii=False))
