#! /usr/bin/env sh

TAG="V$(date '+%Y%m%dT%H%M')"

echo "{\"version_num\": \"${TAG}\"}" > sql_migrations/${TAG}.json
echo ${TAG}
