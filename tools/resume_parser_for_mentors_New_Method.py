from sentence_transformers import SentenceTransformer, util
import PyPDF2
import re

def extract_resume_content(pdf_path):
    """
    Extract text content from a PDF file.
    """
    # Read the PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = "".join([page.extract_text() for page in reader.pages])

    # Optional: Process the text to handle sections
    sections = re.split(r"(\d{4}\s?-\s?\d{4}\n|[A-Z][^\n]*\s?-\s?[A-Z])", text)
    combined_text = " ".join([part.strip() for part in sections])
    return combined_text.strip()

def analyze_skills_with_transformer(pdf_path):
    """
    Analyze skills using a pre-trained transformer model.

    Args:
        pdf_path (str): Path to the resume PDF file.

    Returns:
        str: A string with the name of the person followed by skill levels for each topic.
    """
    # Extract and preprocess resume content
    resume_content = extract_resume_content(pdf_path)

    # Define topics and their descriptions
    topics = {
        "Machine Learning": (
            "Developing, training, and deploying machine learning models using supervised, unsupervised, and deep learning techniques. "
            "Experience with TensorFlow, PyTorch, and scikit-learn. Knowledge in optimizing models for large-scale applications."
        ),
        "Software Engineering": (
            "Designing and maintaining scalable software systems using Python, Java, and other modern programming languages. "
            "Proficiency in APIs, microservices architecture, and containerization tools such as Docker and Kubernetes."
        ),
        "Computer Vision": (
            "Developing image recognition and processing pipelines using advanced frameworks like OpenCV, TensorFlow, and YOLO. "
            "Experience with object detection, semantic segmentation, and optical character recognition (OCR)."
        ),
        "Data Science": (
            "Performing exploratory data analysis (EDA), creating predictive models, and developing machine learning pipelines. "
            "Expertise in data visualization tools like Tableau, matplotlib, and Plotly for interactive dashboards."
        ),
        "Artificial Intelligence": (
            "Implementing advanced AI techniques, including reinforcement learning, generative models, and transformer architectures like BERT and GPT. "
            "Experience in ethical AI principles and explainable AI (XAI) methods."
        )
    }

    # Load the improved sentence transformer model
    model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

    # Generate embeddings for the resume content and topics
    resume_embedding = model.encode(resume_content, convert_to_tensor=True)
    topic_embeddings = model.encode(list(topics.values()), convert_to_tensor=True)

    # Compute cosine similarity between resume and each topic
    similarities = util.cos_sim(resume_embedding, topic_embeddings)[0]

    # Assign skill levels based on similarity thresholds
    skill_levels = []
    for similarity in similarities:
        if similarity > 0.8:
            skill_levels.append(3)  # High expertise
        elif similarity > 0.6:
            skill_levels.append(2)  # Medium expertise
        elif similarity > 0.4:
            skill_levels.append(1)  # Basic understanding
        else:
            skill_levels.append(0)  # No expertise

    # Extract a dummy name (improve with Named Entity Recognition for actual extraction)
    name = "Yoshua Bengio"

    # Return the name followed by skill levels
    return f"{name}, {', '.join(map(str, skill_levels))}"
