create or replace function get_team_stats(team_id varchar)
returns jsonb
as
    $$
declare
    stats jsonb;
begin
    select json_build_object(
       'Teams_Avg', Teams_Avg,
'Number_of_Games_Played', Number_of_Games_Played,
'Number_of_Games_Won', Number_of_Games_Won,
'Number_of_Games_Drawn', Number_of_Games_Drawn,
'Number_of_Games_Lost', Number_of_Games_Lost,
'Number_of_Games_Abandoned', Number_of_Games_Abandoned,
'Number_of_Runs', Number_of_Runs,
'Number_of_Balls_Faced', Number_of_Balls_Faced,
'Number_of_Wickets_Taken', Number_of_Wickets_Taken,
'Number_of_Balls_Bowled', Number_of_Balls_Bowled,
'Batting_Average', Batting_Average,
'Strike_Rate', Strike_Rate,
'Teams_TournamentRating', Teams_TournamentRating,
'Number_of_Tournament_Participated', Number_of_Tournament_Participated
    ) into stats
    from team
    where team.team_id= $1;
    return stats;
end;
$$
language plpgsql;



drop function get_team_stats(team_id varchar);

select get_team_stats('757720230327055031384');

select * from team;