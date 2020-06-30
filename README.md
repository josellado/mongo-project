
# GeoSpartial Data Project
​
<img src=http://www.vidiani.com/maps/maps_of_the_world/detailed_satellite_map_of_the_world.jpg

​

Im ny next project I was asked to find out the best posible location in the world for a gaming comapny , meeting some specific criteria: 



- Developers like to be near successful tech startups that have raised at least 10 Million dollars.

- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.

- All people in the company have between 25 and 40 years, give them some place to go to party.
- The CEO is Vegan

- The office dog "Pepe" needs a hairdresser every month. Ensure there's one not too far away.

In order to satisfy those requests and to answer the question, The best location? I had to follow some steps:

1. Using the Companies. Json file, (which cointains over 18000 companies) and  analysize it to find out the city with the higest concentration of gaming enterprises that have had $10m or more of finance 

        > You can find graphs showing the results of the filter data of companies.json in Output file

2. Making queries to  Google Places Api to find out in San Francisco all  the: 
- starbucks 
- vegan Restuarants 
- nightclubs
- veterinaries

3. Converting all the data to type Geocode format in order to be able to do GeoQuerys 

4. Find out all the starbucks, vegan restaurants, nightclubs and veterinaries that are nearby one off the gaming offices previously selected.
5. Using Foolium library plot all the desire results in a graph





