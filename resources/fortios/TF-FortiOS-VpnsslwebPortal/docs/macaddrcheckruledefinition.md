# TF::FortiOS::VpnsslwebPortal MacAddrCheckRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#macaddrmask" title="MacAddrMask">MacAddrMask</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#macaddrlist" title="MacAddrList">MacAddrList</a>" : <i>[ <a href="macaddrlistdefinition.md">MacAddrListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#macaddrmask" title="MacAddrMask">MacAddrMask</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#macaddrlist" title="MacAddrList">MacAddrList</a>: <i>
      - <a href="macaddrlistdefinition.md">MacAddrListDefinition</a></i>
</pre>

## Properties

#### MacAddrMask

Client MAC address mask.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Client MAC address check rule name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddrList

_Required_: No

_Type_: List of <a href="macaddrlistdefinition.md">MacAddrListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

