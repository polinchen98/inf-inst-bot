import re


def nbsp2space(value):
    return re.sub(' ', ' ', value, flags=re.IGNORECASE)


def parse(html):
    match = re.search(r'<meta content=\"([\d ]+)\D+([\d ]+)\D+([\d ]+).*$', nbsp2space(html), re.MULTILINE)

    if not match:
        return None

    followers = match.group(1)
    following = match.group(2)
    publications = match.group(3)

    comments = re.findall(r'comment\":{\"count\":(\d+)}', html, re.MULTILINE)

    if not comments:
        return None

    comments = [int(x) for x in comments]
    average_comments = sum(comments[:12]) // 12

    likes = re.findall(r'liked_by\":{\"count\":(\d+)', html, re.MULTILINE)

    if not likes:
        return None

    likes = [int(x) for x in likes]
    average_likes = sum(likes[:12]) // 12

    return followers, following, publications, average_comments, average_likes


