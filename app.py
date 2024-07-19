import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


# Use local CS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
#page configure        
st.set_page_config(page_title="Data Science Consultants", page_icon=":bar_chart:", layout="wide")


local_css("style.css")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


  # Path to css

# Load Assets
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json")  # Correct URL to a Lottie JSON file
img_contact_form = Image.open("images-18.jpeg")  # Path to image file
img_contact_form1=Image.open("images-17.jpeg")#path to opening image file
img_contact=Image.open("images-19.jpeg")


with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_contact_form1)
    with text_column:
        st.subheader("Hi Welcome To Axis Consultants :wave:")
        st.title("Real world solutions from real world data.")
        st.write("Are you ready to unlock the full potential of your data? As a company with professional data analysts  and data science consultants, we are here to help you transform your raw data into actionable insights,driving your business toward unparalleled success.Our services are efficient and affordable but our esteemed clients get value for their money.")
        

# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2, 1)
    with left_column:
        st.header("OUR SERVICES")
        st.write("##")
        st.write(
            """
        1.Data Analysis
        -Descriptive Analytics: Gain a clear understanding of your past business performance.
        -Diagnostic Analytics: Identify the root causes of your business challenges.
        -Predictive Analytics: Forecast future trends and behaviors to stay ahead of the competition.
        -Prescriptive Analytics: Receive actionable recommendations to optimize your business strategies.
        
        2. Data Science Solutions
        -Machine Learning Models: Implement cutting-edge algorithms to predict outcomes and automate decision-making.
        -Natural Language Processing (NLP): Extract meaningful information from text data to understand customer sentiment and more.
        -Deep Learning: Leverage neural networks for image recognition, speech processing, and other complex tasks.
        -Big Data Analytics: Process and analyze massive datasets quickly and efficiently.
        
        3. Business Intelligence
        -Dashboard Development: Create interactive dashboards to visualize your key performance indicators (KPIs) in real time.
        -Data Warehousing: Design and implement data storage solutions to ensure your data is organized and accessible.
        -ETL Processes: Extract, transform, and load your data to maintain its integrity and usability.       
        4. Data Strategy Consulting
        -Data Governance: Establish policies and procedures to ensure data quality and security.
        -Data Architecture: Design a robust architecture that supports your business goals and scales with your growth.
        -Data-Driven Culture: Train your team to make informed decisions based on data insights.""")
        st.write("##")
        st.header("WHY CHOOSE US?")
        st.write("""
        **Expertise and Experience**
With 6+ years of experience in the data science field, we have successfully helped 100+ businesses across various industries achieve their goals(an average 45% increase in sales) from the year 2018. Our professional team with a deep understanding of data analytics and machine learning ensures you receive the highest quality service.
        **Customized Solutions**
Every business is unique, and so are its data needs. We provide tailored solutions that align with your specific goals and challenges, ensuring maximum impact and ROI.
        **Cutting-Edge Technology**
Stay ahead of the curve with the latest tools and technologies in data science. From advanced machine learning models to real-time analytics platforms, We use state-of-the-art solutions to deliver the best results.
        ** Proven Track Record**
Don't just take our word for it—our clients' success stories speak volumes. From increasing sales and improving customer satisfaction to optimizing operations and reducing costs, we have a proven track record of delivering measurable results.""")
        st.write("##")
        st.header("GET STARTED TODAY!")
        st.write(
        """Don't let your data go to waste. Contact us today to schedule a consultation and discover how we can help you harness the power of data to achieve your business objectives. Together, we can turn data into your most valuable asset.
        """)
        st.write("##")         
        st.header("Contact Us:")              st.write("email: shivogojohn@gmail.com ")
        st.write("Or Call/Text: +254704234829")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Projects
with st.container():
    st.write("---")
    st.header("Side Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Real world data analysis projects.")
        st.markdown("[Github  ...](https://github.com/SHIVOGOJOHN)")

#Donations
with st.container():
    image_column,text,column=st.columns((2,1))
    with image_column:
        st.image("img_contact")
    with text_column:
        st.header("Support Us! :star:")
        st.write("Your donation is highly appreciated.")
       # st.markdown(f'<a href={} class="button" 👉 Donate here </a>', unsafe_allow_html=True)
        


# Contact Info
with st.container():
    st.write("---")
    st.header("Any Questions? Shoot us a message!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/shivogojohn@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" required>
    <input type="email" name="email" required>
    <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
        
        
        
