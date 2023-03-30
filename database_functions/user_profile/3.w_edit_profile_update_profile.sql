

SELECT update_user_profile('{
  "userid": "0327050758707019",
  "user_username": "zobia",
  "user_email": "zobi@gmail.com",
  "user_callphone": "+8801234567",
  "user_dob": "1990/04/15",
  "user_life_history":
    {
      "jobtitle": "abc",
      "start-at": "1998/12/22",
      "end-at": "2022/12/22"
    },
  "user_interested_sports":
    {
      "interest1" : "cricket",
      "interest2" : "badminton"
    },
  "user_fullname" : "null",
  "user_configuration" :"null",
  "user_playing_sports" : "null"


}');

select * from auth_user_app_user;

drop function update_user_profile;

CREATE OR REPLACE FUNCTION update_user_profile(pass_data jsonb)
RETURNS VOID AS
$$
DECLARE
    user_id varchar := pass_data ->> 'userid';
    user_dob DATE  :=  pass_data ->> 'user_dob';
    user_fullname jsonb := pass_data ->> 'user_fullname';
    user_email varchar := pass_data ->> 'user_email';
    user_callphone varchar := pass_data ->> 'user_callphone';
    user_country varchar := pass_data ->> 'user_country';
    user_state_divition varchar := pass_data ->> 'user_state_divition';
    user_playing_city varchar := pass_data ->> 'user_playing_city';
    user_photopath varchar := pass_data ->> 'user_photopath';
    user_life_history jsonb := pass_data ->> 'user_life_history';
    user_configuration jsonb := pass_data ->> 'user_configuration';
    user_interested_sports jsonb := pass_data ->> 'user_interested_sports';
    user_playing_sports jsonb := pass_data ->> 'user_playing_sports';
    query text ;
BEGIN
raise notice 'Input JSON: %', pass_data; -- add this line
  -- update the row with the same team_id
  IF EXISTS (SELECT 1 FROM auth_user_app_user WHERE userid = user_id) THEN
--
    query = format('UPDATE auth_user_app_user
                   SET  user_dob = ''%s'', user_fullname = ''%s'',user_configuration=''%s'',
                   user_email = ''%s'', user_callphone = ''%s'', user_country = ''%s'',user_state_divition=''%s'',
                   user_playing_city = ''%s'', user_photopath = ''%s'', user_life_history = ''%s'',
                   user_interested_sports = ''%s'', user_playing_sports = ''%s''
                   WHERE userid = ''%s''', user_dob, user_fullname, user_configuration, user_email, user_callphone,
                   user_country,user_state_divition,user_playing_city,user_photopath,user_life_history,
                   user_interested_sports,user_playing_sports,user_id);
   EXECUTE query;
    raise notice 'if block';

  ELSE
      raise notice 'kaj korena';
  END IF;
--
--   -- Return the result data
--   RETURN NEXT t_result;
END;
$$
LANGUAGE plpgsql;
