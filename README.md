This is the result of my very quick foray into visualizing all the (roman) catholic bishops who are successors of Cardinal Scipione Rebiba (whioch includes around 95% of all bishops currently alive)

It is based on data scraped from [https://www.catholic-hierarchy.org] using `scrapy` and visualized using `pyvis`.

It was done in under 5 hours and I've never used `pyvis` before, so don't expect perfection.


The resulting html file `succession_rebiba.html` can be found in the `visualization` directory. It needs to be placed in the same directory as the `lib` subdirectory to load correctly. It can take a few minutes to load, so you may first want to try opening the `succession_zimon.html` file to see if everything works. The html is already created so you dont have to run any code or anything. Just open the html file.

If you do want to make some changes, the source code is included, and the python requirements are dumped in `requirements.txt`. I used python 3.12.4, but any version should work (as long as the dependencies do).