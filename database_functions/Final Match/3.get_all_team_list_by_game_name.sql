select get_all_Team_list_by_game_name('cricket',10,1);



create or replace function get_all_team_list_by_game_name(gamename text, limiting_val int, offset_val int)
returns jsonb
as
$$
declare
  result jsonb;
  offset_value_stored int;
  limit_value_stored int;
begin
  offset_value_stored := offset_val;
  limit_value_stored := limiting_val;

  SELECT jsonb_agg(team) INTO result
  FROM (
    SELECT team_id,team_name
    FROM team
    ORDER BY team.team_id
    OFFSET offset_value_stored LIMIT limit_value_stored
  ) team;

raise notice '%', result;
  return result;
end;
$$
language plpgsql;

select * from team;