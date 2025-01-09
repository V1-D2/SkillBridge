from types import new_class
import PyPDF2
import re
import openai
from openai import OpenAI
import os



def extract_resume_content(pdf_path):
    # Read the PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = "".join([page.extract_text() for page in reader.pages])

    # Regular expression to match job titles, roles, and dates more accurately
    sections = re.split(r"(\d{4}\s?-\s?\d{4}\n|[A-Z][^\n]*\s?-\s?[A-Z])", text)

    # Combine fragments into one large string
    combined_text = ""
    for part in sections:
        combined_text += part.strip() + "\n"

    return combined_text.strip()

def analyze_skills_with_gpt(pdf_path):

    resume_content = extract_resume_content(pdf_path)

    client = client = OpenAI(api_key="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")

    # Define the list of important topics
    topics = [
        "Machine Learning",
        "Software Engineering",
        "Computer Vision",
        "Data Science",
        "Artificial Intelligence",
        "Cybersecurity",
        "Web Development (Frontend and Backend)",
        "Mobile App Development",
        "Database Design and Management",
        "Cloud Computing",
        "DevOps and Automation",
        "Game Development",
        "Embedded Systems",
        "Blockchain Development",
        "Operating Systems",
        "Distributed Systems",
        "Natural Language Processing (NLP)",
        "Computer Graphics",
        "Augmented and Virtual Reality (AR/VR)",
        "Human-Computer Interaction (HCI)",
        "Photography",
        "Architecture (Digital Tools and Traditional Methods)",
        "UI/UX Design",
        "Technical Writing",
        "Digital Marketing",
        "Product Management",
        "Educational Technology",
        "Music Production (Digital Tools)",
        "Entrepreneurship and Startups in Tech",
        "Public Speaking and Communication for Tech Professionals",
        "Data Visualization and Storytelling",
        "Systems Thinking",
        "Knowledge Management",
        "Design Thinking",
        "Innovation Management",
        "Scientific Computing (e.g., MATLAB, R)",
        "Digital Ethics and Privacy Awareness",
        "Business Analytics",
        "Crowdsourcing and Collective Intelligence",
        "Social Media Analytics",
        "Behavioral Economics in Technology",
        "Open Source Contribution and Collaboration",
        "Tech Policy and Regulation",
        "Cognitive Science and Human Behavior",
        "Digital Humanities",
        "Visual Effects (VFX) and Animation",
        "Creative Coding (e.g., Processing, p5.js)",
        "Digital Twin Development",
        "Hardware Prototyping (e.g., Raspberry Pi, Arduino)",
        "Tech Journalism and Blogging"
    ]

    # Prepare the prompt for GPT
    prompt = (
        "Based on the following resume text, assess the level of expertise (0-5) for each topic in the list below.\n\n"
        "Resume Text:\n" + resume_content + "\n\n"
        "Topics:\n" + "\n".join(topics) + "\n\n"
        "Provide your evaluation using the following criteria:\n"
        "5: The individual is one of the greatest specialists in a field."
        "4: The individual demonstrates amazing level of knowledge, being one of the top 1000 specialists in a field."
        "3: The individual demonstrates advanced expertise, working on cutting-edge technologies or creating highly innovative projects in the field.\n"
        "2: The individual demonstrates a solid working knowledge and experience with complex libraries and the ability to develop innovative projects.\n"
        "1: The individual has a strong foundational understanding and is capable of confidently completing basic tasks in the topic.\n"
        "0: The skill is either not mentioned or the individual has minimal or no proficiency.\n\n"
        "Additionally, use the following detailed reference examples for each level:\n"
"#### Machine Learning\n"
"- Level 0: Learn the basics of linear algebra and Python libraries such as NumPy and Pandas.\n"
"- Level 1: Train a simple model (e.g., logistic regression) with scikit-learn on the Iris dataset.\n"
"- Level 2: Build and train a neural network for image classification using PyTorch or TensorFlow.\n"
"- Level 3: Create a custom transformer-based model for text processing using Hugging Face with fine-tuning on large datasets.\n"
"- Level 4: Create an unique high-level architecture."
"\n"
"#### Software Engineering\n"
"- Level 0: Write a simple program, such as a calculator, in Python.\n"
"- Level 1: Develop a CRUD application using Flask and a database like SQLite.\n"
"- Level 2: Build a distributed microservices system with Docker, Kubernetes, and Redis.\n"
"- Level 3: Develop and scale a system comparable to Google’s infrastructure using Apache Kafka, gRPC, and Spring Boot.\n"
"\n"
"#### Computer Vision\n"
"- Level 0: Perform basic image processing using Pillow.\n"
"- Level 1: Set up face detection with OpenCV and dlib.\n"
"- Level 2: Train a segmentation model using PyTorch on a dataset like COCO.\n"
"- Level 3: Deploy a custom real-time video analytics solution using YOLOv8 or Detectron2.\n"
"\n"
"#### Data Science\n"
"- Level 0: Plot data using matplotlib.\n"
"- Level 1: Perform regression and clustering using scikit-learn.\n"
"- Level 2: Build data pipelines for large datasets using Apache Airflow.\n"
"- Level 3: Develop real-time analytics systems using Apache Spark and Google BigQuery.\n"
"\n"
"#### Artificial Intelligence\n"
"- Level 0: Implement basic search algorithms like breadth-first search in Python.\n"
"- Level 1: Build a chatbot using Dialogflow or Rasa.\n"
"- Level 2: Train a reinforcement learning agent using OpenAI Gym.\n"
"- Level 3: Develop custom generative models, such as diffusion models or large multimodal architectures.\n"
"\n"
"#### Cybersecurity\n"
"- Level 0: Learn basic encryption principles like Caesar cipher.\n"
"- Level 1: Implement a port scanner using socket in Python.\n"
"- Level 2: Develop an intrusion detection system (IDS) using Snort or Suricata.\n"
"- Level 3: Design a Zero Trust network system using cutting-edge security approaches.\n"
"\n"
"#### Web Development (Frontend and Backend)\n"
"- Level 0: Create a static website using HTML and CSS.\n"
"- Level 1: Develop a web application with React and Express.js.\n"
"- Level 2: Set up Server-Side Rendering (SSR) using Next.js or Nuxt.js.\n"
"- Level 3: Build a high-load web application using GraphQL, Redis, and CDN services.\n"
"\n"
"#### Mobile App Development\n"
"- Level 0: Create a basic mobile app using Android Studio with Java.\n"
"- Level 1: Build a cross-platform app using Flutter.\n"
"- Level 2: Implement push notifications and API integration using React Native.\n"
"- Level 3: Create a complex app with Kotlin Multiplatform and custom UI components.\n"
"\n"
"#### Database Design and Management\n"
"- Level 0: Set up a simple database using SQLite.\n"
"- Level 1: Configure a relational database with PostgreSQL and SQLAlchemy.\n"
"- Level 2: Implement sharding and replication with MongoDB or Cassandra.\n"
"- Level 3: Develop an OLAP system for big data using ClickHouse or Snowflake.\n"
"\n"
"#### Cloud Computing\n"
"- Level 0: Deploy a basic web server on AWS EC2.\n"
"- Level 1: Use AWS Lambda for serverless computing.\n"
"- Level 2: Set up CI/CD pipelines using Jenkins and AWS CodePipeline.\n"
"- Level 3: Build a multi-cloud solution integrating AWS, Google Cloud, and Azure.\n"
"\n"
"#### DevOps and Automation\n"
"- Level 0: Write a simple automated script in Bash.\n"
"- Level 1: Use Ansible for server configuration.\n"
"- Level 2: Implement CI/CD pipelines with GitLab.\n"
"- Level 3: Develop a fully automated DevOps cycle using Terraform and Kubernetes.\n"
"\n"
"#### Game Development\n"
"- Level 0: Create a simple 2D game using Scratch or Pygame.\n"
"- Level 1: Build a game using Unity or Unreal Engine.\n"
"- Level 2: Implement advanced AI for NPCs in a game.\n"
"- Level 3: Develop an AAA game with a custom engine or Unreal Engine extensions.\n"
"\n"
"#### Blockchain Development\n"
"- Level 0: Write a basic smart contract using Solidity.\n"
"- Level 1: Develop a decentralized application (dApp) using Truffle.\n"
"- Level 2: Implement Layer-2 scaling solutions on Ethereum.\n"
"- Level 3: Build a custom blockchain using Substrate.\n"
"\n"
"#### Embedded Systems\n"
"- Level 0: Assemble a simple LED circuit with Arduino.\n"
"- Level 1: Create a temperature controller using Arduino/ESP32.\n"
"- Level 2: Write firmware for an RTOS (e.g., FreeRTOS) and test on STM32.\n"
"- Level 3: Develop control systems for drones or IoT devices using Zephyr or Yocto.\n"
"\n"
"#### Operating Systems\n"
"- Level 0: Install and configure a Linux distribution like Ubuntu.\n"
"- Level 1: Write a simple Linux user-space program (e.g., shell).\n"
"- Level 2: Develop a device driver or file system for Linux.\n"
"- Level 3: Build a minimalist OS kernel from scratch, similar to xv6.\n"
"\n"
"#### Distributed Systems\n"
"- Level 0: Create a basic server-client model using Python sockets.\n"
"- Level 1: Set up a messaging queue system using RabbitMQ or Kafka.\n"
"- Level 2: Build distributed file storage with Raft or Zookeeper.\n"
"- Level 3: Develop a scalable distributed system for millions of users using Google Spanner or Cassandra.\n"
"\n"
"#### Natural Language Processing (NLP)\n"
"- Level 0: Write a simple text parser using regular expressions.\n"
"- Level 1: Use spaCy for entity recognition or text processing.\n"
"- Level 2: Train a sequence-to-sequence model using TensorFlow or PyTorch.\n"
"- Level 3: Build a transformer model for multilingual translation using BERT architecture.\n"
"\n"
"#### Computer Graphics\n"
"- Level 0: Create a 2D animation using Processing or Pygame.\n"
"- Level 1: Build a 3D object using Three.js or Blender.\n"
"- Level 2: Develop an interactive renderer using OpenGL.\n"
"- Level 3: Implement a physically realistic renderer using Ray Tracing and NVIDIA OptiX.\n"
"\n"
"#### Augmented and Virtual Reality (AR/VR)\n"
"- Level 0: Create a simple AR effect for Instagram or Snapchat.\n"
"- Level 1: Build a VR app using Unity.\n"
"- Level 2: Design an interactive virtual world with Unreal Engine.\n"
"- Level 3: Integrate neural interfaces or tactile feedback into AR/VR systems.\n"
"\n"
"#### Photography\n"
"- Level 0: Take basic photos with a smartphone and edit them using Canva.\n"
"- Level 1: Use Lightroom for professional photo editing.\n"
"- Level 2: Publish in international magazines such as *National Geographic*.\n"
"- Level 3: Win prestigious awards like *World Press Photo*.\n"
"#### Architecture (Digital Tools and Traditional Methods)\n"
"- Level 0: Draw simple 2D floor plans by hand.\n"
"- Level 1: Create 3D building models using SketchUp or AutoCAD.\n"
"- Level 2: Design parametric structures using Grasshopper and Rhino.\n"
"- Level 3: Implement generative design techniques with Autodesk Generative Design.\n"
"\n"
"#### UI/UX Design\n"
"- Level 0: Draw simple app layouts in Figma.\n"
"- Level 1: Create a prototype and conduct usability testing.\n"
"- Level 2: Develop a complex design system with Storybook.\n"
"- Level 3: Design adaptive, personalized interfaces using TensorFlow.js.\n"
"\n"
"#### Technical Writing\n"
"- Level 0: Write a simple project description using Markdown.\n"
"- Level 1: Create professional API documentation using Swagger.\n"
"- Level 2: Write technical articles for platforms like *Medium* or *Dev.to*.\n"
"- Level 3: Author books or comprehensive guides for IEEE or ACM publications.\n"
"\n"
"#### Digital Marketing\n"
"- Level 0: Set up a basic Google Ads campaign.\n"
"- Level 1: Optimize website SEO using tools like Ahrefs or Semrush.\n"
"- Level 2: Build an automated marketing funnel using platforms like HubSpot.\n"
"- Level 3: Manage global campaigns for brands like Google or Apple.\n"
"\n"
"#### Product Management\n"
"- Level 0: Write simple user stories or a project plan.\n"
"- Level 1: Manage sprints and tasks using Jira or Trello.\n"
"- Level 2: Launch a successful MVP and conduct A/B testing using tools like Amplitude.\n"
"- Level 3: Develop large-scale, multi-component products for global markets.\n"
"\n"
"#### Educational Technology\n"
"- Level 0: Set up an LMS platform like Moodle.\n"
"- Level 1: Design interactive courses using tools like Articulate or Canva.\n"
"- Level 2: Build an online learning platform similar to Udemy.\n"
"- Level 3: Integrate AI-powered adaptive learning features into education platforms.\n"
"\n"
"#### Music Production (Digital Tools)\n"
"- Level 0: Record a basic track using GarageBand.\n"
"- Level 1: Use professional DAWs like Logic Pro or Ableton Live.\n"
"- Level 2: Create complex mixes using Pro Tools and third-party plugins.\n"
"- Level 3: Compose soundtracks for films using custom virtual instruments and advanced sound design techniques.\n"
"\n"
"#### Entrepreneurship and Startups in Tech\n"
"- Level 0: Write a simple business model or lean canvas.\n"
"- Level 1: Launch a startup with an initial user base.\n"
"- Level 2: Secure venture capital funding using tools like PitchBook.\n"
"- Level 3: Build a scalable, multi-million-dollar business.\n"
"\n"
"#### Public Speaking and Communication for Tech Professionals\n"
"- Level 0: Deliver a presentation on a chosen topic in a classroom setting.\n"
"- Level 1: Speak at mid-level conferences like PyCon.\n"
"- Level 2: Participate in panel discussions at international forums like Web Summit.\n"
"- Level 3: Deliver TED Talks or keynote speeches at global tech events.\n"
"\n"
"#### Data Visualization and Storytelling\n"
"- Level 0: Create simple bar charts in Excel.\n"
"- Level 1: Build dashboards in Tableau or Power BI.\n"
"- Level 2: Develop interactive visualizations using D3.js.\n"
"- Level 3: Create real-time, large-scale visualizations with Apache ECharts or Three.js.\n"
"\n"
"#### Systems Thinking\n"
"- Level 0: Understand basic principles of cause-effect relationships.\n"
"- Level 1: Apply system mapping tools like Kumu or Miro to analyze problems.\n"
"- Level 2: Conduct detailed modeling of complex systems using Stella Architect or AnyLogic.\n"
"- Level 3: Lead strategic foresight initiatives for large-scale systems redesign.\n"
"\n"
"#### Knowledge Management\n"
"- Level 0: Use simple tools like Google Drive or Notion to organize information.\n"
"- Level 1: Implement knowledge-sharing systems within teams using tools like Confluence.\n"
"- Level 2: Design enterprise-wide KM systems using platforms like SharePoint.\n"
"- Level 3: Develop AI-driven knowledge networks to support large organizations.\n"
"\n"
"#### Design Thinking\n"
"- Level 0: Learn the basics of brainstorming and ideation techniques.\n"
"- Level 1: Facilitate design sprints for product teams.\n"
"- Level 2: Develop innovative solutions using frameworks like Double Diamond.\n"
"- Level 3: Lead transformative design initiatives for global enterprises.\n"
"\n"
"#### Innovation Management\n"
"- Level 0: Summarize key innovation trends from articles or reports.\n"
"- Level 1: Create roadmaps for innovation projects using Trello or Asana.\n"
"- Level 2: Run innovation workshops using frameworks like Design Sprint.\n"
"- Level 3: Lead innovation labs and manage foresight tools like scenario planning.\n"
"\n"
"#### Scientific Computing (e.g., MATLAB, R)\n"
"- Level 0: Perform simple statistical analysis using Excel.\n"
"- Level 1: Use MATLAB or R for solving linear equations and plotting.\n"
"- Level 2: Develop complex numerical models and simulations in MATLAB or SciPy.\n"
"- Level 3: Build high-performance computing solutions for large-scale scientific problems.\n"
"\n"
"#### Digital Ethics and Privacy Awareness\n"
"- Level 0: Understand basic concepts of data privacy and digital rights.\n"
"- Level 1: Conduct privacy audits and ensure compliance with regulations like GDPR.\n"
"- Level 2: Develop privacy-preserving algorithms using tools like Differential Privacy.\n"
"- Level 3: Shape policies or frameworks for ethical AI and technology development.\n"
"\n"
"#### Business Analytics\n"
"- Level 0: Analyze small datasets using Excel or Google Sheets.\n"
"- Level 1: Use Tableau or Power BI to generate business insights.\n"
"- Level 2: Build predictive analytics models using Python and SQL.\n"
"- Level 3: Implement large-scale analytics pipelines for enterprise applications.\n"
"\n"
"#### Crowdsourcing and Collective Intelligence\n"
"- Level 0: Participate in small crowdsourcing projects like Amazon Mechanical Turk.\n"
"- Level 1: Design simple crowdsourcing tasks for platforms like Kaggle.\n"
"- Level 2: Build collaborative intelligence platforms for solving large problems.\n"
"- Level 3: Lead initiatives that leverage global crowdsourcing for societal challenges.\n"
"\n"
"#### Social Media Analytics\n"
"- Level 0: Track basic engagement metrics using built-in tools like Instagram Insights.\n"
"- Level 1: Use platforms like Hootsuite or Sprout Social for analytics.\n"
"- Level 2: Build sentiment analysis models for social media using Python or R.\n"
"- Level 3: Implement real-time, large-scale social media monitoring using Apache Kafka.\n"
"(Additional detailed examples for other topics continue similarly in the prompt...)\n\n"
        "Output a list of numbers corresponding to the level of expertise for each topic, in the same order. In the output must be only list of numbers. Only list of numbers in a raw separated by comma.\n"
        "Be sure to give 5 grade only in a very specific circumstences and only for high level professionals.\n"
        "Please before starting listing scores add the name of a person, and then after comma all the results.\n\n"
    )


    # Call OpenAI GPT model
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert assistant for analyzing resumes."},
            {"role": "user", "content": prompt}
        ]
    )

    new_response = response.choices[0].message.content

    parts = new_response.split(", ")

    # Extract the name (first part)
    name = parts[0]

    # Extract the numerical values (remaining parts) and convert them to integers
    values = list(map(int, parts[1:]))

    # Combine the name and values into the desired format
    result = [name, values]

    # Extract the response content
    return result




