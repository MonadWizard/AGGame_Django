create or replace function get_team_basic_data(team_id varchar)
returns jsonb
as
    $$
declare
    result jsonb;
begin
    select json_build_object(
        'team_owner', team_owner,
        'team_logo', team_logo,
        'team_creator_id', team_creator_id,
        'game_name', game_name,
        'team_name',team_name,
        'country_of_the_team',country_of_the_team,
        'country_of_game_playing',Country_of_GamePlaying,
        'team_email',team_email ,
        'team_mobile', team_mobile
    ) into result
    from team
    where team.team_id= $1;
    return result;
end;
$$
language plpgsql;


drop function get_team_basic_data(team_id varchar);

select get_team_basic_data('757720230327055031384');

select * from team;