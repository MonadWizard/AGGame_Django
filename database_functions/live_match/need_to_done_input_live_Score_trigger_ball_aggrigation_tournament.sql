drop function input_live_Score_trigger_ball_aggrigation(passing_data jsonb);
drop function bowling_aggrigation(passing_data jsonb);

select * from "487620230331180822761__BByBowlerAggrigation";


create or replace function bowling_aggrigation(passing_data jsonb)
returns void
as
$$
declare
    tournamentId varchar := passing_data ->> 'tournamentId';
    matchId varchar := passing_data ->> 'matchId';
    bowling varchar := (passing_data -> 'bowling' ->> 'id');

    table_name TEXT := '"' || tournamentId || '__BByBowlerAggrigation' || '"';
    strikerate float;
    averagerunsperover float;
    oversbowled float;
    ballsbowled INTEGER;
    runsgiven INTEGER;
    runs_0 INTEGER;
    runs_1 INTEGER;
    runs_2 INTEGER;
    runs_3 INTEGER;
    runs_4 INTEGER;
    runs_5 INTEGER;
    runs_6 INTEGER;
    runs_7 INTEGER;
    runs_8 INTEGER;
    wicketstaken INTEGER;
    boldout INTEGER;
    catchout INTEGER;
    caught_behind INTEGER;
    stamped INTEGER;
    lbw INTEGER;
    fielding_runout INTEGER;
    hitwicket INTEGER;
    retired_hurt INTEGER;

    runs_column varchar;
    runs_column_value integer;
    bool_var boolean;
    fractional_part float;
    query text;
-- regular run
    runTaken integer := passing_data ->> 'runTaken';
    whereRunTaken varchar := passing_data ->> 'whereRunTaken';

--     no ball runs
    runNoBall integer := passing_data ->> 'runNoBall';
    byRunsOnNoBall integer := passing_data ->> 'byRunsOnNoBall';

--     again no ball
    againrunNoBall integer := passing_data ->> 'againrunNoBall';

--     after noball right ball
    runsTaken integer := passing_data ->> 'runsTaken';
--     againrunNoBall integer := passing_data ->> 'againrunNoBall';

--     after no ball wide ball
    againrunWideBall integer := passing_data ->> 'againrunWideBall';

--      1st wide ball
    runWideBall integer := passing_data ->> 'runWideBall';
    byRunsOnWideBall integer := passing_data ->> 'byRunsOnWideBall';

--     runs on legs by
    runsOnLegBy integer := passing_data ->> 'runsOnLegBy';

--     overthrough
    byRunsOnOverThrow integer := passing_data ->> 'byRunsOnOverThrow';
    isOverThrow varchar := passing_data ->> 'isSideChange';
    OverThrowBy jsonb := passing_data ->> 'OverThrowBy';

--     catchDrop
    catchDropedAt varchar := passing_data ->> 'catchDropedAt';
    catchDroppedBy jsonb := passing_data ->> 'catchDroppedBy';

--     wicket taken
    wicketsTakenn varchar := passing_data ->> 'wicketsTaken';
    WicketType varchar := passing_data ->> 'WicketType';
    wicketWhereTaken varchar := passing_data ->> 'wicketWhereTaken';
    wicketTakingAssistant jsonb := passing_data ->> 'wicketTakingAssistant';

--     spectaculorCatchFielding
    spectaculorCatchFielding varchar := passing_data ->> 'spectaculorCatchFielding';

--     situation
    situation varchar := passing_data ->> 'situation';

begin


--     take tmatch_baller for specific tmatch_id
    EXECUTE 'SELECT COALESCE(strikerate::float, 0.00), COALESCE(averagerunsperover::float, 0.00),
        COALESCE(oversbowled::float, 0.00), COALESCE(ballsbowled::integer, 0),
        COALESCE(runsgiven::integer, 0), COALESCE(runs_0::integer, 0),
        COALESCE(runs_1::integer, 0), COALESCE(runs_2::integer, 0),
        COALESCE(runs_3::integer, 0), COALESCE(runs_4::integer, 0),
        COALESCE(runs_5::integer, 0), COALESCE(runs_6::integer, 0),COALESCE(runs_7::integer, 0),
        COALESCE(runs_8::integer, 0), COALESCE(wicketstaken::integer, 0),
        COALESCE(boldout::integer, 0), COALESCE(catchout::integer, 0),
        COALESCE(caught_behind::integer, 0), COALESCE(lbw::integer, 0),
        COALESCE(stamped::integer, 0), COALESCE(fielding_runout::integer, 0),
        COALESCE(hitwicket::integer, 0), COALESCE(retired_hurt::integer, 0)
      FROM ' || table_name || '
      WHERE tmatch_id = ''' || matchId || ''' AND tmatch_bowler = ''' || bowling || '''
      LIMIT 1'
    INTO strikerate, averagerunsperover, oversbowled, ballsbowled, runsgiven, runs_0,
        runs_1,runs_2,runs_3,runs_4,runs_5,runs_6,runs_7,runs_8,wicketstaken,boldout,
        catchout,caught_behind,lbw,stamped,fielding_runout,hitwicket,retired_hurt ;

    strikerate := COALESCE(strikerate, 0.00);
    averagerunsperover := COALESCE(averagerunsperover, 0.00);
    oversbowled := COALESCE(oversbowled, 0.00);
    ballsbowled := COALESCE(ballsbowled, 0);
    runsgiven := COALESCE(runsgiven, 0);
    runs_0 := COALESCE(runs_0, 0);
    runs_1 := COALESCE(runs_1, 0);
    runs_2 := COALESCE(runs_2, 0);
    runs_3 := COALESCE(runs_3, 0);
    runs_4 := COALESCE(runs_4, 0);
    runs_5 := COALESCE(runs_5, 0);
    runs_6 := COALESCE(runs_6, 0);
    runs_7 := COALESCE(runs_7, 0);
    runs_8 := COALESCE(runs_8, 0);
    wicketstaken := COALESCE(wicketstaken, 0);
    boldout := COALESCE(boldout, 0);
    catchout := COALESCE(catchout, 0);
    caught_behind := COALESCE(caught_behind, 0);
    lbw := COALESCE(lbw, 0);
    stamped := COALESCE(stamped, 0);
    fielding_runout := COALESCE(fielding_runout, 0);
    hitwicket := COALESCE(hitwicket, 0);
    retired_hurt := COALESCE(retired_hurt, 0);


-- < overs.ball on oversballed >  , < ballsbowled +1 > , <how much $run taken --> runs_$run> ,
--                      <if wicketstaken +1>, <$wicketType -->wicketypye specific column >


-- Update operations ........................................................................

         query := 'SELECT 1 FROM ' || table_name || 'WHERE tmatch_id = ''' || matchId || ''' AND tmatch_bowler = ''' || bowling || '''';
            EXECUTE query INTO bool_var;

        IF bool_var THEN

        IF (passing_data ? 'runTaken') THEN
    --         live_score := (live_score + runTaken);
            strikerate := '0.00';
            averagerunsperover := '0.00';

            ballsbowled := ballsbowled + 1;
            oversbowled := oversbowled + 0.1;
            fractional_part := oversbowled - floor(oversbowled); -- calculate the fractional part
            IF fractional_part = 0.6 THEN
                oversbowled := ceil(oversbowled); -- round up to the next integer
              ELSE
                oversbowled := round(oversbowled::numeric, 1)::float; -- round to one decimal place
            END IF;

            runsgiven := runsgiven + runTaken;
            runs_column = 'runs_'||runTaken;

            if runs_column = 'runs_0' THEN runs_column_value = runs_0 +1;
            elsif runs_column = 'runs_1' THEN runs_column_value = runs_1 +1;
            elsif runs_column = 'runs_2' THEN runs_column_value = runs_2 +1;
            elsif runs_column = 'runs_3' THEN runs_column_value = runs_3 +1;
            elsif runs_column = 'runs_4' THEN runs_column_value = runs_4 +1;
            elsif runs_column = 'runs_5' THEN runs_column_value = runs_5 +1;
            elsif runs_column = 'runs_6' THEN runs_column_value = runs_6 +1;
            elsif runs_column = 'runs_7' THEN runs_column_value = runs_7 +1;
            elsif runs_column = 'runs_8' THEN runs_column_value = runs_8 +1;
            end if ;
            query := format('UPDATE %s
                SET strikerate=''%s'', averagerunsperover=''%s'',oversbowled=''%s'', runsgiven=''%s'',ballsbowled = %s, %s=''%s''
                WHERE tmatch_id=''%s'' AND tmatch_bowler =''%s'' ',
                table_name,
                strikerate,averagerunsperover,oversbowled,runsgiven,ballsbowled,runs_column,runs_column_value,
                matchId,bowling);
            EXECUTE query;

        raise notice 'update run taken';

            --      1st time no ball              ####################################################### 2
        ELSIF (passing_data ? 'runNoBall') THEN

            strikerate := '0.00';
            averagerunsperover := '0.00';

            ballsbowled := ballsbowled + 1;
            runsgiven := runsgiven + (runNoBall + byRunsOnNoBall);

            query := format('UPDATE %s
                SET strikerate=''%s'', averagerunsperover=''%s'', runsgiven=''%s'',ballsbowled = %s
                WHERE tmatch_id=''%s'' AND tmatch_bowler =''%s'' ',
                table_name,
                strikerate,averagerunsperover,runsgiven,ballsbowled,
                matchId,bowling);
            EXECUTE query;

--             raise notice 'query :::: %', query;
            raise notice 'update 1st time no ball';

            -- for after no-ball right ball run taken
        ELSIF  (passing_data ? 'isAfterNoBall') AND (passing_data ? 'isNoBall') AND passing_data ->> 'isNoBall' = 'false' AND passing_data ->> 'isAfterNoBall' = 'true' THEN

            raise notice 'after no ball right ball';

            -- for again no-ball
        ELSIF (passing_data ? 'isAfterNoBall') AND (passing_data ? 'isNoBall') AND passing_data ->> 'isNoBall' = 'true' AND passing_data ->> 'isAfterNoBall' = 'true' THEN

            RAISE NOTICE 'after no-ball taken again no-ball:::::::::::';


            -- for again wide ball
        ELSIF (passing_data ? 'isAfterNoBall') AND (passing_data ? 'isWideBall') AND passing_data ->> 'isWideBall' = 'true' AND passing_data ->> 'isAfterNoBall' = 'true' THEN

            RAISE NOTICE 'after no-ball taken again no-ball:::::::::::';


    --     1st time wide ball
        ELSIF (passing_data ? 'runWideBall') THEN

            RAISE NOTICE 'wide_ball';

        ELSIF (passing_data ? 'runsOnLegBy') THEN

            RAISE NOTICE 'is_legby';

        ELSIF (passing_data ? 'isOverThrow') THEN

            raise notice 'is_over_throw';


        ELSIF (passing_data ? 'catchDropedAt') THEN

            RAISE NOTICE 'catch droped';

        ELSIF (passing_data ? 'wicketsTaken') THEN

            RAISE NOTICE 'is_wicket_taken';

        ELSIF (passing_data ? 'spectaculorCatchFielding') THEN

            RAISE NOTICE 'spectaculorCatchFielding';

        ELSIF (passing_data ? 'situation') THEN

            RAISE NOTICE 'situation';

        ELSE
            RAISE NOTICE ' key does not exist in the JSON object';

        END IF;


--     Insertion operations..............................................................

        ELSE

            IF (passing_data ? 'runTaken') THEN
--                         need logic for
                strikerate := '0.00';
                averagerunsperover := '0.00';
                oversbowled := '0.1';
                runsgiven := runTaken;
                runs_column = 'runs_'||runTaken;

                raise notice ' runs_column :: %',runs_column;

                    query := format('INSERT INTO %s (
                        tmatch_id, tmatch_bowler, strikerate, averagerunsperover, oversbowled, runsgiven,ballsbowled, %s)
                        VALUES (''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', 1, 1)',
                        table_name,runs_column,
                        matchId,bowling,strikerate,averagerunsperover,oversbowled,runsgiven);
                    EXECUTE query;
                    raise notice 'query :::  %',query;
                raise notice 'run taken';

                --      1st time no ball       ######################################## 1
            ELSIF (passing_data ? 'runNoBall') THEN

                strikerate := '0.00';
                averagerunsperover := '0.00';

                oversbowled := '0.0';
                runsgiven := runNoBall + byRunsOnNoBall;


                query := format('INSERT INTO %s (
                    tmatch_id, tmatch_bowler, strikerate, averagerunsperover, oversbowled, runsgiven, ballsbowled)
                    VALUES (''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', 1)',
                    table_name,
                    matchId,bowling,strikerate,averagerunsperover,oversbowled,runsgiven);
                EXECUTE query;
                raise notice 'query :::  %',query;

                raise notice 'insert 1st time no ball';

                -- for after no-ball right ball run taken
            ELSIF  (passing_data ? 'isAfterNoBall') AND (passing_data ? 'isNoBall') AND passing_data ->> 'isNoBall' = 'false' AND passing_data ->> 'isAfterNoBall' = 'true' THEN
        --
                raise notice 'after no ball right ball';

                -- for again no-ball
            ELSIF (passing_data ? 'isAfterNoBall') AND (passing_data ? 'isNoBall') AND passing_data ->> 'isNoBall' = 'true' AND passing_data ->> 'isAfterNoBall' = 'true' THEN
        --
                RAISE NOTICE 'after no-ball taken again no-ball:::::::::::';


                -- for again wide ball
            ELSIF (passing_data ? 'isAfterNoBall') AND (passing_data ? 'isWideBall') AND passing_data ->> 'isWideBall' = 'true' AND passing_data ->> 'isAfterNoBall' = 'true' THEN
        --
                RAISE NOTICE 'after no-ball taken again no-ball:::::::::::';


        --     1st time wide ball
            ELSIF (passing_data ? 'runWideBall') THEN
        --
                RAISE NOTICE 'wide_ball';

            ELSIF (passing_data ? 'runsOnLegBy') THEN
        --
                RAISE NOTICE 'is_legby';

            ELSIF (passing_data ? 'isOverThrow') THEN
        --
                raise notice 'is_over_throw';


            ELSIF (passing_data ? 'catchDropedAt') THEN
        --
                RAISE NOTICE 'catch droped';

            ELSIF (passing_data ? 'wicketsTaken') THEN
        --
                RAISE NOTICE 'is_wicket_taken';

            ELSIF (passing_data ? 'spectaculorCatchFielding') THEN
        --
                RAISE NOTICE 'spectaculorCatchFielding';

            ELSIF (passing_data ? 'situation') THEN
        --
                RAISE NOTICE 'situation';

            ELSE
                RAISE NOTICE ' key does not exist in the JSON object';

        END IF;

    END IF;

END;
$$
language plpgsql;



