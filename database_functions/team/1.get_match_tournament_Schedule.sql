create or replace function team_schedule(teamid varchar(255))
returns jsonb
as
$$
declare
    result jsonb;
begin
select json_agg(json_build_object(
    'game_id',game_id,
    'game_datetime',game_datetime
)) into result
    from match
    where (game_name ->> 'Team_1' = $1 or game_name ->> 'Team_2' = $1) and game_datetime > now();

return result;
end;
$$
language plpgsql;

explain analyse

select team_schedule('757720230327055031384');

drop function team_schedule;

select * from team;

select * from match;

select * from tournament_schedule;