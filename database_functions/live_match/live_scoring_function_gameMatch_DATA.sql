-- for regular ball run taken
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345678","name":"pagol"},
                        "bowling": {"id":"2345678","name":"pagol"},
                        "isSideChange": "False",
                        "extrarunner": {"id":"2345678","name":"pagol"},

                        "whereRunTaken": "any_where",
                        "runTaken": "0"
                        }');


-- for 1st time no-ball taken
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345678","name":"pagol"},
                        "bowling": {"id":"2345678","name":"pagol"},
                        "isSideChange": "False",
                        "extrarunner": {"id":"2345678","name":"pagol"},

                        "runNoBall": "1",
                        "byRunsOnNoBall": "8"
                        }');

-- for after no-ball right ball run taken
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345679","name":"pagol1"},
                        "bowling": {"id":"2345677","name":"pagol2"},
                        "isSideChange": "False",
                        "extrarunner": {"id":"23456787","name":"pagol3"},

                        "isAfterNoBall": true,
                        "isNoBall" : false,
                        "runsTaken": "2",
                        "whereRunTaken": "any where"
                        }');


-- for again no-ball taken
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345679","name":"pagol1"},
                        "bowling": {"id":"2345677","name":"pagol2"},
                        "isSideChange": "False",
                        "extrarunner": {"id":"23456787","name":"pagol3"},

                        "isAfterNoBall": true,
                        "isNoBall" : true,
                        "againrunNoBall": "1",
                        "byRunsOnNoBall": "2",
                        "whereRunTaken": "any where"

                        }');



-- for again wide ball taken
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345679","name":"pagol1"},
                        "bowling": {"id":"2345677","name":"pagol2"},
                        "isSideChange": "False",
                        "extrarunner": {"id":"23456787","name":"pagol3"},

                        "isAfterNoBall": true,
                        "isWideBall" : true,
                        "againrunWideBall": "1",
                        "byRunsOnWideBall": "1",
                        "whereRunTaken": "any where"

                        }');





-- for 1st time wide-ball taken
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345679","name":"pagol1"},
                        "bowling": {"id":"2345677","name":"pagol2"},
                        "isSideChange": false,
                        "extrarunner": {"id":"23456787","name":"pagol3"},

                        "runWideBall": "1",
                        "byRunsOnWideBall": "8",
                        "whereRunTaken": "any where"

                        }');



-- for legBy taken
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345679","name":"pagol1"},
                        "bowling": {"id":"2345677","name":"pagol2"},
                        "extrarunner": {"id":"23456787","name":"pagol3"},
                        "isSideChange": true,

                        "runsOnLegBy": "8",
                        "whereRunTaken": "any where"

                        }');



-- for OverThrow taken
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345679","name":"pagol1"},
                        "bowling": {"id":"2345677","name":"pagol2"},
                        "extrarunner": {"id":"23456787","name":"pagol3"},
                        "isSideChange": true,

                        "isOverThrow": true,
                        "byRunsOnOverThrow": "8",
                        "OverThrowBy": {"id":"23456787","name":"pagol3"},
                        "whereRunTaken": "any where"
                        }');



-- for CatchDrop taken
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345679","name":"pagol1"},
                        "bowling": {"id":"2345677","name":"pagol2"},
                        "extrarunner": {"id":"23456787","name":"pagol3"},
                        "isSideChange": true,

                        "catchDroppedBy": {"playerId":"234567", "playerName": "pagol"},
                        "catchDropedAt" : "any wherer"
                        }');




-- for Bowled-out / LBW / Stumped/ Caught-Behind taken
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345679","name":"pagol1"},
                        "bowling": {"id":"2345677","name":"pagol2"},
                        "extrarunner": {"id":"23456787","name":"pagol3"},
                        "isSideChange": true,

                        "wicketsTaken": "1",
                        "WicketType" : "LBW" ,
                        "wicketWhereTaken": "field_position",
                        "wicketTakingAssistant": {"playedName": "pagol", "playerId": "2345"}
                        }');



-- for spectaculorCatchFielding taken          -- update last column
select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345679","name":"pagol1"},
                        "bowling": {"id":"2345677","name":"pagol2"},
                        "extrarunner": {"id":"23456787","name":"pagol3"},
                        "isSideChange": true,

                        "spectaculorCatchFielding" : "1"
                        }');


-- for situation taken          -- update last column

select input_live_score_game('{
                        "matchId":"724420230329054150986",
                        "scorrerId": "0329043540613666",
                        "facing": {"id":"2345678","name":"pagol"},
                        "runner": {"id":"2345679","name":"pagol1"},
                        "bowling": {"id":"2345677","name":"pagol2"},
                        "extrarunner": {"id":"23456787","name":"pagol3"},
                        "isSideChange": true,

                        "situation" : "nothing nothing"
                        }');



-- remove last history of serial
TRUNCATE "724420230329054150986__GameMatchBByDetails" RESTART IDENTITY;

select * from tournament;

select * from "cricketprofile";

select * from "724420230329054150986__GameMatchBByDetails";










