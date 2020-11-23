def shorten(txt):
    """Creates an shorten from eny text.

    :param str: eny text
    :rtype: str
    :return: shortened
    """
    sh_str = str(txt)
    words = sh_str.split(' ')
    sh_str = ""
    for word in words:
        sh_str += word[0]

    sh_str = sh_str.upper()
    return sh_str


if __name__ == '__main__':
    shortened = shorten("Don't repeat yourself")
    print(shortened)

    shortened = shorten("Read the fine manual")
    print(shortened)

    shortened = shorten("All terrain armoured transport")
    print(shortened)
