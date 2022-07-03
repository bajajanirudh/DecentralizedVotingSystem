# DecentralizedVotingSystem

An Online Voting System is developed based on blockchain architecture.

## Technology-Stack:
* Front-End Development: HTML,CSS,Bootstrap,Vanilla JS,Jquery
* Data-Processing and Blockchain Development: Python 3.6.5
* Back-End Development: Django-Python Framework
* Database management: DB SQLite

## Vote Casting and Blockchain REST API Development:
* Here system will create a unique voter ID for the voter.
* Again the voter will cast a vote for any one of the candidate.
* After vote casting there are six different steps are carried out for which we have designed a special REST API:
  1. Transaction Verification
  2. Proof of Work Algorithm
  3. Block creation and Serialization
  4. Block Broadcasting and validation
  5. Consensus Algorithm

## Peer to Peer (Distributed) Network Design:
* A peer to peer distributed network on which the blockchain architecture works.
* A Web Socket request API for broadcasting the all the requests into P2P network.
* Handling concurrency by using a mutex lock mechanism.

## Database Management:
* A relational DB SQLite is used as a database for the project.
* Many cryptographic and encryption algorithms are used to store the data securely in the database (SHA-256, CSPRNG, salt-hashing, etc).
* Complete normalization is also achieved in different relations of the database. 

## Admin Section:
* This panel is only reserved for the governing body of an election.
* Every admin is assigned a unique Election Commission ID for authentication.
* Result analysis of election is carried out in this section.

## Demo of the Website:

https://user-images.githubusercontent.com/91120579/177051231-b6fb0090-f05b-452e-b106-41d5b59888c0.mp4

## Demo of the admin Portal:

https://user-images.githubusercontent.com/91120579/177051244-658d70d0-0c66-4598-8fa7-194e78bb062e.mp4

## Steps to run the application:
1. Clone this repository.
2. Change this to working directory.
3. Hit command: "docker-compose up --build"
4. Go to http://localhost:5000/auth/ in your browser.
