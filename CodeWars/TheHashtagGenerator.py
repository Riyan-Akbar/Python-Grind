def generate_hashtag(s):
    #your code here
    s = " ".join(s.split())
    s = s.title()
    ans = "#"+"".join(s.split())
    if len(ans) > 140 or len(s) == 0:
        return False
    else:
        return ans


