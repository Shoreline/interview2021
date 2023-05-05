# People with multiple accounts always use the same name to register.
# Graph problem:
#   Each account is a node, let its index in accounts to be its acct_id
#   Each person is a cluster of nodes, all people are a forest
#       Accounts of the same person are connected
#   Each email is an edge -> build a map<email, list<connected_acct_id>> to save edge info
#       One account can link to another account through their shared email address.
#   For each account, do DFS to find out connected accounts (belonging to the same person), and return their email
#   union.
# copied
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Build up the graph.
        # Give each account an ID, (just use its index in accounts)
        # map of <email, [index1, index2,...]>, "johnsmith@mail.com": [0, 2],
        email_to_acct_ids = collections.defaultdict(list)
        for acct_id, account in enumerate(accounts):
            # start from 1 since account[0] is account_name, email addresses start from account[1]
            for j in range(1, len(account)):
                email = account[j]
                email_to_acct_ids[email].append(acct_id)

        # DFS code for traversing accounts.
        # For each account_id i, find emails from all accounts belonging to the same person
        visited = set()

        # emails is a list to be modified and use as the result of this function
        def dfs(acct_id, emails):
            if acct_id in visited:
                return
            visited.add(acct_id)
            for i in range(1, len(accounts[acct_id])):
                email = accounts[acct_id][i]
                emails.add(email)
                for neighbor_acct_id in email_to_acct_ids[email]:
                    dfs(neighbor_acct_id, emails)

        # Perform DFS for accounts and add to result.
        res = []
        for acct_id, account in enumerate(accounts):
            if acct_id in visited:
                continue
            name, emails = account[0], set()
            dfs(acct_id, emails)
            res.append([name] + sorted(emails))  # concat two lists
        return res