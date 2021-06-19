# TF::Panos::SnmptrapServerProfile V2cServerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#community" title="Community">Community</a>" : <i>String</i>,
    "<a href="#manager" title="Manager">Manager</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#community" title="Community">Community</a>: <i>String</i>
<a href="#manager" title="Manager">Manager</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Community

The SNMP community.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Manager

The hostname.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The server name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

