# cloud-starter

Hi there! Welcome to Hack@Brown's Cloud starter kit. We will go over some of the most basic and useful AWS tools, including S3, EC2, and Lambda (but there are LOTS more, so feel free to check them out in your own time). To find more information about AWS, you can check out [this](https://aws.amazon.com/) page, which links many resources for exploring AWS products and applications. You can watch this video from Amazon themselves on AWS (and other videos from their channel): [What is Cloud?](https://www.youtube.com/watch?v=mxT233EdY5c&pp=ygUNd2hhdCBpcyBjbG91ZA%3D%3D)


## Why Use Cloud for Your Hackathon Project? 

Cloud services offer a scalable, flexible, and cost-efficient way to build and deploy projects without needing to manage physical infrastructure. By using cloud platforms like AWS, you can focus on building features while the cloud handles the heavy lifting of provisioning servers, databases, and other resources! You might be wondering what some projects with AWS might be, so here are some example ideas:

### Sample Project Ideas

1. **Real-Time Collaboration App (like a shared whiteboard or document editor)**
   - **AWS Tools**: Amazon EC2 (for hosting), AWS Lambda (to handle real-time updates), Amazon S3 (for file storage).
   - **Use Case**: Build an app that allows multiple users to draw on a shared whiteboard or edit a document in real time. Perfect for collaborative brainstorming during a hackathon!

2. **Personalized Meme Generator**
   - **AWS Tools**: Amazon S3 (for image storage), AWS Lambda (for generating memes), Amazon Rekognition (for facial recognition).
   - **Use Case**: Create a web app where users upload photos, and the app auto-generates memes using facial recognition to caption based on emotions or objects in the photo.

3. **Live Event Tracker (for hackathons, meetups, or sports events)**
   - **AWS Tools**: Amazon DynamoDB (for real-time data storage), AWS Lambda (to handle real-time updates), Amazon SNS (for notifications).
   - **Use Case**: Create a platform where users can track live updates for ongoing events like hackathon schedules, team standings, or meetups. You can send notifications for major events or changes.

4. **AI-Powered Music Playlist Generator**
   - **AWS Tools**: AWS Lambda (for logic and processing), Amazon Polly (to generate speech), Amazon DynamoDB (to store user preferences), and Amazon S3 (to store music files).
   - **Use Case**: Let users create personalized music playlists based on their mood or activity. Use AI to analyze a song's tempo and mood, and generate playlists accordingly.



## Instructions

You can find tutorials for S3, EC2, and Lambda in [this](https://github.com/hackatbrown/cloud-starter/blob/main/Cloud%20Starter%20Kit.pdf) document! This document also explains how to set up an AWS account. At the time of the creation (and updating) of this starter kit, all three of these services (S3, EC2, and Lambda) have a free tier in AWS.

However, note that you must give payment information to AWS to create your account, although you will not be charged if you stay within this free tier. To find more information about how to stay within the free tier, check out [this](https://aws.amazon.com/free/?trk=fce796e8-4ceb-48e0-9767-89f7873fac3d&sc_channel=ps&ef_id=Cj0KCQjwhL6pBhDjARIsAGx8D5-XNwMDCC2vCXxcxJ-_AFJTKnxKGUmttKPANpmGSqo_oHjoNbqqCDwaAkYtEALw_wcB:G:s&s_kwcid=AL!4422!3!432339156150!e!!g!!aws!1644045032!68366401852&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=tier%23trial&awsf.Free%20Tier%20Categories=*all) page. We also explain the free tier in the tutorial document.

## Supplemental Material

Example code, CSV files, and other material referenced in the tutorials can be found in [this](https://github.com/hackatbrown/cloud-starter/tree/main/cloud-kit) folder.

Happy hacking!