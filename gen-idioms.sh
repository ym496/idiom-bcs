#!/bin/bash

source ./.venv/bin/activate
rm -rf Idioms
mkdir Idioms Idioms/S{1..6}

mkdir ep-trans
python scrape.py

for file in ./ep-trans/* ; do 
  name=$(basename "$file" | cut -d. -f1)
  season=${name:1:1}
  python ./query_model.py "$file" > "./Idioms/S${season}/${name}.md"
done

deactivate
