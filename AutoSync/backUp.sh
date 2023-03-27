#/bin/sh

_dataDir="~/IOT2-Projekt"
_commitMsg="Backup at $(date --rfc-2822)"

set -e # error handling: exit if any errors at all

cd $_dataDir

git add .
git commit -m "$_commitMsg"
git push
