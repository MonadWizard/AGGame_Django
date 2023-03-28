create or replace function get_tournament_info(tournament_owner_id varchar,passing_limit int, passing_offset int)
RETURNS jsonb AS $$
DECLARE
  result jsonb; --location will be passed, ill be returning the countires near
  offset_value int;
  limit_value int;
BEGIN

  offset_value := passing_offset;
  limit_value := passing_limit;

  SELECT jsonb_agg(tournament_details) INTO result
  FROM (
    SELECT *
    FROM tournament
    where tournament_owner_id = $1
    ORDER BY tournament_id --id
    OFFSET offset_value LIMIT limit_value
  ) tournament_details;

  RETURN result;
END;
$$ LANGUAGE plpgsql;


select * from tournament;


select get_tournament_info('0327050834329034',3,1);