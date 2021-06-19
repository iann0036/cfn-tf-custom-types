# TF::CheckPoint::ManagementSimpleCluster MembersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#onetimepassword" title="OneTimePassword">OneTimePassword</a>" : <i>String</i>,
    "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ <a href="interfacesdefinition.md">InterfacesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#onetimepassword" title="OneTimePassword">OneTimePassword</a>: <i>String</i>
<a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - <a href="interfacesdefinition.md">InterfacesDefinition</a></i>
</pre>

## Properties

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OneTimePassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

_Required_: No

_Type_: List of <a href="interfacesdefinition.md">InterfacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

