def shorten(txt):
    sh_str=str(txt)
    sh_str=sh_str.upper()
    sh_str=""
    for word in words:
        sh_str+=word[0]

    sh_str = sh_str.split(' ')
    return sh_str
