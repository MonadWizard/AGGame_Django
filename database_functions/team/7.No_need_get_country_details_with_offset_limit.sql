create or replace function choose_your_country(passing_limit int, passing_offset int)
RETURNS jsonb AS $$
DECLARE
  result jsonb; --location will be passed, ill be returning the countires near
  offset_value int;
  limit_value int;
BEGIN

  offset_value := passing_offset;
  limit_value := passing_limit;

  SELECT jsonb_agg(general_settings) INTO result
  FROM (
    SELECT country_name,country_dial_code,country_short_name,country_flag
    FROM general_settings
    ORDER BY general_settings.general_settings --id
    OFFSET offset_value LIMIT limit_value
  ) general_settings;

  RETURN result;
END;
$$ LANGUAGE plpgsql;

drop function choose_your_country(passing_limit int, passing_offset int);

select choose_your_country(4,1);

select * from general_settings;

select * from team;

--ekta neighboring country table banaite hobe, neighbouring kon 4-5ta country(jsonb) ase ta dite hobe, country nam dewa hobe, oi nam dhore neighboring country er nam dibo