#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com

import tempfile
from os.path import expanduser, join

from derpconf import config
from derpconf.config import Config

from thumbor import __version__
from thumbor.filters import BUILTIN_FILTERS
from thumbor.handler_lists import BUILTIN_HANDLERS

HOME = expanduser("~")

Config.define("THUMBOR_LOG_CONFIG", None, "Logging configuration as json", "Logging")
Config.define(
    "THUMBOR_LOG_FORMAT",
    "%(asctime)s %(name)s:%(levelname)s %(message)s",
    "Log Format to be used by thumbor when writing log messages.",
    "Logging",
)

Config.define(
    "THUMBOR_LOG_DATE_FORMAT",
    "%Y-%m-%d %H:%M:%S",
    "Date Format to be used by thumbor when writing log messages.",
    "Logging",
)

Config.define(
    "MAX_WIDTH",
    0,
    "Max width in pixels for images read or generated by thumbor",
    "Imaging",
)
Config.define(
    "MAX_HEIGHT",
    0,
    "Max height in pixels for images read or generated by thumbor",
    "Imaging",
)
Config.define(
    "MAX_PIXELS", 75e6, "Max pixel count for images read by thumbor", "Imaging"
)
Config.define(
    "MIN_WIDTH",
    1,
    "Min width in pixels for images read or generated by thumbor",
    "Imaging",
)
Config.define(
    "MIN_HEIGHT",
    1,
    "Min width in pixels for images read or generated by thumbor",
    "Imaging",
)
Config.define(
    "ALLOWED_SOURCES",
    [],
    "Allowed domains for the http loader to download. These are regular expressions.",
    "Imaging",
)
Config.define("QUALITY", 80, "Quality index used for generated JPEG images", "Imaging")
Config.define(
    "PROGRESSIVE_JPEG",
    True,
    "Exports JPEG images with the `progressive` flag set.",
    "Imaging",
)

Config.define(
    "PILLOW_JPEG_SUBSAMPLING",
    None,
    "Specify subsampling behavior for Pillow (see `subsampling` \
              in http://pillow.readthedocs.org/en/latest/handbook/image-file-formats.html#jpeg)."
    'Be careful to use int for 0,1,2 and string for "4:4:4" notation. '
    "Will ignore `quality`. Using `keep` will copy the original file's subsampling.",
    "Imaging",
)

Config.define(
    "PILLOW_JPEG_QTABLES",
    None,
    "Specify quantization tables for Pillow (see `qtables` \
              in http://pillow.readthedocs.org/en/latest/handbook/image-file-formats.html#jpeg). "
    "Will ignore `quality`. Using `keep` will copy the original file's qtables.",
    "Imaging",
)

Config.define(
    "PILLOW_RESAMPLING_FILTER",
    "LANCZOS",
    "Specify resampling filter for Pillow resize method."
    "One of LANCZOS, NEAREST, BILINEAR, BICUBIC, HAMMING (Pillow>=3.4.0).",
    "Imaging",
)

Config.define(
    "WEBP_QUALITY",
    None,
    "Quality index used for generated WebP images. If not set (None) the same level of "
    "JPEG quality will be used. If 100 the `lossless` flag will be used.",
    "Imaging",
)

Config.define(
    "PNG_COMPRESSION_LEVEL",
    6,
    "Compression level for generated PNG images.",
    "Imaging",
)
Config.define(
    "PILLOW_PRESERVE_INDEXED_MODE",
    True,
    "Indicates if final image should preserve indexed mode (P or 1) of original image",
    "Imaging",
)
Config.define(
    "AUTO_WEBP",
    False,
    "Specifies whether WebP format should be used automatically if the request accepts it "
    "(via Accept header)",
    "Imaging",
)
Config.define(
    "AUTO_PNG_TO_JPG",
    False,
    "Specifies whether a PNG image should be used automatically if the png image has "
    "no transparency (via alpha layer). "
    "WARNING: Depending on case, this is not a good deal. "
    "This transformation maybe causes distortions or the size of image can increase. "
    "Images with texts, for example, the result image maybe will be distorced. "
    "Dark images, for example, the size of result image maybe will be bigger. "
    "You have to evaluate the majority of your use cases "
    "to take a decision about the usage of this conf.",
    "Imaging",
)
Config.define(
    "SVG_DPI",
    150,
    "Specify the ratio between 1in and 1px for SVG images. This is only used when"
    "rasterizing SVG images having their size units in cm or inches.",
    "Imaging",
)
Config.define(
    "MAX_AGE",
    24 * 60 * 60,
    "Max AGE sent as a header for the image served by thumbor in seconds",
    "Imaging",
)
Config.define(
    "MAX_AGE_TEMP_IMAGE",
    0,
    "Indicates the Max AGE header in seconds for "
    "temporary images (images with failed smart detection)",
    "Imaging",
)
Config.define(
    "RESPECT_ORIENTATION",
    False,
    "Indicates whether thumbor should rotate images that have an Orientation EXIF header",
    "Imaging",
)
Config.define(
    "IGNORE_SMART_ERRORS",
    False,
    "Ignore errors during smart detections and return image "
    "as a temp image (not saved in result storage and with MAX_AGE_TEMP_IMAGE age)",
    "Imaging",
)

Config.define(
    "SEND_IF_MODIFIED_LAST_MODIFIED_HEADERS",
    False,
    "Sends If-Modified-Since & Last-Modified headers; requires support from result storage",
    "Imaging",
)

Config.define(
    "PRESERVE_EXIF_INFO",
    False,
    "Preserves exif information in generated images. "
    "Increases image size in kbytes, use with caution.",
    "Imaging",
)

Config.define(
    "ALLOW_ANIMATED_GIFS",
    True,
    "Indicates whether thumbor should enable the EXPERIMENTAL support for animated gifs.",
    "Imaging",
)

Config.define(
    "USE_GIFSICLE_ENGINE",
    False,
    "Indicates whether thumbor should use gifsicle engine. "
    "Please note that smart cropping and filters are not "
    "supported for gifs using gifsicle (but won't give an error).",
    "Imaging",
)

Config.define(
    "USE_BLACKLIST",
    False,
    "Indicates whether thumbor should enable blacklist "
    "functionality to prevent processing certain images.",
    "Imaging",
)

Config.define(
    "ENGINE_THREADPOOL_SIZE",
    0,
    "Size of the thread pool used for image transformations."
    " The default value is 0 (don't use a threadpoool. "
    "Increase this if you are seeing your IOLoop getting "
    "blocked (often indicated by your upstream HTTP "
    "requests timing out)",
    "Imaging",
)

Config.define(
    "METRICS",
    "thumbor.metrics.logger_metrics",
    "The metrics backend thumbor should use to measure internal actions."
    " This must be the full name of a python module "
    "(python must be able to import it)",
    "Extensibility",
)
Config.define(
    "LOADER",
    "thumbor.loaders.http_loader",
    "The loader thumbor should use to load the original image. "
    "This must be the full name of a python module "
    "(python must be able to import it)",
    "Extensibility",
)
Config.define(
    "STORAGE",
    "thumbor.storages.file_storage",
    "The file storage thumbor should use to store original images."
    " This must be the full name of a python module "
    "(python must be able to import it)",
    "Extensibility",
)
Config.define(
    "RESULT_STORAGE",
    None,
    "The result storage thumbor should use to store generated "
    "images. This must be the full name of a python "
    "module (python must be able to import it)",
    "Extensibility",
)
Config.define(
    "ENGINE",
    "thumbor.engines.pil",
    "The imaging engine thumbor should use to perform image "
    "operations. This must be the full name of a "
    "python module (python must be able to import it)",
    "Extensibility",
)

Config.define(
    "GIF_ENGINE",
    "thumbor.engines.gif",
    "The gif engine thumbor should use to perform image operations."
    " This must be the full name of a "
    "python module (python must be able to import it)",
    "Extensibility",
)

Config.define(
    "SECURITY_KEY",
    "MY_SECURE_KEY",
    "The security key thumbor uses to sign image URLs",
    "Security",
)

Config.define(
    "ALLOW_UNSAFE_URL",
    True,
    "Indicates if the /unsafe URL should be available",
    "Security",
)
Config.define("ENABLE_ETAGS", True, "Enables automatically generated etags", "HTTP")
Config.define(
    "MAX_ID_LENGTH",
    32,
    "Set maximum id length for images when stored",
    "Storage",
)
Config.define(
    "GC_INTERVAL",
    None,
    "Set garbage collection interval in seconds",
    "Performance",
)

Config.define(
    "HEALTHCHECK_ROUTE", r"/healthcheck/?", "Healthcheck route.", "Healthcheck"
)

# METRICS OPTIONS
Config.define("STATSD_HOST", None, "Host to send statsd instrumentation to", "Metrics")
Config.define("STATSD_PORT", 8125, "Port to send statsd instrumentation to", "Metrics")
Config.define("STATSD_PREFIX", None, "Prefix for statsd", "Metrics")

# FILE LOADER OPTIONS
Config.define(
    "FILE_LOADER_ROOT_PATH",
    HOME,
    "The root path where the File Loader will try to find images",
    "File Loader",
)

# HTTP LOADER OPTIONS
Config.define(
    "HTTP_LOADER_CONNECT_TIMEOUT",
    5,
    "The maximum number of seconds libcurl can take to connect to an image being loaded",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_REQUEST_TIMEOUT",
    20,
    "The maximum number of seconds libcurl can take to download an image",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_FOLLOW_REDIRECTS",
    True,
    "Indicates whether libcurl should follow redirects when downloading an image",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_MAX_REDIRECTS",
    5,
    "Indicates the number of redirects libcurl should follow when downloading an image",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_MAX_CLIENTS",
    10,
    "The maximum number of simultaneous HTTP connections the loader can make before queuing",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_FORWARD_USER_AGENT",
    False,
    "Indicates whether thumbor should forward the user agent of the requesting user",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_FORWARD_ALL_HEADERS",
    False,
    "Indicates whether thumbor should forward the headers of the request",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_FORWARD_HEADERS_WHITELIST",
    [],
    "Indicates which headers should be forwarded among all the headers of the request",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_DEFAULT_USER_AGENT",
    f"Thumbor/{__version__}",
    "Default user agent for thumbor http loader requests",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_PROXY_HOST",
    None,
    "The proxy host needed to load images through",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_PROXY_PORT",
    None,
    "The proxy port for the proxy host",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_PROXY_USERNAME",
    None,
    "The proxy username for the proxy host",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_PROXY_PASSWORD",
    None,
    "The proxy password for the proxy host",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_CA_CERTS",
    None,
    "The filename of CA certificates in PEM format",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_VALIDATE_CERTS",
    None,
    "Validate the server’s certificate for HTTPS requests",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_CLIENT_KEY",
    None,
    "The filename for client SSL key",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_CLIENT_CERT",
    None,
    "The filename for client SSL certificate",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_CURL_ASYNC_HTTP_CLIENT",
    False,
    "If the CurlAsyncHTTPClient should be used",
    "HTTP Loader",
)
Config.define(
    "HTTP_LOADER_CURL_LOW_SPEED_TIME",
    0,
    "If HTTP_LOADER_CURL_LOW_SPEED_LIMIT and HTTP_LOADER_CURL_ASYNC_HTTP_CLIENT "
    + "are set, then this is the time in seconds as integer after a download should "
    + "timeout if the speed is below HTTP_LOADER_CURL_LOW_SPEED_LIMIT for that long",
)
Config.define(
    "HTTP_LOADER_CURL_LOW_SPEED_LIMIT",
    0,
    "If HTTP_LOADER_CURL_LOW_SPEED_TIME and HTTP_LOADER_CURL_ASYNC_HTTP_CLIENT "
    + "are set, then this is the limit in bytes per second as integer which should "
    + "timeout if the speed is below that limit for HTTP_LOADER_CURL_LOW_SPEED_TIME seconds",
)

# FILE STORAGE GENERIC OPTIONS
Config.define(
    "STORAGE_EXPIRATION_SECONDS",
    60 * 60 * 24 * 30,
    "Expiration in seconds for the images in the File Storage. Defaults to one month",
    "File Storage",
)
Config.define(
    "STORES_CRYPTO_KEY_FOR_EACH_IMAGE",
    False,
    "Indicates whether thumbor should store the signing key for each image in the file storage. "
    + "This allows the key to be changed and old images to still be properly found",
    "File Storage",
)

# FILE STORAGE OPTIONS
Config.define(
    "FILE_STORAGE_ROOT_PATH",
    join(tempfile.gettempdir(), "thumbor", "storage"),
    "The root path where the File Storage will try to find images",
    "File Storage",
)

# PHOTO UPLOAD OPTIONS
Config.define(
    "UPLOAD_MAX_SIZE",
    0,
    "Max size in bytes for images uploaded to thumbor",
    "Upload",
)
Config.define(
    "UPLOAD_ENABLED",
    False,
    "Indicates whether thumbor should enable File uploads",
    "Upload",
)
Config.define(
    "UPLOAD_PHOTO_STORAGE",
    "thumbor.storages.file_storage",
    "The type of storage to store uploaded images with",
    "Upload",
)
Config.define(
    "UPLOAD_DELETE_ALLOWED",
    False,
    "Indicates whether image deletion should be allowed",
    "Upload",
)
Config.define(
    "UPLOAD_PUT_ALLOWED",
    False,
    "Indicates whether image overwrite should be allowed",
    "Upload",
)
Config.define(
    "UPLOAD_DEFAULT_FILENAME",
    "image",
    "Default filename for image uploaded",
    "Upload",
)

# ALIASES FOR OLD PHOTO UPLOAD OPTIONS
Config.alias("MAX_SIZE", "UPLOAD_MAX_SIZE")
Config.alias("ENABLE_ORIGINAL_PHOTO_UPLOAD", "UPLOAD_ENABLED")
Config.alias("ORIGINAL_PHOTO_STORAGE", "UPLOAD_PHOTO_STORAGE")
Config.alias("ALLOW_ORIGINAL_PHOTO_DELETION", "UPLOAD_DELETE_ALLOWED")
Config.alias("ALLOW_ORIGINAL_PHOTO_PUTTING", "UPLOAD_PUT_ALLOWED")

# MIXED STORAGE OPTIONS
Config.define(
    "MIXED_STORAGE_FILE_STORAGE",
    "thumbor.storages.no_storage",
    "Mixed Storage file storage. This must be the full name "
    "of a python module (python must be able to import it)",
    "Mixed Storage",
)
Config.define(
    "MIXED_STORAGE_CRYPTO_STORAGE",
    "thumbor.storages.no_storage",
    "Mixed Storage signing key storage. This must be the full "
    "name of a python module (python must be able to import it)",
    "Mixed Storage",
)
Config.define(
    "MIXED_STORAGE_DETECTOR_STORAGE",
    "thumbor.storages.no_storage",
    "Mixed Storage detector information storage. This must be the full "
    "name of a python module (python must be able to import it)",
    "Mixed Storage",
)

# JSON META ENGINE OPTIONS
Config.define(
    "META_CALLBACK_NAME",
    None,
    "The callback function name that should be used by the META route for JSONP access",
    "Meta",
)

# DETECTORS OPTIONS
Config.define(
    "DETECTORS",
    [],
    "List of detectors that thumbor should use to find faces and/or features. All of them must be "
    + "full names of python modules (python must be able to import it)",
    "Detection",
)

# FACE DETECTOR CASCADE FILE
Config.define(
    "FACE_DETECTOR_CASCADE_FILE",
    "haarcascade_frontalface_alt.xml",
    "The cascade file that opencv will use to detect faces.",
    "Detection",
)

Config.define(
    "GLASSES_DETECTOR_CASCADE_FILE",
    "haarcascade_eye_tree_eyeglasses.xml",
    "The cascade file that opencv will use to detect glasses.",
    "Detection",
)

Config.define(
    "PROFILE_DETECTOR_CASCADE_FILE",
    "haarcascade_profileface.xml",
    "The cascade file that opencv will use to detect profile faces.",
    "Detection",
)

Config.define(
    "OPTIMIZERS",
    [
        # 'thumbor.optimizers.jpegtran',
        # 'thumbor.optimizers.gifv',
    ],
    "List of optimizers that thumbor will use to optimize images",
    "Optimizers",
)

# OPTIMIZER CONFIGURATIONS
Config.define(
    "JPEGTRAN_PATH",
    "/usr/bin/jpegtran",
    "Path for the jpegtran binary",
    "Optimizers",
)

Config.define(
    "JPEGTRAN_SCANS_FILE",
    "",
    "Path for the progressive scans file to use with "
    "jpegtran optimizer. Implies progressive jpeg output",
    "Optimizers",
)

Config.define(
    "FFMPEG_PATH",
    "/usr/local/bin/ffmpeg",
    "Path for the ffmpeg binary used to generate gifv(h.264)",
    "Optimizers",
)

# AVAILABLE FILTERS
Config.define(
    "FILTERS",
    BUILTIN_FILTERS,
    "List of filters that thumbor will allow to be used in generated images. All of them must be "
    + "full names of python modules (python must be able to import it)",
    "Filters",
)

# RESULT STORAGE
Config.define(
    "RESULT_STORAGE_EXPIRATION_SECONDS",
    0,
    "Expiration in seconds of generated images in the result storage",
    "Result Storage",
)  # Never expires
Config.define(
    "RESULT_STORAGE_FILE_STORAGE_ROOT_PATH",
    join(tempfile.gettempdir(), "thumbor", "result_storage"),
    "Path where the Result storage will store generated images",
    "Result Storage",
)
Config.define(
    "RESULT_STORAGE_STORES_UNSAFE",
    False,
    "Indicates whether unsafe requests should also be stored in the Result Storage",
    "Result Storage",
)

# QUEUED DETECTOR REDIS OPTIONS
Config.define(
    "REDIS_QUEUE_SERVER_HOST",
    "localhost",
    "Server host for the queued redis detector",
    "Queued Redis Detector",
)
Config.define(
    "REDIS_QUEUE_SERVER_PORT",
    6379,
    "Server port for the queued redis detector",
    "Queued Redis Detector",
)
Config.define(
    "REDIS_QUEUE_SERVER_DB",
    0,
    "Server database index for the queued redis detector",
    "Queued Redis Detector",
)
Config.define(
    "REDIS_QUEUE_SERVER_PASSWORD",
    None,
    "Server password for the queued redis detector",
    "Queued Redis Detector",
)

# ERROR HANDLING
Config.define(
    "USE_CUSTOM_ERROR_HANDLING",
    False,
    "This configuration indicates whether thumbor should use a custom error handler.",
    "Errors",
)
Config.define(
    "ERROR_HANDLER_MODULE",
    "thumbor.error_handlers.sentry",
    "Error reporting module. Needs to contain a class called ErrorHandler with a "
    + "handle_error(context, handler, exception) method.",
    "Errors",
)

# SENTRY REPORTING MODULE
Config.define(
    "SENTRY_DSN_URL",
    "",
    "Sentry thumbor project dsn. i.e.: "
    + "http://5a63d58ae7b94f1dab3dee740b301d6a:73eea45d3e8649239a973087e8f21f98@localhost:9000/2",
    "Errors - Sentry",
)

# SENTRY REPORTING MODULE
Config.define(
    "SENTRY_ENVIRONMENT",
    None,
    "Sentry environment i.e.: staging ",
    "Errors - Sentry",
)

# FILE REPORTING MODULE
Config.define("ERROR_FILE_LOGGER", None, "File of error log as json", "Errors")
Config.define(
    "ERROR_FILE_NAME_USE_CONTEXT",
    False,
    "File of error log name is parametrized with context attribute",
    "Errors",
)

# SIGNER MODULE
Config.define(
    "URL_SIGNER",
    "libthumbor.url_signers.base64_hmac_sha1",
    "The url signer thumbor should use to verify url signatures."
    + "This must be the full name of a python module "
    + "(python must be able to import it)",
    "Extensibility",
)

# SERVER
Config.define(
    "MAX_WAIT_SECONDS_BEFORE_SERVER_SHUTDOWN",
    0,
    "The amount of time to wait before shutting down the server, i.e. stop accepting requests.",
    "Server",
)
Config.define(
    "MAX_WAIT_SECONDS_BEFORE_IO_SHUTDOWN",
    0,
    "The amount of time to waut before shutting down all io, after the server has been stopped",
    "Server",
)

# HANDLER LISTS
Config.define(
    "HANDLER_LISTS",
    BUILTIN_HANDLERS,
    "Handler Lists are responsible for adding new handlers to thumbor app.",
    "HandlerLists",
)


Config.define(
    "APP_CLASS",
    "thumbor.app.ThumborServiceApp",
    "Custom app class to override ThumborServiceApp. "
    "This config value is overridden by the -a command-line parameter.",
)

Config.define(
    'ACCESS_CONTROL_ALLOW_ORIGIN_HEADER', False,
    'Sends Access-Control-Allow-Origin header'
)


# COMPATIBILITY

Config.define(
    "COMPATIBILITY_LEGACY_LOADER",
    None,
    "Loader that will be used with the compatibility layer, instead of the "
    "compatibility loader. Please only use this if you can't use up-to-date loaders.",
    "Compatibility",
)

Config.define(
    "COMPATIBILITY_LEGACY_STORAGE",
    None,
    "Storage that will be used with the compatibility layer, instead of the "
    "compatibility storage. Please only use this if you can't use up-to-date storages.",
    "Compatibility",
)

Config.define(
    "COMPATIBILITY_LEGACY_RESULT_STORAGE",
    None,
    "Result Storage that will be used with the compatibility layer, instead of the "
    "compatibility result storage. Please only use this if you can't use "
    "up-to-date result storages.",
    "Compatibility",
)


def generate_config():
    config.generate_config()


def format_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, (tuple, list, set)):
        representation = "[\n"
        for item in value:
            representation += f"#    {item}"
        representation += "#]"
        return representation
    return value


if __name__ == "__main__":
    generate_config()
