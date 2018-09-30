# NoobCommender
Submission for CodeChef API Hackathon

A webapp to recommend competitive coders on the platform , new problems based on their bands.
The webapp at it's core uses a presistance storage to which contains cluster tags of the problems 
which are clustered together on the basis of their difficulty level which was acheived with the help of K-means clustering.
The webapp also uses celery and redis to asynchronously update the user tokens and other credentials.
