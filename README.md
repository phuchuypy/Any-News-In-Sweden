# Hej! Any news from The Local Sweden?
Purpose: this script checks if there are any news on The Local Sweden compared to the last time we visited this website.\n
What problem does it solve: The Local Sweden does not post many news daily. Some articles you saw/read might still be there after a few days, or even weeks. Therefore, it takes a bit of time to look for newly-posted articles.\n
What does it do in details:
1. Go to The Local Sweden, get all of the titles of the headlines 
2. If the script is run for the first time, it will save all of these titles in a file
   If not, all of these titles are compared with previous titles in the saved file. New posts' titles will be printed in the console.
