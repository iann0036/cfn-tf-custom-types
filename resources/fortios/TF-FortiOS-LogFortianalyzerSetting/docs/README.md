# TF::FortiOS::LogFortianalyzerSetting

Provides a resource to configure configure logging to FortiAnalyzer log management devices.

!> **Warning:** The resource will be deprecated and replaced by new resource `fortios_logfortianalyzer_setting`, we recommend that you use the new resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::LogFortianalyzerSetting",
    "Properties" : {
        "<a href="#encalgorithm" title="EncAlgorithm">EncAlgorithm</a>" : <i>String</i>,
        "<a href="#hmacalgorithm" title="HmacAlgorithm">HmacAlgorithm</a>" : <i>String</i>,
        "<a href="#reliable" title="Reliable">Reliable</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#uploadoption" title="UploadOption">UploadOption</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::LogFortianalyzerSetting
Properties:
    <a href="#encalgorithm" title="EncAlgorithm">EncAlgorithm</a>: <i>String</i>
    <a href="#hmacalgorithm" title="HmacAlgorithm">HmacAlgorithm</a>: <i>String</i>
    <a href="#reliable" title="Reliable">Reliable</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#uploadoption" title="UploadOption">UploadOption</a>: <i>String</i>
</pre>

## Properties

#### EncAlgorithm

Enable/disable sending FortiAnalyzer log data with SSL encryption.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HmacAlgorithm

FortiAnalyzer IPsec tunnel HMAC algorithm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reliable

Enable/disable reliable logging to FortiAnalyzer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

The remote FortiAnalyzer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IPv4 or IPv6 address used to communicate with FortiAnalyzer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable logging to FortiAnalyzer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadOption

Enable/disable logging to hard disk and then uploading to FortiAnalyzer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

