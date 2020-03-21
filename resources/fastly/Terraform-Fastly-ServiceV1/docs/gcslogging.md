# Terraform::Fastly::ServiceV1 Gcslogging

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
    "<a href="#email" title="Email">Email</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#gziplevel" title="GzipLevel">GzipLevel</a>" : <i>Double</i>,
    "<a href="#messagetype" title="MessageType">MessageType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
    "<a href="#placement" title="Placement">Placement</a>" : <i>String</i>,
    "<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>" : <i>String</i>,
    "<a href="#secretkey" title="SecretKey">SecretKey</a>" : <i>String</i>,
    "<a href="#timestampformat" title="TimestampFormat">TimestampFormat</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
<a href="#email" title="Email">Email</a>: <i>String</i>
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#gziplevel" title="GzipLevel">GzipLevel</a>: <i>Double</i>
<a href="#messagetype" title="MessageType">MessageType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#period" title="Period">Period</a>: <i>Double</i>
<a href="#placement" title="Placement">Placement</a>: <i>String</i>
<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>: <i>String</i>
<a href="#secretkey" title="SecretKey">SecretKey</a>: <i>String</i>
<a href="#timestampformat" title="TimestampFormat">TimestampFormat</a>: <i>String</i>
</pre>

## Properties

#### BucketName

The name of the bucket in which to store the logs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

The email address associated with the target GCS bucket on your account. You may optionally provide this secret via an environment variable, `FASTLY_GCS_EMAIL`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Apache-style string or VCL variables to use for log formatting. Defaults to Apache Common Log format (`%h %l %u %t %r %>s`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GzipLevel

Level of GZIP compression, from `0-9`. `0` is no
compression. `1` is fastest and least compressed, `9` is slowest and most
compressed. Default `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageType

How the message should be formatted; one of: `classic`, `loggly`, `logplex` or `blank`. Default `classic`. [Fastly Documentation](https://docs.fastly.com/api/logging#logging_gcs).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to identify this GCS endpoint.

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

#### ResponseCondition

Name of already defined `condition` to apply. This `condition` must be of type `RESPONSE`. For detailed information about Conditionals, see [Fastly's Documentation on Conditionals][fastly-conditionals].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKey

The secret key associated with the target gcs bucket on your account. You may optionally provide this secret via an environment variable, `FASTLY_GCS_SECRET_KEY`. A typical format for the key is PEM format, containing actual newline characters where required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimestampFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

