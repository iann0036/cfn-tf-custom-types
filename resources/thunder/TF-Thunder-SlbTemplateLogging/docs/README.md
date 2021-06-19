# TF::Thunder::SlbTemplateLogging

`thunder_slb_template_logging` Provides details about thunder slb template logging

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateLogging",
    "Properties" : {
        "<a href="#auto" title="Auto">Auto</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#keepend" title="KeepEnd">KeepEnd</a>" : <i>Double</i>,
        "<a href="#keepstart" title="KeepStart">KeepStart</a>" : <i>Double</i>,
        "<a href="#locallogging" title="LocalLogging">LocalLogging</a>" : <i>Double</i>,
        "<a href="#mask" title="Mask">Mask</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pcremask" title="PcreMask">PcreMask</a>" : <i>String</i>,
        "<a href="#pool" title="Pool">Pool</a>" : <i>String</i>,
        "<a href="#poolshared" title="PoolShared">PoolShared</a>" : <i>String</i>,
        "<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>" : <i>String</i>,
        "<a href="#sharedpartitionpool" title="SharedPartitionPool">SharedPartitionPool</a>" : <i>Double</i>,
        "<a href="#sharedpartitiontcpproxytemplate" title="SharedPartitionTcpProxyTemplate">SharedPartitionTcpProxyTemplate</a>" : <i>Double</i>,
        "<a href="#tcpproxy" title="TcpProxy">TcpProxy</a>" : <i>String</i>,
        "<a href="#templatetcpproxyshared" title="TemplateTcpProxyShared">TemplateTcpProxyShared</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateLogging
Properties:
    <a href="#auto" title="Auto">Auto</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#keepend" title="KeepEnd">KeepEnd</a>: <i>Double</i>
    <a href="#keepstart" title="KeepStart">KeepStart</a>: <i>Double</i>
    <a href="#locallogging" title="LocalLogging">LocalLogging</a>: <i>Double</i>
    <a href="#mask" title="Mask">Mask</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pcremask" title="PcreMask">PcreMask</a>: <i>String</i>
    <a href="#pool" title="Pool">Pool</a>: <i>String</i>
    <a href="#poolshared" title="PoolShared">PoolShared</a>: <i>String</i>
    <a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>: <i>String</i>
    <a href="#sharedpartitionpool" title="SharedPartitionPool">SharedPartitionPool</a>: <i>Double</i>
    <a href="#sharedpartitiontcpproxytemplate" title="SharedPartitionTcpProxyTemplate">SharedPartitionTcpProxyTemplate</a>: <i>Double</i>
    <a href="#tcpproxy" title="TcpProxy">TcpProxy</a>: <i>String</i>
    <a href="#templatetcpproxyshared" title="TemplateTcpProxyShared">TemplateTcpProxyShared</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### Auto

‘auto’: Configure auto NAT for logging, default is auto enabled;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Specfiy a format string for web logging (format string(less than 250 characters) for web logging).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepEnd

Number of unmasked characters at the end (default: 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepStart

Number of unmasked characters at the beginning (default: 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalLogging

1 to enable local logging (1 to enable local logging, default 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mask

Character to mask the matched pattern (default: X).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Logging Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcreMask

Mask matched PCRE pattern in the log.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pool

Specify NAT pool or pool group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolShared

Specify NAT pool or pool group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

Bind a Service Group to the logging template (Service Group Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPool

Reference a NAT pool or pool group from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionTcpProxyTemplate

Reference a TCP Proxy template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpProxy

TCP proxy template (TCP Proxy Config name).

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

