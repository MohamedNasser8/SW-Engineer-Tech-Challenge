# Floy Technical Challenge

## Questions

**1. What were the reasons for your choice of API/protocol/architectural style used for the client-server communication?**


I chose Flask API because it is lightweight, flexible, and well-suited for building scalable RESTful APIs.



**2.  As the client and server communicate over the internet in the real world, what measures would you take to secure the data transmission and how would you implement them?**

- Obtain an SSL/TLS certificate and configure the server
- Distributes traffic across multiple servers to prevent DDoS attacks (use CDN)
- Fixes vulnerabilities that could be exploited by attackers.
- Ensures that only authorized clients can access my API (using API keys, OAuth, etc.)
- Encrypts sensitive data before transmitting it over the network.
- Use two factor authentication