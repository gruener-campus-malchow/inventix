#dot -Tsvg mvc.dot > mvc.svg
for f in *.dot ; do dot -Tsvg "$f" > "${f%.dot}.svg" ; done

for f in *.dot ; do dot -Tpng "$f" > "${f%.dot}.png" ; done

