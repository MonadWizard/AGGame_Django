CREATE OR REPLACE FUNCTION create_dynamic_table_for_tournament( tournament_id varchar)
RETURNS VOID AS $$
DECLARE
    tournamentMatch_ballbyballDetails TEXT := tournament_id || '__BByDetails';
    tournamentMatch_ballbyball_bowlerAggrigation TEXT := tournament_id || '__BByBowlerAggrigation';
    tournamentMatch_ballbyball_batsmanAggrigation TEXT := tournament_id || '__BByBatsmanAggrigation';
    tournamentShedule TEXT := tournament_id || '__tournamentShedule';
    query text;
BEGIN




-- -- Create the tournamentShedule table with dynamic name

 EXECUTE 'CREATE TABLE IF NOT EXISTS "' || tournamentShedule || '" (
    Tmatch_id varchar(255) primary key,
    tournament_ID varchar(30) ,
    TMatch_Date	TIMESTAMP,
    TMatch_ReportingTime TIME,
    TMatch_team1 varchar(50),
    TMatch_team2 varchar(50),
    TMatch_No int,
    TMatch_Status varchar(255),
    TMatchField_name varchar(255),
    TMatchField_GMap varchar(255),
    Game_Result_Accepted varchar(255),
    TMatch_Type VARCHAR(50),
    TMatch_Overs FLOAT,
    Teams_Played VARCHAR(255),
    Match_Winner VARCHAR(255),
    Match_Won_by VARCHAR(50),
    Points INT,
    Toss_Won VARCHAR(255),
    First_Batting VARCHAR(255),
    First_Batting_Runs_Scored INT,
    First_Batting_Wicket_loss INT,
    First_Batting_Overs_Played FLOAT,
    Second_batting VARCHAR(255),
    Second_Batting_Runs_Scored INT,
    Second_Batting_Wicket_loss INT,
    Second_Batting_Overs_Played FLOAT,
    Game_Result VARCHAR(50),
    TMatch_Location VARCHAR(255),
    TMatch_LiveLink VARCHAR(255),
    TMatch_Umpire VARCHAR(255),
    TMatch_Scorer VARCHAR(255),
    TMatch_LiveStreamer VARCHAR(255),
    TMatch_Toss VARCHAR(50),
    TMatch_Result VARCHAR(50),
    TMatch_ManOfTheMatch VARCHAR(255),
    foreign key(tournament_ID) references tournament(tournament_ID),
    foreign key(TMatch_team1) references team(team_id),
    foreign key(TMatch_team1) references team(team_id)

    )';



--     -- Create the tournamentMatch_ballbyballDetails table with dynamic name
    EXECUTE 'CREATE TABLE IF NOT EXISTS "' || tournamentMatch_ballbyballDetails || '" (
        TournamentId varchar(50),
        TMatchID varchar(50),
        balls int,
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
        wicketTakingAssistant varchar(250),
        spectaculorCatchFielding int,
        change_side boolean,
        runNoBall boolean,
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
        Foreign key(TMatchID) references "' || tournamentShedule || '"(Tmatch_id),
        Foreign key(matchLiveScorrerID) references auth_user_app_user(userid)
    )';


    -- Create the tournamentMatch_ballbyball_bowlerAggrigation table with dynamic name

    EXECUTE 'CREATE TABLE IF NOT EXISTS "' || tournamentMatch_ballbyball_bowlerAggrigation || '" (
        TMatch_ID varchar(30),
        TMatch_DateTime timestamp,
        TMatch_Bowler varchar(50),
        StrikeRate float,
        AverageRunsPerOver float,
        OversBowled float,
        BallsBowled	int,
        RunsGiven int,
        runs_0 int,
        runs_1 int,
        runs_2 int,
        runs_3 int,
        runs_4 int,
        runs_5 int,
        runs_6 int,
        runs_7 int,
        runs_8 int,
        WicketsTaken int,
        BoldOut int,
        CatchOut int,
        Caught_Behind int,
        LBW	int,
        Stamped int,
        Fielding_RunOut int,
        HitWicket int,
        Retired_Hurt int,
        Foreign key(TMatch_ID) references "' || tournamentShedule || '" (Tmatch_id),
        Foreign key(TMatch_Bowler) references auth_user_app_user(userid)
    )';

--     raise notice ':::::::: %', query;


    -- Create the tournamentMatch_ballbyball_batsmanAggrigation table with dynamic name

    EXECUTE 'CREATE TABLE IF NOT EXISTS "' || tournamentMatch_ballbyball_batsmanAggrigation || '" (
        TMatch_ID varchar(30),
        TMatch_DateTime timestamp,
        TMatch_Batsman jsonb,
        StrikeRate real,
        RunsScored int,
        Life int, --if catch is missed, 1 life will be added for the runner
        Life_GivenWhen jsonb,
                --"Ball no: 56
                -- Bowled: ID, Name
                -- Dropped by: ID, Name
                -- Dropped Where: FieldPosition "
        BallsFaced int,
        "0" boolean,
        "1" boolean,
        "2" boolean,
        "3" boolean,
        "4" boolean,
        "5" boolean,
        "6" boolean,
        NotOut boolean,
        Retired_Hurt boolean,
        Foreign key(tmatch_id) references "' || tournamentShedule || '" (Tmatch_id)
    )';



END;
$$ LANGUAGE plpgsql;


SELECT create_dynamic_table_for_tournament('822420230327085423799');

drop function create_dynamic_table_for_tournament;

select * from tournament;




select * from "822420230327085423799__tournamentShedule";






