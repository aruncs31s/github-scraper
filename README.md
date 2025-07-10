# github-scraper

! Under Construction 
This name may not reflect the actual purpose , may get changed later.
## Contribution 
This projects main goal is to convert this [template](https://raw.githubusercontent.com/aruncs31s/es_gcek_electronics_projects_template/refs/heads/main/README.md) to this [template](https://raw.githubusercontent.com/mearashadowfax/ScrewFast/refs/heads/main/src/content/products/en/item-t845.md), First one will be [Embedded Systems And IOT GCEK(ESDC-> Embedded Systems Design Club's)](https://github.com/Embedded-Systems-GCEK) **Electronics Projects** starter template.


#### So How to contribute? 
You can get the sites source code from [here](https://github.com/aruncs31s/es_website_gcek) , Go to `src/content/projects/en` , you will see the following files 
```
item-a765.md
item-b203.md
item-f303.md
item-t845.md
```
this files will serve as the base content for the website , which means , all the contents for a project entry in the [projects page](https://es-gcek.netlify.app/projects/) , this will show some random contents but acutally if you select one of that , eg: Machine Screws you can see that , has the same title as the title in `item-t845.md`( you have to open the file to see it) 

#### Why all this? 
Our goal is to convert the `README.md` of our projects to the required format , required format in the sense that the structured format like `item-t845.md` this one has.

#### How to approach this

```bash
git clone https://github.com/aruncs31s/github-scraper
```
This repo will contain some unfinished scripts , there will be some documentation there , you can just read through that if you want , i will use `python` for the conversion and something like thi
```python
with open(output_file, 'w') as file:
    file.write(f"---\n")
    file.write(f"title: {yaml_helper.title}\n")
    file.write(f"description: {yaml_helper.description}\n")
    file.write("main:\n")
    file.write(f"  id: {id}\n")
    file.write("  " + "content: |\n")
    file.write("    " + newProps.main['content'])
    file.write(f"\n---\n")
```
maybe its not the optimal way but it achives almost 100% structure simularity eg 

```
---
title: Test Project
description: This is a test description
main:
  id: 1
  content: |
    This section should contain the description and introduction to the project.
---
```

### What you need to know to contribute

1. basic idea of git , if dont download the source code and email changes at `aruncs31s@proton.me`
2. little python , yaml , json 

To know the frontend server side of things
read [1](https://github.com/aruncs31s/es_website_gcek/blob/main/src/pages/projects/%5Bid%5D.astro), [2](https://github.com/aruncs31s/es_website_gcek/blob/main/src/content.config.ts)


## After Attempting
you we this line 
```
imgCard: "@/images/product-image-1.avif"
imgMain: "@/images/product-image-main-1.avif"
```
about this, i have not decided that whether i should download and send it to the `flask_server` or just share link , if i share the link the loading time will limited by github.


