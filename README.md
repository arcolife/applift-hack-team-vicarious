# applift-hack-team-vicarious

Datathon centered around finding/recommending patterns in mobile/tablet market, and investing for various app markets domain-upliftment. Refer to docs/ for more on problem statement, slides & screenshots of the approach and such. Some samples are included below:

## 3 Phases

### P1
Raw statistics, subject to answering qualms about bidding, and such

### P2
Visualizations depicting correlations and to help with extracting meaningful features meant for Phase 3

### P3
Predictions, with ExchangeBid as input, Outcome as output and the features obtained from Phase 2 as weights.

## Note
So, we started with an ipython notebook then moved on to IBM watson analytics, and finally ended up using Dato's GraphLab for logistic regression, elasticsearch & Kibana for visualizations and some spreadsheet magic to infer "Where to put my money?"

`- Team Vicarious`

## Screen shots

- Comaprision of Average ExchangeBid with Age
- Comparision of Aberage ExchangeBid over Country and Outcome

![Vicarious1](https://raw.githubusercontent.com/HackerEcology/SuggestU/master/docs/vicarious1.png)

- ExchangeBid% v/s DeviceType
- ExchangeBid avg. compared over Manufacturer and Outcome

![Vicarious2](https://raw.githubusercontent.com/HackerEcology/SuggestU/master/docs/vicarious2.png)

- ExchangeBid avg. over countries

![Vicarious3](https://raw.githubusercontent.com/HackerEcology/SuggestU/master/docs/vicarious3.png)

- Successful CampaignID(s) v/s avg ExchangeBid

![Vicarious4](https://raw.githubusercontent.com/HackerEcology/SuggestU/master/docs/vicarious4.png)

- Elasticsearch indexed dataset

![Vicarious5](https://raw.githubusercontent.com/HackerEcology/SuggestU/master/docs/vicarious5.png)
