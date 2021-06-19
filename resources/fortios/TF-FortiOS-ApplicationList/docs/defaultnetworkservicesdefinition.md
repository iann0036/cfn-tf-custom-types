# TF::FortiOS::ApplicationList DefaultNetworkServicesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#services" title="Services">Services</a>" : <i>String</i>,
    "<a href="#violationaction" title="ViolationAction">ViolationAction</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#services" title="Services">Services</a>: <i>String</i>
<a href="#violationaction" title="ViolationAction">ViolationAction</a>: <i>String</i>
</pre>

## Properties

#### Id

Entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

Network protocols. Valid values: `http`, `ssh`, `telnet`, `ftp`, `dns`, `smtp`, `pop3`, `imap`, `snmp`, `nntp`, `https`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolationAction

Action for protocols not white listed under selected port. Valid values: `pass`, `monitor`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

