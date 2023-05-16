create or replace function get_profile_info(user_id varchar)
returns jsonb
as
$$
declare
details jsonb;
begin
select to_jsonb(userinfo)
into details
from (
    select userid, user_username,user_fullname,user_dob, user_callphone, user_configuration, user_callphone,user_country,user_photopath,user_state_divition,user_email, user_playing_city,user_life_history, user_interested_sports, user_playing_sports
    from auth_user_app_user
    where userid = $1
) as userinfo;
return details;
end;
$$
language plpgsql;

    select * from auth_user_app_user;

select get_profile_info('0329043540613666');