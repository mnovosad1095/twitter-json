import json
import pprint


def get_dirs(js_f):
    """
    show the keys of the dict and let user select
    :param js_f:
    :return: str
    """
    for i in js_f.keys():
        print(i)
    selected = input('Select key, which you want: ')
    if selected in js_f.keys():
        return selected


def get_users(users):
    """
    creates users dict of type {username: users info dict}
    :param users: list(dicts)
    :return: dict
    """
    users_dict = dict()
    for user_object in users:
        username = user_object['name']
        users_dict[username] = user_object
    return users_dict


def select_user(users):
    """
    provides options to select for user
    :param users:
    :return: dict
    """
    for user in users.keys():
        print(user)
    selected_user = input("Select the user you want to get info about ")
    return users[selected_user]


def interact_with_user(js_f):
    """
    interacts with user, does the main work
    :param js_f:
    :return: nothing
    """
    key = get_dirs(js_f)
    if type(js_f[key]) == dict:
        get_dirs(js_f[key])
    elif key == 'users':
        user_dict = get_users(js_f['users'])
        selected_user = select_user(user_dict)
        interact_with_user(selected_user)

    else:
        pprint.pprint(js_f[key])
        print(type(js_f[key]))
        print("That's it")


if __name__ == '__main__':
    with open('user_friends.json', 'r', encoding='utf-8') as f:
        js = json.load(f)

    interact_with_user(js)



