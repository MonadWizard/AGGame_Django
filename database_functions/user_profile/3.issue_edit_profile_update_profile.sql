    CREATE OR REPLACE FUNCTION update_table(col_values JSONB)
    RETURNS void AS
    $$
    DECLARE
      userid varchar(30) := (col_values->>'userid')::varchar(30);
      column_name varchar;
      column_value jsonb;
        query text;
    BEGIN
      FOR column_name, column_value IN SELECT * FROM jsonb_each(col_values)
      LOOP
        IF column_name <> 'userid' THEN
         query := format('UPDATE auth_user_app_user SET %s = $1 WHERE userid = $2', column_name
        USING column_value, userid);



        END IF;
      END LOOP;
    END;
    $$
    LANGUAGE plpgsql;

SELECT update_table('{
  "userid": "0322050024752326",
  "user_username": "zobia11",
  "user_email": "zobi@gmail.com",

  "user_life_history":
    {
      "jobtitle": "abc",
      "start-at": "22/12/1998",
      "end-at": "22/12/2022"
    },
  "user_interested_sports":
    {
      "jobtitle": "abc",
      "start-at": "22/12/1998",
      "end-at": "22/12/2022"
    }

}');

select * from auth_user_app_user;

CREATE OR REPLACE FUNCTION update_table(col_values jsonb)
RETURNS void AS $$
DECLARE
  column_name text;
  column_value text;
  v_data_type text;
  userid varchar;
BEGIN
  column_name := '';
  column_value := '';
  userid := col_values->>'userid';
  FOR column_name, column_value IN SELECT * FROM jsonb_each(col_values)
  LOOP
    IF column_name <> 'userid' THEN
      SELECT data_type INTO v_data_type FROM information_schema.columns WHERE table_name = 'auth_user_app_user' AND column_name = column_name;
      IF v_data_type = 'jsonb' THEN
        EXECUTE format('UPDATE auth_user_app_user SET %I = %s WHERE userid = %L', column_name, column_value, userid);
      ELSE
        EXECUTE format('UPDATE auth_user_app_user SET %I = %L WHERE userid = %L', column_name, column_value, userid);
      END IF;
    END IF;
  END LOOP;
END;
$$ LANGUAGE plpgsql;





SELECT update_table('{
  "userid": "0322050024752326",
  "user_username": "zobia",
  "user_email": "zobi@gmail.com"
}')