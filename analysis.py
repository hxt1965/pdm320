import pandas as pd 
import matplotlib.pyplot as plt 
from controllers import demographics
import numpy as np

op_list = ['eminuse', 'intmob', 'intfreq', 'pial5a', 'pial5b', 'pial5c', 'pial5d',
                'pial11', 'pial11a', 'pial12', 'books1', 'books2a',
                'books2b', 'books2c']
dem_list = ['sex', 'age', 'marital', 'educ2', 'emplnw', 'inc', 'party', \
                'partyln', 'books1', 'state']

device_list = ['home4nw', 'bbhome1', 'bbhome2', 'device1a', 'smart2', \
                'device1b', 'device1c', 'device1d']

social_media = ['web1a', 'web1b', 'web1c', 'web1d', 'web1e']
social_media_names = ['Twitter', 'Instagram', 'Facebook', 'Snapchat', 'Youtube']

#People who use the internet - Opinions for several times a day
# People who dont use the internet, average age?
# opinions based on intmob = 1 or intmob = 2 
# bar plot for values of home4nw
# how many had a cell phone, how many smartphones 
# device 1 abcd against opinions 
# device 1 abcd against web 1abcd TIFSY

# People on twitter have polarizing opinions?
# Social media threshold? 


usage  = ['Nan', 'Several times a day', 'Once a day', 'few times a week', 'every few weeks', 'less often', 'Nan', 'nan', 'dont know', 'refused']
def plot_by_features(x, y, filename):
    return 

def main():
    df = pd.read_csv('trends.csv')
    op_df = df[op_list]
    high_school = df.where(df.educ2<=3)
    df_uni = df.where(df.educ2<=8)
    uni = df_uni.where(df_uni.educ2>3)
    #print(df_uni.head().educ2)
    pg = df.where(df.educ2>9)
    poor = df.where(df.party == 1)
    rich = df.where(df.party == 2)
    ind = df.where(df.party == 3)

    df['int_usage'] = np.full(len(df), 0)
    #print(df.int_usage)
    for i in range(len(df)):
        sum = 0
        for web in social_media:
            sum = sum + df[web][i] if df[web][i] <=9 else 9
        df.int_usage = float(sum/len(social_media))
    
    df_freq_apps_user = df.where(df['int_usage']>2.0)
    df_freq_apps_user2 = df.where(df['int_usage']<=2.0)
    ed = ['male', 'female']
    for i in ['pial5c', 'pial5d']:
        fig, ax = plt.subplots()
        width = -1/2.0
        track = 1/4.0
        cnt = 0
        c = ['r', 'g', 'b']
        for dat in df_freq_apps_user, df_freq_apps_user2:
            elements, counts = np.unique(dat[i], return_counts=True)
            elements = elements[:5]
            np.sort(elements)
            counts = counts[:5]
            counts = counts/np.sum(counts)
            print(elements, counts, )
            ax.bar(elements+width, counts,track, color=c[cnt])
            cnt = cnt+1
            width = width + 1/4.0
        #str_rep = ['Good thing', 'bad thing', 'some of both', 'dont know', 'refused']
        str_rep = ['Very hard', 'Somewhat hard', 'Not too hard', 'not hard at all', 'Impossible']
        ax.set_xticks(elements)
        ax.tick_params(axis = 'x', rotation = 20)
        ax.set_xticklabels(str_rep)
        plt.show()


def slice_by_dem(df, dem, val=None):
    return 

def show_demographics(df, dem):

    return 

if __name__ == '__main__':
    main()