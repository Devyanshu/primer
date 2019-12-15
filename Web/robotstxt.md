# Robots.txt
  ##### By [Devyanshu](https://github.com/Devyanshu)
  
  robots.txt is a text file, in the root folder of a site, which tells web crawlers the pages they can or cannot access on the site. It is to be noted that there is no mechanism that enforces this check, it lies on the crawlers' end to honor the limitations. Many crawlers like Googlebot, Bingbot, Alexa Crawler, etc obey the restrictions in robots.txt, other crawlers might not.
  
  The main reason to have a robots.txt file is to prevent overloading because of the crawlers. Let's say you manage a site with a lot of web pages, now imagine a crawler going through each of them, multiple times a month, with more than twenty major crawlers, you can visualize the massive traffic that they generate.
  
  ##### A sample robots.txt file  
 ```
# Group 1
User-agent: bot1
Disallow: /users

# Group 2
User-agent: *
Allow: /
  ```
  From the above rules, 'bot1' should not access the 'users' page from the site, whereas all the other crawlers can access every page on the site.
  
  
  As mentioned earlier, robots.txt does not enforce its rules, therefore, if some pages have to be hidden from the crawlers then it should be password protected.
  
  
 ##### Other important points
 - The encoding of robots.txt should be UTF-8, to make sure every crawler understands it
 - A link to the sitemap should be present as ```Sitemap: <link to sitemap.xml> ```

  ## Further reads
  - [robotstxt.org](https://www.robotstxt.org/)
  - [Create a robots.txt](https://developers.google.com/search/reference/robots_txt)
