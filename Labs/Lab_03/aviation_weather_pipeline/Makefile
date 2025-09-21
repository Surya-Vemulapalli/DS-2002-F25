.PHONY: all fetch analyze clean

analyze: fetch
	@echo " --- Analyzing the data --- "
	bash ./analyze_data.sh
	@echo "--- Analysis complete ---"

fetch: 
	@echo "--- Fetching the data --- "
	bash ./fetch_metars.sh
	@echo "--- Fetching finished --- "
clean:
	@echo  "--- Cleaning up ---"
	rm -rf weather_report.csv raw_metars/
