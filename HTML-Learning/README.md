# Day 001   
<h1>This is Heading1</h1>

<p>This is a Paragraph</p>

## The basic syntax  
    <element attribute="value"></element>  
1. the URL of a link :  
```{<a href="https://www.example-website.com">Visit our Website</a>}```
2. image :  
```{<img src="image.jpg" alt="A beautiful image" /> }```   
notes:   
src = source ;  
alt = alternatice   
3. input :  
```{<input type="checkbox" checked />}```   
notes:  
checked = specify the checkbox should be checked by default

# Day 002   
# HTML Boilerplate
### 1. link element  

    <link rel="stylesheet" href="./styles.css"/>    
  
notes:      
rel = specify the relationship between the linker source and HTML document    
href = the location of the URL  
./ = look in the current folder or dictory   
style.css = the file name
function : instead writing everything in HTML    

### 2. head element     
`link` always is placed inside `head` element
```
{
<head>    
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Example of the link element</title>
  <link rel="stylesheet" href="./styles.css"/>
</head>
}
```  

# Day 003   
1.  What is it?   
content : HTML   
Presentation: CSS   
Programming language : JS   
2. Install   
VScode: Prettier  ➡️  setting: format ： Prettier ➡️ format on save ➡️ auto save ➡️ tab size : 2
Vscode: one monokai
Vscode : settings : file icon theme :  Seti   
3. First Test   
  First: make index always your first html(it is the default name of any website)
  Seconed: create and open HTML File, add some code, and open it at Google.

# Day 004   
1. basic syntax
element : 
```
 <p>HTML is a make up language</p>  
# '<p>' : opening tag   + content + '</p>' : endding tag
```
first :  clarify doc-type
second : content   
  head : cannot be visible    
  body : can be see    

# Day 005  
1.basic syntax  
1) each html have only one h1 heading
2) comment : ```<-- -->```
3) bold text :``` <strong> or <b>```   
4) italic text :```<em> of <i>``` emphasis
5) order list : ```<ol>```   
   list item :```<li>```   
6) unordered list : ```<ol>```     
7) image element : ```<img /> ```   
   src: source attribute   
   alt : alternative attribute : allow search engine know the image and allow blind people use it
   width / height : attribute    
   ```<img src="post-img.jpg" alt="HTML code on a screen"/>```
8) language : a HTML attribute : ```<lang=" ">```
9) metadata : ```<meta charset="UTF-8" />```

# Day 006  
1. Hyperlink : category to our own website and outside of ours.
2. OUTSIDE  
   a.every website on internate has its own URL  
   b."a": anchor
     "href" : attribute
   c. ```target = "_black"``` open a link in a new web
   d."#" : point to non place
   e."nav" :navigation element : create an invisible box to make HTML structure clearly
    "div" : a new box without any meaning   
   d."header" : element :  the top part of a page
    "article" :  element
   f."footer" :element : text or create a paragraph
    "c" : ```&copy;```
   g. make HTML avaiable to search engine and people rely on screen reader

# Day 007
1. install at VS code  
   image preview    
   color highlight
   auto rename tag : close will change with you change open tag
   live server : page change with your code automacially
2. "aside" element : secondary information

# Day 008 
CSS : Cascading Style Sheets : describe the visual style and prensentation of the content written in HTML  
1.CSS Rule : Selector {declaration block}  
2.internal, inline and outline CSS  
3. "link" element : connecting css style file : use at head of a html  
    “href" : point to the css file;  
    "rel"(relation): clear the relationship between html and css;  

# Day 009 
CSS elements  
1.font
    font-size:26px...  
    font-family:Times New Roman...  
    font-style: italic...  
    text-transform:uppercase......  
    text-align:center/left......  
    line-height:  
2.descendant selector 


   
   
   














