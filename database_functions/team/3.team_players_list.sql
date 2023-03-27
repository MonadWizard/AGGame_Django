
select team_player_list('757720230327055031384');


CREATE OR REPLACE FUNCTION team_player_list(teamid varchar)
RETURNS jsonb
AS $$
DECLARE
    result jsonb;
    player_details jsonb;
BEGIN
    -- Extract player details
    SELECT json_agg(
        json_build_object(
            'player_id', elem->>'player_id',
            'PlayerName', auth_user_app_user.user_username,
            'Strike_Rate', cricketprofile.Strike_Rate,
            'player_image', cricketprofile.player_image,
            'player_average', cricketprofile.player_average
        )
    ) INTO player_details
    FROM auth_user_app_user
    JOIN cricketprofile ON auth_user_app_user.userid = cricketprofile.player_id
    JOIN team ON auth_user_app_user.userid = team.team_creator_id
    CROSS JOIN jsonb_array_elements(team.team_members) AS elem
    WHERE team.team_id = $1;

    -- Combine team and player details into a single JSON object
    result :=  player_details;
    RETURN result;
END;
$$ LANGUAGE plpgsql;



drop function team_player_list(teamid varchar);
