#--------------------------------- FUNCTIONS ---------------------------------#

def getUsernameAndDomain(userEmail):
    splitEmail = userEmail.split("@")

    emailUsername = splitEmail[0]
    emailDomain = splitEmail[1]

    print("The username and domain for " + userEmail + " are: ")
    print("Username: " + emailUsername)
    print("Domain: " + emailDomain)


#--------------------------------- MAIN ---------------------------------#

print("Please enter your email address: ")
userEmail = input("Email: ")
print("\n")

getUsernameAndDomain(userEmail)
