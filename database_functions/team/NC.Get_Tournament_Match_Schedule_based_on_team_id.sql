
CREATE OR REPLACE FUNCTION tournament_perform_details(teamid varchar)
RETURNS jsonb AS $$
DECLARE
  tournament_id_list varchar[];
  tournament_id varchar;
  tournament_schedule varchar;
  storing_data timestamp[];
    storing_match_data timestamp[];

  result_json jsonb := '[]'::jsonb;
match_result jsonb := '[]'::jsonb;
    result jsonb;
    BEGIN
  SELECT tournament_perform INTO tournament_id_list FROM team WHERE team_id = teamid;

  FOREACH tournament_id IN ARRAY tournament_id_list LOOP
  tournament_schedule := tournament_id || '__tournamentShedule';
  EXECUTE format('SELECT array_agg(tmatch_date) FROM %I WHERE %I.tmatch_team1 = $1 OR %I.tmatch_team2 = $1', tournament_schedule,tournament_schedule,tournament_schedule)
    INTO storing_data
    USING teamid;
  result_json = result_json || jsonb_build_object(tournament_id, storing_data);
END LOOP;



   SELECT array_agg(game_datetime) INTO storing_match_data
FROM match
WHERE team1 = $1 OR team2 = $1;

result = jsonb_build_object('tournament_details', result_json, 'match_datetime', jsonb_build_array(storing_match_data));

   raise notice 'result here %',result;
RETURN result;
END;
$$ LANGUAGE plpgsql;



select tournament_perform_details('219120230327074511488');


SELECT * FROM match;



