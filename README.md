# CS-340
Python and MongoDB dashboard for Grazioso Salvare that filters animal shelter records to identify potential search-and-rescue dogs. CS 340 portfolio project.
## How do you write programs that are maintainable, readable, and adaptable?

I keep my code organized by using clear names, helpful comments, and smaller functions that each have a specific job. For this project, I kept the database operations in my CRUD Python module and the dashboard code in the notebook. This made it easier to understand what each part did and where to look when something needed to change.

Reusing my CRUD module from Project One saved time because I did not have to write the database connection and operations again. The dashboard could call the module to retrieve records whenever someone selected a rescue category. I could update the database code in one place without changing every dashboard widget. In the future, I could adapt this module for another shelter dashboard, an inventory application, or another program that uses MongoDB.

## How do you approach a problem as a computer scientist?

I start by understanding what the client needs and breaking the work into smaller steps. For Grazioso Salvare, I reviewed the requirements for each rescue category and identified the breed, age, and sex fields needed to find matching dogs. I built the database queries, connected them to the dashboard filters, and checked that the table, breed chart, and map responded correctly.

This project involved bringing several pieces together and building on earlier assignments. I had to make sure the database, CRUD module, and dashboard worked together as one application. For future database projects, I would clarify the client's requirements, review sample records, choose appropriate fields and data types, and test the queries before connecting them to the interface. I would also check how the system handles missing data and confirm that the results meet the client's needs.

## What do computer scientists do, and why does it matter?

Computer scientists solve problems by creating programs and systems that help people use information. Their work includes understanding a problem, organizing data, building a solution, and testing it. This matters because a useful system can save time, reduce repetitive work, and help people make informed decisions.

For Grazioso Salvare, my dashboard makes it easier to find dogs that meet the initial requirements for search-and-rescue training. Staff can select a rescue category and review matching records instead of searching through every animal individually. The breed chart and map provide additional information about the results. This gives staff more time to evaluate potential candidates and decide which dogs are suitable for training.
