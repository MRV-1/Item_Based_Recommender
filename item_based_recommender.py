###########################################
# Item-Based Collaborative Filtering
###########################################

# Veri seti: https://grouplens.org/datasets/movielens/

"""
Online bir film izleme platformu (kuzukuzu.tv) iş birlikçi filtreleme yöntemi ile bir öneri sistemi geliştirmek istemektedir.
İçerik temelli öneri sistemlerini deneyen şirket topluluğun kanaatlerini barındıracak şekilde öneriler geliştirmek istemektedir.
Kullanıcılar bir film beğendiğinde o film ile benzer beğenilme örüntüsüne sahip olan diğer filmler önerilmek istenmektedir.

veri seti hikayesi
MovieLens isimli firma tarafından sağlanmıştır.
İçerisinde filmler ve bu filmlere verilen puanları barındırmaktadır.
Veri seti yaklaşık 27000 film için yaklaşık 2000000 derecelendirme içermektedir.

"""



# Adım 1: Veri Setinin Hazırlanması
# Adım 2: User Movie Df'inin Oluşturulması
# Adım 3: Item-Based Film Önerilerinin Yapılması
# Adım 4: Çalışma Scriptinin Hazırlanması

######################################
# Adım 1: Veri Setinin Hazırlanması
######################################
import pandas as pd
pd.set_option('display.max_columns', 500)
movie = pd.read_csv( r'C:\Users\MerveATASOY\Desktop\data_scientist_miuul\egitim_teorik_icerikler\Bolum_6_Tavsiye_Sistemleri\dataset\movie_lens_dataset\movie.csv')
rating = pd.read_csv(r'C:\Users\MerveATASOY\Desktop\data_scientist_miuul\egitim_teorik_icerikler\Bolum_6_Tavsiye_Sistemleri\dataset\movie_lens_dataset\rating.csv')
df = movie.merge(rating, how="left", on="movieId")
df.head()


######################################
# Adım 2: User Movie Df'inin Oluşturulması
######################################
# temel amaç bu adım

# bir kullanıcı sadece bir filme puan vermiş olsun bu durumda user_movie_df'de bütün filmler için bir hücre teşkil edecektir
# bu durum hesaplama işlemlerinde gecikmeye ve performans problemlerine sebep olmaktdır
# hem bu duruma çözüm  hemde kullanıcıların hiç izlemedikleri filmlere film önermeyeceklerinden dolayı yapılması gereken bazı indirgeme işlemleri vardır
# 1000'den az sayıda rate almış filmleri çalışmanın dışından bırakmak çözüm olabilir


df.head()
df.shape    # yaklaşık 20 milyon yorum var

df["title"].nunique()    # toplam 27 bin küsür film var

# soru : 10.000 yorum alaan filmde var, 30 yorum alan filmde var hepsine odaklanmalı mıyım gerçekten?

df["title"].value_counts().head()  #titleların value_counts'u hangi filmin kaç tane rate aldıkları bulunur


comment_counts = pd.DataFrame(df["title"].value_counts())
rare_movies = comment_counts[comment_counts["count"] <= 1000].index    #24103 film 1000dene az rate'e sahiptir
common_movies = df[~df["title"].isin(rare_movies)]                     # bu df'de bu isimleri barındırmayanları getireceğim
common_movies.shape
common_movies["title"].nunique()
df["title"].nunique()

#gelen bilgiler üzerinde öyle bir işlem yapılmalı ki satırlarda kullanıcılar, sutunlarda ise title'lar olsun

user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
#pivot_table indexe hangi değişken gelecek, sutuna hangi değişken gelecek, bunların kesişimine ne gelecek sorularına olan cevaba ait verileri alır


user_movie_df.shape  #(138493, 3159)  (user, film)
user_movie_df.columns


######################################
# Adım 3: Item-Based Film Önerilerinin Yapılması
######################################

movie_name = "Matrix, The (1999)"
movie_name = "Ocean's Twelve (2004)"
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)


movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)


# girilen keyword'e ait tüm filmleri getirir
def check_film(keyword, user_movie_df):
    return [col for col in user_movie_df.columns if keyword in col]

check_film("Insomnia", user_movie_df)


######################################
# Adım 4: Çalışma Scriptinin Hazırlanması
######################################

def create_user_movie_df():
    import pandas as pd
    movie = pd.read_csv(r'C:\Users\MerveATASOY\Desktop\data_scientist_miuul\egitim_teorik_icerikler\Bolum_6_Tavsiye_Sistemleri\dataset\movie_lens_dataset\movie.csv')
    rating = pd.read_csv(r'C:\Users\MerveATASOY\Desktop\data_scientist_miuul\egitim_teorik_icerikler\Bolum_6_Tavsiye_Sistemleri\dataset\movie_lens_dataset\rating.csv')
    df = movie.merge(rating, how="left", on="movieId")
    comment_counts = pd.DataFrame(df["title"].value_counts())
    rare_movies = comment_counts[comment_counts["count"] <= 1000].index
    common_movies = df[~df["title"].isin(rare_movies)]
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return user_movie_df

user_movie_df = create_user_movie_df()

# verilen film ve diğer filmlerin beğenilme patternlerine bakar, ardından 10 tan corelasyonu yüksek film getirir
def item_based_recommender(movie_name, user_movie_df):
    movie_name = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)

item_based_recommender("Matrix, The (1999)", user_movie_df)

# Sonuçlar  geç dönüyor; db'ye sonuçlar aktarılmalı ve web sitesi arayüzünden önerilmesi gereken filmler indexler(db'de) vasıtasıyla hızlıca döndürülür


movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]

item_based_recommender(movie_name, user_movie_df)





