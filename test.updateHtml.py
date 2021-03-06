# -*- coding: UTF-8 -*-
import PixivUtil2

import getpass

br = None

def prepare():
    global br
    PixivUtil2.__config__.loadConfig()
    br = PixivUtil2.configBrowser()

    ## Log in
    username = PixivUtil2.__config__.username
    if username == '':
        username = raw_input('Username ? ')
    password = PixivUtil2.__config__.password
    if password == '':
        password = getpass.getpass('Password ? ')
        
    result = False
    if len(PixivUtil2.__config__.cookie) > 0:
        result = PixivUtil2.pixivLoginCookie()

    if not result:
        if PixivUtil2.__config__.useSSL:
            result = PixivUtil2.pixivLoginSSL(username,password)
        else:
            result = PixivUtil2.pixivLogin(username,password)

def downloadPage(url, filename):
    print "Dumping " + url + " to " + filename
    html = br.open(url).read()
    try:
        dump = file(filename, 'wb')
        dump.write(html)
        dump.close()
    except :
        pass
    
def main():
    prepare()
    ## ./test/test-image-manga.htm
    ## http://www.pixiv.net/member_illust.php?mode=medium&illust_id=28820443
    downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=28820443', './test/test-image-manga.htm')

    ## ./test/test-image-unicode.htm
    ## http://www.pixiv.net/member_illust.php?mode=medium&illust_id=2493913
    downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=2493913', './test/test-image-unicode.htm')

    ## ./test/test-helper-avatar-name.htm
    ## http://www.pixiv.net/member_illust.php?id=1107124
    downloadPage('http://www.pixiv.net/member_illust.php?id=1107124', './test/test-helper-avatar-name.htm')

    downloadPage('http://www.pixiv.net/member_illust.php?id=1', './test/test-nouser.htm')
    downloadPage('http://www.pixiv.net/member_illust.php?id=26357', './test/test-member-noavatar.htm')
    downloadPage('http://www.pixiv.net/member_illust.php?id=1233', './test/test-noimage.htm')
    downloadPage('http://www.pixiv.net/bookmark.php?id=3281699', './test/test-member-bookmark.htm')

    downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=32039274', './test/test-image-info.html')
    downloadPage('http://www.pixiv.net/bookmark_new_illust.php', './test/test-bookmarks_new_ilust.htm')
    downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=12467674', './test/test-image-my_pick.html')
    downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=20496355', './test/test-image-noavatar.htm')
    downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=11164869', './test/test-image-parse-tags.htm')
    downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=9175987', './test/test-image-no_tags.htm')
    downloadPage('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=28865189', './test/test-image-rate_count.htm')
    ## downloadPage('http://www.pixiv.net/member_illust.php?mode=big&illust_id=20644633', './test/test-image-parsebig.htm')
    downloadPage('http://www.pixiv.net/member_illust.php?mode=manga&illust_id=20592252', './test/test-image-parsemanga.htm')
    downloadPage('http://www.pixiv.net/bookmark.php', './test/test-image-bookmark.htm')
    
    ## Not updated:
    ## ./test/test-login-error.htm
    ## ./test/test-member-suspended.htm
    ## ./test/test-member-nologin.htm
    

if __name__ == '__main__':
    main()
