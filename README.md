# Pricerr

A simple Python script that tracks a product on any e-commerce website and sends you an e-mail when the price of the product drops below price specifed.

<h2> To get Started </h2>

1.Clone this repository onto your desktop using the command below

```
git clone https://github.com/Sumit-0311/Pricerr.git
```

2. Check the Requirements.txt file to check for python dependencies and install them

```
pip install requests
pip install bs4
```

3. Change the <b>URL variable</b> to your liking and the desired price in the <b>yourPrice</b> variable. Also, fill in your account details and the reciever's email.

4. Finally, run this command, it checks for the price daily but you can also change that in the argument of time.sleep() function.

```
python scraper.py
```
