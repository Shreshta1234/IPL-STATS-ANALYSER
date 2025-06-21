import streamlit as st
from utils.stats import (
    load_data, get_season_summary,
    get_team_matches, get_season_match_ids, get_player_runs
)

st.set_page_config(page_title="IPL Stats Analyzer", layout="centered")
st.title("IPL Stats Analyzer")

matches, deliveries = load_data()


st.sidebar.header(" Filters")
season = st.sidebar.selectbox("Season", sorted(matches['season'].unique()))
team = st.sidebar.selectbox("Team", sorted(set(matches['team1']).union(matches['team2'])))
player = st.sidebar.selectbox("Player", sorted(deliveries['batsman'].unique()))


st.subheader(f"📅Summary of Season {season}")
st.dataframe(get_season_summary(matches, season))


st.subheader(f"{team}'s Matches in {season}")
st.dataframe(get_team_matches(matches, season, team))


st.subheader(f"{player}'s Runs in {season}")
match_ids = get_season_match_ids(matches, season)
st.write(f"*Total Runs:* {get_player_runs(deliveries, match_ids, player)}")