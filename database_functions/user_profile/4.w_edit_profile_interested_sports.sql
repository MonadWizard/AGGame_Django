CREATE OR REPLACE FUNCTION profile_interested_sports(col_values jsonb)
    RETURNS void AS
$$
DECLARE
    userid      varchar(30) := (col_values ->> 'userid');
    column_name  text;
    column_value jsonb;

  interested_sports_json JSONB;
  interested_sports_array JSONB[];
  sport_item JSONB;
  sport_name TEXT;

BEGIN

    FOR column_name, column_value IN SELECT * FROM jsonb_each(col_values)
        LOOP
            IF column_name <> 'userid' THEN
                EXECUTE format('UPDATE auth_user_app_user SET %I = %L WHERE userid = %L ', column_name,
                               column_value::text, userid);
            END IF;
    END LOOP;


-- create sports profile
    interested_sports_json := col_values -> 'user_playing_sports';

      IF NOT(interested_sports_json IS NULL OR jsonb_typeof(interested_sports_json) = 'null') THEN
        interested_sports_array := array(SELECT jsonb_array_elements(interested_sports_json));

        FOREACH sport_item IN ARRAY interested_sports_array
        LOOP
          sport_name := sport_item ->> 'sports_name';

            IF sport_name = 'cricket' AND  NOT EXISTS (SELECT player_id FROM cricketprofile WHERE player_id = userid) THEN
                INSERT INTO cricketprofile (player_id) VALUES (userid);
            END IF;

          RAISE NOTICE 'Sports name: %', sport_name;
        END LOOP;
      END IF;

END;
$$
    LANGUAGE plpgsql;







select * from auth_user_app_user;




-- insert single sports
SELECT profile_interested_sports('{"userid": "0327050834329034", "user_playing_sports": [
    {
        "sports_name": "cricket",
         "player_nickname": "kitty",
         "highlight_of_career": [
             "link1", "link2", "link3" ] }

]}'::jsonb);


-- insert multiple sports

SELECT profile_interested_sports('{"userid": "0322050024752326", "user_playing_sports": [
    {
        "sports_name": "cricket",
         "player_nickname": "kitty",
         "highlight_of_career": [
             "link1", "link2", "link3" ] },
    {
        "sports_name": "football",
         "player_nickname": "kittyball",
         "highlight_of_career": [
             "link1", "link2", "link3" ] }

]}'::jsonb);




select *
from auth_user_app_user;


select * from cricketprofile;









