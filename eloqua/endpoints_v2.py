"""
API MAPPING FOR Eloqua API V2
"""

mapping_table = {

    'content_type': 'application/json',
    'path_prefix': '/API/REST/2.0',

    # Campaigns
    'get_campaign': {
        'method': 'GET',
        'path': '/assets/campaign/{{campaign_id}}',
        'valid_params': ['depth']
    },
    'list_campaigns': {
        'method': 'GET',
        'path': '/assets/campaigns',
        'valid_params': ['depth','count','page','search','sort','dir','orderBy','lastUpdatedAt']
    },

}
