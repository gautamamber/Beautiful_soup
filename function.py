from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
	<title>Kapisha</title>
</head>
<body>

<h1>Mahendra Singh Dhoni</h1>
<p>Mahendra Singh Dhoni is an Indian cricketer who captained the Indian team in limited-overs formats from 11th of September 2007 to 4th of January 2017 and in Test cricket from 2008 to 28th of December 2014.</p>
<ul>
	<li>Indian caption</li>
	<li>caption cool</li>
</ul>
<h1>Profile</h1>
<ol>
	<li>Born: 7 July 1981 (age 36), Ranchi</li>
	<li>Height: 1.75 m</li>
	<li>Spouse: Sakshi Dhoni (m. 2010)</li>
	<li>Awards: Padma Shri, Rajiv Gandhi Khel Ratna, MORE</li>
	<li>Siblings: Jayanti Gupta, Narendra Singh Dhoni</li>
	<li>Parents: Devaki Devi, Pan Singh</li>
</ol><br>
<h2>Q. When did MS Dhoni play his first ODI?</h2>
<input type="radio" name="gender" value="opt1" checked> 2004<br>
  <input type="radio" name="gender" value="opt2"> 2005<br>
  <input type="radio" name="gender" value="opt3"> 2002<br>  
  <input type="radio" name="gender" value="opt4"> 2003<br> <br>

<a href="http://www.cricbuzz.com/profiles/265/ms-dhoni">Click me for complete details about M S Dhoni</a>
</body>
</html>

"""
soup = BeautifulSoup(html_doc, 'html.parser')
h = soup.contents
print h

b = soup.body
for i in b.children:
	print i
for j in b.descendants: #each individual tag is seperate
	print j