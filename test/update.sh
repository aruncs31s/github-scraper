#!/bin/bash
echo "Updating" 
git add ./scraper.ipynb
git commit -m "automatic update" 
git push origin main
sleep 5
