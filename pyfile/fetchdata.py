from get_nba_data import advanced_stats

advanced = advanced_stats()
fatties = advanced.get_data(college="duke", weight=">250")
sticks = advanced.get_data(college="duke", weight="<200")
