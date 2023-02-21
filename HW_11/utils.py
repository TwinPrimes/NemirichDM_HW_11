import json


def load_candidates_from_json():
    with open('candidates.json', 'rt', encoding='UTF-8') as file:
        candidates = json.loads(file.read())
        return candidates


def get_candidates_list():
    candidates = []
    candidates_data = load_candidates_from_json()
    for candidate in candidates_data:
        candidates.append(candidate['name'])
    return candidates


def get_candidate_by_id(id_):
    candidates_data = load_candidates_from_json()
    for candidate in candidates_data:
        if candidate['id'] == id_:
            return candidate['name']


def get_candidates_by_name(name_):
    candidates = {}
    candidates_data = load_candidates_from_json()
    for candidate in candidates_data:
        if candidate['name'].split(' ')[0].lower() == name_.lower():
            candidates[candidate['id']] = candidate['name']
    return candidates


def get_candidates_by_skill(skill_):
    candidates = {}
    candidates_data = load_candidates_from_json()
    for candidate in candidates_data:
        if skill_.lower() in candidate['skills'].lower().split(', '):
            candidates[candidate['id']] = candidate['name']
    return candidates
