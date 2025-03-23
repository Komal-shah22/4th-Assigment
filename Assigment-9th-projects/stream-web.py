
import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
from PIL import Image
import os

# Initialize Database
def init_db():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    
    # Blog table create/update
    c.execute('''CREATE TABLE IF NOT EXISTS blog
                 (id INTEGER PRIMARY KEY, title TEXT, content TEXT, category TEXT, date TEXT, image_path TEXT, likes INTEGER DEFAULT 0)''')

    # Comments table
    c.execute('''CREATE TABLE IF NOT EXISTS comments
                 (id INTEGER PRIMARY KEY, blog_id INTEGER, comment TEXT, date TEXT)''')

    conn.commit()
    conn.close()

# Function to add a blog
def add_blog(title, content, category, image_path):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("INSERT INTO blog (title, content, category, image_path, date, likes) VALUES (?, ?, ?, ?, ?, 0)", 
              (title, content, category, image_path, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# Function to delete a blog
def delete_blog(blog_id):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("DELETE FROM blog WHERE id = ?", (blog_id,))
    c.execute("DELETE FROM comments WHERE blog_id = ?", (blog_id,))
    conn.commit()
    conn.close()

# Function to get blogs (filtered by category)
def get_blogs(category="All"):
    conn = sqlite3.connect("blog.db")
    query = "SELECT * FROM blog ORDER BY date DESC"
    
    if category != "All":
        query = f"SELECT * FROM blog WHERE category='{category}' ORDER BY date DESC"

    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Function to like a blog
def like_blog(blog_id):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("UPDATE blog SET likes = likes + 1 WHERE id = ?", (blog_id,))
    conn.commit()
    conn.close()

# Function to add a comment
def add_comment(blog_id, comment):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("INSERT INTO comments (blog_id, comment, date) VALUES (?, ?, ?)", 
              (blog_id, comment, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# Function to get comments for a blog
def get_comments(blog_id):
    conn = sqlite3.connect("blog.db")
    df = pd.read_sql(f"SELECT * FROM comments WHERE blog_id={blog_id} ORDER BY date DESC", conn)
    conn.close()
    return df

# Initialize DB
init_db()

# Streamlit UI
st.set_page_config(page_title="My Blog", page_icon="📝", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Blog Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "✍️ Write a Blog", "📚 Browse Blogs"])

# Home Page
if page == "🏠 Home":
    st.title("📝 Welcome to My Blog!")
    st.write("A simple and interactive blog website where you can read and write blogs!")
    st.image("https://images.unsplash.com/photo-1535378917042-10a22c95931a?q=80&w=1448&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", use_container_width=True)

# Write Blog Page
elif page == "✍️ Write a Blog":
    st.title("✍️ Write a New Blog")
    title = st.text_input("Blog Title")
    content = st.text_area("Blog Content", height=200)
    category = st.selectbox("Select Category", ["Technology", "Lifestyle", "Education", "Health", "Others"])

    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
    image_path = ""

    if uploaded_image:
        image_path = f"images/{uploaded_image.name}"
        os.makedirs("images", exist_ok=True)

        # Resize Image
        img = Image.open(uploaded_image)
        img = img.resize((300, 300))
        img.save(image_path)


    if st.button("Publish Blog 📝"):
       if title and content:
        add_blog(title, content, category, image_path)
        st.toast("✅ Blog Published Successfully!", icon="✅")
        st.rerun()
    else:
        st.error("⚠️ Title and Content cannot be empty!")


# Browse Blogs Page
elif page == "📚 Browse Blogs":
    st.title("📚 All Blogs")

    category_filter = st.selectbox("Filter by Category", ["All", "Technology", "Lifestyle", "Education", "Health", "Others"])
    blogs = get_blogs(category_filter)

    for _, row in blogs.iterrows():
        with st.container():
            st.markdown(f"### 📝 {row['title']} ({row['category']})")
            
            if row['image_path']:
                st.image(row['image_path'], width=300) 

            st.write(row['content'])
            st.caption(f"🕒 {row['date']}")

            col1, col2, col3 = st.columns([1, 2, 2])
            
            with col1:
                if st.button(f"👍 {row['likes']}", key=f"like_{row['id']}"):
                    like_blog(row['id'])
                    st.rerun()
            
            with col2:
                comment = st.text_input("💬 Add a Comment", key=f"comment_{row['id']}")
                if st.button("Post Comment", key=f"post_{row['id']}"):
                    if comment:
                        add_comment(row['id'], comment)
                        st.success("✅ Comment Added!")
                        st.rerun()

            with col3:
                if st.button("🗑 Delete Blog", key=f"delete_{row['id']}"):
                    delete_blog(row['id'])
                    st.warning("🗑 Blog Deleted!")
                    st.rerun()

            comments = get_comments(row['id'])
            if not comments.empty:
                st.subheader("Comments:")
                for _, comm in comments.iterrows():
                    st.write(f"🗨 {comm['comment']} - _{comm['date']}_")





