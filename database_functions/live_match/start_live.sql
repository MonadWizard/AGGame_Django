CREATE OR REPLACE FUNCTION create_dynamic_table_for_tournament_single_match_start(match_id varchar, tournament_id varchar)
RETURNS VOID AS $$
DECLARE

    tournamentSingleMatch_ballbyballDetails TEXT := tournament_id || '__' || match_id || '__tSingleMatchBByDetails';
    tournamentShedule TEXT := tournament_id || '__tournamentShedule';


BEGIN


        EXECUTE 'CREATE TABLE IF NOT EXISTS "' || tournamentSingleMatch_ballbyballDetails || '" (
        TournamentId varchar(50),
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

        Foreign key(TournamentId) references tournament(tournament_id),
        Foreign key(TMatchID) references "' ||tournamentShedule || '"(Tmatch_id),
        Foreign key(matchLiveScorrerID) references auth_user_app_user(userid)
    )';

    raise notice ':::: %', tournamentSingleMatch_ballbyballDetails;

END;
$$ LANGUAGE plpgsql;


SELECT create_dynamic_table_for_tournament_single_match_start('456', '822420230327085423799');


select * from tournament_schedule;

select * from tournament;

select * from "526020230322102230626__123__tSingleMatchBByDetails";

drop table "526020230322102230626__123__tSingleMatchBByDetails";


