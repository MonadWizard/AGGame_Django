CREATE OR REPLACE FUNCTION create_dynamic_table_for_game_match_start(match_id varchar)
RETURNS VOID AS $$
DECLARE

    tournamentSingleMatch_ballbyballDetails TEXT := match_id || '__GameMatchBByDetails';

BEGIN

        EXECUTE 'CREATE TABLE IF NOT EXISTS "' || tournamentSingleMatch_ballbyballDetails || '" (
        TMatchID varchar(50),
        balls serial,
        ballsByOver int,
        over INTEGER,
        liveScore jsonb,
        matchLiveScorrerID varchar(30),
        bowling jsonb,
        facing jsonb,
        runner jsonb,
        extraRunner jsonb,
        runsTaken int,
        runsWhereTaken varchar(255),
        wicketsTaken int,
        wicketType varchar(255),
        wicketWhereTaken varchar(250),
        wicketTakingAssistant jsonb,
        spectaculorCatchFielding int,
        change_side boolean,
        runNoBall int,
        byRunsOnNoBall int,
        runWideBall int,
        byRunsOnWideBall  int,
        isOverThrow boolean,
        byRunsOnOverThrow int,
        OverThrowBy jsonb,
        runsOnLegBy int,
        catchDroppedBy jsonb, --player ID and name
        catchDroppedAt varchar(255),
        situation varchar(250),

        Foreign key(matchLiveScorrerID) references auth_user_app_user(userid)
    )';

    raise notice ':::: %', tournamentSingleMatch_ballbyballDetails;

END;
$$ LANGUAGE plpgsql;


SELECT create_dynamic_table_for_game_match_start('724420230329054150986');



select * from match;

select * from "724420230329054150986__GameMatchBByDetails";


