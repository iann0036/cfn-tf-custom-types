# TF::Thunder::SlbTemplateReqmodIcap

`thunder_slb_template_reqmod_icap` Provides details about thunder slb template reqmod icap

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateReqmodIcap",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#allowedhttpmethods" title="AllowedHttpMethods">AllowedHttpMethods</a>" : <i>String</i>,
        "<a href="#cylance" title="Cylance">Cylance</a>" : <i>Double</i>,
        "<a href="#disablehttpserverreset" title="DisableHttpServerReset">DisableHttpServerReset</a>" : <i>Double</i>,
        "<a href="#failclose" title="FailClose">FailClose</a>" : <i>Double</i>,
        "<a href="#includeprotocolinuri" title="IncludeProtocolInUri">IncludeProtocolInUri</a>" : <i>Double</i>,
        "<a href="#logonlyallowedmethod" title="LogOnlyAllowedMethod">LogOnlyAllowedMethod</a>" : <i>Double</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>String</i>,
        "<a href="#minpayloadsize" title="MinPayloadSize">MinPayloadSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#preview" title="Preview">Preview</a>" : <i>Double</i>,
        "<a href="#serverssl" title="ServerSsl">ServerSsl</a>" : <i>String</i>,
        "<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>" : <i>String</i>,
        "<a href="#serviceurl" title="ServiceUrl">ServiceUrl</a>" : <i>String</i>,
        "<a href="#sharedpartitionpersistsourceiptemplate" title="SharedPartitionPersistSourceIpTemplate">SharedPartitionPersistSourceIpTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitiontcpproxytemplate" title="SharedPartitionTcpProxyTemplate">SharedPartitionTcpProxyTemplate</a>" : <i>Double</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#tcpproxy" title="TcpProxy">TcpProxy</a>" : <i>String</i>,
        "<a href="#templatepersistsourceipshared" title="TemplatePersistSourceIpShared">TemplatePersistSourceIpShared</a>" : <i>String</i>,
        "<a href="#templatetcpproxyshared" title="TemplateTcpProxyShared">TemplateTcpProxyShared</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#bypassipcfg" title="BypassIpCfg">BypassIpCfg</a>" : <i>[ <a href="bypassipcfgdefinition.md">BypassIpCfgDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateReqmodIcap
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#allowedhttpmethods" title="AllowedHttpMethods">AllowedHttpMethods</a>: <i>String</i>
    <a href="#cylance" title="Cylance">Cylance</a>: <i>Double</i>
    <a href="#disablehttpserverreset" title="DisableHttpServerReset">DisableHttpServerReset</a>: <i>Double</i>
    <a href="#failclose" title="FailClose">FailClose</a>: <i>Double</i>
    <a href="#includeprotocolinuri" title="IncludeProtocolInUri">IncludeProtocolInUri</a>: <i>Double</i>
    <a href="#logonlyallowedmethod" title="LogOnlyAllowedMethod">LogOnlyAllowedMethod</a>: <i>Double</i>
    <a href="#logging" title="Logging">Logging</a>: <i>String</i>
    <a href="#minpayloadsize" title="MinPayloadSize">MinPayloadSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#preview" title="Preview">Preview</a>: <i>Double</i>
    <a href="#serverssl" title="ServerSsl">ServerSsl</a>: <i>String</i>
    <a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>: <i>String</i>
    <a href="#serviceurl" title="ServiceUrl">ServiceUrl</a>: <i>String</i>
    <a href="#sharedpartitionpersistsourceiptemplate" title="SharedPartitionPersistSourceIpTemplate">SharedPartitionPersistSourceIpTemplate</a>: <i>Double</i>
    <a href="#sharedpartitiontcpproxytemplate" title="SharedPartitionTcpProxyTemplate">SharedPartitionTcpProxyTemplate</a>: <i>Double</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#tcpproxy" title="TcpProxy">TcpProxy</a>: <i>String</i>
    <a href="#templatepersistsourceipshared" title="TemplatePersistSourceIpShared">TemplatePersistSourceIpShared</a>: <i>String</i>
    <a href="#templatetcpproxyshared" title="TemplateTcpProxyShared">TemplateTcpProxyShared</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#bypassipcfg" title="BypassIpCfg">BypassIpCfg</a>: <i>
      - <a href="bypassipcfgdefinition.md">BypassIpCfgDefinition</a></i>
</pre>

## Properties

#### Action

‘continue’: Continue; ‘drop’: Drop; ‘reset’: Reset;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedHttpMethods

List of allowed HTTP methods. Default is “Allow All”. (List of HTTP methods allowed (default “Allow All”)).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cylance

cylance external server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableHttpServerReset

Don’t reset http server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailClose

When template sg is down mark vport down.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeProtocolInUri

Include protocol and port in HTTP URI.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogOnlyAllowedMethod

Only log allowed HTTP method.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

logging template (Logging template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinPayloadSize

min-payload-size value 1 - 65536, default is 4096.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Reqmod ICAP Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preview

Preview value 1 - 32768, default is 32768.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSsl

Server SSL template (Server SSL template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

Bind a Service Group to the template (Service Group Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceUrl

URL to send to ICAP server (Service URL Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPersistSourceIpTemplate

Reference a persist source ip template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionTcpProxyTemplate

Reference a TCP Proxy template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP persistence template (Source IP persistence template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpProxy

TCP proxy template (TCP proxy template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePersistSourceIpShared

Source IP Persistence Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTcpProxyShared

TCP Proxy Template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassIpCfg

_Required_: No

_Type_: List of <a href="bypassipcfgdefinition.md">BypassIpCfgDefinition</a>

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

