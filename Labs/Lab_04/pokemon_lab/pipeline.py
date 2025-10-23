#!/usr/bin/env python3
import pandas as pd
import os
import json
import sys
import csv
import update_portfolio
import generate_summary

def run_production_pipeline():
    print("Started...",file=sys.stderr)
    print("Updating the portfolio")
    update_portfolio.main()
    print("Reporting...")
    generate_summary.main()
    print("Completed",file=sys.stderr)

if __name__ == "__main__":
    run_production_pipeline()