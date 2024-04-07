# AirBnB MongoDB Analysis

## Data Set Details

### Origin of the Data Set
This dataset offers a thorough examination of the Airbnb listings in Dallas, Texas, United States.The data offering the information of the variety of accommodations, pricing, location specifics, host information, etc. This dataset works as a valuable resource for understanding the short-term rental landscape in Dallas. The datast is ideal for and tourism researchers or someone who want to know about local Airbnb information. The dataset is from (URL) [Inside Airbnb](https://insideairbnb.com/get-the-data/)

### Data Set Format
The format of the original data file is in CVS.

### Raw Data Set Display
<div style="height: 500px; overflow-y: scroll;">

| id      | listing_url                          | scrape_id   | last_scraped | source      | name                                               | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | neighborhood_overview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | picture_url                                                                                              | host_id  | host_url                                   | host_name   | host_since | host_location | host_about                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | host_response_time | host_response_rate | host_acceptance_rate | host_is_superhost | host_thumbnail_url                                                                                         | host_picture_url                                                                                              | host_neighbourhood                     | host_listings_count | host_total_listings_count | host_verifications               | host_has_profile_pic | host_identity_verified | neighbourhood                | neighbourhood_cleansed | neighbourhood_group_cleansed | latitude  | longitude  | property_type                     | room_type       | accommodates | bathrooms | bathrooms_text | bedrooms | beds | amenities                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | price    | minimum_nights | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | calendar_updated | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review | last_review | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication | review_scores_location | review_scores_value | license | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |
|---------|--------------------------------------|-------------|--------------|-------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------|--------------------------------------------|-------------|------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------|----------------------|-------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------|---------------------|---------------------------|----------------------------------|----------------------|------------------------|------------------------------|------------------------|------------------------------|-----------|------------|-----------------------------------|-----------------|--------------|-----------|----------------|----------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------|----------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------|------------------|-----------------|-----------------|-----------------|------------------|-----------------------|-------------------|-----------------------|------------------------|--------------|-------------|----------------------|------------------------|---------------------------|-----------------------|-----------------------------|------------------------|---------------------|---------|------------------|--------------------------------|---------------------------------------------|----------------------------------------------|---------------------------------------------|-------------------|
| 61878   | https://www.airbnb.com/rooms/61878   | 2.02402E+13 | 2024/2/22    | city scrape | MODERN LIVING AND FURNISHINGS                      | Close to downtown and Uptown.  Fast and convenient to highway, grocery shops, dinner, clubbing and much more. Very modern home.<br /><br />Pets welcomed with approval and additional fee $100 per pet.                                                                                                                                                                                                                                                                                                                                     | Enjoy the heart of Dallas right out your door step.  Cedar Springs offers a eclectic night life as well as great restaurants.  Or take a minute drive/Uber to Uptown for shopping.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | https://a0.muscache.com/pictures/c4d9625e-bcc5-4790-b699-3b1acb0a2b3d.jpg                                | 300211   | https://www.airbnb.com/users/show/300211   | Sasha       | 2010/11/26 | Roanoke, TX   | "Love is Love" :) I'm originally from Florida, but call Texas home.  Things I can't live without are coffee, family & friends, my dog, traveling and love.   When I travel, I love having the comforts of home all while enjoying a new city. This was my thought when I wanted my home to a part of AirBNB. You will enjoy all the comforts of a home . . . Who doesn't like a clean, modern apartment all to themselves? All in the heart of Dallas. Come visit and stay awhile . . . You will love it!                                                                                                                                                                                                                                                                                                                                                                             | within an hour     | 100%               | 100%                 | f                 | https://a0.muscache.com/im/pictures/user/5f63d226-6de3-4b43-a863-64b8a9ff8fa2.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/5f63d226-6de3-4b43-a863-64b8a9ff8fa2.jpg?aki_policy=profile_x_medium | Oak Lawn                               | 2                   | 3                         | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 2             |                              | 32.8169   | -96.82018  | Entire condo                      | Entire home/apt | 3            | 1         | 1 bath         | 1        | 2    | ["Kitchen", "Gym", "Washer", "Essentials", "Hangers", "Hair dryer", "Dishes and silverware", "Pets allowed", "Carbon monoxide alarm", "Smoke alarm", "Shared pool", "Fire extinguisher", "TV with standard cable", "Free parking on premises", "Iron", "Wifi", "Hot water", "Self check-in", "Heating", "Air conditioning", "Shampoo", "Long term stays allowed", "Keypad", "Dryer"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | $85.00   | 30             | 1125           | 3                      | 30                     | 1125                   | 1125                   | 28.4                   | 1125                   |                  | t                | 0               | 0               | 11              | 212              | 2024/2/22             | 55                | 3                     | 0                      | 2010/12/29   | 2023/12/30  | 4.7                  | 4.79                   | 4.62                      | 4.85                  | 4.92                        | 4.75                   | 4.77                |         | f                | 1                              | 1                                           | 0                                            | 0                                           | 0.34              |
| 776810  | https://www.airbnb.com/rooms/776810  | 2.02402E+13 | 2024/2/22    | city scrape | Goldies Bohemian Loft                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 15 min walk to downtown Dallas and American Airlines center. Seven minute drive to Lovefield airport , 20 minute drive to DFW                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | https://a0.muscache.com/pictures/9201ddbc-b015-415b-a95a-80a2d3af01c1.jpg                                | 4096626  | https://www.airbnb.com/users/show/4096626  | Eric        | 2012/11/8  | Seattle, WA   | Hi, my name is Eric and I work globally as a remote duty paramedic . I live in the Seattle area . I've been Airbnb'ing since 2012. Please contact me with any questions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | within an hour     | 100%               | 0%                   | f                 | https://a0.muscache.com/im/pictures/user/85293a6b-b373-4ebe-9668-16dc48432b61.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/85293a6b-b373-4ebe-9668-16dc48432b61.jpg?aki_policy=profile_x_medium | Oak Lawn                               | 1                   | 1                         | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 2             |                              | 32.81462  | -96.81586  | Entire loft                       | Entire home/apt | 2            | 1.5       | 1.5 baths      | 1        | 1    | ["Stove", "Kitchen", "Washer", "Essentials", "Hangers", "Coffee maker", "Hair dryer", "Dishes and silverware", "Bathtub", "Extra pillows and blankets", "Refrigerator", "Luggage dropoff allowed", "Carbon monoxide alarm", "Oven", "Smoke alarm", "Backyard", "Dishwasher", "Fire extinguisher", "Free parking on premises", "Bed linens", "Cooking basics", "Patio or balcony", "Microwave", "Cleaning available during stay", "Wifi", "Hot water", "Heating", "Air conditioning", "Shampoo", "BBQ grill", "Long term stays allowed", "Dryer", "Pool"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | $75.00   | 5              | 1125           | 5                      | 5                      | 1125                   | 1125                   | 5                      | 1125                   |                  | t                | 18              | 43              | 49              | 320              | 2024/2/22             | 29                | 0                     | 0                      | 2012/11/16   | 2020/3/26   | 4.9                  | 4.89                   | 4.71                      | 4.89                  | 4.96                        | 5                      | 4.78                |         | f                | 1                              | 1                                           | 0                                            | 0                                           | 0.21              |
| 795703  | https://www.airbnb.com/rooms/795703  | 2.02402E+13 | 2024/2/22    | city scrape | Amazing location walk to Downtown Dallas           | ***** Over 30% Discounts for stays over 30 days or more  ******<br />You can't beat the location of this beautiful penthouse condo. This residential neighborhood is walking distance to Uptown and Downtown Dallas. You can also take Uber to the many local restaurants and bars on Oak Lawn, downtown,  or to McKinney Ave. Please take advantage of a nature walk on the Katy Trail or in Reverchon park. Guest has access to free garage parking, outdoor pool & spa, gas grill, and business center.                                  | Located in Turtle Creek neighborhood steps from Reverchon park and Katy Trail. Blocks from several restaurants including The Common Table, Nick & Sam's Steak House, Katy Trail Ice House, and several along McKinney Ave. Uptown, downtown, and Love Field airport are within minutes of the condo. On a not so hot day you can walk to the AAC and downtown arts district.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | https://a0.muscache.com/pictures/miso/Hosting-795703/original/a7e4959e-6661-4df1-808b-baa66375e284.png   | 4191322  | https://www.airbnb.com/users/show/4191322  | Michelle    | 2012/11/19 | Memphis, TN   | I enjoy living in such a invigorating and upbeat neighborhood. On any day I can take advantage of a occasional stage play,  go to a park and listen to some live music, or sunbathe on a nearby rooftop patio.  My hobbies include traveling, skiing, golfing, boating, and attending social events with  my friends. My life's motto is "live like there's no tomorrow"!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | within an hour     | 100%               | 100%                 | t                 | https://a0.muscache.com/im/users/4191322/profile_pic/1357176516/original.jpg?aki_policy=profile_small      | https://a0.muscache.com/im/users/4191322/profile_pic/1357176516/original.jpg?aki_policy=profile_x_medium      | Oak Lawn                               | 2                   | 4                         | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 14            |                              | 32.80327  | -96.80976  | Entire condo                      | Entire home/apt | 2            | 1         | 1 bath         | 1        | 1    | ["Coffee", "Fire pit", "Kitchen", "Free street parking", "Exercise equipment: elliptical, free weights, stationary bike, treadmill, yoga mat", "Conditioner", "Essentials", "Hangers", "First aid kit", "Baking sheet", "Outdoor dining area", "Hair dryer", "Free washer \u2013 In unit", "Bathtub", "70\" HDTV", "Dishes and silverware", "Shared outdoor pool - available seasonally, open specific hours", "Extra pillows and blankets", "Refrigerator", "Cleaning products", "Coffee maker: drip coffee maker", "Single level home", "Board games", "Central heating", "City skyline view", "Outdoor furniture", "Luggage dropoff allowed", "Carbon monoxide alarm", "Shared hot tub - available seasonally, open specific hours", "Sun loungers", "Central air conditioning", "Hot water kettle", "Smoke alarm", "Books and reading material", "Dishwasher", "Ethernet connection", "Fire extinguisher", "Stainless steel electric stove", "Toaster", "Iron", "Bed linens", "Elevator", "Cooking basics", "Microwave", "Shared outdoor kitchen", "Security cameras on property", "Freezer", "Cleaning available during stay", "Wifi", "Clothing storage: closet", "Hot water", "Wine glasses", "Dining table", "Shampoo", "BBQ grill", "Free residential garage on premises", "Shared gym in building", "Self check-in", "Free dryer \u2013 In unit", "Window guards", "Blender", "Long term stays allowed", "Building staff", "Electric  stainless steel oven", "Shower gel", "Dedicated workspace"]                                                                                                                      | $243.00  | 30             | 365            | 30                     | 30                     | 365                    | 365                    | 30                     | 365                    |                  | t                | 30              | 60              | 90              | 270              | 2024/2/22             | 70                | 0                     | 0                      | 2013/2/1     | 2022/9/25   | 4.84                 | 4.91                   | 4.97                      | 4.91                  | 4.97                        | 4.91                   | 4.75                |         | f                | 1                              | 1                                           | 0                                            | 0                                           | 0.52              |
| 826118  | https://www.airbnb.com/rooms/826118  | 2.02402E+13 | 2024/2/22    | city scrape | Far North Dallas -- Blue Room                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | https://a0.muscache.com/pictures/96902813/2eab882b_original.jpg                                          | 804559   | https://www.airbnb.com/users/show/804559   | Rod         | 2011/7/11  | Dallas, TX    | Bookmaker (both print and electronic) to major associations; editor and photographer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | within a day       | 100%               | 67%                  | f                 | https://a0.muscache.com/im/users/804559/profile_pic/1310595991/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/804559/profile_pic/1310595991/original.jpg?aki_policy=profile_x_medium       | North Central Dallas                   | 2                   | 3                         | ['email', 'phone']               | t                    | f                      |                              | District 12            |                              | 32.98825  | -96.78926  | Private room in home              | Private room    | 2            | 1         | 1 private bath | 1        | 1    | ["Breakfast", "Kitchen", "Cooking basics", "Free street parking", "Washer", "Heating", "Carbon monoxide alarm", "Dryer", "Essentials", "First aid kit", "Wifi", "Smoke alarm", "Hot water", "Dishes and silverware", "Air conditioning", "Fire extinguisher", "TV with standard cable", "Free parking on premises"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | $62.00   | 14             | 180            | 14                     | 14                     | 180                    | 180                    | 14                     | 180                    |                  | t                | 0               | 0               | 19              | 31               | 2024/2/22             | 27                | 5                     | 1                      | 2015/7/4     | 2024/1/31   | 4.85                 | 4.81                   | 4.74                      | 4.85                  | 4.85                        | 4.81                   | 4.78                |         | f                | 2                              | 0                                           | 2                                            | 0                                           | 0.26              |
| 826201  | https://www.airbnb.com/rooms/826201  | 2.02402E+13 | 2024/2/22    | city scrape | Far North Dallas -- Gray Room                      | Quiet first-floor location where you can see your car in the drive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | https://a0.muscache.com/pictures/96716450/7671e1ef_original.jpg                                          | 804559   | https://www.airbnb.com/users/show/804559   | Rod         | 2011/7/11  | Dallas, TX    | Bookmaker (both print and electronic) to major associations; editor and photographer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | within a day       | 100%               | 67%                  | f                 | https://a0.muscache.com/im/users/804559/profile_pic/1310595991/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/804559/profile_pic/1310595991/original.jpg?aki_policy=profile_x_medium       | North Central Dallas                   | 2                   | 3                         | ['email', 'phone']               | t                    | f                      |                              | District 12            |                              | 32.98853  | -96.78903  | Private room in home              | Private room    | 2            | 1         | 1 private bath | 1        | 1    | ["Breakfast", "Rice maker", "Kitchen", "Free street parking", "Washer", "Room-darkening shades", "Essentials", "Hangers", "First aid kit", "Coffee maker", "Bathtub", "Dishes and silverware", "Refrigerator", "Gas stove", "Carbon monoxide alarm", "Oven", "Smoke alarm", "Dishwasher", "Ethernet connection", "Fire extinguisher", "Free parking on premises", "Iron", "Bed linens", "Cooking basics", "Microwave", "Wifi", "Hot water", "Heating", "Air conditioning", "BBQ grill", "Lock on bedroom door", "Indoor fireplace", "Private backyard \u2013 Fully fenced", "Long term stays allowed", "Dryer"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | $54.00   | 30             | 90             | 30                     | 30                     | 90                     | 90                     | 30                     | 90                     |                  | t                | 23              | 53              | 83              | 173              | 2024/2/22             | 32                | 3                     | 0                      | 2013/5/14    | 2024/1/15   | 4.75                 | 4.81                   | 4.66                      | 4.81                  | 4.81                        | 4.78                   | 4.78                |         | f                | 2                              | 0                                           | 2                                            | 0                                           | 0.24              |
| 860248  | https://www.airbnb.com/rooms/860248  | 2.02402E+13 | 2024/2/22    | city scrape | Peaceful Home By the Lake: Safe, Cozy, Quiet       | Traveling nurses, SMU students welcome - 10% discount when you book for 3 months! Close to SMU, Fair Park, the downtown Arts/Design District, 4 blocks to the lake & 1 mile to the beautiful Arboretum. Nice neighborhood, large trees, friendly ambiance. Comfy queen bed, 3 closets, private bathroom. Watch the 72" TV (or TV in your room), enjoy high speed Wifi/work in the courtyard. Restaurants in walking distance. Bus & DART train stations close by. Runners and cyclists love it here.                                        | Wonderful big trees and nice sidewalks throughout the neighborhood, plus two parks within four blocks to visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | https://a0.muscache.com/pictures/99e67741-3728-415c-9943-84ffeeeffa40.jpg                                | 4505460  | https://www.airbnb.com/users/show/4505460  | Judy        | 2012/12/27 | Dallas, TX    | Former high school teacher and tennis coach, I work full time now as a PR person for local neighborhood heroes and small businesses and non-profit agencies. My home is well laid out so everybody has their own space, nobody lives above or below you! Quiet neighborhood, lots of trees. A great place to live! Kind neighbors and so a great place to walk about. White Rock lake is five blocks away.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | within an hour     | 100%               | 94%                  | t                 | https://a0.muscache.com/im/pictures/user/357da3ca-e360-4d73-8d4c-39840e41b019.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/357da3ca-e360-4d73-8d4c-39840e41b019.jpg?aki_policy=profile_x_medium | Old Lake Highlands                     | 3                   | 3                         | ['email', 'phone']               | t                    | f                      | Dallas, Texas, United States | District 9             |                              | 32.85509  | -96.70625  | Private room in home              | Private room    | 2            | 1         | 1 private bath | 1        | 1    | ["Free washer \u2013 In building", "Stove", "Kitchen", "Lake access", "Free street parking", "Essentials", "Hangers", "First aid kit", "Coffee maker", "Baking sheet", "Hair dryer", "Dishes and silverware", "Extra pillows and blankets", "Refrigerator", "Window AC unit", "Outdoor furniture", "Lockbox", "Carbon monoxide alarm", "Central air conditioning", "Oven", "Smoke alarm", "Backyard", "Portable air conditioning", "Dishwasher", "Fire extinguisher", "Free parking on premises", "Iron", "Bed linens", "Cooking basics", "Courtyard view", "Microwave", "Wifi", "Hot water", "Self check-in", "Heating", "Shampoo", "32\" HDTV with standard cable", "Indoor fireplace", "Lock on bedroom door", "Shared patio or balcony", "Dryer", "Dedicated workspace"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | $43.00   | 7              | 365            | 7                      | 7                      | 365                    | 365                    | 7                      | 365                    |                  | t                | 0               | 16              | 46              | 136              | 2024/2/22             | 72                | 6                     | 0                      | 2016/8/29    | 2023/9/30   | 4.83                 | 4.86                   | 4.82                      | 4.93                  | 4.93                        | 4.92                   | 4.83                |         | f                | 3                              | 0                                           | 3                                            | 0                                           | 0.79              |
| 1154424 | https://www.airbnb.com/rooms/1154424 | 2.02402E+13 | 2024/2/22    | city scrape | Uptown, Charming Studio 1B,Fast Free WiFi Parking  | Welcome to the Knox District, a neighborhood that needs to be appreciated. Dallas’s history rich and beloved SAFE, live-work-play destinations.<br /><br />Comfortable 1 bd/1b<br /><br />WALKABLE - The Katy Trail with miles of walking, jogging, and biking pleasure is a few blocks away. There are wonderful places to see and visit.<br /><br />WALKABLE - Plethora of shops, restaurants, bistros, and bars (including an Apple Computer Super Store) are within easy walking distance. Trader Joe's supermarket is two blocks away. | Great Community to Live, Work and Play<br />Located in the trendy Knox Districted area of Uptown Dallas<br />Fabulous Central Location<br />Family Owned and Operated<br />Our Guests have said “we didn’t need our car”<br />THE PICTURES AND REVIEWS TELL IT ALL!!!<br />Lots to do with about 30 restaurants, bistros, and bars within safe, easy walking distance<br />Plethora of shops, boutiques and stores including a Apple Computer Super Store<br />Trader Joe’s Supermarket 2 blocks away<br />Katy Trail, Only three blocks away, it is a 15 mile long walking, jogging and biking trail<br /><br />We are close to Downtown Dallas - the Arts District - Deep Ellum - Fair Park - the Science Center - Perot Science Museum – the West End District – the American Airlines Center -  the Klyde Warren Park which is built over the Woodall Rodgers Freeway - George W. Bush Presidential Center and Library - Lower Greenville with all of its restaurants and nightclubs | https://a0.muscache.com/pictures/aed270ea-765d-412c-b4f2-534670f1ade2.jpg                                | 6063232  | https://www.airbnb.com/users/show/6063232  | Joan        | 2013/4/23  | Dallas, TX    | Hello, I am Joan.  I was born in Czechoslovakia and I have lived in Czechoslovakia, Austria, Canada and now Dallas, TX.  I have traveled extensively in Europe, Canada, Costa Rica and the United States.  My favorite places are Tuscany, Italy; Prague, Czech Republic; Toronto, Canada; San Jose, Costa Rica; and southern California, plus Dallas.  I speak fluent Czech, understand most Slavic languages, and even speak a little German.  I enjoy life, exercise, the coasts and the beach, good dining, theatre, music and travel.  I love my work managing my apartments and caring for my tenants and guests.                                                                                                                                                                                                                                                               | within an hour     | 100%               | 96%                  | f                 | https://a0.muscache.com/im/users/6063232/profile_pic/1368294811/original.jpg?aki_policy=profile_small      | https://a0.muscache.com/im/users/6063232/profile_pic/1368294811/original.jpg?aki_policy=profile_x_medium      | Central Dallas                         | 9                   | 11                        | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 14            |                              | 32.818684 | -96.790154 | Entire rental unit                | Entire home/apt | 2            | 1         | 1 bath         | 0        | 1    | ["Free washer \u2013 In building", "Portable fans", "Kitchen", "Free street parking", "Free dryer \u2013 In building", "Room-darkening shades", "Essentials", "Hangers", "Coffee maker", "Outdoor dining area", "Hair dryer", "Bathtub", "Dishes and silverware", "Extra pillows and blankets", "Single level home", "Outdoor furniture", "Central heating", "Carbon monoxide alarm", "Central air conditioning", "Smoke alarm", "Fire extinguisher", "TV with standard cable", "Free parking on premises", "Clothing storage: closet and dresser", "Mini fridge", "Toaster", "Iron", "Bed linens", "Cooking basics", "Microwave", "Cleaning available during stay", "Wifi", "Hot water", "Wine glasses", "Laundromat nearby", "Dining table", "Shampoo", "Self check-in", "Shared patio or balcony", "Keypad", "Portable heater"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | $89.00   | 3              | 1125           | 3                      | 3                      | 1125                   | 1125                   | 3                      | 1125                   |                  | t                | 0               | 0               | 0               | 215              | 2024/2/22             | 92                | 0                     | 0                      | 2013/6/2     | 2022/7/5    | 4.61                 | 4.7                    | 4.85                      | 4.74                  | 4.62                        | 4.93                   | 4.66                |         | t                | 9                              | 9                                           | 0                                            | 0                                           | 0.7               |
| 1277933 | https://www.airbnb.com/rooms/1277933 | 2.02402E+13 | 2024/2/22    | city scrape | The Santa Fe Suite and Maxfield Parrish Suite      | There are Two Suites - The Maxfield Parrish Suite has a King Size bed and the Santa Fe Suite has a Queen Size bed. For 1 or 2 people to use one Suite it is $65 per night. For an additional 1 or 2 people to use the second Suite is $30 per night. The two suites have a shared master bath.                                                                                                                                                                                                                                              | Very safe and friendly neighborhood to take morning and evening walks in if one so desires.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | https://a0.muscache.com/pictures/19427714/2edb6948_original.jpg                                          | 6904484  | https://www.airbnb.com/users/show/6904484  | C. F. Sandy | 2013/6/13  | Dallas, TX    | We have a warm two story home with two bedrooms and two baths downstairs for our guests. It is always most enjoyable making new friends and providing a pleasant comfortable home for people while they are visiting Dallas. I have traveled extensively through Europe, South America, and the Orient and welcome the stories of enchanting places others have visited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | N/A                | N/A                | N/A                  | f                 | https://a0.muscache.com/im/pictures/user/7b7e8039-60fb-489d-a17c-1b52b9d1f351.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/7b7e8039-60fb-489d-a17c-1b52b9d1f351.jpg?aki_policy=profile_x_medium | North Central Dallas                   | 1                   | 1                         | ['email', 'phone', 'work_email'] | t                    | t                      | Dallas, Texas, United States | District 11            |                              | 32.92449  | -96.79062  | Private room in home              | Private room    | 4            | 1         | 1 shared bath  | 2        | 2    | ["Stove", "Kitchen", "Washer", "Essentials", "Hangers", "Coffee maker", "Hair dryer", "Dishes and silverware", "Extra pillows and blankets", "Refrigerator", "Host greets you", "Single level home", "Oven", "Private living room", "Backyard", "Dishwasher", "Ethernet connection", "TV with standard cable", "Free parking on premises", "Bed linens", "Cooking basics", "Patio or balcony", "Microwave", "Wifi", "Hot water", "Heating", "Air conditioning", "BBQ grill", "EV charger", "Indoor fireplace", "Dryer"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | $65.00   | 1              | 1125           | 1                      | 1                      | 1125                   | 1125                   | 1                      | 1125                   |                  | t                | 22              | 52              | 82              | 357              | 2024/2/22             | 30                | 0                     | 0                      | 2017/4/23    | 2019/11/9   | 4.63                 | 4.7                    | 4.17                      | 4.93                  | 4.93                        | 4.5                    | 4.53                |         | f                | 1                              | 0                                           | 1                                            | 0                                           | 0.36              |
| 1479800 | https://www.airbnb.com/rooms/1479800 | 2.02402E+13 | 2024/2/22    | city scrape | Sunny/MStreet/SMU/Trendy Greenville/Private Bath   | Great location!! 6 min walk to train. 10 min walk to Iyengar Yoga. 8 min to Katy Trail. Walk to: Movies, restaurants, bars, concerts at Granada theatre. Downtown: museums, parks, SMU. Relax: White Rock Lake Park, Dallas Arboretum, Klyde Warren Park.                                                                                                                                                                                                                                                                                   | The best neighborhood and the most desirable, centrally located neighborhood in the city. 6 minutes to the Dart Rail Line. An 8 minute walk to the finest BKS Iyengar Yoga Studio in the city. Close Southern Methodist University and the New Bush Presidential Center. Within walking distance or movies, theatre, comedy, restaurants, shopping and parks. 10 minutes to downtown: there is every kind of art, music, museums, concert halls, entertainment, shopping and delicious restaurants that one could image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | https://a0.muscache.com/pictures/62628813/237228d5_original.jpg                                          | 3809024  | https://www.airbnb.com/users/show/3809024  | Holly       | 2012/10/9  | Paris, France | Photographer who loves to dance.  Widow. Two grown children.  Interested in museums, the arts, dancing, cooking and outdoors. I have been a freelance photographer for 45 years. My daughter is an actress and singer, my son is an independent IOS developer and blogs at : biketoeverything. I travel all the time to see new places, to dance workshops and to visit family and friends.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | within an hour     | 100%               | 92%                  | t                 | https://a0.muscache.com/im/pictures/user/0e6fcf64-6b49-4980-9c77-3ea65164892e.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/0e6fcf64-6b49-4980-9c77-3ea65164892e.jpg?aki_policy=profile_x_medium | Lower Greenville                       | 4                   | 4                         | ['phone', 'work_email']          | t                    | t                      | Dallas, Texas, United States | District 14            |                              | 32.83103  | -96.7638   | Private room in home              | Private room    | 2            | 1         | 1 private bath | 1        | 1    | ["Coffee", "Garden view", "Portable fans", "Kitchen", "Free street parking", "Conditioner", "Essentials", "Hangers", "First aid kit", "Gaggenau stainless steel gas stove", "Coffee maker", "Baking sheet", "Hair dryer", "Outdoor dining area", "Smart lock", "Dishes and silverware", "Extra pillows and blankets", "Refrigerator", "Cleaning products", "Single level home", "Outdoor furniture", "Luggage dropoff allowed", "Barbecue utensils", "Body soap", "Central air conditioning", "Free washer", "Oven", "Smoke alarm", "Hot water kettle", "BBQ grill: gas", "Books and reading material", "Dishwasher", "Beach essentials", "Fire extinguisher", "TV with standard cable", "Free parking on premises", "Clothing storage: closet and dresser", "Toaster", "Private patio or balcony", "Iron", "Bed linens", "Ceiling fan", "Cooking basics", "Piano", "Microwave", "Security cameras on property", "Freezer", "Wifi", "Hot water", "Wine glasses", "Laundromat nearby", "Heating", "Shampoo", "Dining table", "Self check-in", "Bikes", "Lock on bedroom door", "Free dryer \u2013 In unit", "Blender", "Long term stays allowed", "Drying rack for clothing", "Shower gel", "Shared backyard \u2013 Fully fenced"]                                                                                                                                                                                                                                                                                                                                                                                                | $90.00   | 2              | 1125           | 1                      | 2                      | 1125                   | 1125                   | 2                      | 1125                   |                  | t                | 0               | 0               | 12              | 261              | 2024/2/22             | 102               | 1                     | 0                      | 2013/8/24    | 2023/5/15   | 4.93                 | 4.95                   | 4.93                      | 4.93                  | 4.94                        | 4.95                   | 4.8                 |         | f                | 3                              | 0                                           | 3                                            | 0                                           | 0.8               |
| 1507428 | https://www.airbnb.com/rooms/1507428 | 2.02402E+13 | 2024/2/22    | city scrape | Uptown – Studio  #8, Free Fast WiFi Parking Cable  | Welcome to the Knox District, a neighborhood that needs to be appreciated. Dallas’s history rich and beloved SAFE, live-work-play destinations.<br /><br />Comfortable 1 bd/1b<br /><br />WALKABLE - The Katy Trail with miles of walking, jogging, and biking pleasure is a few blocks away. There are wonderful places to see and visit.<br /><br />WALKABLE - Plethora of shops, restaurants, bistros, and bars (including an Apple Computer Super Store) are within easy walking distance. Trader Joe's supermarket is two blocks away. | Great Community to Live, Work and Play<br />Located in the trendy Knox Districted area of Uptown Dallas<br />Fabulous Central Location<br />Family Owned and Operated<br />Our Guests have said “we didn’t need our car”<br />THE PICTURES AND REVIEWS TELL IT ALL!!!<br />Lots to do with about 30 restaurants, bistros, and bars within safe, easy walking distance<br />Plethora of shops, boutiques and stores including a Apple Computer Super Store<br />Trader Joe’s Supermarket 2 blocks away<br />Katy Trail, Only three blocks away, it is a 15 mile long walking, jogging and biking trail<br /><br />We are close to Downtown Dallas - the Arts District - Deep Ellum - Fair Park - the Science Center - Perot Science Museum – the West End District – the American Airlines Center -  the Klyde Warren Park which is built over the Woodall Rodgers Freeway - George W. Bush Presidential Center and Library - Lower Greenville with all of its restaurants and nightclubs | https://a0.muscache.com/pictures/008eb142-bcff-41d8-9ea8-95fbb2913517.jpg                                | 6063232  | https://www.airbnb.com/users/show/6063232  | Joan        | 2013/4/23  | Dallas, TX    | Hello, I am Joan.  I was born in Czechoslovakia and I have lived in Czechoslovakia, Austria, Canada and now Dallas, TX.  I have traveled extensively in Europe, Canada, Costa Rica and the United States.  My favorite places are Tuscany, Italy; Prague, Czech Republic; Toronto, Canada; San Jose, Costa Rica; and southern California, plus Dallas.  I speak fluent Czech, understand most Slavic languages, and even speak a little German.  I enjoy life, exercise, the coasts and the beach, good dining, theatre, music and travel.  I love my work managing my apartments and caring for my tenants and guests.                                                                                                                                                                                                                                                               | within an hour     | 100%               | 96%                  | f                 | https://a0.muscache.com/im/users/6063232/profile_pic/1368294811/original.jpg?aki_policy=profile_small      | https://a0.muscache.com/im/users/6063232/profile_pic/1368294811/original.jpg?aki_policy=profile_x_medium      | Central Dallas                         | 9                   | 11                        | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 14            |                              | 32.81961  | -96.78996  | Entire rental unit                | Entire home/apt | 1            | 1         | 1 bath         | 0        | 1    | ["Free washer \u2013 In building", "Portable fans", "Kitchen", "Free street parking", "Free dryer \u2013 In building", "Essentials", "Hangers", "Outdoor dining area", "Hair dryer", "Dishes and silverware", "Extra pillows and blankets", "Window AC unit", "Coffee maker: drip coffee maker", "Single level home", "Outdoor furniture", "Central heating", "Lockbox", "Luggage dropoff allowed", "Carbon monoxide alarm", "Smoke alarm", "Ethernet connection", "Fire extinguisher", "TV with standard cable", "Clothing storage: closet and dresser", "Mini fridge", "Electric stove", "Toaster", "Iron", "Bed linens", "Cooking basics", "Microwave", "Cleaning available during stay", "Wifi", "Hot water", "Wine glasses", "Self check-in", "Shampoo", "Shared patio or balcony", "Free carport on premises \u2013 1 space", "Long term stays allowed", "Safe"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | $78.00   | 3              | 1125           | 3                      | 3                      | 1125                   | 1125                   | 3                      | 1125                   |                  | t                | 22              | 49              | 79              | 303              | 2024/2/22             | 68                | 2                     | 0                      | 2013/9/13    | 2023/6/19   | 4.63                 | 4.76                   | 4.75                      | 4.96                  | 4.84                        | 4.87                   | 4.58                |         | t                | 9                              | 9                                           | 0                                            | 0                                           | 0.53              |
| 1826550 | https://www.airbnb.com/rooms/1826550 | 2.02402E+13 | 2024/2/22    | city scrape | Private Room in Canton Townhouse                   | Comfortable and private guest room with a queen size bed, desk, couch, TV, attached bathroom and more, located all by itself on the first floor of a 3 story downtown townhome. Enjoy the privacy of staying on your own floor, coming and going as you please using keypad locks and your own personal pass-code while at the same time enjoying all the comforts of home including a kitchen, living/dining area, covered parking, laundry and a rooftop terrace with a downtown view of the Dallas skyline.                              | The townhouse is conveniently located downtown directly across from the Dallas Farmers Market with easy access to the Business District, Deep Ellum, the Arts District, West End, Convention Center and the DART.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | https://a0.muscache.com/pictures/miso/Hosting-1826550/original/b4d0781b-96dc-41e6-8183-4dd0c9f5f292.jpeg | 9557710  | https://www.airbnb.com/users/show/9557710  | Jeff        | 2013/10/21 | Dallas, TX    | Following 15 years tied to a desk, I quit my finance job and decided to take a break from work to go see the world.  I live with my husband Aaron who is a high school Choir Director.  We both share a love of traveling, meeting new people and learning about different places and cultures and for us staying with locals is the only way to travel. During my hiatus from work we are now enjoying the hosting side of Airbnb.  When school is out or on long weekends we will often leave town and rent out our entire home.  When we're in town we rent out our guest room(s).   Collectively, we have visited over 60 countries and nearly all 50 states and are constantly looking for new and exciting places to explore.  We look forward to adding you to our growing list of friends from all over the world whether we are hosting you in our home or visiting yours.   | within an hour     | 100%               | 99%                  | t                 | https://a0.muscache.com/im/pictures/user/333a39fc-cc0d-4e5e-a767-bb8f579d1714.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/333a39fc-cc0d-4e5e-a767-bb8f579d1714.jpg?aki_policy=profile_x_medium | Downtown                               | 3                   | 5                         | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 14            |                              | 32.78112  | -96.79165  | Private room in townhouse         | Private room    | 3            | 1         | 1 private bath | 1        | 1    | ["Sound system with aux", "Coffee", "Portable fans", "Rice maker", "Kitchen", "Free street parking", "Conditioner", "Essentials", "Hangers", "Pack \u2019n play/Travel crib - available upon request", "First aid kit", "Coffee maker", "Baking sheet", "Hair dryer", "Free washer \u2013 In unit", "Outdoor dining area", "Bathtub", "Dishes and silverware", "Extra pillows and blankets", "Refrigerator", "Cleaning products", "Baby safety gates", "Stainless steel gas stove", "Board games", "Outdoor furniture", "City skyline view", "Luggage dropoff allowed", "Carbon monoxide alarm", "Body soap", "Barbecue utensils", "Central air conditioning", "Paid parking lot off premises", "Oven", "Smoke alarm", "Hot water kettle", "BBQ grill: gas", "Books and reading material", "Dishwasher", "Ethernet connection", "Fire extinguisher", "Clothing storage: closet and dresser", "Mini fridge", "Toaster", "Iron", "Bed linens", "Ceiling fan", "Cooking basics", "Piano", "Microwave", "Patio or balcony", "Security cameras on property", "Freezer", "Wifi", "EV charger - level 2", "Hot water", "Wine glasses", "Self check-in", "Heating", "Shampoo", "Dining table", "Lock on bedroom door", "Free dryer \u2013 In unit", "Blender", "Long term stays allowed", "Keypad", "Children\u2019s dinnerware", "42\" HDTV with Amazon Prime Video, Fire TV, Hulu, Netflix, standard cable", "Free residential garage on premises \u2013 1 space", "Shower gel", "Dedicated workspace"]                                                                                                                                | $83.00   | 1              | 28             | 1                      | 1                      | 1125                   | 1125                   | 1                      | 1125                   |                  | t                | 8               | 18              | 31              | 44               | 2024/2/22             | 620               | 48                    | 2                      | 2013/11/21   | 2024/2/4    | 4.94                 | 4.97                   | 4.97                      | 4.98                  | 4.98                        | 4.9                    | 4.92                |         | t                | 3                              | 1                                           | 2                                            | 0                                           | 4.97              |
| 1832427 | https://www.airbnb.com/rooms/1832427 | 2.02402E+13 | 2024/2/23    | city scrape | Beautiful 3BR Canton Townhouse                     | This beautiful 3 story townhouse with downtown views is the ideal stop for both business and leisure travelers. Comes with 3BR, 3.5 Bath, full kitchen, living room, dining room, laundry, garage and spectacular rooftop deck.                                                                                                                                                                                                                                                                                                             | The townhouse is conveniently located downtown directly across from the Dallas Farmers Market with easy access to the Business District, Deep Ellum, the Arts District, West End, Convention Center and the DART.<br /><br />You can literally walk to just about anything you need.  Restaurants, bars, live music venues, shopping, public transportation, etc... D Magazine's top burger, pizza and BBQ joints are within a 10 minute walk.  In addition, the location is just a few blocks from both the central expressway and I-30 allowing easy access to the rest of Dallas if needed.                                                                                                                                                                                                                                                                                                                                                                                           | https://a0.muscache.com/pictures/40732061/f2f87ad9_original.jpg                                          | 9557710  | https://www.airbnb.com/users/show/9557710  | Jeff        | 2013/10/21 | Dallas, TX    | Following 15 years tied to a desk, I quit my finance job and decided to take a break from work to go see the world.  I live with my husband Aaron who is a high school Choir Director.  We both share a love of traveling, meeting new people and learning about different places and cultures and for us staying with locals is the only way to travel. During my hiatus from work we are now enjoying the hosting side of Airbnb.  When school is out or on long weekends we will often leave town and rent out our entire home.  When we're in town we rent out our guest room(s).   Collectively, we have visited over 60 countries and nearly all 50 states and are constantly looking for new and exciting places to explore.  We look forward to adding you to our growing list of friends from all over the world whether we are hosting you in our home or visiting yours.   | within an hour     | 100%               | 99%                  | t                 | https://a0.muscache.com/im/pictures/user/333a39fc-cc0d-4e5e-a767-bb8f579d1714.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/333a39fc-cc0d-4e5e-a767-bb8f579d1714.jpg?aki_policy=profile_x_medium | Downtown                               | 3                   | 5                         | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 2             |                              | 32.77805  | -96.79362  | Entire townhouse                  | Entire home/apt | 8            | 3.5       | 3.5 baths      | 3        | 3    | ["Coffee", "Rice maker", "Stove", "Kitchen", "Free street parking", "Washer", "Essentials", "Hangers", "Pantene conditioner", "First aid kit", "Coffee maker", "Baking sheet", "Hair dryer", "Bathtub", "Dishes and silverware", "Extra pillows and blankets", "Refrigerator", "Cleaning products", "Board games", "Outdoor furniture", "City skyline view", "Carbon monoxide alarm", "Body soap", "Barbecue utensils", "Oven", "Smoke alarm", "Hot water kettle", "Dishwasher", "Fire extinguisher", "TV with standard cable", "Free parking on premises", "Mini fridge", "Toaster", "Private patio or balcony", "Iron", "Bed linens", "Ceiling fan", "Cooking basics", "Microwave", "Security cameras on property", "Freezer", "Wifi", "EV charger - level 2", "Hot water", "Wine glasses", "Self check-in", "Air conditioning", "Heating", "Dining table", "BBQ grill", "Indoor fireplace", "Blender", "Long term stays allowed", "Keypad", "Children\u2019s dinnerware", "Dryer", "Pantene shampoo", "Pack \u2019n play/Travel crib", "Shower gel", "Dedicated workspace"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | $408.00  | 2              | 28             | 1                      | 2                      | 28                     | 28                     | 2                      | 28                     |                  | t                | 0               | 0               | 0               | 0                | 2024/2/23             | 167               | 16                    | 0                      | 2014/2/17    | 2023/12/30  | 4.99                 | 4.99                   | 4.94                      | 4.99                  | 5                           | 4.95                   | 4.96                |         | f                | 3                              | 1                                           | 2                                            | 0                                           | 1.37              |
| 1856710 | https://www.airbnb.com/rooms/1856710 | 2.02402E+13 | 2024/2/22    | city scrape | Sunny Bedroom/MStreet/SMU/Trendy Greenville Ave    | Perfect location for business or pleasure. Stay and work downtown. Play and bike the Katy Trail, walk to movies, restaurants, bars, concerts and theatre. Visit museums, parks, SMU, Bush Center. Relax at White Rock Lake Park, the Dallas Arboretum and Klyde Warren Park or in my back yard.                                                                                                                                                                                                                                             | The best neighborhood and the most desirable, centrally located neighborhood in the city. 6 minutes to the Dart Rail Line. An 8 minute walk to the finest BKS Iyengar Yoga Studio in the city. Close Southern Methodist University and the New Bush Presidential Center. Within walking distance or movies, theatre, comedy, restaurants, shopping and parks. 10 minutes to downtown: there is every kind of art, music, museums, concert halls, entertainment, shopping and delicious restaurants that one could image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | https://a0.muscache.com/pictures/520cee29-c12b-467f-8285-b2a7fe4abdee.jpg                                | 3809024  | https://www.airbnb.com/users/show/3809024  | Holly       | 2012/10/9  | Paris, France | Photographer who loves to dance.  Widow. Two grown children.  Interested in museums, the arts, dancing, cooking and outdoors. I have been a freelance photographer for 45 years. My daughter is an actress and singer, my son is an independent IOS developer and blogs at : biketoeverything. I travel all the time to see new places, to dance workshops and to visit family and friends.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | within an hour     | 100%               | 92%                  | t                 | https://a0.muscache.com/im/pictures/user/0e6fcf64-6b49-4980-9c77-3ea65164892e.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/0e6fcf64-6b49-4980-9c77-3ea65164892e.jpg?aki_policy=profile_x_medium | Lower Greenville                       | 4                   | 4                         | ['phone', 'work_email']          | t                    | t                      | Dallas, Texas, United States | District 14            |                              | 32.83531  | -96.77386  | Private room in home              | Private room    | 1            | 1         | 1 shared bath  | 1        | 1    | ["Coffee", "Free washer \u2013 In building", "Garden view", "Portable fans", "Kitchen", "Free street parking", "Free dryer \u2013 In building", "Room-darkening shades", "Conditioner", "Essentials", "Hangers", "First aid kit", "Coffee maker", "Baking sheet", "Smart lock", "Hair dryer", "Bathtub", "Dishes and silverware", "Extra pillows and blankets", "Refrigerator", "Cleaning products", "Single level home", "Board games", "Gas stove", "Outdoor furniture", "Luggage dropoff allowed", "Barbecue utensils", "Body soap", "Central air conditioning", "Oven", "Smoke alarm", "Hot water kettle", "BBQ grill: gas", "Books and reading material", "Dishwasher", "Fire extinguisher", "TV with standard cable", "Free parking on premises", "Clothing storage: closet and dresser", "Toaster", "Private patio or balcony", "Iron", "Bed linens", "Ceiling fan", "Cooking basics", "Piano", "Microwave", "Security cameras on property", "Freezer", "Wifi", "Hot water", "Wine glasses", "Self check-in", "Heating", "Shampoo", "Dining table", "Bikes", "Lock on bedroom door", "Private backyard \u2013 Fully fenced", "Blender", "Long term stays allowed", "Drying rack for clothing", "Shower gel", "Safe"]                                                                                                                                                                                                                                                                                                                                                                                                      | $95.00   | 2              | 1125           | 2                      | 2                      | 1125                   | 1125                   | 2                      | 1125                   |                  | t                | 0               | 0               | 0               | 235              | 2024/2/22             | 44                | 6                     | 0                      | 2013/11/20   | 2024/1/6    | 4.8                  | 4.95                   | 4.98                      | 4.98                  | 4.95                        | 5                      | 4.84                |         | f                | 3                              | 0                                           | 3                                            | 0                                           | 0.35              |
| 2082487 | https://www.airbnb.com/rooms/2082487 | 2.02402E+13 | 2024/2/22    | city scrape | Uptown Spacious Studio #2, Free Fast WiFi Parking  | Welcome to the Knox District, a neighborhood that needs to be appreciated. Dallas’s history rich and beloved SAFE, live-work-play destinations.<br /><br />Comfortable 1 bd/1b<br /><br />WALKABLE - The Katy Trail with miles of walking, jogging, and biking pleasure is a few blocks away. There are wonderful places to see and visit.<br /><br />WALKABLE - Plethora of shops, restaurants, bistros, and bars (including an Apple Computer Super Store) are within easy walking distance. Trader Joe's supermarket is two blocks away. | Great Community to Live, Work and Play<br />Located in the trendy Knox Districted area of Uptown Dallas<br />Fabulous Central Location<br />Family Owned and Operated<br />Our Guests have said “we didn’t need our car”<br />THE PICTURES AND REVIEWS TELL IT ALL!!!<br />Lots to do with about 30 restaurants, bistros, and bars within safe, easy walking distance<br />Plethora of shops, boutiques and stores including a Apple Computer Super Store<br />Trader Joe’s Supermarket 2 blocks away<br />Katy Trail, Only three blocks away, it is a 15 mile long walking, jogging and biking trail<br /><br />We are close to Downtown Dallas - the Arts District - Deep Ellum - Fair Park - the Science Center - Perot Science Museum – the West End District – the American Airlines Center -  the Klyde Warren Park which is built over the Woodall Rodgers Freeway - George W. Bush Presidential Center and Library - Lower Greenville with all of its restaurants and nightclubs | https://a0.muscache.com/pictures/miso/Hosting-2082487/original/6486d146-ed44-4139-b43a-e5f42dcb51af.jpeg | 6063232  | https://www.airbnb.com/users/show/6063232  | Joan        | 2013/4/23  | Dallas, TX    | Hello, I am Joan.  I was born in Czechoslovakia and I have lived in Czechoslovakia, Austria, Canada and now Dallas, TX.  I have traveled extensively in Europe, Canada, Costa Rica and the United States.  My favorite places are Tuscany, Italy; Prague, Czech Republic; Toronto, Canada; San Jose, Costa Rica; and southern California, plus Dallas.  I speak fluent Czech, understand most Slavic languages, and even speak a little German.  I enjoy life, exercise, the coasts and the beach, good dining, theatre, music and travel.  I love my work managing my apartments and caring for my tenants and guests.                                                                                                                                                                                                                                                               | within an hour     | 100%               | 96%                  | f                 | https://a0.muscache.com/im/users/6063232/profile_pic/1368294811/original.jpg?aki_policy=profile_small      | https://a0.muscache.com/im/users/6063232/profile_pic/1368294811/original.jpg?aki_policy=profile_x_medium      | Central Dallas                         | 9                   | 11                        | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 14            |                              | 32.820461 | -96.789574 | Entire rental unit                | Entire home/apt | 3            | 1         | 1 bath         | 0        | 1    | ["Kitchen", "Free street parking", "Washer", "Free dryer \u2013 In building", "Room-darkening shades", "Essentials", "Hangers", "Coffee maker", "Outdoor dining area", "Hair dryer", "Bathtub", "Dishes and silverware", "Extra pillows and blankets", "Refrigerator", "Free driveway parking on premises \u2013 1 space", "Single level home", "Outdoor furniture", "Central heating", "Lockbox", "Luggage dropoff allowed", "Carbon monoxide alarm", "Central air conditioning", "Oven", "Smoke alarm", "Ethernet connection", "Fire extinguisher", "TV with standard cable", "Toaster", "Clothing storage: walk-in closet and dresser", "Iron", "Bed linens", "Ceiling fan", "Cooking basics", "Microwave", "Freezer", "Cleaning available during stay", "Wifi", "Hot water", "Wine glasses", "Self check-in", "Dining table", "Shampoo", "Shared patio or balcony", "Long term stays allowed", "Security cameras on property"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | $89.00   | 3              | 1125           | 3                      | 3                      | 1125                   | 1125                   | 3                      | 1125                   |                  | t                | 0               | 0               | 15              | 239              | 2024/2/22             | 61                | 1                     | 0                      | 2013/12/21   | 2023/11/4   | 4.56                 | 4.56                   | 4.7                       | 4.9                   | 4.75                        | 4.9                    | 4.48                |         | t                | 9                              | 9                                           | 0                                            | 0                                           | 0.49              |
| 2169463 | https://www.airbnb.com/rooms/2169463 | 2.02402E+13 | 2024/2/22    | city scrape | The French House                                   | Single residence in quiet neighborhood backing up to creek. Ideally located for DFW & Love Field airports, SMU, Downtown, & major arteries. Private upstairs rooms are  spacious, each with a double-sink bathroom. Flexible (retired) owners.                                                                                                                                                                                                                                                                                              | Super quiet & residential. There are lovely walks & runs for our guests (& doggie). The creek & wildlife is special. Green everywhere. Well tended yards, sidewalks, too.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | https://a0.muscache.com/pictures/29491309/f3ee450d_original.jpg                                          | 11067935 | https://www.airbnb.com/users/show/11067935 | Thierry     | 2014/1/6   |               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | N/A                | N/A                | 0%                   | f                 | https://a0.muscache.com/im/users/11067935/profile_pic/1389222750/original.jpg?aki_policy=profile_small     | https://a0.muscache.com/im/users/11067935/profile_pic/1389222750/original.jpg?aki_policy=profile_x_medium     | Glen Meadow/Westhollow/Northhaven Park | 1                   | 1                         | ['email', 'phone']               | t                    | f                      | Dallas, Texas, United States | District 13            |                              | 32.90005  | -96.84828  | Private room in bed and breakfast | Private room    | 4            | 2         | 2 baths        | 1        | 3    | ["Pets allowed", "Heating", "Wifi", "Air conditioning", "TV with standard cable", "Free parking on premises"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | $85.00   | 1              | 1125           | 1                      | 1                      | 1125                   | 1125                   | 1                      | 1125                   |                  | t                | 23              | 53              | 83              | 358              | 2024/2/22             | 42                | 0                     | 0                      | 2014/4/6     | 2022/4/3    | 4.79                 | 4.83                   | 4.64                      | 4.83                  | 4.83                        | 4.93                   | 4.83                |         | f                | 1                              | 0                                           | 1                                            | 0                                           | 0.35              |
| 2537593 | https://www.airbnb.com/rooms/2537593 | 2.02402E+13 | 2024/2/22    | city scrape | Victor's Old East Dallas Bedroom                   | A when my kids grew up and left to start their own lives I wanted to downsize and go be a dorm or Fraternity house mother and bank all the money that I did not bank as a single mom.....  Well here I am basically doing just that!  <br /> I generally I have young professionals or students in their last year doing an internship stay with me, so my place has a peaceful, serious and not the Animal house frat house vibe.  The dogs are great company but so are the other guests!                                                 | This neighborhood is quiet and peaceful. Birds will sing you awake in the morning.  Within walking distance are parks, historic neighborhoods and the wonderful Garden Cafe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | https://a0.muscache.com/pictures/miso/Hosting-2537593/original/c40851cb-5bd6-4267-a19e-fa712495d065.jpeg | 12993311 | https://www.airbnb.com/users/show/12993311 | Jan         | 2014/3/10  | Dallas, TX    | I live in this 5 bedroom house with my dogs Daisy, Jacques and Cora in old East Dallas.. 2.2 miles  to the cotton bowl and 2.7 to downtown Dallas.    I work at SMU and keep myself busy volunteering at the Dallas Museum of Art, with friends and book clubs but I love my quite down time at home, what little of it I have.  I love to garden, walk my dogs on the Santa Fe Trail 2 blocks from the house, and visit with a cup of tea or glass of wine.                                                                                                                                                                                                                                                                                                                                                                                                                          | within an hour     | 100%               | 100%                 | f                 | https://a0.muscache.com/im/pictures/user/e5998032-f0c3-42a5-a500-5a17ba9324a0.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/e5998032-f0c3-42a5-a500-5a17ba9324a0.jpg?aki_policy=profile_x_medium | Central Dallas                         | 4                   | 4                         | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 2             |                              | 32.7991   | -96.75911  | Private room in home              | Private room    | 1            | 1         | 1 shared bath  | 1        | 1    | ["Free washer \u2013 In building", "36\" HDTV with Netflix, premium cable, Roku", "Kitchen", "Free street parking", "Free dryer \u2013 In building", "Essentials", "Hangers", "Coffee maker", "Baking sheet", "Dishes and silverware", "Refrigerator", "Host greets you", "Board games", "Central air conditioning", "Oven", "Smoke alarm", "Free parking on premises", "Electric stove", "Iron", "Bed linens", "Cooking basics", "Microwave", "Wifi", "Hot water", "Heating", "Shared patio or balcony", "Private backyard \u2013 Fully fenced", "Security cameras on property", "Dedicated workspace"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | $55.00   | 5              | 1125           | 5                      | 5                      | 1125                   | 1125                   | 5                      | 1125                   |                  | t                | 30              | 60              | 90              | 365              | 2024/2/22             | 56                | 6                     | 1                      | 2014/4/5     | 2024/2/18   | 4.86                 | 4.89                   | 4.77                      | 5                     | 4.91                        | 4.62                   | 4.8                 |         | f                | 4                              | 0                                           | 4                                            | 0                                           | 0.47              |
| 2707172 | https://www.airbnb.com/rooms/2707172 | 2.02402E+13 | 2024/2/22    | city scrape | Queen, Walk in Shower-TV-- Internet                | Spacious upstairs bedroom.  Private bath, breakfast, tea and coffee.  Upstairs lounge/office with 55" wall mount TV.  Wireless Internet.  Off street parking or garage.  Exercise bike, Ping Pong, free weights.   Shopping & exclusive restaurants nearby                                                                                                                                                                                                                                                                                  | Quiet, beautiful neighborhood with manicured lawns.  Great for walking, banks, shops and restaurants nearby.  Minutes to Dallas North and George Bush Tollways.  25 minutes to DFW airport and 20 minutes to Love Field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | https://a0.muscache.com/pictures/38544048/31928731_original.jpg                                          | 12321313 | https://www.airbnb.com/users/show/12321313 | Judith      | 2014/2/17  | Dallas, TX    | Professional woman with elegant two-story house in beautiful, quiet and safe neighborhood.  Two to five minutes to Dallas North Tollway or George Bush Tollway to all major highways in DFW Metroplex. Love to provide comfort for guests, including healthy, delicious food.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | within an hour     | 100%               | 100%                 | f                 | https://a0.muscache.com/im/users/12321313/profile_pic/1396464461/original.jpg?aki_policy=profile_small     | https://a0.muscache.com/im/users/12321313/profile_pic/1396464461/original.jpg?aki_policy=profile_x_medium     | Bent Tree                              | 3                   | 3                         | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 12            |                              | 32.99264  | -96.83711  | Private room in home              | Private room    | 2            | 1         | 1 private bath | 1        | 1    | ["Exercise equipment", "Indoor fireplace", "Breakfast", "Gym", "Washer", "Heating", "Carbon monoxide alarm", "Dryer", "Essentials", "First aid kit", "Smoke alarm", "Fast wifi \u2013 55 Mbps", "Hair dryer", "Hot water", "Backyard", "Air conditioning", "Shampoo", "Fire extinguisher", "TV with standard cable", "Free parking on premises"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | $78.00   | 1              | 1125           | 1                      | 1                      | 1125                   | 1125                   | 1                      | 1125                   |                  | t                | 29              | 59              | 89              | 364              | 2024/2/22             | 16                | 2                     | 0                      | 2015/7/17    | 2023/11/17  | 4.5                  | 4.56                   | 4.75                      | 4.53                  | 4.38                        | 4.53                   | 4.33                |         | f                | 2                              | 0                                           | 2                                            | 0                                           | 0.15              |
| 2745099 | https://www.airbnb.com/rooms/2745099 | 2.02402E+13 | 2024/2/22    | city scrape | Dallas: Private 2-Story Loft-6-Miles from Downtown | This cozy residence is nestled in a secure & tranquil gated neighborhood, just 5.9 miles East of Dallas' bustling downtown, conveniently accessible via Interstate 30. It's near the enchanting Dallas Arboretum, Botanical Gardens, & the serene White Rock Lake.<br /><br />Guests will appreciate the home's warm ambiance, complemented with a well-equipped kitchen & private areas. Ideal for car travel with garage & driveway parking. For those preferring public transport, a bus stop is within a 10-minute walk.                | -5.9 miles East of downtown Dallas.<br />-Safe & Quiet Gated community. <br />-Professional neighbors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | https://a0.muscache.com/pictures/1f7c5693-3dce-454c-ac40-28429340ccee.jpg                                | 14042475 | https://www.airbnb.com/users/show/14042475 | Mina        | 2014/4/8   | Pearland, TX  | Our home is your home. We will do our best to ensure that your stay is as pleasant as possible.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | within an hour     | 100%               | 100%                 | f                 | https://a0.muscache.com/im/pictures/user/a953f888-1de5-49be-b95b-66578e65bb35.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/a953f888-1de5-49be-b95b-66578e65bb35.jpg?aki_policy=profile_x_medium | Southeast Dallas                       | 4                   | 8                         | ['email', 'phone', 'work_email'] | t                    | t                      | Dallas, Texas, United States | District 7             |                              | 32.78619  | -96.71823  | Private room in home              | Private room    | 4            | 3         | 3 baths        | 2        | 2    | ["Coffee", "Free washer \u2013 In building", "Kitchen", "Free dryer \u2013 In building", "Room-darkening shades", "Conditioner", "Essentials", "Hangers", "Pack \u2019n play/Travel crib - available upon request", "First aid kit", "Coffee maker", "Baking sheet", "Hair dryer", "Outdoor dining area", "Smart lock", "Bathtub", "Dishes and silverware", "Extra pillows and blankets", "Refrigerator", "Cleaning products", "Sound system with Bluetooth and aux", "Board games", "Outdoor furniture", "Luggage dropoff allowed", "Carbon monoxide alarm", "Body soap", "Barbecue utensils", "Central air conditioning", "Hammock", "Hot water kettle", "Smoke alarm", "Private living room", "Movie theater", "Books and reading material", "Dishwasher", "Ethernet connection", "Fire extinguisher", "Exercise equipment: free weights, treadmill", "Mini fridge", "Stainless steel electric stove", "Toaster", "Clothing storage: walk-in closet and dresser", "55\" HDTV with Amazon Prime Video, Netflix", "Iron", "Bed linens", "Ceiling fan", "Cooking basics", "Patio or balcony", "Indoor fireplace: electric", "Microwave", "Theme room", "Freezer", "Wifi", "Hot water", "Wine glasses", "Self check-in", "Heating", "Shampoo", "Dining table", "BBQ grill", "Shared gym in building", "Lock on bedroom door", "Outlet covers", "Shared backyard \u2013 Fully fenced", "Blender", "Long term stays allowed", "Ping pong table", "Free residential garage on premises \u2013 1 space", "Mosquito net", "Stainless steel oven", "Security cameras on property", "Game console: Nintendo Wii", "Dedicated workspace"] | $40.00   | 31             | 1025           | 31                     | 31                     | 1025                   | 1025                   | 31                     | 1025                   |                  | t                | 0               | 0               | 5               | 210              | 2024/2/22             | 30                | 0                     | 0                      | 2014/8/31    | 2020/3/31   | 4.93                 | 4.97                   | 4.9                       | 5                     | 4.97                        | 4.87                   | 4.97                |         | f                | 4                              | 0                                           | 4                                            | 0                                           | 0.26              |
| 2762537 | https://www.airbnb.com/rooms/2762537 | 2.02402E+13 | 2024/2/22    | city scrape | Safe Uptown Studio 7A Free Fast WIFI Private Entry | Welcome to the Knox District, a neighborhood that needs to be appreciated. Dallas’s history rich and beloved SAFE, live-work-play destinations.<br /><br />Comfortable 1 bd/1b<br /><br />WALKABLE - The Katy Trail with miles of walking, jogging, and biking pleasure is a few blocks away. There are wonderful places to see and visit.<br /><br />WALKABLE - Plethora of shops, restaurants, bistros, and bars (including an Apple Computer Super Store) are within easy walking distance. Trader Joe's supermarket is two blocks away. | Great Community to Live, Work and Play<br />Located in the trendy Knox Districted area of Uptown Dallas<br />Fabulous Central Location<br />Family Owned and Operated<br />Our Guests have said “we didn’t need our car”<br />THE PICTURES AND REVIEWS TELL IT ALL!!!<br />Lots to do with about 30 restaurants, bistros, and bars within safe, easy walking distance<br />Plethora of shops, boutiques and stores including a Apple Computer Super Store<br />Trader Joe’s Supermarket 2 blocks away<br />Katy Trail, Only three blocks away, it is a 15 mile long walking, jogging and biking trail<br /><br />We are close to Downtown Dallas - the Arts District - Deep Ellum - Fair Park - the Science Center - Perot Science Museum – the West End District – the American Airlines Center -  the Klyde Warren Park which is built over the Woodall Rodgers Freeway - George W. Bush Presidential Center and Library - Lower Greenville with all of its restaurants and nightclubs | https://a0.muscache.com/pictures/ddc494f2-90ad-4b25-b10b-25c6c622c814.jpg                                | 6063232  | https://www.airbnb.com/users/show/6063232  | Joan        | 2013/4/23  | Dallas, TX    | Hello, I am Joan.  I was born in Czechoslovakia and I have lived in Czechoslovakia, Austria, Canada and now Dallas, TX.  I have traveled extensively in Europe, Canada, Costa Rica and the United States.  My favorite places are Tuscany, Italy; Prague, Czech Republic; Toronto, Canada; San Jose, Costa Rica; and southern California, plus Dallas.  I speak fluent Czech, understand most Slavic languages, and even speak a little German.  I enjoy life, exercise, the coasts and the beach, good dining, theatre, music and travel.  I love my work managing my apartments and caring for my tenants and guests.                                                                                                                                                                                                                                                               | within an hour     | 100%               | 96%                  | f                 | https://a0.muscache.com/im/users/6063232/profile_pic/1368294811/original.jpg?aki_policy=profile_small      | https://a0.muscache.com/im/users/6063232/profile_pic/1368294811/original.jpg?aki_policy=profile_x_medium      | Central Dallas                         | 9                   | 11                        | ['email', 'phone']               | t                    | t                      | Dallas, Texas, United States | District 14            |                              | 32.81821  | -96.78901  | Entire rental unit                | Entire home/apt | 2            | 1         | 1 bath         | 0        | 1    | ["Portable fans", "Kitchen", "Free street parking", "Washer", "Free dryer \u2013 In building", "Room-darkening shades", "Essentials", "Hangers", "Outdoor dining area", "Hair dryer", "Bathtub", "Dishes and silverware", "Extra pillows and blankets", "Free driveway parking on premises \u2013 1 space", "Window AC unit", "Coffee maker: drip coffee maker", "Outdoor furniture", "Central heating", "Luggage dropoff allowed", "Carbon monoxide alarm", "Central air conditioning", "Smoke alarm", "Ethernet connection", "Fire extinguisher", "TV with standard cable", "Clothing storage: closet and dresser", "Mini fridge", "Toaster", "Iron", "Bed linens", "Cooking basics", "Microwave", "Cleaning available during stay", "Wifi", "Hot water", "Wine glasses", "Laundromat nearby", "Dining table", "Shampoo", "Self check-in", "Shared patio or balcony", "Long term stays allowed", "Keypad", "Portable heater", "Security cameras on property"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | $89.00   | 3              | 1125           | 3                      | 3                      | 1125                   | 1125                   | 3                      | 1125                   |                  | t                | 0               | 0               | 0               | 184              | 2024/2/22             | 81                | 8                     | 0                      | 2014/5/10    | 2023/12/29  | 4.72                 | 4.74                   | 4.84                      | 4.84                  | 4.81                        | 4.94                   | 4.75                |         | t                | 9                              | 9                                           | 0                                            | 0                                           | 0.68              |

</div>

### Problems present in the data.
Upon observing the original data, several issues necessitated attention before import
1. Some descriptions contained HTML tags like `<br />`, which could disrupt text processing and data analysis. So I remove all of these HTML tags, in order to make the description more readable.
`````
Example: "Close to downtown and Uptown.  Fast and convenient to highway, grocery shops, dinner, clubbing and much more. Very modern home.<br /><br />Pets welcomed with approval and additional fee $100 per pet."
`````
I use the following python code to remove it
```python
def clean_html_tags(text):
    return re.sub(r'<[^>]+>', '', text)
```
2. Some numeric fields such as price included currency symbols and commas, making them unsuitable for numerical operations. I convert then to a float type. In this case, we can make comparison on the price.
`````
Example: "$80"
`````
I use the following python code to change it
```python
def clean_price(price):
    return float(re.sub(r'[$,]', '', price))
```

3. The amenities were listed in a single string, enclosed within square brackets and separated by commas, rather than as an array of strings. I transform it into a list of amenities. In this case, it could have a better structure and easy to categorize.
`````
Example: "["Kitchen", "Gym", "Washer", "Essentials", "Hangers", "Hair dryer", "Dishes and silverware", "Pets allowed", "Carbon monoxide alarm", "Smoke alarm", "Shared pool", "Fire extinguisher", "TV with standard cable", "Free parking on premises", "Iron", "Wifi", "Hot water", "Self check-in", "Heating", "Air conditioning", "Shampoo", "Long term stays allowed", "Keypad", "Dryer"]"
`````
I use the following python code to change it
```python
def clean_amenities(amenities):
    amenities = amenities.strip('[]').split(', ')
    amenities = [amenity.strip('"') for amenity in amenities]
    return amenities
```


## Analysis
### Query 1: Show exactly two documents from the listings collection in any order
Description: This query retrieves two documents from the collection, and the order is not specified.
```python
db.listings_clean.find().limit(2)
```
The result shown (up to first three):
`````
{
  _id: ObjectId('6610d6366bce64540e9f1e96'),
  id: 61878,
  listing_url: 'https://www.airbnb.com/rooms/61878',
  scrape_id: {
    $numberLong: '20240222071419'
  },
  last_scraped: {
    $date: '2024-02-22T00:00:00.000Z'
  },
  source: 'city scrape',
  name: 'MODERN LIVING AND FURNISHINGS',
  description: 'Close to downtown and Uptown.  Fast and convenient to highway, grocery shops, dinner, clubbing and much more. Very modern home.<br /><br />Pets welcomed with approval and additional fee $100 per pet.',
  neighborhood_overview: 'Enjoy the heart of Dallas right out your door step.  Cedar Springs offers a eclectic night life as well as great restaurants.  Or take a minute drive/Uber to Uptown for shopping.',
  picture_url: 'https://a0.muscache.com/pictures/c4d9625e-bcc5-4790-b699-3b1acb0a2b3d.jpg',
  host_id: 300211,
  host_url: 'https://www.airbnb.com/users/show/300211',
  host_name: 'Sasha',
  host_since: {
    $date: '2010-11-26T00:00:00.000Z'
  },
  host_location: 'Roanoke, TX',
  host_about: '"Love is Love" :)\r\nI''m originally from Florida, but call Texas home.  Things I can''t live without are coffee, family & friends, my dog, traveling and love. \r\n\r\nWhen I travel, I love having the comforts of home all while enjoying a new city. This was my thought when I wanted my home to a part of AirBNB. You will enjoy all the comforts of a home . . . Who doesn''t like a clean, modern apartment all to themselves? All in the heart of Dallas. Come visit and stay awhile . . . You will love it!',
  host_response_time: 'within an hour',
  host_response_rate: '100%',
  host_acceptance_rate: '100%',
  host_is_superhost: false,
  host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/5f63d226-6de3-4b43-a863-64b8a9ff8fa2.jpg?aki_policy=profile_small',
  host_picture_url: 'https://a0.muscache.com/im/pictures/user/5f63d226-6de3-4b43-a863-64b8a9ff8fa2.jpg?aki_policy=profile_x_medium',
  host_neighbourhood: 'Oak Lawn',
  host_listings_count: 2,
  host_total_listings_count: 3,
  host_verifications: '[''email'', ''phone'']',
  host_has_profile_pic: true,
  host_identity_verified: true,
  neighbourhood: 'Dallas, Texas, United States',
  neighbourhood_cleansed: 'District 2',
  latitude: 32.8169,
  longitude: -96.82018,
  property_type: 'Entire condo',
  room_type: 'Entire home/apt',
  accommodates: 3,
  bathrooms: 1,
  bathrooms_text: '1 bath',
  bedrooms: 1,
  beds: 2,
  amenities: [
    'Kitchen',
    'Gym',
    'Washer',
    'Essentials',
    'Hangers',
    'Hair dryer',
    'Dishes and silverware',
    'Pets allowed',
    'Carbon monoxide alarm',
    'Smoke alarm',
    'Shared pool',
    'Fire extinguisher',
    'TV with standard cable',
    'Free parking on premises',
    'Iron',
    'Wifi',
    'Hot water',
    'Self check-in',
    'Heating',
    'Air conditioning',
    'Shampoo',
    'Long term stays allowed',
    'Keypad',
    'Dryer'
  ],
  price: '$85.00',
  minimum_nights: 30,
  maximum_nights: 1125,
  minimum_minimum_nights: 3,
  maximum_minimum_nights: 30,
  minimum_maximum_nights: 1125,
  maximum_maximum_nights: 1125,
  minimum_nights_avg_ntm: 28.4,
  maximum_nights_avg_ntm: 1125,
  has_availability: true,
  availability_30: 0,
  availability_60: 0,
  availability_90: 11,
  availability_365: 212,
  calendar_last_scraped: {
    $date: '2024-02-22T00:00:00.000Z'
  },
  number_of_reviews: 55,
  number_of_reviews_ltm: 3,
  number_of_reviews_l30d: 0,
  first_review: {
    $date: '2010-12-29T00:00:00.000Z'
  },
  last_review: {
    $date: '2023-12-30T00:00:00.000Z'
  },
  review_scores_rating: 4.7,
  review_scores_accuracy: 4.79,
  review_scores_cleanliness: 4.62,
  review_scores_checkin: 4.85,
  review_scores_communication: 4.92,
  review_scores_location: 4.75,
  review_scores_value: 4.77,
  instant_bookable: false,
  calculated_host_listings_count: 1,
  calculated_host_listings_count_entire_homes: 1,
  calculated_host_listings_count_private_rooms: 0,
  calculated_host_listings_count_shared_rooms: 0,
  reviews_per_month: 0.34
}
{
  _id: ObjectId('6610d6366bce64540e9f1e97'),
  id: 776810,
  listing_url: 'https://www.airbnb.com/rooms/776810',
  scrape_id: {
    $numberLong: '20240222071419'
  },
  last_scraped: {
    $date: '2024-02-22T00:00:00.000Z'
  },
  source: 'city scrape',
  name: 'Goldies Bohemian Loft',
  neighborhood_overview: '15 min walk to downtown Dallas and American Airlines center. Seven minute drive to Lovefield airport , 20 minute drive to DFW',
  picture_url: 'https://a0.muscache.com/pictures/9201ddbc-b015-415b-a95a-80a2d3af01c1.jpg',
  host_id: 4096626,
  host_url: 'https://www.airbnb.com/users/show/4096626',
  host_name: 'Eric',
  host_since: {
    $date: '2012-11-08T00:00:00.000Z'
  },
  host_location: 'Seattle, WA',
  host_about: 'Hi, my name is Eric and I work globally as a remote duty paramedic . I live in the Seattle area . I''ve been Airbnb''ing since 2012. Please contact me with any questions.',
  host_response_time: 'within an hour',
  host_response_rate: '100%',
  host_acceptance_rate: '0%',
  host_is_superhost: false,
  host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/85293a6b-b373-4ebe-9668-16dc48432b61.jpg?aki_policy=profile_small',
  host_picture_url: 'https://a0.muscache.com/im/pictures/user/85293a6b-b373-4ebe-9668-16dc48432b61.jpg?aki_policy=profile_x_medium',
  host_neighbourhood: 'Oak Lawn',
  host_listings_count: 1,
  host_total_listings_count: 1,
  host_verifications: '[''email'', ''phone'']',
  host_has_profile_pic: true,
  host_identity_verified: true,
  neighbourhood: 'Dallas, Texas, United States',
  neighbourhood_cleansed: 'District 2',
  latitude: 32.81462,
  longitude: -96.81586,
  property_type: 'Entire loft',
  room_type: 'Entire home/apt',
  accommodates: 2,
  bathrooms: 1.5,
  bathrooms_text: '1.5 baths',
  bedrooms: 1,
  beds: 1,
  amenities: [
    'Stove',
    'Kitchen',
    'Washer',
    'Essentials',
    'Hangers',
    'Coffee maker',
    'Hair dryer',
    'Dishes and silverware',
    'Bathtub',
    'Extra pillows and blankets',
    'Refrigerator',
    'Luggage dropoff allowed',
    'Carbon monoxide alarm',
    'Oven',
    'Smoke alarm',
    'Backyard',
    'Dishwasher',
    'Fire extinguisher',
    'Free parking on premises',
    'Bed linens',
    'Cooking basics',
    'Patio or balcony',
    'Microwave',
    'Cleaning available during stay',
    'Wifi',
    'Hot water',
    'Heating',
    'Air conditioning',
    'Shampoo',
    'BBQ grill',
    'Long term stays allowed',
    'Dryer',
    'Pool'
  ],
  price: '$75.00',
  minimum_nights: 5,
  maximum_nights: 1125,
  minimum_minimum_nights: 5,
  maximum_minimum_nights: 5,
  minimum_maximum_nights: 1125,
  maximum_maximum_nights: 1125,
  minimum_nights_avg_ntm: 5,
  maximum_nights_avg_ntm: 1125,
  has_availability: true,
  availability_30: 18,
  availability_60: 43,
  availability_90: 49,
  availability_365: 320,
  calendar_last_scraped: {
    $date: '2024-02-22T00:00:00.000Z'
  },
  number_of_reviews: 29,
  number_of_reviews_ltm: 0,
  number_of_reviews_l30d: 0,
  first_review: {
    $date: '2012-11-16T00:00:00.000Z'
  },
  last_review: {
    $date: '2020-03-26T00:00:00.000Z'
  },
  review_scores_rating: 4.9,
  review_scores_accuracy: 4.89,
  review_scores_cleanliness: 4.71,
  review_scores_checkin: 4.89,
  review_scores_communication: 4.96,
  review_scores_location: 5,
  review_scores_value: 4.78,
  instant_bookable: false,
  calculated_host_listings_count: 1,
  calculated_host_listings_count_entire_homes: 1,
  calculated_host_listings_count_private_rooms: 0,
  calculated_host_listings_count_shared_rooms: 0,
  reviews_per_month: 0.21
}
`````
 Insights the analysis shows: This analysis can be used to get a quick sample of the dataset for the viewer. By examining these documents, they can gain a preliminary understanding of the data structure and contents.


### Query 2: Show Exactly 10 Documents with Pretty Print
Description: The query retrieves ten documents from the collection and formats the output for easier reading.
```python
db.listings_clean.find().limit(10).pretty()
```
The result shown (up to first three):
`````
{
  "_id: ObjectId("6610d6366bce64540e9f1e96"),
  "id": 61878,
  "listing_url": "https://www.airbnb.com/rooms/61878",
  "scrape_id": {
    "$numberLong": "20240222071419"
  },
  "last_scraped": {
    "$date": "2024-02-22T00:00:00.000Z"
  },
  "source": "city scrape",
  "name": "MODERN LIVING AND FURNISHINGS",
  "description": "Close to downtown and Uptown.  Fast and convenient to highway, grocery shops, dinner, clubbing and much more. Very modern home.<br /><br />Pets welcomed with approval and additional fee $100 per pet.",
  "neighborhood_overview": "Enjoy the heart of Dallas right out your door step.  Cedar Springs offers a eclectic night life as well as great restaurants.  Or take a minute drive/Uber to Uptown for shopping.",
  "picture_url": "https://a0.muscache.com/pictures/c4d9625e-bcc5-4790-b699-3b1acb0a2b3d.jpg",
  "host_id": 300211,
  "host_url": "https://www.airbnb.com/users/show/300211",
  "host_name": "Sasha",
  "host_since": {
    "$date": "2010-11-26T00:00:00.000Z"
  },
  "host_location": "Roanoke, TX",
  "host_about": "\"Love is Love\" :)\r\nI'm originally from Florida, but call Texas home.  Things I can't live without are coffee, family & friends, my dog, traveling and love. \r\n\r\nWhen I travel, I love having the comforts of home all while enjoying a new city. This was my thought when I wanted my home to a part of AirBNB. You will enjoy all the comforts of a home . . . Who doesn't like a clean, modern apartment all to themselves? All in the heart of Dallas. Come visit and stay awhile . . . You will love it!",
  "host_response_time": "within an hour",
  "host_response_rate": "100%",
  "host_acceptance_rate": "100%",
  "host_is_superhost": false,
  "host_thumbnail_url": "https://a0.muscache.com/im/pictures/user/5f63d226-6de3-4b43-a863-64b8a9ff8fa2.jpg?aki_policy=profile_small",
  "host_picture_url": "https://a0.muscache.com/im/pictures/user/5f63d226-6de3-4b43-a863-64b8a9ff8fa2.jpg?aki_policy=profile_x_medium",
  "host_neighbourhood": "Oak Lawn",
  "host_listings_count": 2,
  "host_total_listings_count": 3,
  "host_verifications": "['email', 'phone']",
  "host_has_profile_pic": true,
  "host_identity_verified": true,
  "neighbourhood": "Dallas, Texas, United States",
  "neighbourhood_cleansed": "District 2",
  "latitude": 32.8169,
  "longitude": -96.82018,
  "property_type": "Entire condo",
  "room_type": "Entire home/apt",
  "accommodates": 3,
  "bathrooms": 1,
  "bathrooms_text": "1 bath",
  "bedrooms": 1,
  "beds": 2,
  "amenities": [
    "Kitchen",
    "Gym",
    "Washer",
    "Essentials",
    "Hangers",
    "Hair dryer",
    "Dishes and silverware",
    "Pets allowed",
    "Carbon monoxide alarm",
    "Smoke alarm",
    "Shared pool",
    "Fire extinguisher",
    "TV with standard cable",
    "Free parking on premises",
    "Iron",
    "Wifi",
    "Hot water",
    "Self check-in",
    "Heating",
    "Air conditioning",
    "Shampoo",
    "Long term stays allowed",
    "Keypad",
    "Dryer"
  ],
  "price": "$85.00",
  "minimum_nights": 30,
  "maximum_nights": 1125,
  "minimum_minimum_nights": 3,
  "maximum_minimum_nights": 30,
  "minimum_maximum_nights": 1125,
  "maximum_maximum_nights": 1125,
  "minimum_nights_avg_ntm": 28.4,
  "maximum_nights_avg_ntm": 1125,
  "has_availability": true,
  "availability_30": 0,
  "availability_60": 0,
  "availability_90": 11,
  "availability_365": 212,
  "calendar_last_scraped": {
    "$date": "2024-02-22T00:00:00.000Z"
  },
  "number_of_reviews": 55,
  "number_of_reviews_ltm": 3,
  "number_of_reviews_l30d": 0,
  "first_review": {
    "$date": "2010-12-29T00:00:00.000Z"
  },
  "last_review": {
    "$date": "2023-12-30T00:00:00.000Z"
  },
  "review_scores_rating": 4.7,
  "review_scores_accuracy": 4.79,
  "review_scores_cleanliness": 4.62,
  "review_scores_checkin": 4.85,
  "review_scores_communication": 4.92,
  "review_scores_location": 4.75,
  "review_scores_value": 4.77,
  "instant_bookable": false,
  "calculated_host_listings_count": 1,
  "calculated_host_listings_count_entire_homes": 1,
  "calculated_host_listings_count_private_rooms": 0,
  "calculated_host_listings_count_shared_rooms": 0,
  "reviews_per_month": 0.34
}
{
  "_id": {
    "$oid": "6610d6366bce64540e9f1e97"
  },
  "id": 776810,
  "listing_url": "https://www.airbnb.com/rooms/776810",
  "scrape_id": {
    "$numberLong": "20240222071419"
  },
  "last_scraped": {
    "$date": "2024-02-22T00:00:00.000Z"
  },
  "source": "city scrape",
  "name": "Goldies Bohemian Loft",
  "neighborhood_overview": "15 min walk to downtown Dallas and American Airlines center. Seven minute drive to Lovefield airport , 20 minute drive to DFW",
  "picture_url": "https://a0.muscache.com/pictures/9201ddbc-b015-415b-a95a-80a2d3af01c1.jpg",
  "host_id": 4096626,
  "host_url": "https://www.airbnb.com/users/show/4096626",
  "host_name": "Eric",
  "host_since": {
    "$date": "2012-11-08T00:00:00.000Z"
  },
  "host_location": "Seattle, WA",
  "host_about": "Hi, my name is Eric and I work globally as a remote duty paramedic . I live in the Seattle area . I've been Airbnb'ing since 2012. Please contact me with any questions.",
  "host_response_time": "within an hour",
  "host_response_rate": "100%",
  "host_acceptance_rate": "0%",
  "host_is_superhost": false,
  "host_thumbnail_url": "https://a0.muscache.com/im/pictures/user/85293a6b-b373-4ebe-9668-16dc48432b61.jpg?aki_policy=profile_small",
  "host_picture_url": "https://a0.muscache.com/im/pictures/user/85293a6b-b373-4ebe-9668-16dc48432b61.jpg?aki_policy=profile_x_medium",
  "host_neighbourhood": "Oak Lawn",
  "host_listings_count": 1,
  "host_total_listings_count": 1,
  "host_verifications": "['email', 'phone']",
  "host_has_profile_pic": true,
  "host_identity_verified": true,
  "neighbourhood": "Dallas, Texas, United States",
  "neighbourhood_cleansed": "District 2",
  "latitude": 32.81462,
  "longitude": -96.81586,
  "property_type": "Entire loft",
  "room_type": "Entire home/apt",
  "accommodates": 2,
  "bathrooms": 1.5,
  "bathrooms_text": "1.5 baths",
  "bedrooms": 1,
  "beds": 1,
  "amenities": [
    "Stove",
    "Kitchen",
    "Washer",
    "Essentials",
    "Hangers",
    "Coffee maker",
    "Hair dryer",
    "Dishes and silverware",
    "Bathtub",
    "Extra pillows and blankets",
    "Refrigerator",
    "Luggage dropoff allowed",
    "Carbon monoxide alarm",
    "Oven",
    "Smoke alarm",
    "Backyard",
    "Dishwasher",
    "Fire extinguisher",
    "Free parking on premises",
    "Bed linens",
    "Cooking basics",
    "Patio or balcony",
    "Microwave",
    "Cleaning available during stay",
    "Wifi",
    "Hot water",
    "Heating",
    "Air conditioning",
    "Shampoo",
    "BBQ grill",
    "Long term stays allowed",
    "Dryer",
    "Pool"
  ],
  "price": "$75.00",
  "minimum_nights": 5,
  "maximum_nights": 1125,
  "minimum_minimum_nights": 5,
  "maximum_minimum_nights": 5,
  "minimum_maximum_nights": 1125,
  "maximum_maximum_nights": 1125,
  "minimum_nights_avg_ntm": 5,
  "maximum_nights_avg_ntm": 1125,
  "has_availability": true,
  "availability_30": 18,
  "availability_60": 43,
  "availability_90": 49,
  "availability_365": 320,
  "calendar_last_scraped": {
    "$date": "2024-02-22T00:00:00.000Z"
  },
  "number_of_reviews": 29,
  "number_of_reviews_ltm": 0,
  "number_of_reviews_l30d": 0,
  "first_review": {
    "$date": "2012-11-16T00:00:00.000Z"
  },
  "last_review": {
    "$date": "2020-03-26T00:00:00.000Z"
  },
  "review_scores_rating": 4.9,
  "review_scores_accuracy": 4.89,
  "review_scores_cleanliness": 4.71,
  "review_scores_checkin": 4.89,
  "review_scores_communication": 4.96,
  "review_scores_location": 5,
  "review_scores_value": 4.78,
  "instant_bookable": false,
  "calculated_host_listings_count": 1,
  "calculated_host_listings_count_entire_homes": 1,
  "calculated_host_listings_count_private_rooms": 0,
  "calculated_host_listings_count_shared_rooms": 0,
  "reviews_per_month": 0.21
}
{
  "_id": {
    "$oid": "6610d6366bce64540e9f1e98"
  },
  "id": 795703,
  "listing_url": "https://www.airbnb.com/rooms/795703",
  "scrape_id": {
    "$numberLong": "20240222071419"
  },
  "last_scraped": {
    "$date": "2024-02-22T00:00:00.000Z"
  },
  "source": "city scrape",
  "name": "Amazing location walk to Downtown Dallas",
  "description": "***** Over 30% Discounts for stays over 30 days or more  ******<br />You can't beat the location of this beautiful penthouse condo. This residential neighborhood is walking distance to Uptown and Downtown Dallas. You can also take Uber to the many local restaurants and bars on Oak Lawn, downtown,  or to McKinney Ave. Please take advantage of a nature walk on the Katy Trail or in Reverchon park. Guest has access to free garage parking, outdoor pool & spa, gas grill, and business center.",
  "neighborhood_overview": "Located in Turtle Creek neighborhood steps from Reverchon park and Katy Trail. Blocks from several restaurants including The Common Table, Nick & Sam's Steak House, Katy Trail Ice House, and several along McKinney Ave. Uptown, downtown, and Love Field airport are within minutes of the condo. On a not so hot day you can walk to the AAC and downtown arts district.",
  "picture_url": "https://a0.muscache.com/pictures/miso/Hosting-795703/original/a7e4959e-6661-4df1-808b-baa66375e284.png",
  "host_id": 4191322,
  "host_url": "https://www.airbnb.com/users/show/4191322",
  "host_name": "Michelle",
  "host_since": {
    "$date": "2012-11-19T00:00:00.000Z"
  },
  "host_location": "Memphis, TN",
  "host_about": "I enjoy living in such a invigorating and upbeat neighborhood. On any day I can take advantage of a occasional stage play,  go to a park and listen to some live music, or sunbathe on a nearby rooftop patio.\n My hobbies include traveling, skiing, golfing, boating, and attending social events with  my friends. My life's motto is \"live like there's no tomorrow\"!",
  "host_response_time": "within an hour",
  "host_response_rate": "100%",
  "host_acceptance_rate": "100%",
  "host_is_superhost": true,
  "host_thumbnail_url": "https://a0.muscache.com/im/users/4191322/profile_pic/1357176516/original.jpg?aki_policy=profile_small",
  "host_picture_url": "https://a0.muscache.com/im/users/4191322/profile_pic/1357176516/original.jpg?aki_policy=profile_x_medium",
  "host_neighbourhood": "Oak Lawn",
  "host_listings_count": 2,
  "host_total_listings_count": 4,
  "host_verifications": "['email', 'phone']",
  "host_has_profile_pic": true,
  "host_identity_verified": true,
  "neighbourhood": "Dallas, Texas, United States",
  "neighbourhood_cleansed": "District 14",
  "latitude": 32.80327,
  "longitude": -96.80976,
  "property_type": "Entire condo",
  "room_type": "Entire home/apt",
  "accommodates": 2,
  "bathrooms": 1,
  "bathrooms_text": "1 bath",
  "bedrooms": 1,
  "beds": 1,
  "amenities": [
    "Coffee",
    "Fire pit",
    "Kitchen",
    "Free street parking",
    "Exercise equipment: elliptical, free weights, stationary bike, treadmill, yoga mat",
    "Conditioner",
    "Essentials",
    "Hangers",
    "First aid kit",
    "Baking sheet",
    "Outdoor dining area",
    "Hair dryer",
    "Free washer – In unit",
    "Bathtub",
    "70\" HDTV",
    "Dishes and silverware",
    "Shared outdoor pool - available seasonally, open specific hours",
    "Extra pillows and blankets",
    "Refrigerator",
    "Cleaning products",
    "Coffee maker: drip coffee maker",
    "Single level home",
    "Board games",
    "Central heating",
    "City skyline view",
    "Outdoor furniture",
    "Luggage dropoff allowed",
    "Carbon monoxide alarm",
    "Shared hot tub - available seasonally, open specific hours",
    "Sun loungers",
    "Central air conditioning",
    "Hot water kettle",
    "Smoke alarm",
    "Books and reading material",
    "Dishwasher",
    "Ethernet connection",
    "Fire extinguisher",
    "Stainless steel electric stove",
    "Toaster",
    "Iron",
    "Bed linens",
    "Elevator",
    "Cooking basics",
    "Microwave",
    "Shared outdoor kitchen",
    "Security cameras on property",
    "Freezer",
    "Cleaning available during stay",
    "Wifi",
    "Clothing storage: closet",
    "Hot water",
    "Wine glasses",
    "Dining table",
    "Shampoo",
    "BBQ grill",
    "Free residential garage on premises",
    "Shared gym in building",
    "Self check-in",
    "Free dryer – In unit",
    "Window guards",
    "Blender",
    "Long term stays allowed",
    "Building staff",
    "Electric  stainless steel oven",
    "Shower gel",
    "Dedicated workspace"
  ],
  "price": "$243.00",
  "minimum_nights": 30,
  "maximum_nights": 365,
  "minimum_minimum_nights": 30,
  "maximum_minimum_nights": 30,
  "minimum_maximum_nights": 365,
  "maximum_maximum_nights": 365,
  "minimum_nights_avg_ntm": 30,
  "maximum_nights_avg_ntm": 365,
  "has_availability": true,
  "availability_30": 30,
  "availability_60": 60,
  "availability_90": 90,
  "availability_365": 270,
  "calendar_last_scraped": {
    "$date": "2024-02-22T00:00:00.000Z"
  },
  "number_of_reviews": 70,
  "number_of_reviews_ltm": 0,
  "number_of_reviews_l30d": 0,
  "first_review": {
    "$date": "2013-02-01T00:00:00.000Z"
  },
  "last_review": {
    "$date": "2022-09-25T00:00:00.000Z"
  },
  "review_scores_rating": 4.84,
  "review_scores_accuracy": 4.91,
  "review_scores_cleanliness": 4.97,
  "review_scores_checkin": 4.91,
  "review_scores_communication": 4.97,
  "review_scores_location": 4.91,
  "review_scores_value": 4.75,
  "instant_bookable": false,
  "calculated_host_listings_count": 1,
  "calculated_host_listings_count_entire_homes": 1,
  "calculated_host_listings_count_private_rooms": 0,
  "calculated_host_listings_count_shared_rooms": 0,
  "reviews_per_month": 0.52
}
`````
Insights the analysis shows: This query provides a more extensive and clear view of the data. The pretty print function enhances readability for analysis, so that they can get the information needed more quickly.

### Query 3: Show All Listings for Two Specific Superhosts (only show the name, price, neighbourhood, host_name, and host_is_superhost for each result)
Description: This query shows all listings from two superhosts which is identified by their host_id. Only the specified fields are displayed.
```python
db.listings_clean.find(
  {
    host_id: { $in: ["4191322", "38090241"] },
    host_is_superhost: "true"
  },
  {
    name: 1, price: 1, neighbourhood: 1, host_name: 1, host_is_superhost: 1
  }
)
```
The 
`````
{
  name: 'Amazing location walk to Downtown Dallas',
  host_name: 'Michelle',
  host_is_superhost: true,
  neighbourhood: 'Dallas, Texas, United States',
  price: '$243.00'
}
{
  name: "Sunny/MStreet/SMU/Trendy Greenville/Private Bath",
  host_name: "Holly",
  host_is_superhost: true,
  neighbourhood: "Dallas, Texas, United States",
  price: "$90.00"
}
{
  name: 'Sunny Bedroom/MStreet/SMU/Trendy Greenville Ave',
  host_name: 'Holly',
  host_is_superhost: true,
  neighbourhood: 'Dallas, Texas, United States',
  price: '$95.00'
}
`````
Insights the analysis shows: This data can help the viewer focuses on theo two specific superhosts in the listings. This may can highlight the variance in offerings and price points from specific top-rated hosts.


### Query 4:  Find All Unique Host Names
Description: The query retrieves a list of all unique host_name values from the collection.
```python
db.listings_clean.distinct("host_name")
```
The result shown (up to first three):
`````
[
    'A-Solutions BnB'         'Aaja',            'Aamir',
    'Aaeliss',                'Aahanmord',       'Aaili',
    ...
]
`````
Insights the analysis shows: This query gives us a sense of the diversity of hosts in the dataset.

### Query 5:  Find all of the places that have more than 2 beds in a neighborhood
Description: Finds all listings with more than 2 beds in a specific neighborhood ( I refer to neighbourhood_cleansed, I choose the neighborhood of "District 2"), ordered by review score rating descending.
```python
db.listings_clean.find(
  {
    beds: { $gt: 2 },
    neighbourhood: "District 2"
  },
  {
    name: 1, beds: 1, review_scores_rating: 1, price: 1
  }
).sort({ review_scores_rating: -1 })
```
The result shown (up to first three):
`````
{
  name: 'Business / Corporate  Travelers',
  beds: 1,
  price: '$150.00',
  review_scores_rating: 5
}
{
  name: 'Art Loft with Zen Den - Cedars / Downtown Dallas',
  beds: 1,
  price: '$94.00',
  review_scores_rating: 5
}
`````
Insights the analysis shows: The viewers who want to search for the airbnb with more than 2 beds in a specific neighbourhood can quickly get the information. Also, they can identify which larger accommodations are rated highly by guests.

### Query 6:  Show the number of listings per host
Description: Groups the documents in the collection by host_id to count the number of listings each host has.
```python
db.listings_clean.aggregate([
  { $group: { _id: "$host_id", count: { $sum: 1 } } }
])
```
The result shown (up to first three):
`````
{
  _id: 108514926,
  count: 165
}
{
  _id: 498579365,
  count: 103
}
{
  _id: 43042344,
  count: 79
}
`````
Insights the analysis shows: This aggregation query helps viewer to understand the distribution of listings among hosts. In this case, the viewer can identify those who are more investment-heavy.

// Results will be added after execution


### Query 7:  Find the Average Review Scores Rating per Neighborhood
Description: Calculates the average review_scores_rating per neighborhood, showing only those averages that are 4 or above, sorted in descending order of rating.
```python
db.listings_clean.aggregate([
  { $group: { _id: "$neighbourhood", averageRating: { $avg: "$review_scores_rating" } } },
  { $match: { averageRating: { $gte: 4 } } },
  { $sort: { averageRating: -1 } }
])
```
The result shown (up to first four, in order to show decending orer):
`````
{
  _id: 'Frisco , Texas, United States',
  averageRating: 5
}
{
  _id: 'Heath, Texas, United States',
  averageRating: 5
}
{
  _id: 'Garland, Texas, United States',
  averageRating: 5
}
{
  _id: 'TX , United States',
  averageRating: 4.97
}
`````
Insights the analysis shows: The viewer can quickly see the general satisfaction guests have in various neighborhoods. It is useful for potential hosts and guests looking for high-quality neighborhoods.