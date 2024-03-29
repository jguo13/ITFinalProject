from __future__ import print_function
import basc_py4chan
import pandas as pd
import os
import time

#define important variables

board_name = 'pol'
filename = 'crawled_data.csv'
chinese_hate_speech_filename = "hatebase_vocab_chinese.csv"
asian_hate_speech_filename = "hatebase_vocab_asian.csv"

##########DONOT EDIT BELOW##################################################################

while True:
    try:
        df_chinese = pd.read_csv(hate_speech_filename)
        df_asian = pd.read_csv(asian_hate_speech_filename)
        list_id = []
        if os.path.isfile(filename):
            list_id = pd.read_csv(filename)["post_id"].to_list()
        
        df_total = pd.concat([df_chinese, df_asian])
        list_hate = df_total["term"]

        col_names = ["text_comment", "datetime", "post_id"]
        df_asian_hate = pd.DataFrame(columns = col_names)

        # get the board we want
        board = basc_py4chan.Board(board_name)

        # select the first thread on the board
        all_thread_ids = board.get_all_thread_ids()
        thread_list = []

        for id in all_thread_ids:

            first_thread_id = id
            thread = board.get_thread(first_thread_id)
            print("this is thread: ", thread)
            if thread == None:
                continue
            topic = thread.topic
            for thread in thread.all_posts:
                if any(s.lower() in thread.comment.lower() for s in list_hate) and thread.post_id not in list_id:
                    temp_dict = {}
                    temp_dict["text_comment"] = thread.text_comment
                    temp_dict["datetime"] = thread.datetime
                    temp_dict["post_id"] = thread.post_id
                    df_asian_hate = df_asian_hate.append(temp_dict, ignore_index = True)

        if not os.path.isfile(filename):
            df_asian_hate.to_csv(filename, header='column_names')

        else: # else it exists so append without writing the header
            df_asian_hate.to_csv(filename, mode='a', header=False)
    except:
        time.sleep(2)
        continue
