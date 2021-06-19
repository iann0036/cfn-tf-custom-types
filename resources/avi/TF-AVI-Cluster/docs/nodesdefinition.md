# TF::AVI::Cluster NodesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#categories" title="Categories">Categories</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#vmhostname" title="VmHostname">VmHostname</a>" : <i>String</i>,
    "<a href="#vmmor" title="VmMor">VmMor</a>" : <i>String</i>,
    "<a href="#vmname" title="VmName">VmName</a>" : <i>String</i>,
    "<a href="#vmuuid" title="VmUuid">VmUuid</a>" : <i>String</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>[ <a href="ipdefinition.md">IpDefinition</a>, ... ]</i>,
    "<a href="#publiciporname" title="PublicIpOrName">PublicIpOrName</a>" : <i>[ <a href="publicipornamedefinition.md">PublicIpOrNameDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#categories" title="Categories">Categories</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#vmhostname" title="VmHostname">VmHostname</a>: <i>String</i>
<a href="#vmmor" title="VmMor">VmMor</a>: <i>String</i>
<a href="#vmname" title="VmName">VmName</a>: <i>String</i>
<a href="#vmuuid" title="VmUuid">VmUuid</a>: <i>String</i>
<a href="#ip" title="Ip">Ip</a>: <i>
      - <a href="ipdefinition.md">IpDefinition</a></i>
<a href="#publiciporname" title="PublicIpOrName">PublicIpOrName</a>: <i>
      - <a href="publicipornamedefinition.md">PublicIpOrNameDefinition</a></i>
</pre>

## Properties

#### Categories

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmHostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmMor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of <a href="ipdefinition.md">IpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpOrName

_Required_: No

_Type_: List of <a href="publicipornamedefinition.md">PublicIpOrNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

