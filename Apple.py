access_token = "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"
g = Github(access_token)
current_user = g.get_user()
print(current_user.name)