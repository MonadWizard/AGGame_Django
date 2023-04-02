
SELECT update_profile('{
  "userid": "0327050758707019",
  "user_email": "zobi@gmail.com",
  "user_dob": "1990/04/15",
  "user_callphone": "+880123456",
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
  "user_configuration" :"null"

}');

select * from auth_user_app_user;

drop function update_user_profile;






CREATE OR REPLACE FUNCTION update_profile(pass_data jsonb)
RETURNS VOID AS
$$
DECLARE
    user_id varchar := pass_data ->> 'userid';
    username varchar := pass_data ->> 'user_username';
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
    query text ;
BEGIN
raise notice 'Input JSON: %', pass_data;
  -- update the row with the same userid
  IF EXISTS (SELECT 1 FROM auth_user_app_user WHERE userid = user_id) THEN
--
    query = format('UPDATE auth_user_app_user
                   SET user_dob = ''%s'', user_fullname = ''%s'',user_configuration=''%s'',
                   user_email = ''%s'', user_callphone = ''%s'', user_country = ''%s'',user_state_divition=''%s'',
                   user_playing_city = ''%s'', user_photopath = ''%s'', user_life_history = ''%s'',
                   user_interested_sports = ''%s''
                   WHERE userid = ''%s''',user_dob, user_fullname, user_configuration, user_email, user_callphone,
                   user_country,user_state_divition,user_playing_city,user_photopath,user_life_history,
                   user_interested_sports,user_id);
    raise notice '::::::::::::::::::::::::::::::::::::::::::::::%', query;
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











SELECT update_profile('{"userid": "0327051025349287",
    "user_email": "zobi123234@gmail.com",
    "user_dob": "1990/04/15",
    "user_callphone": "+88017113090807",
    "user_life_history": {"jobtitle": "abc", "start-at": "1998/12/22", "end-at": "2022/12/22"},
    "user_interested_sports": [{"interest1": "cricket"}],
    "user_fullname": {"first_name": "Abdul", "last_name": "Kuddus"},
    "user_configuration": {"body_type": "Ectomorphs", "height": "5feet", "weight": "85kg"},
    "user_photopath": "/profilepic/0327051025349287.png"}')








