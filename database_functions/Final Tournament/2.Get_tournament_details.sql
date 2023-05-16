CREATE OR REPLACE FUNCTION get_tournament_details(tournament_id varchar, gamename text)
RETURNS jsonb AS $$
DECLARE
    result jsonb;
BEGIN
    SELECT json_agg(t) INTO result
    FROM (
        SELECT *
        FROM tournament
        WHERE tournament.tournament_id = $1
    ) t;
    RETURN result;
END;
$$ LANGUAGE plpgsql;

select get_tournament_details('470120230327065356771','cricket');

select * from tournament;