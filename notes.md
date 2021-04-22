# twitterdev twarc demo

Link to join the stream tomorrow: https://streamyard.com/e8gi9yafsx

Link to Tweet about the webinar with forum post:
https://twitter.com/suhemparack/status/1384922554041782275

## Agenda:

1. Intro (Suhem & Ed) Document The Now project and motivation for Twarc (Ed)

  1. origins and Mellon: docnow.io
  2. collaborators Betsy Alpert, Igor Brigadir, Sam Hames, Jeff Sauer, and Daniel Verdeer
  3. principles of twarc2: link to blog post
  3. documentation: https://twarc-project.readthedocs.io

2. Academic Research product track (Suhem) Why use a library (Suhem)

3. Installing twarc2 (Ed)

  1. dev portal: bearer token 
  2. twarc: v1 api
  3. twarc2 help
  4. twarc2 configure

4. Search for Tweets using twarc2 (Ed) 

  1. just try a search: twarc2 search covid19
  2. limit with --limit
  3. remove retweets: twarc2 search 'covid19 -is:retweet'
  4. limit by time (WHO covid-19 on 2020-02-11): twarc2 search '(covid19 OR covid-19) -is:retweet' --start-time 2020-02-11 --end-time 2020-02-12  
  5. twarc.log

5. Payload structures (Suhem)

6. Ed to show how twarc2 handles the payloads for you)

  1. twarc requests all fields and expansions for you (docnow community will monitor for changes)
  2. we also have a flatten option and subcommand
  3. https://twitter.com/Yamiche/status/1385008025140871168
  4. vimdiff example.json example-flat.json 
  5. jsonl pipeline: twarc2 search 'youtube.com/watch?v=dQw4w9WgXcQ' --flatten --archive --limit 30000 | jq -r '.created_at[0:10]' | uniq -c | awk '{print $2 "," $1}' 

7. Support for CSV (Ed)

* twarc-csv plugin: will be moved into twarc when it is stable

8. Demo any other endpoints (which are supported in twarc2) (Ed)

* sample
* stream: stream-rules add/list/delete + stream
* followers/following
* timeline
* twarc-timelines
* twarc-videos
* hydrate (catalog, dataset in Downloads)
* other ones in the works: twarc-sqlite, twarc-activitystreams

Q&A (Suhem & Ed)

