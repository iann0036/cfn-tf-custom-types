# TF::FortiOS::FirewallInternetserviceextension PortRangeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endport" title="EndPort">EndPort</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#startport" title="StartPort">StartPort</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#endport" title="EndPort">EndPort</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#startport" title="StartPort">StartPort</a>: <i>Double</i>
</pre>

## Properties

#### EndPort

Ending TCP/UDP/SCTP destination port (1 to 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Custom entry port range ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartPort

Starting TCP/UDP/SCTP destination port (1 to 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

