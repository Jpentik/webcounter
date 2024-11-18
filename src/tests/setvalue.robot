*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Set Counter to Specific Value
    Go To  ${HOME_URL}
    Input Text  value  10
    Click Button  Aseta
    Page Should Contain  nappia painettu 10 kertaa
