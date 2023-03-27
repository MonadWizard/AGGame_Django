create or replace function MatchCreation(passing_data jsonb)
RETURNS VOID AS $$
DECLARE
    game_ownerr text := passing_data ->> 'Game_Owner';
    type_of_gamee text :=  passing_data ->> 'Type_Of_Game';
    Game_Configurationn jsonb := passing_data ->> 'Game_Configuration';
    Game_DateTimee timestamp := to_timestamp(passing_data ->> 'Game_DateTime', 'YYYY/MM/DD HH24:MI');
    game_namee jsonb := passing_data ->> 'Game_Name';
         Game_Locationn varchar[]:= ARRAY[passing_data ->> 'Game_Location'];
GameOwner_Phonee varchar(255) := passing_data ->> 'GameOwner_Phone';
GameOwner_emaill varchar(255):= passing_data ->> 'GameOwner_email';
Game_LiveLinkk jsonb:= passing_data ->> 'Game_LiveLink';
    query text ;
BEGIN
      query = format('INSERT INTO match(Game_ID,Game_Owner,Type_Of_Game,Game_Configuration,Game_DateTime,Game_Name,Game_Location,GameOwner_Phone,GameOwner_email,Game_LiveLink)
                VALUES(''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'','' %s'', ''%s'','' %s'')',
                (floor(random() * 9000 + 1000)::INT || TO_CHAR(now(), 'YYYYMMDDHH24MISSMS')),game_ownerr,type_of_gamee,Game_Configurationn,
Game_DateTimee,game_namee,Game_Locationn,GameOwner_Phonee,GameOwner_emaill,Game_LiveLinkk);
execute query;
      raise notice '% ', query;
END;
$$
LANGUAGE plpgsql;

SELECT MatchCreation('{
  "Game_Owner" : "0322045932619415",
  "Type_Of_Game" : "Cricket",
  "Game_Configuration" : {
    "over of the match":"15",
    "match_prize":"50k"
  },
  "Game_DateTime" : "2023/12/02 07:20",
  "Game_Name": {"Team_1":"684020230322063225364", "Team_2":"625120230322063207706", "additional text":"they will be playing against each other for the 1st time"},
  "Game_Location" : ["Stadium", "link here"],
  "GameOwner_Phone" : "+8801827064227",
  "GameOwner_email":"adnan@gmail.com",
  "Game_LiveLink":{"www.adnanfoundationmatches/cricket.com":"youtube_id"}
}');


select * from match;

drop function matchcreation(passing_data jsonb);

select * from team;

select * from auth_user_app_user;