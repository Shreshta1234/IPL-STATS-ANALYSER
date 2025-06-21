import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """
    Loads match and delivery data from CSV files.
    """
    matches = pd.read_csv("ipl_data/matches.csv")
    deliveries = pd.read_csv("ipl_data/deliveries.csv")
    return matches, deliveries


@st.cache_data
def get_season_match_ids(matches_df, season):
    """
    Gets all match IDs for the selected season.
    """
    return matches_df[matches_df['season'] == season]['id'].unique()


@st.cache_data
def get_season_summary(matches_df, season):
    """
    Returns summary stats for a selected season.
    """
    season_data = matches_df[matches_df['season'] == season]
    total_matches = season_data.shape[0]
    top_team = season_data['winner'].value_counts().idxmax()
    wins = season_data['winner'].value_counts().max()

    return pd.DataFrame({
        "Season": [season],
        "Total Matches": [total_matches],
        "Most Wins (Team)": [top_team],
        "Wins": [wins]
    })


@st.cache_data
def get_player_runs(deliveries_df, match_ids, player):
    """
    Returns total runs scored by the selected player in the selected matches.
    """
    player_data = deliveries_df[
        (deliveries_df['match_id'].isin(match_ids)) & 
        (deliveries_df['batsman'] == player)
    ]
    return player_data['batsman_runs'].sum()


@st.cache_data
def get_team_matches(matches_df, season, team):
    """
    Returns all matches a team played in a selected season.
    """
    return matches_df[
        ((matches_df['team1'] == team) | (matches_df['team2'] == team)) &
        (matches_df['season'] == season)
    ][['date', 'team1', 'team2', 'winner']]