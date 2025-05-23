function setup_venv {
    if (!(Test-Path env:VIRTUAL_ENV)) {
        python -m pip install --upgrade pip
        python -m venv .\venv
    }
    .\venv\Scripts\Activate
    Write-Output "venv active"
    Write-Output "venv installed in $env:VIRTUAL_ENV"
}

setup_venv