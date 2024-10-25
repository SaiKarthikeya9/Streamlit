import streamlit as st

st.set_page_config(page_title='My Website', page_icon=":bar_chart:", layout="wide")

custom_css = """
<style>
    body, h1, h2, h3, h4, p, ul, li {
      color: #00000;
    }

    h1,h2,h3,h4 {
      text-align: center;
      color: #32CD32;
    }

    .centered-image img {
      display: block;
      margin-left: auto;
      margin-right: auto;
      margin-top:-40px;
      border-radius: 50%;
      width: 150px;
      height: 150px;
      object-fit: cover;
    }

</style>
"""

#Inject CSS
st.markdown(custom_css, unsafe_allow_html=True)


# Main content of the page
with st.container():
    st.markdown(
    """
    <div class="centered-image">
    <img src = "https://motionbgs.com/media/1953/monkey-d-luffy-straw-hat2.jpg" width="100"/>
    </div>

    """,
    unsafe_allow_html=True
    )

#Introduction
with st.container():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2 style="color: #1E90FF;">Hello!</h2>
            <h3>I am Sai Kaarthikeya Mokkapati.</h3>
            <h5>I have completed my MBA from Aurora's P.G College, which comes under Osmania University.</h5>      
        </div>
        """,
        unsafe_allow_html=True
    )

#Objective
with st.container():
    st.write("----")
    st.markdown(
      """
      <div style="text-align: left;">
          <h4 style="text-align: left;">Objective :</h4>
          <p style="font-size:17px;"><b>To Secure a Challenging Position in an Organization that Fosters Professional Growth, where I can Contribute My skills to the Company's Success while Advancing My Own Development.<b></p>
      </div>

      """,
      unsafe_allow_html=True
    )

#project
with st.container():
    st.write('----')
    st.markdown(
      """
      <div style='text-align: left';>
        <h4 style='text-align: left;'>Project :</h4>
        <p style='font-size: 17px;'><b>Personal Portfolio and Professional Showcase: Integrating Skills, Certifications, and Career Aspirations in Data Analytics.</b></p>
      </div>

      """,
      unsafe_allow_html=True
    )
    
#Qualification   
with st.container():
    st.write('----')
    st.markdown(
      """
      <div style='text-align: left;'>
        <h4 style='text-align: left;'>Qualification :</h4>
        <ul style="list-style-type: disc; padding: 0;">
              <li><b>Masters in Business Administration(MBA) - Completed</b></li>
              <li><b>Bachelor of Science(Chemistry) - 8.04 CGPA</b></li>
              <li><b>Intermediate - 73.3</b></li>
              <li><b>Secondary School Certificate (SSC) - 7.7 CGPA</b></li>
        </ul>
      </div>
          
      """,
      unsafe_allow_html=True
    )

#Certificates
with st.container():
    st.write('----')
    left_side, right_side = st.columns(2)

    with left_side:
        st.markdown(
        """
        <div style="text-align: left;">
          <h4 style='text-align: left;'>Certificates :</h4>
          <ul style='list-style: disc; padding: 0;'>
                <li><b>Preparing Data for Analysis with Microsoft Excel</b></li>
                <li><b>Data Modeling in Power BI</b></li>
                <li><b>Data Analysis and Visualization with Power BI</b></li>   
                <li><b>Extract, Transform and Load Data in Power BI</b></li>
                <li><b>Creative Designing in Power BI</b></li>
                <li><b>Harnessing the Power of Data with Power BI</b></li>
                <li><b>Microsoft Power BI Data Analyst</b></li>
          </ul>
        </div>

       """, 
       unsafe_allow_html=True
       
     )
        
    with right_side:
        st.markdown(
        """
        <div style='text-align: right;'>
          <h4 style='text-align: right;'>Links</h4>
          <ul style='list-style: none; padding: 0;'>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/GHZ3NP3JZ8F4" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/RP4V24X7XMMD" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/2NJ5NQVCTFTW" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/9V9N6LR22X2X" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/Z8L6BYS2BYLH" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/MKCAGXXP3NSQ" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/professional-cert/ULF9YVXJ2XTA" target='_blank'>View Certificate</a></li>
          </ul>
        </div>

        """,
        unsafe_allow_html=True
      )

#Skills and Hobbies
with st.container():
    st.write('----')
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown(
        """
        <div style="text-align :left;">
          <h4 style="text-align: left;">Skills :</h4>
          <ul style="list-style-type: disc; padding: 0;">
                <li><b>Power BI</b></li>
                <li><b>Microsoft Office (PowerPoint, Excel, Word)</b></li>
                <li><b>Basics In Python</b></li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True
       )
        

    with right_column:
        st.markdown("""
        <div style="text-align :left;">
          <h4 style="text-align: left;">Hobbies and Interest:</h4>
          <ul style="list-style-type: disc; padding: 0;">
                <li><b>Playing Video Games</b></li>
                <li><b>Listening to Music</b></li>
                <li><b>Watching Movies</b></li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True
       )
# Contact info
with st.container():
  st.write("----")
  st.markdown(
     """

  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"> 

  <div style="text-align: center; margin: 20px;">
    <h2><b>Contact on :</b></h2>

    <p style="margin: 10px 0;">
      <span class="material-icons" style="vertical-align: middle;">email</span>
      <b>Email</b>: <a href="mailto:karthikeya18032001@gmail.com">karthikeya18032001@gmail.com</a>
    </p>

    <p style="margin: 10px 0;">
      <span class="material-icons" style="vertical-align: middle;">business_center</span>
      <b>LinkedIn</b>: <a href="https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit">Profile</a>
    </p>

    <p style="margin: 10px 0;">
      <span class="material-icons" style="vertical-align: middle;">phone</span>
      <b>Phone</b>: +91-8309383175
    </p>

  </div>

     """,
    unsafe_allow_html = True
 
 )




 


