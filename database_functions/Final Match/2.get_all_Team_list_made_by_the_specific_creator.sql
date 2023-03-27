create or replace function get_team_list_by_creatorId (team_creators_id varchar,gamename text)
returns jsonb
as
$$
declare
result jsonb;
begin
select json_agg(json_build_object(
    'team_name',team_name,
    'team_id', team_id
           )) into result
from team
where team_creator_id = $1 and game_name = $2;
return result;
end;
$$
language plpgsql;

select get_team_list_by_creatorId('0327050758707019','cricket');

select * from team;

