import os 
from datetime import datetime
import json

from api_utils import API_Utils

if __name__ == '__main__':
    # get directory path 
    dir_path = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(dir_path, 'data')
    dir_path = os.path.join(dir_path, datetime.now().strftime('%Y%m%d_%H%M%S'))

    # construct API instance
    api_utils = API_Utils()

    # get top story ids
    if api_utils.call_api('v0', 'topstories', 'pretty'):
       api_utils.write_response_data(os.path.join(dir_path, 'top_story_ids.txt'))
        top_story_ids = api_utils.api_response.json()

        for story_id in top_story_ids:
            if api_utils.call_api('v0', 'item/' + str(story_id), 'pretty'):
                api_utils.write_response_data(os.path.join(dir_path, str(story_id) + '.txt'))
