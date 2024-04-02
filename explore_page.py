import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def load_data():
    df = pd.read_csv("Salary_Data.csv")
    df = df[['Education Level', 'Job Title', 'Years of Experience', 'Salary']]
    df = df[df['Salary'].notnull()]
    df = df.dropna()
    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] >= 10000]
    
    # Filter out job titles appearing less than 25 times
    job_title_counts = df['Job Title'].value_counts()
    job_title_edited = job_title_counts[job_title_counts >= 25]
    df = df[df['Job Title'].isin(job_title_edited.index)]
    
    # Replace values in 'Education Level' column
    df['Education Level'] = df['Education Level'].replace(["Bachelor's Degree", "Master's Degree", "phD"], ["Bachelor's", "Master's", "PhD"])

    return df

def show_explore_page():
    """
    This function displays the explore page with visualizations for job salaries.
    """
    st.title("Explore Job Salaries")

    st.write(
        """
        
        """
    )

    # Load data (replace with your data loading logic)
    df = load_data()

    # Get the top 10 highest paying job titles
    top_10_highest_paying_jobs = df.groupby('Job Title')['Salary'].mean().nlargest(10)

    # Create a single bar plot for the top 10 highest paying job titles and their mean salaries
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=top_10_highest_paying_jobs.index, y=top_10_highest_paying_jobs.values, ax=ax)

    # Customize the plot
    ax.set_xlabel('Job Title')
    ax.set_ylabel('Mean Salary')
    ax.set_title('Top 10 Highest Paying Jobs')
    plt.xticks(rotation=45)  # Rotate x-axis labels if needed
    plt.tight_layout()

    # Display the plot using Streamlit
    st.pyplot(fig)

    # Distribution of Salary based on Education Level
    st.write(
        """
        #### Distribution of Mean Salary based on Education Level
        """
    )

    data_education_salary = df.groupby(['Education Level'])['Salary'].mean().sort_values(ascending=False)
    st.bar_chart(data_education_salary)

    # Distribution of Salary based on Years of Experience
    st.write(
        """
        #### Distribution of Salary based on Years of Experience
        """
    )

    data_experience_salary = df.groupby(['Years of Experience'])['Salary'].mean().sort_index()
    plt.figure(figsize=(10, 6))
    plt.plot(data_experience_salary.index, data_experience_salary.values, marker='o', linestyle='-')
    plt.xlabel('Years of Experience')
    plt.ylabel('Mean Salary')
    plt.title('Mean Salary based on Years of Experience')
    plt.grid(True)
    st.pyplot(plt)

if __name__ == '__main__':
    show_explore_page()

