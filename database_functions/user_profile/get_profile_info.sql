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
    select userid, user_username, user_email, user_life_history, user_interested_sports, user_playing_sports
    from auth_user_app_user
    where userid = $1
) as userinfo;
return details;
end;
$$
language plpgsql;


select get_profile_info('0327050758707019');

select * from auth_user_app_user;
