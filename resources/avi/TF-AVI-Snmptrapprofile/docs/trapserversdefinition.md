# TF::AVI::Snmptrapprofile TrapServersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#community" title="Community">Community</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#ipaddr" title="IpAddr">IpAddr</a>" : <i>[ <a href="ipaddrdefinition.md">IpAddrDefinition</a>, ... ]</i>,
    "<a href="#user" title="User">User</a>" : <i>[ <a href="userdefinition.md">UserDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#community" title="Community">Community</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#ipaddr" title="IpAddr">IpAddr</a>: <i>
      - <a href="ipaddrdefinition.md">IpAddrDefinition</a></i>
<a href="#user" title="User">User</a>: <i>
      - <a href="userdefinition.md">UserDefinition</a></i>
</pre>

## Properties

#### Community

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddr

_Required_: No

_Type_: List of <a href="ipaddrdefinition.md">IpAddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: List of <a href="userdefinition.md">UserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

