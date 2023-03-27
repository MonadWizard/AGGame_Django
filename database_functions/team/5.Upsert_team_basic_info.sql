-- update

SELECT upsert_team('{
                                "team_id" : "551520230327074756692",
                                "game_name": "cricket",
                                "team_creator_id": "0327050758707019",
                                "team_owner": "updated owner" ,
                                "country_of_the_team":"England",
                                "team_logo":"logo2.jpg",
                                "team_name": "cricket1",
                                "team_email": "updatemail.com",
                                "team_mobile":"+880173456789",
                                "country_of_gameplaying":"Unknown"}');


-- insert
SELECT upsert_team('{
                                "game_name": "cricket",
                                "team_creator_id": "0327050758707019",
                                "team_owner": "adnan234" ,
                                "country_of_the_team":"England",
                                "team_logo":"logo.jpg",
                                "team_name": "cricket",
                                "team_email": "javeria@jav.com",
                                "team_mobile":"+880173456789",
                                "country_of_gameplaying":"Unknown"}');

select * from team;

CREATE OR REPLACE FUNCTION upsert_team(pass_team jsonb)
RETURNS VOID AS $$
DECLARE
    teamm_owner text := pass_team ->> 'team_owner';
    teamm_logo text :=  pass_team ->> 'team_logo';
    teamm_id varchar(255) := pass_team ->> 'team_id';
    teamm_creator_id varchar(255) := pass_team ->> 'team_creator_id';
    gamee_name text := pass_team ->> 'game_name';
team_name text := pass_team ->> 'team_name';
country_of_the_team text := pass_team ->> 'country_of_the_team';
Country_of_GamePlaying text := pass_team ->> 'Country_of_GamePlaying';
email text := pass_team ->> 'team_email';
mobile_number text := pass_team ->> 'team_mobile';

    query text ;
BEGIN

  IF EXISTS (SELECT 1 FROM team WHERE team_id = teamm_id) THEN
        query := format('UPDATE team SET game_name = ''%s'', team_owner = ''%s'', team_logo = ''%s'',
                        team_name = ''%s'',country_of_the_team = ''%s'',Country_of_GamePlaying = ''%s'',team_email  = ''%s'',team_mobile = ''%s''
                       WHERE team_id = ''%s'' AND team_creator_id = ''%s''',
                        gamee_name, teamm_owner, teamm_logo,
                        team_name, country_of_the_team,Country_of_GamePlaying,email,mobile_number,teamm_id,teamm_creator_id);

        EXECUTE query;
    ELSE
    -- Insert new row with provided details
      query := format('INSERT INTO team(team_id, team_creator_id, game_name, team_owner, team_logo, team_name,country_of_the_team,Country_of_GamePlaying,team_email,team_mobile)
                  VALUES((floor(random() * 9000 + 1000)::INT || TO_CHAR(now(), ''YYYYMMDDHH24MISSMS'')), ''%s'', ''%s'', ''%s'', ''%s'', ''%s'', ''%s'',''%s'', ''%s'', ''%s'')',
                teamm_creator_id, gamee_name, teamm_owner, teamm_logo, team_name,country_of_the_team,Country_of_GamePlaying,email,mobile_number );
      execute query;
  END IF;

END;
$$
LANGUAGE plpgsql;



drop function upsert_team(p_team jsonb);

select * from team;

select * from auth_user_app_user;










select upsert_team('{"game_name": "cricket", "team_creator_id": "0327050758707019", "team_owner": "adnan", "country_of_the_team": "England", "team_logo": "logo.jpg", "team_name": "cricket", "team_email": "javeria@jav.com", "team_mobile": "+880173456789", "country_of_gameplaying": "Unknown"}');



