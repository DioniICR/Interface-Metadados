@echo off
setlocal

:: Caminhos das pastas
set "AUDIO_DIR=audios"
set "TABELA_DIR=tabelas"
set "ZIP_NAME=backup.zip"

:: Criar o zip (requer compactação nativa do Windows via PowerShell)
powershell -Command "Compress-Archive -Path '%AUDIO_DIR%\*.wav','%TABELA_DIR%\*.xlsx' -DestinationPath '%ZIP_NAME%'"

:: Verificar se o ZIP foi criado com sucesso
if exist "%ZIP_NAME%" (
    echo Arquivo zip criado com sucesso.

    :: Apagar os arquivos .wav
    del /q "%AUDIO_DIR%\*.wav"

    :: Apagar os arquivos .xlsx
    del /q "%TABELA_DIR%\*.xlsx"

    echo Arquivos originais removidos.
) else (
    echo Falha ao criar o arquivo zip. Nada foi removido.
)

endlocal
