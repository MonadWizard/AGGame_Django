drop function input_live_Score_tournament(passing_data jsonb);


create or replace function input_live_Score_tournament(passing_data jsonb)
returns void
as
$$
declare
    tournamentId varchar := passing_data ->> 'tournamentId';
    matchId varchar := passing_data ->> 'matchId';
    scorrerId varchar := passing_data ->> 'scorrerId';
    facing jsonb := passing_data ->> 'facing';
    runner jsonb := passing_data ->> 'runner';
    bowling jsonb := passing_data ->> 'bowling';
    isSideChange varchar := passing_data ->> 'isSideChange';
    extrarunner jsonb := passing_data ->> 'extrarunner';

    table_name TEXT := '"' || tournamentId || '__' || matchId || '__tSingleMatchBByDetails' || '"';
    total_balls integer;
    live_score integer;
    totalOver INTEGER;
    balByOver INTEGER;

    noBallRun INTEGER;
    noBallByRun INTEGER;
    wideBallRun INTEGER;
    wideBallByRun INTEGER;

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
    wicketsTaken varchar := passing_data ->> 'wicketsTaken';
    WicketType varchar := passing_data ->> 'WicketType';
    wicketWhereTaken varchar := passing_data ->> 'wicketWhereTaken';
    wicketTakingAssistant jsonb := passing_data ->> 'wicketTakingAssistant';

--     spectaculorCatchFielding
    spectaculorCatchFielding varchar := passing_data ->> 'spectaculorCatchFielding';

--     situation
    situation varchar := passing_data ->> 'situation';

begin




-- noBallRun ,noBallByRun, wideBallRun, wideBallByRun
    EXECUTE 'SELECT COALESCE(balls::integer, 0), COALESCE(livescore::integer, 0),
                COALESCE(runnoball::integer, 0), COALESCE(byrunsonnoball::integer, 0),
                COALESCE(runwideball::integer, 0), COALESCE(byrunsonwideball::integer, 0)
              FROM ' || table_name || '
              ORDER BY balls DESC
              LIMIT 1'
            INTO total_balls, live_score, noBallRun, noBallByRun, wideBallRun, wideBallByRun;


    live_score := COALESCE(live_score, 0);
    total_balls := COALESCE(total_balls, 0);
    totalOver := (total_balls+1) / 6 ;
    balByOver := (total_balls+1) % 6;

    noBallRun := COALESCE(noBallRun, 0);
    noBallByRun := COALESCE(noBallByRun, 0);
    wideBallRun := COALESCE(wideBallRun, 0);
    wideBallByRun := COALESCE(wideBallByRun, 0);


    IF (passing_data ? 'runTaken') THEN
        live_score := (live_score + runTaken);
        query := format('INSERT INTO %s (
	                    tournamentid, tmatchid, ballsbyover, over, livescore, matchlivescorrerid, bowling, facing,
                         runner, extrarunner, runstaken, runswheretaken,change_side)
	            VALUES (''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'',''%s'')',
                table_name,tournamentId,matchId,balByOver,totalOver,live_score,scorrerId,bowling,facing,runner,extrarunner,runTaken,whereRunTaken,isSideChange);
        EXECUTE query;
        raise notice 'run taken';

        --      1st time no ball
    ELSIF (passing_data ? 'runNoBall') THEN
        live_score := (live_score + runNoBall+byRunsOnNoBall);
        query := format('INSERT INTO %s (
	                    tournamentid, tmatchid, ballsbyover, over, livescore, matchlivescorrerid, bowling, facing,
                         runner,change_side, extrarunner, runnoball, byrunsonnoball)
	            VALUES (''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'',''%s'')',
                table_name,tournamentId,matchId,balByOver,totalOver,live_score,scorrerId,bowling,facing,runner,isSideChange,extrarunner,runNoBall,byRunsOnNoBall);
        EXECUTE query;
        raise notice 'no ball';

        -- for after no-ball right ball run taken
    ELSIF  (passing_data ? 'isAfterNoBall') AND (passing_data ? 'isNoBall') AND passing_data ->> 'isNoBall' = 'false' AND passing_data ->> 'isAfterNoBall' = 'true' THEN
        live_score := (live_score + runsTaken);
        query := format('UPDATE %s
            SET livescore=''%s'', matchlivescorrerid=''%s'',bowling=''%s'', facing=''%s'', runner=''%s'', extrarunner=''%s'', runstaken=''%s'', runswheretaken=''%s'',  change_side=''%s''
            WHERE balls=''%s'' ',table_name,live_score,scorrerId,bowling,facing,runner,extrarunner,runsTaken,whereRunTaken,isSideChange,total_balls);
        EXECUTE query;
        raise notice 'after no ball right ball';

        -- for again no-ball
    ELSIF (passing_data ? 'isAfterNoBall') AND (passing_data ? 'isNoBall') AND passing_data ->> 'isNoBall' = 'true' AND passing_data ->> 'isAfterNoBall' = 'true' THEN
        live_score := (live_score + againrunNoBall + byRunsOnNoBall);
        noBallRun := (noBallRun + againrunNoBall);
        noBallByRun := (noBallByRun + byRunsOnNoBall);
        query := format('UPDATE %s
            SET livescore=''%s'', matchlivescorrerid=''%s'',bowling=''%s'', facing=''%s'', runner=''%s'', extrarunner=''%s'', byRunsOnNoBall=''%s'', runswheretaken=''%s'',  change_side=''%s'', runnoball=''%s''
            WHERE balls=''%s'' ',table_name,live_score,scorrerId,bowling,facing,runner,extrarunner,noBallByRun,whereRunTaken,isSideChange,noBallRun,total_balls);
        EXECUTE query;
        RAISE NOTICE 'after no-ball taken again no-ball:::::::::::';


        -- for again wide ball
    ELSIF (passing_data ? 'isAfterNoBall') AND (passing_data ? 'isWideBall') AND passing_data ->> 'isWideBall' = 'true' AND passing_data ->> 'isAfterNoBall' = 'true' THEN
        live_score := (live_score + againrunWideBall + byRunsOnWideBall);
        wideBallRun := (wideBallRun + againrunWideBall);
        wideBallByRun := (wideBallByRun + byRunsOnWideBall);
        query := format('UPDATE %s
            SET livescore=''%s'', matchlivescorrerid=''%s'',bowling=''%s'', facing=''%s'', runner=''%s'', extrarunner=''%s'',runWideBall=''%s'' ,byRunsOnWideBall=''%s'', runswheretaken=''%s'',  change_side=''%s''
            WHERE balls=''%s'' ',table_name,live_score,scorrerId,bowling,facing,runner,extrarunner,wideBallRun,wideBallByRun,whereRunTaken,isSideChange,total_balls);
        EXECUTE query;
        RAISE NOTICE 'after no-ball taken again no-ball:::::::::::';


--     1st time wide ball
    ELSIF (passing_data ? 'runWideBall') THEN
        live_score := (live_score + runWideBall+byRunsOnWideBall);
        query := format('INSERT INTO %s (
	                    tournamentid, tmatchid, ballsbyover, over, livescore, matchlivescorrerid, bowling, facing,
                         runner,change_side, extrarunner, runwideball, byrunsonwideball,runswheretaken)
	            VALUES (''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'',''%s'',''%s'')',
                table_name,tournamentId,matchId,balByOver,totalOver,live_score,scorrerId,bowling,facing,runner,isSideChange,extrarunner,runWideBall,byRunsOnWideBall,whereRunTaken);
        EXECUTE query;
        RAISE NOTICE 'wide_ball';

    ELSIF (passing_data ? 'runsOnLegBy') THEN
        live_score := (live_score + runsOnLegBy);
        query := format('INSERT INTO %s (
	                    tournamentid, tmatchid, ballsbyover, over, livescore, matchlivescorrerid, bowling, facing,
                         runner, extrarunner, runsonlegby, runswheretaken,change_side)
	            VALUES (''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'',''%s'')',
                table_name,tournamentId,matchId,balByOver,totalOver,live_score,scorrerId,bowling,facing,runner,extrarunner,runsOnLegBy,whereRunTaken,isSideChange);
        EXECUTE query;
        RAISE NOTICE 'is_legby';

    ELSIF (passing_data ? 'isOverThrow') THEN
        live_score := (live_score + byRunsOnOverThrow);
        query := format('UPDATE %s
            SET livescore=''%s'', matchlivescorrerid=''%s'',bowling=''%s'', facing=''%s'', runner=''%s'', extrarunner=''%s'',  change_side=''%s'', isoverthrow=''%s'', byrunsonoverthrow=''%s'', overthrowBy=''%s'', runswheretaken=''%s''
            WHERE balls=''%s'' ',table_name,live_score,scorrerId,bowling,facing,runner,extrarunner,isSideChange,isOverThrow,byRunsOnOverThrow,OverThrowBy,whereRunTaken,total_balls);
        EXECUTE query;
        raise notice 'is_over_throw';


    ELSIF (passing_data ? 'catchDropedAt') THEN
        query := format('UPDATE %s
            SET livescore=''%s'', matchlivescorrerid=''%s'',bowling=''%s'', facing=''%s'', runner=''%s'', extrarunner=''%s'',  change_side=''%s'', catchdroppedby=''%s'', catchdroppedat=''%s''
            WHERE balls=''%s'' ',table_name,live_score,scorrerId,bowling,facing,runner,extrarunner,isSideChange,catchDroppedBy,catchDropedAt,total_balls);
        EXECUTE query;
        RAISE NOTICE 'catch droped';

    ELSIF (passing_data ? 'wicketsTaken') THEN
        live_score := (live_score);
        query := format('INSERT INTO %s (
	                    tournamentid, tmatchid, ballsbyover, over, livescore, matchlivescorrerid, bowling, facing,
                         runner, extrarunner,change_side,wicketstaken,wickettype,wicketwheretaken,wickettakingassistant)
	            VALUES (''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'',''%s'', ''%s'',''%s'')',
                table_name,tournamentId,matchId,balByOver,totalOver,live_score,scorrerId,bowling,facing,runner,extrarunner,isSideChange,wicketsTaken,WicketType,wicketWhereTaken,wicketTakingAssistant);
        EXECUTE query;
        RAISE NOTICE 'is_wicket_taken';

    ELSIF (passing_data ? 'spectaculorCatchFielding') THEN
        query := format('UPDATE %s
            SET livescore=''%s'', matchlivescorrerid=''%s'',bowling=''%s'', facing=''%s'', runner=''%s'', extrarunner=''%s'',  change_side=''%s'', spectaculorcatchfielding=''%s''
            WHERE balls=''%s'' ',table_name,live_score,scorrerId,bowling,facing,runner,extrarunner,isSideChange,spectaculorCatchFielding,total_balls);
        EXECUTE query;
        RAISE NOTICE 'spectaculorCatchFielding';

    ELSIF (passing_data ? 'situation') THEN
        query := format('UPDATE %s
            SET livescore=''%s'', matchlivescorrerid=''%s'',bowling=''%s'', facing=''%s'', runner=''%s'', extrarunner=''%s'',  change_side=''%s'', situation=''%s''
            WHERE balls=''%s'' ',table_name,live_score,scorrerId,bowling,facing,runner,extrarunner,isSideChange,situation,total_balls);
        EXECUTE query;
        RAISE NOTICE 'situation';

    ELSE
        RAISE NOTICE ' key does not exist in the JSON object';

 END IF;


END;
$$
language plpgsql;





