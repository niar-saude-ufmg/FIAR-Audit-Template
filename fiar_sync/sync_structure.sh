#!/bin/bash

echo "🔄 FIAR SYNC START"

# rename legacy root folder
if [ -d "artefatos_operacionais" ]; then
  git mv artefatos_operacionais operational_artifacts
fi

# rename legacy subfolders
declare -A MAP=(
  ["historico_versoes"]="version_history"
  ["incidentes"]="incidents"
  ["monitoramento"]="monitoring"
  ["revisao_periodica"]="periodic_review"
)

for old in "${!MAP[@]}"; do
  new=${MAP[$old]}

  if [ -d "operational_artifacts/$old" ]; then
    git mv "operational_artifacts/$old" "operational_artifacts/$new"
    echo "✔ migrated $old → $new"
  fi
done

echo "✅ FIAR SYNC COMPLETE"