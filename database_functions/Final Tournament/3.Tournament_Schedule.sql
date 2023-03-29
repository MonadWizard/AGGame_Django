
SELECT print_json(ARRAY[
'{"tournament_id":"822420230327085423799",
                                  "tmatch_date": "2023-03-01 15:20:00",
                                  "tmatch_reportingtime": "02:45",
                                  "tmatch_teams":{"playerId": "0322045912807866", "playerId": "0322045932619415"},
"tmatch_no":"3",
"tmatch_status":"won 5 matches",
"tmatchfield_name":"Army Stadium",
"tmatchfield_gmap":"somelink.com"
}'::json,
'{"tournament_id":"853320230323103918069",
"tmatch_date": "2022-04-02 15:20:00",
"tmatch_reportingtime": "02:45",
"tmatch_teams":{"playerId": "0322045912807866", "playerId": "0322045932619415"},
"tmatch_no":"3",
"tmatch_status":"won 5 matches",
"tmatchfield_name":"Army Stadium",
"tmatchfield_gmap":"somelink.com"}'::json]
);

select * from tournament_schedule;

--dymanic input to the schedule table depending on the tournament_id

CREATE OR REPLACE FUNCTION tournament_schedule(data json[]) RETURNS void AS $$
DECLARE
    obj json;
    query text ;
    t_match_id varchar;
    t_match_time timestamp;
    t_match_number varchar;
    table_store text;
 id_store varchar;
BEGIN
 FOREACH obj IN ARRAY data
    LOOP
        RAISE NOTICE '%', obj;
        RAISE NOTICE '%', obj ->> 'tournament_id';
        RAISE NOTICE '%', obj ->> 'tmatch_date';
        RAISE NOTICE '%', obj ->> 'tmatch_reportingtime';
        RAISE NOTICE '%', obj ->> 'tmatch_teams';
        RAISE NOTICE '%', obj ->> 'tmatch_no';
        RAISE NOTICE '%', obj ->> 'tmatch_status';
        RAISE NOTICE '%', obj ->> 'tmatchfield_name';
        RAISE NOTICE '%', obj ->> 'tmatchfield_gmap';

      id_store := obj ->> 'tournament_id';
        table_store := '"' || id_store  || '__' || 'tournament_schedule'|| '"';
        t_match_number := (obj ->> 'tmatch_no')::VARCHAR;
        t_match_time := obj ->> 'tmatch_date' ;
        t_match_id := obj ->> 'tournament_id' || '_' || TO_CHAR(t_match_time, 'YYYYMMDDHH24MISSMS') || '_' || t_match_number;
--         t_match_id := TO_CHAR(t_match_time, 'YYYYMMDDHH24MISSMS') ;

       query := format('INSERT INTO %s(tmatch_id,tournament_id,  tmatch_date, tmatch_reportingtime,
                      tmatch_teams, tmatch_no, tmatch_status, tmatchfield_name, tmatchfield_gmap)
                     VALUES (''%s'',''%s'', ''%s'', ''%s'', ''%s'', %s, ''%s'', ''%s'', ''%s'')',
                    table_store, t_match_id,obj ->> 'tournament_id', obj ->> 'tmatch_date',obj ->> 'tmatch_reportingtime', obj ->> 'tmatch_teams', obj ->> 'tmatch_no',obj ->> 'tmatch_status', obj ->> 'tmatchfield_name',
                     obj ->> 'tmatchfield_gmap');
    execute query;
    raise notice '%',query;
    raise notice '_____________________ %',table_store;
--         raise notice '%',tmatch_date_to_char;


raise notice ':::::::::::::::::::::::::::';
    END LOOP;
END;
$$ LANGUAGE plpgsql;


SELECT tournament_schedule(ARRAY[
'{"tournament_id":"470120230327065356771",
                                  "tmatch_date": "2023-03-01 15:20:00",
                                  "tmatch_reportingtime": "02:45",
                                  "tmatch_teams":{"TeamId1": "0322045912807866", "TeamId2": "0322045932619415"},
"tmatch_no":"3",
"tmatch_status":"won 5 matches",
"tmatchfield_name":"Army Stadium",
"tmatchfield_gmap":"somelink.com"
}'::json,
'{"tournament_id":"470120230327065356771",
"tmatch_date": "2022-04-02 15:20:00",
"tmatch_reportingtime": "02:45",
"tmatch_teams":{"TeamId1": "0322045912807866", "TeamId2": "0322045932619415"},
"tmatch_no":"3",
"tmatch_status":"won 5 matches",
"tmatchfield_name":"Army Stadium",
"tmatchfield_gmap":"somelink.com"}'::json]
);

select * from tournament;

create table "470120230327065356771_tournament_schedule" (
Tmatch_id varchar(255) primary key,
tournament_ID varchar(30) ,
TMatch_Date	TIMESTAMP,
TMatch_ReportingTime TIME,
TMatch_teams jsonb,
TMatch_No int,
TMatch_Status varchar(255),
TMatchField_name varchar(255),
TMatchField_GMap varchar(255),
Game_Result_Accepted varchar(255),
foreign key(tournament_ID) references Tournament(tournament_ID));

select * from "470120230327065356771_tournament_schedule";

select * from tournament;