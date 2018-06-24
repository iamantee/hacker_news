import os 
from datetime import datetime
import json

from api_utils import API_Utils
from get_content import HTML_Utils 

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
                #api_utils.write_response_data(os.path.join(dir_path, str(story_id) + '.txt'))
                html_utils = HTML_Utils()
                html_utils.get_response(api_utils.api_response.json()["url"])
                
                print api_utils.api_response.json()["url"]
                
                with open("test.txt", 'w') as test_file:
                    #test_file.write(str(html_utils.response.__dict__))
                    json.dump(html_utils.response.json(), test_file)
                '''
                if os.path.exists(os.path.dirname(file_path)) == False:
                    try:
                        os.makedirs(os.path.dirname(file_path))
                    except OSError as ex:
                        raise ex
                    
                    with open(file_path, 'w') as content_file:
                        content_file.write(str(html_utils.responese.__dict__))
                '''

                break 


