"""
Contains application wide constants
"""
import json

from modules.analytics.sketch import QueryType
from modules.io.base import DataFormat, DataSource
from modules.util.hashes import HashFunctionFactory, Murmur3
from modules.util.validators import Validators
from paths import FileUtils


class Configs(object):
    default_config_file = "{0}/{1}".format(FileUtils.application_directory, "defaults.json")

    def __init__(self, **kwargs):
        self.__initialize_defaults()
        self.config = {}
        self.config.update(**kwargs)

    @staticmethod
    def __load_json_config_file(file_path=''):
        """
        Loads a json configuration file from a specified file_path
        :param file_path: the json config file path
        :return: the configuration map
        """
        json_config = {}

        with open(file_path) as config_file:
            json_config = json.load(config_file)

        return json_config

    @staticmethod
    def from_file(file_path='defaults.json'):
        file_path = FileUtils.get_absolute_path(file_path=file_path)

        if not Validators.is_valid_file(file_path=file_path):
            raise ValueError("Invalid config file: {0}".format(file_path))

        print("Obtaining application settings from file \"{0}\"".format(file_path))
        json_config = Configs.__load_json_config_file(file_path=file_path)
        # print("Using JSON configuration: ")
        # pprint.pprint(json_config)
        defaults = Configs(**json_config)
        defaults.__process_config()
        return defaults

    def __initialize_defaults(self):
        """
        Initialize default configurations
        """
        self.hash_function = Murmur3()
        self.hash_field_name = None

        self.data_format = {
            'type': DataFormat.COMMON_LOG,
            'params': DataFormat.metadata(data_format=DataFormat.COMMON_LOG)['params']
        }

        self.data_source = {
            'type': DataSource.FILE,
            'params': DataSource.metadata(data_source=DataSource.FILE)['params']
        }

        self.queries = []

    def __process_config(self):
        # initialize hash function
        hash_function_name = self.config['hash_function']
        self.hash_function = HashFunctionFactory.hash_function_for_name(name=hash_function_name)
        print("hash_function={0}".format(self.hash_function.__class__.__name__))

        self.hashed_properties = self.config['hashed_properties']
        print("hashed_properties={0}".format(self.hashed_properties))

        # initialize data format configurations
        self.__process_data_format_config()

        # initialize data source configurations
        self.__process_data_source_config()

        # initialize query configurations
        self.__process_query_config()

    def __process_data_format_config(self):
        """
        Process data format configurations
        """
        data_format_config = self.config['data_format']
        data_format_name = data_format_config['type']

        data_format = DataFormat.for_name(name=data_format_name)
        print("data_format={0}".format(data_format))

        data_format_metadata = DataFormat.metadata(data_format=data_format)
        data_format_params = data_format_metadata['params']
        data_format_params.update(data_format_config['params'])
        print("data_format[params]={0}".format(data_format_params))

        self.data_format.update({
            'type': data_format,
            'params': data_format_params
        })

        # initialize data format parameters
        if data_format == DataFormat.XML:
            if not data_format_params['xml_element']:
                raise ValueError("Invalid xml element: \"{0}\"".format(data_format_params['xml_element']))

        elif data_format == DataFormat.DELIMITED_TEXT:
            if not data_format_params['field_delimiter']:
                raise ValueError("Invalid field delimiter: \"{0}\"".format(data_format_params['field_delimiter']))
            elif not data_format_params['record_delimiter']:
                raise ValueError("Invalid record delimiter: \"{0}\"".format(data_format_params['record_delimiter']))

        if data_format in [DataFormat.TSV, DataFormat.CSV, DataFormat.DELIMITED_TEXT]:
            first_data_line_number = data_format_params['first_data_line_number']

            if not first_data_line_number:
                raise ValueError("Invalid first data line number: \"{0}\"".format(first_data_line_number))

    def __process_data_source_config(self):
        """
        Process data source configurations
        """
        # initialize data source
        data_source_config = self.config['data_source']
        data_source_name = data_source_config['type']
        data_source_type = DataSource.for_name(name=data_source_name)

        print("data_source={0}".format(data_source_type))
        data_source_metadata = DataSource.metadata(data_source=data_source_type)
        data_source_params = data_source_metadata['params']
        data_source_params.update(data_source_config['params'])

        print("data_source[params]={0}".format(data_source_params))

        self.data_source.update({
            'type': data_source_type,
            'params': data_source_params
        })

        # initialize data source parameters
        if data_source_type == DataSource.FILE:
            data_file = data_source_params['data_file']

            if not Validators.is_valid_file(data_file):
                raise ValueError("Invalid data file: \"{0}\"".format(data_file))

        elif data_source_type == DataSource.IN_MEMORY:
            data_contents = data_source_params['data_contents']

            if not data_contents:
                raise ValueError("Invalid in-memory data contents: \"{0}\"".format(data_contents))

        else:
            request_uri = data_source_params.get('request_uri', '')
            request_method = data_source_params.get('request_method', '')

            if not request_uri or not Validators.is_url(request_uri):
                raise ValueError("Invalid HTTP request URI: \"{0}\"".format(request_uri))

            if not Validators.is_http_method(request_method):
                raise ValueError("Invalid HTTP request method: \"{0}\"".format(request_method))

    def __process_query_config(self):
        """
        Process query configurations
        """
        queries_config = self.config['queries']

        print('query_count={0}'.format(len(queries_config)))
        for index, query_config in enumerate(queries_config):
            query_type_name = query_config['type']
            query_params = query_config['params']
            query_type = QueryType.for_name(name=query_type_name)

            print("query_type[{0}]={1}".format(index, query_type))
            print("query_type[{0}][params]={1}".format(index, query_params))

            self.queries.append({
                'type': query_type,
                'params': query_params
            })
