
select team_and_player_info('757720230327055031384');

select * from team;

select * from cricketprofile;

CREATE OR REPLACE FUNCTION team_and_player_info(teamid varchar)
RETURNS jsonb
AS $$
DECLARE
    result jsonb;
    player_details jsonb;
    team_details jsonb;
BEGIN
    -- Extract team details
    SELECT json_agg(
        json_build_object(
            'team_name', team.team_name,
            'team_members', team.team_members
        )
    ) INTO team_details
    FROM team
    WHERE team.team_id = $1;

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
    result := team_details || player_details;
    RETURN result;
END;
$$ LANGUAGE plpgsql;

