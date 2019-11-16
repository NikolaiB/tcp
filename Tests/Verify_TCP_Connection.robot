*** Settings ***
Library           SeleniumLibrary
Resource          ../Resources/python_keywords.robot

*** Test Cases ***
Verify Conncetion
    Check TCP Connection    localhost    8000

