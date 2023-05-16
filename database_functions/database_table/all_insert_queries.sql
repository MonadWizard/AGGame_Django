select * from cricketprofile;

select * from auth_user_app_user;

select
           cricketprofile.player_id,
           auth_user_app_user.user_username as PlayerName,
           cricketprofile.Strike_Rate,
           cricketprofile.player_image,
           cricketprofile.player_average,
           cricketprofile.playing_position
FROM auth_user_app_user
JOIN cricketprofile ON auth_user_app_user.userid = cricketprofile.player_id
JOIN team ON auth_user_app_user.userid = team.team_creator_id
WHERE auth_user_app_user.userid = '0322045912807866';
