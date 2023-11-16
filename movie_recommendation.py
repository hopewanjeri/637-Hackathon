import pandas as pd


file_path = 'data.txt'  
data = pd.read_csv(file_path)

print("Original Data:")
print(data.head())

data.drop_duplicates(inplace=True)


cleaned_file_path = 'data.txt'  
data.to_csv(cleaned_file_path, index=False)


print("\nCleaned Data:")
print(data.head())
top_rated_movies = data.groupby('Movie')['Rating'].mean().sort_values(ascending=False)
print("\nTop Rated Movies:")
print(top_rated_movies.head(10))



user_movie_matrix = data.pivot_table(index='User', columns='Movie', values='Rating')
def recommend_movies(user, n=5):
    if user in user_movie_matrix.index:
        
        from sklearn.metrics.pairwise import cosine_similarity

        
        user_similarity_matrix = cosine_similarity(user_movie_matrix.fillna(0))

    
        user_similarity_df = pd.DataFrame(user_similarity_matrix, index=user_movie_matrix.index, columns=user_movie_matrix.index)
    else:
        
        popular_movies = data.groupby('Movie')['Rating'].mean().sort_values(ascending=False).head(n)
        return popular_movies.index.tolist()
import tkinter as tk
from tkinter import messagebox

def get_recommendations_for_user(user_name, num_recommendations=5):
    recommended_movies = recommend_movies(user_name, n=num_recommendations)
    return recommended_movies

def display_recommendations(recommended_movies):
    recommendations_window = tk.Tk()
    recommendations_window.title("Movie Recommendations")
    
    label = tk.Label(recommendations_window, text="Recommended Movies:", font=("Arial", 12))
    label.pack()

    for i, movie in enumerate(recommended_movies, start=1):
        movie_label = tk.Label(recommendations_window, text=f"{i}. {movie}", font=("Arial", 10))
        movie_label.pack()

    recommendations_window.mainloop()

def get_user_recommendations():
    user_name = entry_name.get()
    if user_name.strip() == "":
        messagebox.showwarning("Warning", "Please enter your name.")
    else:
        recommended_movies = get_recommendations_for_user(user_name)
        if recommended_movies:
            display_recommendations(recommended_movies)
        else:
            messagebox.showinfo("Info", "Sorry, no recommendations available at the moment.")


root = tk.Tk()
root.title("Movie Recommender")


label_name = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label_name.pack()

entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack()


btn_recommend = tk.Button(root, text="Get Recommendations", command=get_user_recommendations, font=("Arial", 12))
btn_recommend.pack()

root.mainloop()
