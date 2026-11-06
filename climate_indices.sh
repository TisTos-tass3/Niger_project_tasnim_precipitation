#!/bin/bash

# 1. Directories
INPUT="/path"
OUTPUT="/path/results"

mkdir -p "$OUTPUT"

CSV="$OUTPUT/annual_indices.csv"
TEMP="$OUTPUT/temporary_year.nc"

echo "experiment,model,year,PR,SDII,R20mm" > "$CSV"

# 2. Experiments
for exp in historical ssp126 ssp245 ssp585; do

    if [ "$exp" = "historical" ]; then
        start=1985
        end=2014
    else
        start=2019
        end=2050
    fi

    # 3. Models
    for model in ACCESS-CM2 MPI-ESM1-2-HR; do

        # 4. Years
        for year in $(seq "$start" "$end"); do

            file="$INPUT/pr_day_${model}_${exp}_r1i1p1f1_gn_${year}_Africa.nc"

            echo "Processing $exp $model $year"

            # 5. Extract Niger and convert precipitation
         cdo -O -sellonlatbox,0,16,11,24 \
    	-setunit,mm \
    	-mulc,86400 \
    	-selname,pr \
    	"$file" "$TEMP"

            # 6. Annual precipitation
            pr=$(cdo -s output -fldmean -yearsum "$TEMP")

            # 7. SDII
            sdii=$(cdo -s output -fldmean -eca_sdii "$TEMP")

            # 8. R20mm
            r20=$(cdo -s output -fldmean -eca_r20mm "$TEMP")

            # 9. Save results
            echo "$exp,$model,$year,$pr,$sdii,$r20" >> "$CSV"

        done
    done
done

rm -f "$TEMP"

echo "Processing finished!"
echo "Results saved in $CSV"
