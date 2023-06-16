import json
import os

with open('tpls_history.json', 'r', encoding='utf8') as f:
    hfile = json.loads(f.read())
issue_body = os.getenv('ISSUE_JSON','{}')
issue_json:dict = json.loads(issue_body)
if len(issue_json) > 0 and 'name' in issue_json and 'filename' in issue_json:
    commenturl = os.getenv('ISSUE_URL','')
    issue_json['name'] = issue_json['name'].replace(' ','_')
    issue_json['filename'] = issue_json['filename'].replace(' ','_')
    filename = issue_json['filename']
    existed = False
    if 'har' not in hfile or not isinstance(hfile['har'], dict):
        hfile['har'] = {}
    elif issue_json['name'] in hfile['har']:
        existed = True
        if filename != hfile['har'][issue_json['name']]['filename'] and os.path.exists(hfile['har'][issue_json['name']]['filename']):
            os.remove(hfile['har'][issue_json['name']]['filename'])
        hfile['har'].pop(issue_json['name'])
    else:
       for k,v in list(hfile['har'].items()):
            if v['commenturl'] == commenturl:
                existed = True
                if filename != v['filename'] and os.path.exists(v['filename']):
                    os.remove(v['filename'])
                hfile['har'].pop(k)
                break

    if os.path.exists(filename):
        os.remove(filename)

    if existed:
        print('True')
        with open('tpls_history.json', 'w', encoding='utf8') as f:
            f.write(json.dumps(hfile, indent=4, ensure_ascii=False))
    else:
        print('False')
else:
    print('False')
