# Terraform::Fastly::ServiceV1 Blobstoragelogging

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
    "<a href="#container" title="Container">Container</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#formatversion" title="FormatVersion">FormatVersion</a>" : <i>Double</i>,
    "<a href="#gziplevel" title="GzipLevel">GzipLevel</a>" : <i>Double</i>,
    "<a href="#messagetype" title="MessageType">MessageType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
    "<a href="#placement" title="Placement">Placement</a>" : <i>String</i>,
    "<a href="#publickey" title="PublicKey">PublicKey</a>" : <i>String</i>,
    "<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>" : <i>String</i>,
    "<a href="#sastoken" title="SasToken">SasToken</a>" : <i>String</i>,
    "<a href="#timestampformat" title="TimestampFormat">TimestampFormat</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
<a href="#container" title="Container">Container</a>: <i>String</i>
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#formatversion" title="FormatVersion">FormatVersion</a>: <i>Double</i>
<a href="#gziplevel" title="GzipLevel">GzipLevel</a>: <i>Double</i>
<a href="#messagetype" title="MessageType">MessageType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#period" title="Period">Period</a>: <i>Double</i>
<a href="#placement" title="Placement">Placement</a>: <i>String</i>
<a href="#publickey" title="PublicKey">PublicKey</a>: <i>String</i>
<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>: <i>String</i>
<a href="#sastoken" title="SasToken">SasToken</a>: <i>String</i>
<a href="#timestampformat" title="TimestampFormat">TimestampFormat</a>: <i>String</i>
</pre>

## Properties

#### AccountName

The unique Azure Blob Storage namespace in which your data objects are stored.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

The name of the Azure Blob Storage container in which to store logs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Apache-style string or VCL variables to use for log formatting. Default `%h %l %u %t \"%r\" %>s %b`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormatVersion

The version of the custom logging format used for the configured endpoint. Can be either `1` or `2`. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. Default `2`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GzipLevel

Level of GZIP compression from `0`to `9`. `0` means no compression. `1` is the fastest and the least compressed version, `9` is the slowest and the most compressed version. Default `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageType

How the message should be formatted. Can be either `classic`, `loggly`, `logplex` or `blank`.  Default `classic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to identify the Azure Blob Storage endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path to upload logs to. Must end with a trailing slash. If this field is left empty, the files will be saved in the container's root path.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

How frequently the logs should be transferred in seconds. Default `3600`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

Where in the generated VCL the logging call should be placed, overriding any `format_version` default. Can be either `none` or `waf_debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKey

A PGP public key that Fastly will use to encrypt your log files before writing them to disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCondition

The name of the `condition` to apply. If empty, always execute.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SasToken

The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimestampFormat

`strftime` specified timestamp formatting. Default `%Y-%m-%dT%H:%M:%S.000`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

