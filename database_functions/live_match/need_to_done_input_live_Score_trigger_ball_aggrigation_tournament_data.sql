select * from "487620230331180822761__BByBowlerAggrigation";
select * from "487620230331180822761__tournamentShedule";

select * from cricketprofile;

-- for regular ball run taken
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"0322045932619415","name":"pagol"},

                        "runTaken": "7"
                        }');


-- for 1st time no-ball taken
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"0322045932619415","name":"pagol"},

                        "runNoBall": "1",
                        "byRunsOnNoBall": "2"
                        }');

-- for after no-ball right ball run taken
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"2345678","name":"pagol"},

                        "isAfterNoBall": true,
                        "isNoBall" : false,
                        "runsTaken": "2",
                        "whereRunTaken": "any where"
                        }');


-- for again no-ball taken
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"2345678","name":"pagol"},

                        "isAfterNoBall": true,
                        "isNoBall" : true,
                        "againrunNoBall": "1",
                        "byRunsOnNoBall": "2",
                        "whereRunTaken": "any where"

                        }');



-- for again wide ball taken
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"2345678","name":"pagol"},

                        "isAfterNoBall": true,
                        "isWideBall" : true,
                        "againrunWideBall": "1",
                        "byRunsOnWideBall": "1",
                        "whereRunTaken": "any where"

                        }');





-- for 1st time wide-ball taken
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"2345678","name":"pagol"},

                        "runWideBall": "1",
                        "byRunsOnWideBall": "8",
                        "whereRunTaken": "any where"

                        }');



-- for legBy taken
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"2345678","name":"pagol"},

                        "runsOnLegBy": "8",
                        "whereRunTaken": "any where"

                        }');



-- for OverThrow taken
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"2345678","name":"pagol"},

                        "isOverThrow": true,
                        "byRunsOnOverThrow": "8",
                        "OverThrowBy": {"id":"23456787","name":"pagol3"},
                        "whereRunTaken": "any where"
                        }');



-- for CatchDrop taken
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"2345678","name":"pagol"},

                        "catchDroppedBy": {"playerId":"234567", "playerName": "pagol"},
                        "catchDropedAt" : "any wherer"
                        }');




-- for Bowled-out / LBW / Stumped/ Caught-Behind taken
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"2345678","name":"pagol"},

                        "wicketsTaken": "1",
                        "WicketType" : "LBW" ,
                        "wicketWhereTaken": "field_position",
                        "wicketTakingAssistant": {"playedName": "pagol", "playerId": "2345"}
                        }');



-- for spectaculorCatchFielding taken          -- update last column
select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"2345678","name":"pagol"},

                        "spectaculorCatchFielding" : "1"
                        }');


-- for situation taken          -- update last column

select bowling_aggrigation('{
                        "tournamentId": "487620230331180822761",
                        "matchId":"1111",
                        "bowling": {"id":"2345678","name":"pagol"},

                        "situation" : "nothing nothing"
                        }');



-- remove last history of serial
TRUNCATE "724420230329054150986__GameMatchBByDetails" RESTART IDENTITY;

select * from tournament;

select * from "cricketprofile";

select * from "724420230329054150986__GameMatchBByDetails";










