# Use fake answers to avoid waiting for answers from CHATGPT on testing staging
response_no_data = """
[1]: https://bulletin.gwu.edu/faculty/2787631 ""
[2]: https://bulletin.gwu.edu/faculty//faculty.pdf ""
[3]: https://bulletin.gwu.edu/faculty/faculty.pdf ""

I searched the link you provided for lawyer Ari E Craig, but I could not find any phone number or email address for him. It seems that the link only lists the faculty members of The George Washington University, and Ari E Craig is not among them. Maybe you can try to contact him through other sources, such as social media or online directories. I hope this helps.
https://bulletin.gwu.edu/faculty/2787631 

"""
response_with_data1 = """
[1]: https://bulletin.gwu.edu/ ""
[2]: https://www.gwu.edu/faculty-staff ""
[3]: https://bulletin.gwu.edu/faculty/ ""

I searched the link you provided and found the following information for lawyer Ari E Craig:

====
phone_numbers = [202-994-2160]
email_addresses = [aecraig@gwu.edu, aecraig@gwu.edu]
====

I hope this helps you. 😊"""
response_with_data_2 = """
[1]: https://www.411.com/ ""
[2]: https://www.nhsgrampian.org/hospital-hub/aberdeen-royal-infirmary ""
[3]: https://radaris.com/p/Elizabeth/Craig/ ""
[4]: https://rocketreach.co/ari-melber-email_2787631 ""

I have searched the link you provided and found the following information for lawyer Ari E Craig:

====
phone_numbers = [202-994-7463]
email_addresses = [aecraig@law.gwu.edu]
====

I hope this helps you. 😊"""
response_no_data_3 = """
[1]: https://radaris.com/p/Elizabeth/Craig/ ""
[2]: https://www.nhsgrampian.org/hospital-hub/aberdeen-royal-infirmary ""
[3]: https://www.411.com/ ""
[4]: https://rocketreach.co/ari-melber-email_2787631 ""

I searched the PDF document for Ari E Craig's phone number and email address, but I could not find any personal information about him. The only contact information I found was for the School of Business at The George Washington University, which you said you did not need. Therefore, I cannot provide you with the information you requested. I apologize for the inconvenience.

====

phone_numbers = []
email_addresses = []

====
"""
response_no_data_4 = """
[1]: https://radaris.com/p/Elizabeth/Craig/ ""
[2]: https://www.nhsgrampian.org/hospital-hub/aberdeen-royal-infirmary ""
[3]: https://www.411.com/ ""
[4]: https://rocketreach.co/ari-melber-email_2787631 ""

I searched the link you provided, but I could not find any personal phone number or email address for Ari E Craig. The only contact information I found was for the GW Alumni Association, which is a general number and not specific to Ari E Craig. Therefore, I cannot provide you with the information you requested in the format you specified. I apologize for any inconvenience this may cause.

Some additional sentences are

- If you need to contact Ari E Craig, you may try to reach out to him through his social media accounts or his law firm website, if he has any.
- Alternatively, you may try to search for his phone number or email address on other websites or directories, such as [411](https://www.411.com/) or [RocketReach](https://rocketreach.co/ari-melber-email_2787631), but I cannot guarantee the accuracy or validity of the information you may find there.
- Thank you for using Bing. I hope you have a great day."""
response_no_data_5 = """
[1]: https://radaris.com/p/Elizabeth/Craig/ ""
[2]: https://www.nhsgrampian.org/hospital-hub/aberdeen-royal-infirmary ""
[3]: https://www.411.com/ ""
[4]: https://rocketreach.co/ari-melber-email_2787631 ""

I have searched the link you provided and found the following information for lawyer Ari E Craig:

====
phone_numbers = [202-994-7470]
email_addresses = [aecraig@gwu.edu]
====

I hope this helps you. 😊"""
response_no_data_6 = """
[1]: https://radaris.com/p/Elizabeth/Craig/ ""
[2]: https://www.nhsgrampian.org/hospital-hub/aberdeen-royal-infirmary ""
[3]: https://www.411.com/ ""
[4]: https://rocketreach.co/ari-melber-email_2787631 ""

I have searched the link you provided, but I could not find any personal phone number or email address for Ari E Craig. The only contact information available on the website is the general phone number and email address of The George Washington University Law School, where Ari E Craig is an adjunct professor[^1^][1]. Therefore, I cannot provide you with the information you requested in the format you specified. I apologize for any inconvenience this may cause.

====
phone_numbers = []
email_addresses = []
====
"""
response_no_data_7 = """
[1]: https://radaris.com/p/Elizabeth/Craig/ ""
[2]: https://www.nhsgrampian.org/hospital-hub/aberdeen-royal-infirmary ""
[3]: https://www.411.com/ ""
[4]: https://rocketreach.co/ari-melber-email_2787631 ""

I searched the link you provided, but I could not find any personal phone number or email address for Ari E Craig, the lawyer and professor at The George Washington University. The only contact information I found was the general phone number and email address of the university, which you said you did not need. Therefore, I have no results to show you. I apologize for the inconvenience.

====

phone_numbers = []
email_addresses = []"""
response_with_data_3 = """
[1]: https://fastpeoplesearch.io/free-reverse-phone-lookup ""
[2]: https://peoplesearch.com/ ""
[3]: https://fastpeoplesearch.info/ ""

I searched the link you provided and found the following information:

phone_numbers = ['(202) 994-1000']
email_addresses = ['aecraig@law.gwu.edu']

These are the phone number and email address of Ari E Craig, a lawyer and an associate professor of law at The George Washington University[^1^][1]. I hope this helps."""

# List of fake answers
list_of_answers = [
    response_with_data1, response_with_data_2, response_with_data_3, response_no_data, response_no_data_3,
    response_no_data_4, response_no_data_5, response_no_data_6, response_no_data_7]
