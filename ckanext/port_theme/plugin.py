import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.lib.helpers as helpers
import json 

def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(data_dict={'sort': 'package_count desc', 'all_fields': True})

    # Truncate the list to the 10 most popular groups only.
    groups = groups[:12]

    return groups


def new_datasets_homepage():
   
    new_datasets = toolkit.get_action('package_search')(
        data_dict={'sort': 'metadata_created desc', 'all_fields': True})

    new_datasets = new_datasets[:3]

    return new_datasets


def get_summary_list(num_packages):
    list_without_summary = toolkit.get_action('package_search')(data_dict={'rows': num_packages, 'sort': 'metadata_modified desc'})['results']
    list_with_summary = []
    for package in list_without_summary:
        list_with_summary.append(toolkit.get_action('package_show')(
            data_dict={'id': package['name'], 'include_tracking': False})
        )
    return list_with_summary


def get_summary_list_sort(num_packages):
    list_without_summary = toolkit.get_action('package_search')(data_dict={'rows': num_packages, 'sort': 'views_recent desc'})['results']
    list_with_summary = []
    for package in list_without_summary:
        list_with_summary.append(toolkit.get_action('package_show')(
            data_dict={'id': package['name'], 'include_tracking': False})
        )
    return list_with_summary

def get_showcase_items():
    showcase = toolkit.get_action('ckanext_showcase_list')(data_dict={})
    sortedshowcase = sorted(showcase, key = lambda i: i['metadata_modified'],reverse = True)
    showcase = sortedshowcase
    showcase = showcase[:4]
    return showcase


class Port_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IPackageController, inherit=True)
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'port_theme')


    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        

	return {
             'example_theme_most_popular_groups': most_popular_groups,
	     'new_datasets_homepage': new_datasets_homepage,
	     'get_summary_list': get_summary_list,
	     'get_summary_list_sort': get_summary_list_sort,
	     'get_showcase_items': get_showcase_items,
        }





@helpers.core_helper
def gravatar(email_hash, size=100, default=None):
    return helpers.literal('''
        <svg style="vertical-align:middle;" class="gravatar" width="{size}" height="{size}">
        <circle r="{r1}" cx="{center}" cy="{center2}" fill="#7a99ca" stroke="#5582bf" stroke-width="{stroke_width}"/>
        <circle r="{r2}" cx="{center}" cy="{center}" fill="#7a99ca" stroke="#5582bf" stroke-width="{stroke_width}"/>
        </svg>'''.format(size=size, center=size/2, r1=size/3, r2=size/6,
                         fill1=email_hash[:6], fill2=email_hash[6:12],
                         stroke_width=size/100, center2=size*0.9))

@helpers.core_helper
def linked_gravatar(email_hash, size=100, default=None):
    return gravatar(email_hash, size, default)

helpers.gravatar = gravatar
helpers.linked_gravatar = gravatar



