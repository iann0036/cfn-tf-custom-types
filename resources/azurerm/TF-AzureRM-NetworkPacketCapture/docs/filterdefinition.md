# TF::AzureRM::NetworkPacketCapture FilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#localipaddress" title="LocalIpAddress">LocalIpAddress</a>" : <i>String</i>,
    "<a href="#localport" title="LocalPort">LocalPort</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#remoteipaddress" title="RemoteIpAddress">RemoteIpAddress</a>" : <i>String</i>,
    "<a href="#remoteport" title="RemotePort">RemotePort</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#localipaddress" title="LocalIpAddress">LocalIpAddress</a>: <i>String</i>
<a href="#localport" title="LocalPort">LocalPort</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#remoteipaddress" title="RemoteIpAddress">RemoteIpAddress</a>: <i>String</i>
<a href="#remoteport" title="RemotePort">RemotePort</a>: <i>String</i>
</pre>

## Properties

#### LocalIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemotePort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

