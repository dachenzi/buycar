import hashlib


def get_password_md5(string):
    """
    Encrypt the password entered by the user
    :param string: Password
    :return: md5 string
    :param string:
    :return:
    """
    md5 = hashlib.md5()
    md5.update(string.encode('utf-8'))
    return md5.hexdigest()


