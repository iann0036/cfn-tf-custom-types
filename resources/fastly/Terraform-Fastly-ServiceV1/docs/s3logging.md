# Terraform::Fastly::ServiceV1 S3logging

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
    "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#formatversion" title="FormatVersion">FormatVersion</a>" : <i>Double</i>,
    "<a href="#gziplevel" title="GzipLevel">GzipLevel</a>" : <i>Double</i>,
    "<a href="#messagetype" title="MessageType">MessageType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
    "<a href="#placement" title="Placement">Placement</a>" : <i>String</i>,
    "<a href="#redundancy" title="Redundancy">Redundancy</a>" : <i>String</i>,
    "<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>" : <i>String</i>,
    "<a href="#s3accesskey" title="S3AccessKey">S3AccessKey</a>" : <i>String</i>,
    "<a href="#s3secretkey" title="S3SecretKey">S3SecretKey</a>" : <i>String</i>,
    "<a href="#timestampformat" title="TimestampFormat">TimestampFormat</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
<a href="#domain" title="Domain">Domain</a>: <i>String</i>
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#formatversion" title="FormatVersion">FormatVersion</a>: <i>Double</i>
<a href="#gziplevel" title="GzipLevel">GzipLevel</a>: <i>Double</i>
<a href="#messagetype" title="MessageType">MessageType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#period" title="Period">Period</a>: <i>Double</i>
<a href="#placement" title="Placement">Placement</a>: <i>String</i>
<a href="#redundancy" title="Redundancy">Redundancy</a>: <i>String</i>
<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>: <i>String</i>
<a href="#s3accesskey" title="S3AccessKey">S3AccessKey</a>: <i>String</i>
<a href="#s3secretkey" title="S3SecretKey">S3SecretKey</a>: <i>String</i>
<a href="#timestampformat" title="TimestampFormat">TimestampFormat</a>: <i>String</i>
</pre>

## Properties

#### BucketName

The name of the bucket in which to store the logs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

If you created the S3 bucket outside of `us-east-1`,
then specify the corresponding bucket endpoint. Example: `s3-us-west-2.amazonaws.com`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Apache-style string or VCL variables to use for log formatting. Defaults to Apache Common Log format (`%h %l %u %t %r %>s`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormatVersion

The version of the custom logging format used for the configured endpoint. Can be either 1 (the default, version 1 log format) or 2 (the version 2 log format).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GzipLevel

Level of GZIP compression, from `0-9`. `0` is no
compression. `1` is fastest and least compressed, `9` is slowest and most
compressed. Default `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageType

How the message should be formatted; one of: `classic`, `loggly`, `logplex` or `blank`.  Default `classic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to identify this S3 Logging Bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Path to store the files. Must end with a trailing slash.
If this field is left empty, the files will be saved in the bucket's root path.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

How frequently the logs should be transferred, in
seconds. Default `3600`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

Where in the generated VCL the logging call should be placed; one of: `none` or `waf_debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redundancy

The S3 redundancy level. Should be formatted; one of: `standard`, `reduced_redundancy` or null. Default `null`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCondition

Name of already defined `condition` to apply. This `condition` must be of type `RESPONSE`. For detailed information about Conditionals,
see [Fastly's Documentation on Conditionals][fastly-conditionals].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3AccessKey

AWS Access Key of an account with the required
permissions to post logs. It is **strongly** recommended you create a separate
IAM user with permissions to only operate on this Bucket. This key will be
not be encrypted. You can provide this key via an environment variable, `FASTLY_S3_ACCESS_KEY`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3SecretKey

AWS Secret Key of an account with the required
permissions to post logs. It is **strongly** recommended you create a separate
IAM user with permissions to only operate on this Bucket. This secret will be
not be encrypted. You can provide this secret via an environment variable, `FASTLY_S3_SECRET_KEY`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimestampFormat

`strftime` specified timestamp formatting (default `%Y-%m-%dT%H:%M:%S.000`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

