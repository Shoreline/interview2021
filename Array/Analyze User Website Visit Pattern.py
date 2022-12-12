# For each user, find all patterns from his/her browsing history
# Then count pattern frequency based on all users
#
# itertools.combinations(a_list, num):
#   Each combination is a list
#   elements in each returned combination are kept the same sequence as in the input list
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # <username, list<website>> map. We want website to be added by time sequence
        user_to_sitelist = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):  # sort by time
            user_to_sitelist[u].append(w)  # note that sites in sitelist can be duplicated

        # Count for all patterns (all combinations of every 3 sites), how many user visited it.
        patterns = Counter()  # key is a set of 3 sites
        for sites in user_to_sitelist.values():
            unique_site_combos = set(itertools.combinations(sites, 3))
            patterns.update(Counter(unique_site_combos))  # we are told each pattern has 3 sites

        # Two sorts: 1) sort by the counter's value; 2) sort by the key
        # return max(sorted(patterns), key=patterns.get)
        # return min(patterns, key=lambda k: (-patterns[k], k))
        return min(patterns.items(), key=lambda x: (-x[1], x[0]))[0]

# Here is the complete solution without explanation.
# Detailed explanation can be found below.


#     def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

#         users = defaultdict(list)

#         for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])):
#             users[user].append(site)

#         patterns = Counter()

#         for user, sites in users.items():
#             patterns.update(Counter(set(combinations(sites, 3))))

#         return max(sorted(patterns), key=patterns.get)
# DETAILED SOLUTION

# Libraries used: itertools, collections
# Note:
# These libraries aren't necessearily needed but they definitely help speed up the process of writing code while also making the solution more efficient.
# However, it is certainly possible to manually code the functions of these libraries that we will be using.
# So far, I have noticed that these are standard and common libraries, so they can be used in interviews too.

# class Solution:
#     def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

# 		# Create tuples as shown in description
# 		# The timestamps may not always be pre-ordered (one of the testcases)
# 		# Sort first based on user, then time (grouping by user)
# 		# This also helps to maintain order of websites visited in the later part of the solution

# 		users = defaultdict(list)
# 	    # It is not necessary to use defaultdict here, we can manually create dictionaries too

#         for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])):
#             users[user].append(site)     # defaultdicts simplify and optimize code

#         patterns = Counter()   # this can also be replaced with a manually created dictionary of counts

# 		# Get unique 3-sequence (note that website order will automatically be maintained)
# 		# Note that we take the set of each 3-sequence for each user as they may have repeats
# 		# For each 3-sequence, count number of users

#         for user, sites in users.items():
#             patterns.update(Counter(set(combinations(sites, 3))))

# 		# Re-iterating above step for clarity
# 		# 1. first get all possible 3-sequences combinations(sites, 3)
# 		# 2. then, count each one once (set)
# 		# 3. finally, count the number of times we've seen the 3-sequence for every user (patterns.update(Counter))
# 		# - updating a dictionary will update the value for existing keys accordingly (int in this case)

# 		# An expanded version of the above step is given below.

#     #         print(patterns)  # sanity check

# 		# get most frequent 3-sequence sorted lexicographically
#         return max(sorted(patterns), key=patterns.get)
# Expanding that one confusing (but most critical!) part of the solution:
# It seems like one-liner code is perceived as "more cool" sometimes.
# It may also lead to some performance optimization.
# However, when we are learning neat tricks for the first time, it helps to look at an expanded version and then make it concise.

# for user, sites in users.items():
# 	patterns.update(Counter(set(combinations(sites, 3))))
# The above step can be expanded as:

# for user, sites in users.items():

# 	three_sequence_combos = combinations(sites, 3)
# 	three_sequence_combos = set(three_sequence_combos)    # avoid counting repeats

# 	three_sequence_combos = Counter(three_sequence_combos)     # convert to dictionary of counts
# 	patterns.update(three_sequence_combos)    # count the number of users having the same 3-sequence
