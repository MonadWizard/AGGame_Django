
--  <user table>
select * from auth_user_app_user;

--  user table  end


-- <cricket profile table>  (checked) and added
create table CricketProfile(
player_ID varchar(30),

player_fullname jsonb,
player_image varchar(255),
playing_order varchar(255),
playing_country varchar(255),
isCaptain boolean,
isViceCaptain boolean,
is12thman boolean,
Batting_Rating float,
Number_of_games_appeared_for_a_Batsman int,
Number_of_Tournaments_for_a_Batsman int,
Games_Batted int,
Runs_Scored int,
Best_score int, --max run taken in a match
Balls_Faced int,
Batting_Average float,
Batting_Strike_rate float,
Not_out int,
"50s" int,
"100s" int,
"150s" int,
"200s"  int,
Bowling_Rating int,
Number_of_Games_Appeared_for_a_bowler int,
Number_of_tournaments_for_a_bowler int,
Games_Bowled int,
Balls_Bowled int,
-- Runs_Given int,
Wickets_Taken int,
Bowling_Average int,
Bowling_Strike_Rate int,
Bold_outs int,
Catch_outs int,
Caught_behind int,
Fielding_Rating float,
Overall_Rating float,
Strike_Rate float,
player_average float,
Player_Ranking_World_Wide int,
Player_Ranking_Own_Country int,
Ranking_in_own_district_or_State int,
Ranking_in_Own_city_or_UpoZila_or_Zila int,
foreign key(player_ID) references auth_user_app_user(userid)
);

-- ALTER TABLE cricketprofile add column captain varchar;
-- ALTER TABLE cricketprofile add column vice_captain varchar;
-- ALTER TABLE cricketprofile add column player_role varchar;
-- ALTER TABLE cricketprofile add column Twelfth_man varchar;


select * from cricketprofile;

drop table CricketProfile;





select * from auth_user_app_user;

select  * from cricketprofile;
--  team table start

create table Team(
team_creator_id varchar(30),
Team_ID varchar(30) primary key,
Game_Name text,
Team_Owner varchar(255),
Team_logo varchar(255),
Team_Name varchar(255),
Team_email varchar(255),
Team_Mobile varchar(255),
Country_of_The_team varchar(255),
Country_of_GamePlaying varchar(255),
Team_Members jsonb,
Teams_Avg float,
Number_of_Games_Played int,
Number_of_Games_Won int,
Number_of_Games_Drawn int,
Number_of_Games_Lost int,
Number_of_Games_Abandoned int,
Number_of_Runs int,
Number_of_Balls_Faced int,
Number_of_Wickets_Taken int,
Number_of_Balls_Bowled int,
Batting_Average float,
Strike_Rate float,
Teams_TournamentRating int,
Number_of_Tournament_Participated int,
Captain varchar(255),
Vice_Captain varchar(255),
foreign key(team_creator_id) references auth_user_app_user(userid),
foreign key(Captain) references auth_user_app_user(userid),
foreign key(Vice_Captain) references auth_user_app_user(userid));



-- tournament table start

create table Tournament(
Tournament_ID varchar(30) primary key ,
Tournament_Owner varchar(30),
Tournament_logo varchar(255),
Tournament_Name	varchar(255),
Type_of_Tournament varchar(255)	,
Sport_or_Game_Configuration jsonb,
TournamentLocation jsonb,
OrganizerName varchar(255),
HostName varchar(255),
OrganizerEmail varchar(255),
OrganizerPhone varchar(255),
Tournament_Admin varchar(255),
TournamentStartDate	TIMESTAMP,
TournamentMatchType	varchar(255),
NumberOfTeamsInGroup int,
NumberOfGroupsInTournament int,
groupTeamDetails	jsonb,
Tournament_MatchConfiguration jsonb, -- match count, day, and time
Tournament_ManOfTheTournament varchar(255),
Tournament_HighestWicketTaker varchar(255),
Tournament_HighestRunScorer varchar(255),
Tournament_BestBatsman varchar(255),
Tournament_BestBowler varchar(255),
Tournament_BestWicketKeeper varchar(255),
Tournament_BestFielder varchar(255),
foreign key(Tournament_Owner) references auth_user_app_user(userid)
);






--  match table start

create table Match(
Game_ID	varchar(30) primary key,
Game_Owner varchar(30),
Game_Name jsonb,
Type_of_Game varchar(255),
Game_Configuration jsonb,
Game_DateTime timestamp,
Game_Location varchar[],
GameOwner_Phone varchar(20),
GameOwner_email varchar(100),
Game_LiveLink jsonb,
Game_Umpire	varchar(255),
Game_Scorer varchar(255),
Game_LiveStreamer varchar(255),
Toss jsonb,
Game_Result jsonb,
GameResult_Accepted jsonb,
ManOfTheMatch varchar(255),
Team_Manager varchar(255),
foreign key(Game_Owner) references auth_user_app_user(userid));




-- general setting table start



create table general_settings(
general_settings serial primary key,
country_name varchar(255),
    country_dial_code varchar(255),
    country_short_name varchar(255),
    country_flag varchar(255),
sex varchar(10),
body_type varchar(30),
Size_Type varchar(255),
Sports jsonb, --sports name and logo
Games varchar(255),
Board_Games varchar(255),
Virtual_Games varchar(255),
Hobbies varchar(255),
Cricket	varchar(255),
Cricket_ShortNames varchar(255),
Cricket_Icons varchar(255),
Cricket_Skills varchar(255));



















--  tournament shedule table start   >.....................no need.........................<

create table tournament_schedule(
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

drop table tournament_schedule;

select * from tournament_schedule;

-- TournamentID_Match_Results table start

create table Tournament_Match_Results(
Tournament_id varchar(50),
TMatch_ID varchar(50),
TMatch_DateTime	timestamp,
TMatch_Type varchar(255),
TMatch_Overs int,
Teams_Played jsonb,
Match_Winner varchar(255),
Match_Won_by varchar(255),
Toss_Won varchar(255),
First_Batting varchar(255),
First_Batting_Runs_Scored int,
First_Batting_Wicket_loss int,
First_Batting_Overs_Played int,
Second_batting varchar(255),
Second_Batting_Runs_Scored int,
Second_Batting_Wicket_loss int,
Second_Batting_Overs_Played int,
Foreign key(TMatch_ID) references tournament_schedule(Tmatch_id),
Foreign key(Tournament_id) references tournament(tournament_ID)
);


drop table Tournament_Match_Results;






































