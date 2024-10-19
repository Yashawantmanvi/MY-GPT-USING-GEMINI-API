###Home.py####
## It Contains the basic login and signup page which it connected to the MongoDb.![Screenshot (116)](https://github.com/user-attachments/assets/dc1618d2-894e-45e5-8fe1-3eae683d5bb6)

## MongoDb Connection##
Create a connection and replace this link with yours("mongodb://localhost:27017/")
Create a Database and collection in MongoDb
Make sure that password saved is HASHED.

# When you Signup the messege will be displayed that acoount created successfully. Using that credentials login.
After a successfull login a  Welcome@ user messege will be displayed 
Below that message list of cards will be displayed.
## Note: the cards are not clickable( when you click  AI Chatbot it will not redirect the page). for the easey access the tools are displayed in the sidebar, you can click on that to open the page

# Sidebar contains 

  ## 1) AI Chatbot.

              It is more likely a chatbot where it generally answers all your questions.
              IT has an input area where you can enter your query and when you click on Ask Question button , it takes some time to understad your question and then it gives answer to your question.

              Here is a preview of AI Chatbot : ![Screenshot (101)](https://github.com/user-attachments/assets/abf2cd5e-b76a-4751-8569-9399b3446d2f)

              It also stores the history in the form of buttons , when you click on the button the history will retrieved from the mongodb and displayed.
              IT has got the feature to adjust your screen as you wish, that is Dark mode and Light mode

## 2) Chat with pdf
        This feature generally helps the students who read from the PDF's 
        
        then what becomes this feature different from othe other pdf reader??
        
        It has the file uploader in the sidebar, so we have to upload the file that we want to chat with. After submitting the file it processes and stores in the Local machine that is faiss Index.
        This solves the problem of searching for the answers in the pdfs which contains more pages. so what we can do with this is, we ask the question, chat with pdf processess that question and answers that question from the pdf uploaded.
        We can upload file upto 200mb per file,
        We can upload and chat with more than one pdf.

        Here is a preview of Chat with pdf : ![Screenshot (106)](https://github.com/user-attachments/assets/498d5746-627e-4960-8fa9-af9647676ba9)

## 3) Invoice Extractor

        The main feature of this is it is multilanguage..
        what it does is we can upload the invoice, it translates it to english. we can upload The invoice in whatever language.

         Here is a preview of Invoice Extractor: ![Screenshot (103)](https://github.com/user-attachments/assets/a9d5a7a2-b2c4-418b-b4cb-899f591b267e)

         we can input the prompt like: date, tax, address etc ...
         ![Screenshot (112)](https://github.com/user-attachments/assets/2c3019bf-5715-4e0d-9105-8b7d0b2ce97f)


## 4) vision pro

        it is a tool in which we can know about an image, for example if i had a dish on the plate with the lot of fruits, we can upload  that image and ask the vision pro that list the fruits on the plates with their essentials nutrients filled in it.

        we can also ask about A person whom we dont know about. it gives brief description about that person, for example in this project i have uploaded a image of cricketer " Virat Kohli"
         
        Here is a preview of vision pro: ![Screenshot (107)](https://github.com/user-attachments/assets/1c14d989-32d6-424b-8018-7305c2069c55)
        the response we got is: ![Screenshot (109)](https://github.com/user-attachments/assets/d427b0ec-5de4-476a-a89f-634027d96d5a).

        isn't it amazing.


        
