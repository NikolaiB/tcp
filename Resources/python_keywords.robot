*** Settings ***
Library          ../Scripts/reach_tcp.py

*** Keywords ***
Check TCP Connection
    [Documentation]  Verify TCP connection
    [Arguments]    ${ip}    ${port}
    check_connection  ${ip}    ${port}
