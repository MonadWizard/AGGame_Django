create or replace function get_team_info(team_creator_id varchar,passing_limit int, passing_offset int)
RETURNS jsonb AS $$
DECLARE
  result jsonb; --location will be passed, ill be returning the countires near
  offset_value int;
  limit_value int;
BEGIN

  offset_value := passing_offset;
  limit_value := passing_limit;

  SELECT jsonb_agg(team_details) INTO result
  FROM (
    SELECT *
    FROM team
    where team.team_creator_id = $1
    ORDER BY team_creator_id --id
    OFFSET offset_value LIMIT limit_value
  ) team_details;

  RETURN result;
END;
$$ LANGUAGE plpgsql;


-- select * from team;


select get_team_info('0329043540613666',7,0);




select * from team where team_creator_id = '0329043540613666';

select * from auth_user_app_user;




