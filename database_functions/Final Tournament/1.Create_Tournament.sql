CREATE OR REPLACE FUNCTION TournamentCreation(passing_data JSONB)
RETURNS VOID AS $$
DECLARE
    Tournament_ID VARCHAR(255) := (floor(random() * 9000 + 1000)::INT || TO_CHAR(now(), 'YYYYMMDDHH24MISSMS'));
    Tournament_Owner VARCHAR(255) := passing_data ->> 'Tournament_Owner';
    Tournament_logo VARCHAR(255) := passing_data ->> 'Tournament_logo';
    Tournament_Name VARCHAR(255) := passing_data ->> 'Tournament_Name';
    TournamentMatchType VARCHAR(255) := passing_data ->> 'TournamentMatchType';
    Type_of_Tournament VARCHAR(255) := passing_data ->> 'Type_of_Tournament';
    Sport_or_Game_Configuration JSONB := passing_data ->> 'Sport_or_Game_Configuration';
    TournamentLocation JSONB := passing_data ->> 'TournamentLocation';
    OrganizerName VARCHAR(255) := passing_data ->> 'OrganizerName';
    HostName VARCHAR(255) := passing_data ->> 'HostName';
    OrganizerEmail VARCHAR(255) := passing_data ->> 'OrganizerEmail';
    OrganizerPhone VARCHAR(255) := passing_data ->> 'OrganizerPhone';
    Tournament_Admin VARCHAR(255) := passing_data ->> 'Tournament_Admin';
    TournamentStartDate timestamp := passing_data ->> 'TournamentStartDate';
    NumberOfTeamsInGroup INT := passing_data ->> 'NumberOfTeamsInGroup';
    NumberOfGroupsInTournament INT := passing_data ->> 'NumberOfGroupsInTournament';
    groupTeamDetails JSONB := passing_data ->> 'groupTeamDetails';
    Tournament_MatchConfiguration JSONB := passing_data ->> 'Tournament_MatchConfiguration';
    query TEXT;
BEGIN
    query = format('INSERT INTO tournament (
                    Tournament_ID,Tournament_Owner, Tournament_logo, Tournament_Name,
                    TournamentMatchType, Type_of_Tournament, Sport_or_Game_Configuration,
                    TournamentLocation, OrganizerName, HostName, OrganizerEmail,
                    OrganizerPhone, Tournament_Admin, TournamentStartDate, NumberOfTeamsInGroup,
                    NumberOfGroupsInTournament, groupTeamDetails, Tournament_MatchConfiguration)
                    VALUES (
                    ''%s'', ''%s'', ''%s'', ''%s'',
                    ''%s'', ''%s'', ''%s'',
                    ''%s'', ''%s'', ''%s'', ''%s'',
                    ''%s'', ''%s'', ''%s'', ''%s'',
                    ''%s'', ''%s'', ''%s'')',
        Tournament_ID, Tournament_Owner, Tournament_logo, Tournament_Name,
        TournamentMatchType, Type_of_Tournament, Sport_or_Game_Configuration,
        TournamentLocation, OrganizerName, HostName, OrganizerEmail,
        OrganizerPhone, Tournament_Admin, TournamentStartDate, NumberOfTeamsInGroup,
        NumberOfGroupsInTournament, groupTeamDetails, Tournament_MatchConfiguration);
    EXECUTE query;

    PERFORM create_dynamic_table_for_tournament(Tournament_ID);

END;
$$ LANGUAGE plpgsql;




SELECT TournamentCreation(
    '{
      "Tournament_Owner": "0322045912807866",
      "Tournament_logo": "http://example.com/logo.png",
      "Tournament_Name": "Example Tournament",
      "TournamentMatchType": "Single Elimination",
      "Type_of_Tournament": "Amateur",
      "Sport_or_Game_Configuration": {"field_type": "grass", "ball_type": "leather"},
      "TournamentLocation": {"city": "New York", "state": "NY", "country": "USA"},
      "OrganizerName": "Jane Doe",
      "HostName": "Example Sports Club",
      "OrganizerEmail": "jane.doe@example.com",
      "OrganizerPhone": "555-1234",
      "Tournament_Admin": "admin@example.com",
      "TournamentStartDate": "2023-04-01 15:20:00+06",
      "NumberOfTeamsInGroup": 4,
      "NumberOfGroupsInTournament": 2,
      "groupTeamDetails": {"group1": ["Team A", "Team B", "Team C", "Team D"], "group2": ["Team E", "Team F", "Team G", "Team H"]},
      "Tournament_MatchConfiguration": {"match_length": 90, "halftime_length": 15, "overtime_length": 30}}'
);


select * from match;

select * from tournament;

select * from cricketprofile;

select * from auth_user_app_user;









INSERT INTO tournament (
Tournament_ID,Tournament_Owner, Tournament_logo, Tournament_Name,
TournamentMatchType, Type_of_Tournament, Sport_or_Game_Configuration,
TournamentLocation, OrganizerName, HostName, OrganizerEmail,
OrganizerPhone, Tournament_Admin, TournamentStartDate, NumberOfTeamsInGroup,
NumberOfGroupsInTournament, groupTeamDetails, Tournament_MatchConfiguration)
VALUES (
(floor(random() * 9000 + 1000)::INT || TO_CHAR(now(), 'YYYYMMDDHH24MISSMS')),
        '0315094604478486', 'http://example.com/logo.png', 'Example Tournament',
        'Single Elimination', 'Amateur', '{"ball_type": "leather", "field_type": "grass"}',
        '{"city": "New York", "state": "NY", "country": "USA"}', 'Jane Doe', 'Example Sports Club', 'jane.doe@example.com',
        '555-1234', 'admin@example.com', '2024-03-22 07.40', '4',
        '2', '{"group1": ["Team A", "Team B", "Team C", "Team D"],
      "group2": ["Team E", "Team F", "Team G", "Team H"]}', '{"match_length": 90, "halftime_length": 15, "overtime_length": 30}')



