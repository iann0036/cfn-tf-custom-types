# TF::AVI::Networkprofile ProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#tcpfastpathprofile" title="TcpFastPathProfile">TcpFastPathProfile</a>" : <i>[ <a href="tcpfastpathprofiledefinition.md">TcpFastPathProfileDefinition</a>, ... ]</i>,
    "<a href="#tcpproxyprofile" title="TcpProxyProfile">TcpProxyProfile</a>" : <i>[ <a href="tcpproxyprofiledefinition.md">TcpProxyProfileDefinition</a>, ... ]</i>,
    "<a href="#udpfastpathprofile" title="UdpFastPathProfile">UdpFastPathProfile</a>" : <i>[ <a href="udpfastpathprofiledefinition.md">UdpFastPathProfileDefinition</a>, ... ]</i>,
    "<a href="#udpproxyprofile" title="UdpProxyProfile">UdpProxyProfile</a>" : <i>[ <a href="udpproxyprofiledefinition.md">UdpProxyProfileDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#tcpfastpathprofile" title="TcpFastPathProfile">TcpFastPathProfile</a>: <i>
      - <a href="tcpfastpathprofiledefinition.md">TcpFastPathProfileDefinition</a></i>
<a href="#tcpproxyprofile" title="TcpProxyProfile">TcpProxyProfile</a>: <i>
      - <a href="tcpproxyprofiledefinition.md">TcpProxyProfileDefinition</a></i>
<a href="#udpfastpathprofile" title="UdpFastPathProfile">UdpFastPathProfile</a>: <i>
      - <a href="udpfastpathprofiledefinition.md">UdpFastPathProfileDefinition</a></i>
<a href="#udpproxyprofile" title="UdpProxyProfile">UdpProxyProfile</a>: <i>
      - <a href="udpproxyprofiledefinition.md">UdpProxyProfileDefinition</a></i>
</pre>

## Properties

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpFastPathProfile

_Required_: No

_Type_: List of <a href="tcpfastpathprofiledefinition.md">TcpFastPathProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpProxyProfile

_Required_: No

_Type_: List of <a href="tcpproxyprofiledefinition.md">TcpProxyProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpFastPathProfile

_Required_: No

_Type_: List of <a href="udpfastpathprofiledefinition.md">UdpFastPathProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpProxyProfile

_Required_: No

_Type_: List of <a href="udpproxyprofiledefinition.md">UdpProxyProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

