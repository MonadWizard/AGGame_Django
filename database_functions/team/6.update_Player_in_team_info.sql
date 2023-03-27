-- a jsonb variable will be passed where team_id will be checked, if team_id exists then, the function will update or else insertion will happen

CREATE OR REPLACE FUNCTION update_player_info_in_team(pass_team jsonb)
RETURNS VOID AS
$$
DECLARE
    player_details text := pass_team ->> 'team_members';
    IScaptain varchar(255)  :=  pass_team ->> 'captain';
    ISvicecaptain varchar(255)  := pass_team ->> 'vice_captain';
    teamm_id varchar(255) := pass_team ->> 'team_id';
    query text ;
BEGIN

  IF EXISTS (SELECT 1 FROM team WHERE team_id = teamm_id) THEN

    query = format('UPDATE team SET team_members = ''%s'', captain = ''%s'', vice_captain = ''%s'' WHERE team_id = ''%s''',player_details,
      IScaptain,ISvicecaptain,teamm_id);
    raise notice '%', query;
   EXECUTE query;
    raise notice 'if block';
  raise notice '%', IScaptain;
  raise notice '%', ISvicecaptain;
    raise notice '%', player_details;
  ELSE
      raise notice 'kaj korena';
  END IF;

END;
$$
LANGUAGE plpgsql;




select * from team;

drop function update_player_info_in_team(pass_team jsonb);

select * from auth_user_app_user;

SELECT update_player_info_in_team('{
"team_id": "757720230327055031384",
"team_members": [{
                        "playerId": "0322045912807866",
                        "is12thMan": "True",
                        "playing_order": "5/11"
                },
                {
                        "playerId": "0322045932619415",
                        "is12thMan": "False",
                        "playing_Order": "5/11"
                }
        ],
"captain": "0327050834329034",
"vice_captain": "0327051025349287"
}');



select * from team;

select * from auth_user_app_user;

select * from cricketprofile;
