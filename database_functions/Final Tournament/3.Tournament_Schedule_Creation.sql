CREATE OR REPLACE FUNCTION tournament_schedule(data jsonb) RETURNS void AS $$
DECLARE
    obj json;
    query text ;
    t_match_id varchar;
    t_match_time timestamp;
    t_match_number varchar;
    table_store text;
    id_store varchar;
    query1 text;
    team_id1 varchar;
    team_id2 varchar;
BEGIN
 FOR obj IN SELECT * FROM json_array_elements(data::text::json)
    LOOP

      id_store := obj ->> 'tournament_id';
        table_store := '"' || id_store  || '__tournamentShedule'|| '"';
        t_match_number := (obj ->> 'tmatch_no')::VARCHAR;
        t_match_time := obj ->> 'tmatch_date' ;
        t_match_id := obj ->> 'tournament_id' || '_' || TO_CHAR(t_match_time, 'YYYYMMDDHH24MISSMS') || '_' || t_match_number;

       query := format('INSERT INTO %s
                       (tmatch_id,tournament_id, tmatch_date, tmatch_reportingtime,tmatch_team1,tmatch_team2,tmatch_no, tmatch_status,tmatchfield_name,tmatchfield_gmap)
                     VALUES (''%s'',''%s'', ''%s'', ''%s'',''%s'', ''%s'',''%s'',''%s'', ''%s'',''%s'')',
                    table_store,
                    t_match_id,obj ->> 'tournament_id', obj ->> 'tmatch_date',obj ->> 'tmatch_reportingtime', obj ->> 'tmatch_team1',obj ->> 'tmatch_team2',obj ->> 'tmatch_no',obj ->> 'tmatch_status', obj ->> 'tmatchfield_name', obj ->> 'tmatchfield_gmap');

    execute query;
--     raise notice 'query:::::::: %',query;

    team_id1 := obj ->> 'tmatch_team1';
    team_id2 := obj ->> 'tmatch_team2';


   IF EXISTS (
      SELECT 1
FROM team
WHERE ((team_id = team_id1 OR team_id = team_id2)
  AND NOT id_store = ANY(ARRAY(SELECT quote_literal(tp) FROM unnest(tournament_perform) AS tp)))
    ) THEN

      query1 := format('UPDATE team SET tournament_perform = array_append(tournament_perform, %L) WHERE team_id = %L OR team_id = %L', id_store, team_id1, team_id2);

--         raise notice 'query 1 ################ %',query1;

              EXECUTE query1;

END IF;

    END LOOP;
 UPDATE team SET tournament_perform = (SELECT ARRAY(SELECT DISTINCT unnest(tournament_perform))) WHERE array_length(tournament_perform, 1) > 1;

END;
$$ LANGUAGE plpgsql;


SELECT tournament_schedule('[
{"tournament_id":"142520230402083023696",
  "tmatch_date": "2024-11-18 15:20:00",
  "tmatch_reportingtime": "02:48",
"tmatch_team1":"202020230327074550833",
"tmatch_team2":"312520230327074551961",
"tmatch_no":"61634",
"tmatch_status":"won 5 matches",
"tmatchfield_name":"Army Stadium",
"tmatchfield_gmap":"somelink.com"
},
{"tournament_id":"142520230402083023696",
"tmatch_date": "2024-12-20 15:20:00",
"tmatch_reportingtime": "02:45",
"tmatch_team1":"202020230327074550833",
"tmatch_team2":"312520230327074551961",
"tmatch_no":"75812",
"tmatch_status":"won 5 matches",
"tmatchfield_name":"Army Stadium",
"tmatchfield_gmap":"somelink.com"}
]'::jsonb
);

select * from tournament;
-- 142520230402083023696

select * from team where team_id = '202020230327074550833';

-- 202020230327074550833
-- 312520230327074551961


select * from team where team_id = '516620230330062221106' ;

select * from "142520230402083023696__tournamentShedule";


select * from team where team_id='425220230402085506305';























