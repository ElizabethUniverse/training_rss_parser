## Iteration 1
RSS reader it's command line utility, which receives RSS URL and prints result in convenient output format

Input data has following interface:

`rss_reader.py source [-h] [--version] [--verbose] [--json] [--limit LIMIT]`
````
positional arguments:
source - that's news API
optionals arguments:
-h - provides common information about our rss parser
--version - print in stdout current version
--verbose - print all logs in stdout
--json - print news in JSON format
--limit LIMIT - limit amount of news topics
````
JSON structure:
```
{
	{
		"title":   "A black man was put in handcuffs after a police officer stopped him on a trainplatform because he was eating",
		"article": "Bay Area Rapid Transit police said Steve Foster, of Concord, California,violated state law by eating a sandwich on a BART station's platform.  ",
		"links": [
			"https://news.yahoo.com/black-man-put-handcuffs-police-170516695.html",
			"http://l.yimg.com/uu/api/res/1.2/iLcp4eQPeHI64PZ9LpeQcw--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media.zenfs.com/en-US/insider_articles_922/e4254e78d7432dae4387d72624ee3086"
		],
		"link": "https://news.yahoo.com/black-man-put-handcuffs-police-170516695.html",
		"date": "Mon, 11 Nov 2019 17:06:55 -0500"
	},
	{
		...
	},
	...
}
```

## Iteration 2
to run rss parser on your computer you need to:
1) clone repository from https://github.com/ElizabethUniverse/FinalTaskRssParser
2) `$cd final_task`
3)  `$python setup.py sdist upload`
4)  `$cd dist`
3) `$pip install rss_reader-1.1.tar.gz`
4) run `$rss_reader https://news.yahoo.com/rss` --limit 2 --verbose

## Iteration 3
News is stored in the csv cache in following format and with tab delimiter.

`date    title    link   article   list_links`

To run application with updates:

`$python rss_reader.py https://news.yahoo.com/rss --date 20191115`

--date argument works without internet connection and with --verbose, --json, --limit LIMIT arguments the same way 