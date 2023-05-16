select * from auth_user_app_user;

select * from cricketprofile;


CREATE OR REPLACE FUNCTION name_Search(search_string text)
RETURNS jsonb
AS $$
DECLARE
    result jsonb;
    player_details jsonb;
BEGIN
    -- Extract player details
    SELECT json_agg(player)
    INTO player_details
    FROM (
        SELECT
            json_build_object(
                'name', cricketprofile.player_fullname,
                'player_image',cricketprofile.player_image,
                'playing_role',cricketprofile.playing_role,
                'strike_rate',cricketprofile.strike_rate,
                'player_average', cricketprofile.player_average
            ) AS player
        FROM
            auth_user_app_user
            JOIN cricketprofile ON auth_user_app_user.userid = cricketprofile.player_id
        WHERE
            lower(auth_user_app_user.user_fullname->>'first_name') LIKE lower('%' || search_string || '%')
            OR lower(auth_user_app_user.user_fullname->>'last_name') LIKE lower('%' || search_string || '%')
            OR lower(cricketprofile.player_nickname) LIKE lower('%' || search_string || '%')
    ) AS players;

    -- Combine player details into a single JSON object
    result := json_build_object('players', player_details);
    RETURN result;
END;
$$ LANGUAGE plpgsql;


select name_Search('faz');