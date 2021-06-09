# Count Min Sketch Stream Processor
# Execution
To run the stream processor application:

1. Create a JSON config file similar to the ones in the *"configs"* folder of the source directory
 and using the guidelines in the Configuration section below
2. Execute the *application.py* file
3. When asked for the configuration file location, enter the location to the config file
 (use absolute path if outside the application source directory)


# Configuration
The runtime configuration file is a JSON file specifying the runtime parameters for the stream processor application.

## Hash Function Configurations
The following are a list of supported hash algorithms/functions:

- **Murmur3**
- **Murmur2**
- **Md5**
- **Sha256**
- **Djb2**
- **Djb2a**
- **Fnv1**
- **Fnv1a**
- **Sdbm**

Below is an example configuration for the hash function section of the config file:
```json
{
  "hash_algorithm": "murmur3"
}
```

## Query Types Configurations
The following are a list of supported Query types:

- **Point_Query**
- **K Minimum Query**
- **K Maximum Query**
- **Range Query**

Below are example configurations for the queries section of the config file:
It contains *2 point queries, 1 k-minimum query, 1 k-maximum query and 1 range query*
```json
{
    "queries": [
        {
          "type": "point_query",
          "params": {
            "item": "Animal's Action"
          }
        },
        {
          "type": "point_query",
          "params": {
            "item": "Unsafe Lane Changing"
          }
        },
        {
          "type": "k_maximum_query",
          "params": {
            "k": 5
          }
        },
        {
          "type": "k_minimum_query",
          "params": {
            "k": 5
          }
        },
        {
          "type": "range_query",
          "params": {}
        }
    ]
}
```

## Data Format Configurations
The following are the supported data formats:

- **XML**
- **CSV (Comma-Separated Values)**
- **TSV (Tab-Separated Values)**
- **COMMON_LOG (Common Log Format)**

Below is an example configurations for the data format section of the config file:
1. For data sources in **XML data format**, the *xml_element* is the XML tag represent each data set item:
```json
{
    "data_format": {
        "type": "xml",
        "params": {
            "xml_element": ""
        }
    }
}
```
2. For data sources in **CSV or TSV data formats**, *has_headers* is true if the CSV/TSV file has a header row as the first row,
*first_data_line_number* is the row in which the actual data set items start:
```json
{
    "data_format": {
        "type": "csv",
        "params": {
            "has_headers": true,
            "first_data_line_number": 1
        }
    }
}
```

3. For data sources in **CommonLog format**:
```json
{
    "data_format": {
        "type": "common_log",
        "params": {}
    }
}
```

## Data Source Configurations
The following are the supported data source types:

- **File**
- **Web**
- **In_Memory**

Below are example configurations for the data source section of the config file:

For **File data sources**, the *data_file* attribute should contain the file path of the data file:
```json
{
    "data_source": {
        "type": "file",
        "params": {
            "data_file": ""
        }
    }
}
```
For **Web based data sources**, the *request_uri* is the web address of the data source, *request_method* is the HTTP method (defaults to *GET*):
```json
{
    "data_source": {
        "type": "web",
        "params": {
            "request_uri": "",
            "request_method": "GET",
            "request_body": "",
            "request_headers": {}
        }
    }
}
```

For **in-memory / clipboard data sources**, the *data_contents* should contain the entire dataset for processing:
```json
{
    "data_source": {
        "type": "in_memory",
        "params": {
            "data_contents": ""
        }
    }
}
```