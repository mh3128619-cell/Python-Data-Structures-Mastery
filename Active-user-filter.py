all_users = ["ahmed", "sara", "mohamed", "ali", "sara", "ahmed", "omar"]
blocked_users = ["ali", "omar"]

all_users_set = set(all_users)
blocked_users_set = set(blocked_users)

print(all_users_set)
print(blocked_users_set)

active_users = all_users_set - blocked_users_set
print(active_users)
