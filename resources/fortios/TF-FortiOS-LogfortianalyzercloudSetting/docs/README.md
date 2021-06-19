# TF::FortiOS::LogfortianalyzercloudSetting

Global FortiAnalyzer Cloud settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::LogfortianalyzercloudSetting",
    "Properties" : {
        "<a href="#accessconfig" title="AccessConfig">AccessConfig</a>" : <i>String</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#conntimeout" title="ConnTimeout">ConnTimeout</a>" : <i>Double</i>,
        "<a href="#encalgorithm" title="EncAlgorithm">EncAlgorithm</a>" : <i>String</i>,
        "<a href="#hmacalgorithm" title="HmacAlgorithm">HmacAlgorithm</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>" : <i>String</i>,
        "<a href="#ipsarchive" title="IpsArchive">IpsArchive</a>" : <i>String</i>,
        "<a href="#maxlograte" title="MaxLogRate">MaxLogRate</a>" : <i>Double</i>,
        "<a href="#monitorfailureretryperiod" title="MonitorFailureRetryPeriod">MonitorFailureRetryPeriod</a>" : <i>Double</i>,
        "<a href="#monitorkeepaliveperiod" title="MonitorKeepalivePeriod">MonitorKeepalivePeriod</a>" : <i>Double</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#sslminprotoversion" title="SslMinProtoVersion">SslMinProtoVersion</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#uploadday" title="UploadDay">UploadDay</a>" : <i>String</i>,
        "<a href="#uploadinterval" title="UploadInterval">UploadInterval</a>" : <i>String</i>,
        "<a href="#uploadoption" title="UploadOption">UploadOption</a>" : <i>String</i>,
        "<a href="#uploadtime" title="UploadTime">UploadTime</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::LogfortianalyzercloudSetting
Properties:
    <a href="#accessconfig" title="AccessConfig">AccessConfig</a>: <i>String</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#conntimeout" title="ConnTimeout">ConnTimeout</a>: <i>Double</i>
    <a href="#encalgorithm" title="EncAlgorithm">EncAlgorithm</a>: <i>String</i>
    <a href="#hmacalgorithm" title="HmacAlgorithm">HmacAlgorithm</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>: <i>String</i>
    <a href="#ipsarchive" title="IpsArchive">IpsArchive</a>: <i>String</i>
    <a href="#maxlograte" title="MaxLogRate">MaxLogRate</a>: <i>Double</i>
    <a href="#monitorfailureretryperiod" title="MonitorFailureRetryPeriod">MonitorFailureRetryPeriod</a>: <i>Double</i>
    <a href="#monitorkeepaliveperiod" title="MonitorKeepalivePeriod">MonitorKeepalivePeriod</a>: <i>Double</i>
    <a href="#priority" title="Priority">Priority</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#sslminprotoversion" title="SslMinProtoVersion">SslMinProtoVersion</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#uploadday" title="UploadDay">UploadDay</a>: <i>String</i>
    <a href="#uploadinterval" title="UploadInterval">UploadInterval</a>: <i>String</i>
    <a href="#uploadoption" title="UploadOption">UploadOption</a>: <i>String</i>
    <a href="#uploadtime" title="UploadTime">UploadTime</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AccessConfig

Enable/disable FortiAnalyzer access to configuration and data. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

Certificate used to communicate with FortiAnalyzer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnTimeout

FortiAnalyzer connection time-out in seconds (for status and log buffer).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncAlgorithm

Configure the level of SSL protection for secure communication with FortiAnalyzer. Valid values: `high-medium`, `high`, `low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HmacAlgorithm

FortiAnalyzer IPsec tunnel HMAC algorithm. Valid values: `sha256`, `sha1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Specify outgoing interface to reach server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceSelectMethod

Specify how to select outgoing interface to reach server. Valid values: `auto`, `sdwan`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsArchive

Enable/disable IPS packet archive logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLogRate

FortiAnalyzer maximum log rate in MBps (0 = unlimited).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorFailureRetryPeriod

Time between FortiAnalyzer connection retries in seconds (for status and log buffer).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorKeepalivePeriod

Time between OFTP keepalives in seconds (for status and log buffer).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Set log transmission priority. Valid values: `default`, `low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IPv4 or IPv6 address used to communicate with FortiAnalyzer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinProtoVersion

Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). Valid values: `default`, `SSLv3`, `TLSv1`, `TLSv1-1`, `TLSv1-2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable logging to FortiAnalyzer. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadDay

Day of week (month) to upload logs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadInterval

Frequency to upload log files to FortiAnalyzer. Valid values: `daily`, `weekly`, `monthly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadOption

Enable/disable logging to hard disk and then uploading to FortiAnalyzer. Valid values: `store-and-upload`, `realtime`, `1-minute`, `5-minute`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadTime

Time to upload logs (hh:mm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

