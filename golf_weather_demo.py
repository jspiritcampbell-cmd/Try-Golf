import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# Page configuration
st.set_page_config(
    page_title="Golf Basics for Beginners",
    page_icon="⛳",
    layout="wide"
)

# Helper function to create demo images
def create_demo_image(title, description, color):
    """Create a simple demo image with text"""
    img = Image.new('RGB', (800, 600), color=color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        font_desc = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        font_title = ImageFont.load_default()
        font_desc = ImageFont.load_default()
    
    # Add text to image
    draw.text((400, 250), title, fill='white', font=font_title, anchor='mm')
    draw.text((400, 350), description, fill='white', font=font_desc, anchor='mm')
    
    return img

# Title and introduction
st.title("⛳ Golf Basics for Beginners")
st.markdown("### Welcome to your golf journey! Here are some fundamental concepts to get you started.")

# Sidebar with navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Choose a topic:",
    ["Overview", "Grip", "Stance", "Swing", "Putting", "Course Etiquette"]
)

# Main content based on selection
if section == "Overview":
    st.header("Getting Started with Golf")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("What You'll Learn")
        st.write("""
        - Proper grip technique
        - Correct stance and posture
        - Basic swing mechanics
        - Putting fundamentals
        - Golf course etiquette
        """)
    
    with col2:
        img = create_demo_image("Welcome to Golf!", "Let's Learn Together", (34, 139, 34))
        st.image(img, caption="Your Golf Journey Begins Here", use_container_width=True)

elif section == "Grip":
    st.header("🤝 The Golf Grip")
    
    col1, col2 = st.columns(2)
    
    with col1:
        img = create_demo_image("Grip Basics", "Hands Together", (70, 130, 180))
        st.image(img, caption="Proper Grip Position", use_container_width=True)
    
    with col2:
        st.subheader("Key Points:")
        st.write("""
        **Overlapping Grip (Most Common)**
        - Left hand at top of grip (for right-handed golfers)
        - Right pinky overlaps left index finger
        - Maintain light, consistent pressure
        - Both thumbs point down the shaft
        
        **Remember:** A proper grip is the foundation of a good swing!
        """)
    
    st.info("💡 Tip: Your grip should be firm but not tight - imagine holding a bird!")

elif section == "Stance":
    st.header("🧍 Proper Stance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Stance Fundamentals:")
        st.write("""
        **Positioning:**
        - Feet shoulder-width apart
        - Slight knee bend
        - Weight balanced on balls of feet
        - Spine tilted slightly forward
        - Arms hanging naturally
        
        **Ball Position:**
        - Driver: Inside left heel
        - Irons: Center of stance
        - Short irons: Slightly back of center
        """)
    
    with col2:
        img = create_demo_image("Stance Position", "Balance & Posture", (220, 20, 60))
        st.image(img, caption="Athletic Stance", use_container_width=True)
    
    st.warning("⚠️ Avoid: Standing too upright or bending over too much")

elif section == "Swing":
    st.header("🏌️ The Golf Swing")
    
    tab1, tab2, tab3 = st.tabs(["Backswing", "Downswing", "Follow Through"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            img = create_demo_image("Backswing", "Rotate & Load", (255, 140, 0))
            st.image(img, use_container_width=True)
        with col2:
            st.write("""
            **Backswing Tips:**
            - Rotate shoulders, not just arms
            - Keep left arm straight (right-handed)
            - Shift weight to back foot
            - Maintain spine angle
            - Stop when shoulders are 90° rotated
            """)
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            img = create_demo_image("Downswing", "Power & Control", (186, 85, 211))
            st.image(img, use_container_width=True)
        with col2:
            st.write("""
            **Downswing Tips:**
            - Start with lower body rotation
            - Shift weight to front foot
            - Keep head behind the ball
            - Release hands through impact
            - Square clubface at contact
            """)
    
    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            img = create_demo_image("Follow Through", "Complete the Motion", (0, 128, 128))
            st.image(img, use_container_width=True)
        with col2:
            st.write("""
            **Follow Through Tips:**
            - Finish with weight on front foot
            - Belt buckle faces target
            - Hands high by lead shoulder
            - Balanced finish position
            - Hold the pose!
            """)

elif section == "Putting":
    st.header("⛳ Putting Basics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        img = create_demo_image("Putting", "Precision Matters", (46, 139, 87))
        st.image(img, caption="The Short Game", use_container_width=True)
    
    with col2:
        st.subheader("Putting Fundamentals:")
        st.write("""
        **Setup:**
        - Eyes directly over the ball
        - Pendulum motion from shoulders
        - Minimal wrist movement
        - Smooth, consistent tempo
        
        **Reading the Green:**
        - Look for slopes and breaks
        - Check from multiple angles
        - Consider grain direction
        - Practice speed control
        """)
    
    st.success("🎯 Remember: Drive for show, putt for dough!")

elif section == "Course Etiquette":
    st.header("🤝 Golf Course Etiquette")
    
    col1, col2 = st.columns(2)
    
    with col1:
        img = create_demo_image("Respect the Game", "Etiquette Matters", (178, 34, 34))
        st.image(img, caption="Be a Good Golf Citizen", use_container_width=True)
    
    with col2:
        st.subheader("Essential Rules:")
        st.write("""
        **On the Course:**
        - ✅ Repair divots and ball marks
        - ✅ Rake bunkers after use
        - ✅ Keep pace of play
        - ✅ Stay quiet during others' shots
        - ✅ Let faster groups play through
        
        **Safety First:**
        - ⚠️ Yell "FORE!" for errant shots
        - ⚠️ Wait for group ahead to clear
        - ⚠️ Stand to the side, not ahead
        """)
    
    st.info("📱 Tip: Keep your phone on silent and minimize usage on the course")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🏌️ Practice makes perfect! Enjoy your golf journey! ⛳</p>
</div>
""", unsafe_allow_html=True)
