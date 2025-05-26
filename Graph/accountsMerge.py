from typing import List
from collections import defaultdict

class Solution:
    """
    LeetCode 721: Accounts Merge

    Given a list of accounts where each element accounts[i] is a list of strings,
    where the first element accounts[i][0] is a name, and the rest are emails.
    Merge accounts that have the same email address, and return the merged accounts
    in the required format.

    Each account will be in the format: [name, email1, email2, ...], sorted by email.
    """

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Initialize parent and email_to_name
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
            first_email = account[1]
            for email in account[2:]:
                union(first_email, email)

        # Group emails by their root parent
        unions = defaultdict(list)
        for email in parent:
            root = find(email)
            unions[root].append(email)

        # Build the result
        result = []
        for root, emails in unions.items():
            result.append([email_to_name[root]] + sorted(emails))
        return result