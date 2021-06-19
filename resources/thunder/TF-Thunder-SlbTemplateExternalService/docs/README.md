# TF::Thunder::SlbTemplateExternalService

`thunder_slb_template_external_service` Provides details about thunder slb template external service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateExternalService",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#failureaction" title="FailureAction">FailureAction</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>" : <i>String</i>,
        "<a href="#sharedpartitionpersistsourceiptemplate" title="SharedPartitionPersistSourceIpTemplate">SharedPartitionPersistSourceIpTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitiontcpproxytemplate" title="SharedPartitionTcpProxyTemplate">SharedPartitionTcpProxyTemplate</a>" : <i>Double</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#tcpproxy" title="TcpProxy">TcpProxy</a>" : <i>String</i>,
        "<a href="#templatepersistsourceipshared" title="TemplatePersistSourceIpShared">TemplatePersistSourceIpShared</a>" : <i>String</i>,
        "<a href="#templatetcpproxyshared" title="TemplateTcpProxyShared">TemplateTcpProxyShared</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#bypassipcfg" title="BypassIpCfg">BypassIpCfg</a>" : <i>[ <a href="bypassipcfgdefinition.md">BypassIpCfgDefinition</a>, ... ]</i>,
        "<a href="#requestheaderforwardlist" title="RequestHeaderForwardList">RequestHeaderForwardList</a>" : <i>[ <a href="requestheaderforwardlistdefinition.md">RequestHeaderForwardListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateExternalService
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#failureaction" title="FailureAction">FailureAction</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>: <i>String</i>
    <a href="#sharedpartitionpersistsourceiptemplate" title="SharedPartitionPersistSourceIpTemplate">SharedPartitionPersistSourceIpTemplate</a>: <i>Double</i>
    <a href="#sharedpartitiontcpproxytemplate" title="SharedPartitionTcpProxyTemplate">SharedPartitionTcpProxyTemplate</a>: <i>Double</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#tcpproxy" title="TcpProxy">TcpProxy</a>: <i>String</i>
    <a href="#templatepersistsourceipshared" title="TemplatePersistSourceIpShared">TemplatePersistSourceIpShared</a>: <i>String</i>
    <a href="#templatetcpproxyshared" title="TemplateTcpProxyShared">TemplateTcpProxyShared</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#bypassipcfg" title="BypassIpCfg">BypassIpCfg</a>: <i>
      - <a href="bypassipcfgdefinition.md">BypassIpCfgDefinition</a></i>
    <a href="#requestheaderforwardlist" title="RequestHeaderForwardList">RequestHeaderForwardList</a>: <i>
      - <a href="requestheaderforwardlistdefinition.md">RequestHeaderForwardListDefinition</a></i>
</pre>

## Properties

#### Action

‘continue’: Continue; ‘drop’: Drop; ‘reset’: Reset;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureAction

‘continue’: Continue; ‘drop’: Drop; ‘reset’: Reset;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

External Service Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

Bind a Service Group to the template (Service Group Name).

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

#### Timeout

Timeout value 1 - 200 in units of 200ms, default is 5 (default is 1000ms) (1 - 200 in units of 200ms, default is 5 (1000ms)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

‘skyfire-icap’: Skyfire ICAP service; ‘url-filter’: URL filtering service;.

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

#### RequestHeaderForwardList

_Required_: No

_Type_: List of <a href="requestheaderforwardlistdefinition.md">RequestHeaderForwardListDefinition</a>

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

