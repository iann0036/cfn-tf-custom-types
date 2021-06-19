# TF::AVI::Hardwaresecuritymodulegroup SlunaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hagroupnum" title="HaGroupNum">HaGroupNum</a>" : <i>Double</i>,
    "<a href="#isha" title="IsHa">IsHa</a>" : <i>Boolean</i>,
    "<a href="#serverpem" title="ServerPem">ServerPem</a>" : <i>String</i>,
    "<a href="#usededicatednetwork" title="UseDedicatedNetwork">UseDedicatedNetwork</a>" : <i>Boolean</i>,
    "<a href="#nodeinfo" title="NodeInfo">NodeInfo</a>" : <i>[ <a href="nodeinfodefinition.md">NodeInfoDefinition</a>, ... ]</i>,
    "<a href="#server" title="Server">Server</a>" : <i>[ <a href="serverdefinition.md">ServerDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hagroupnum" title="HaGroupNum">HaGroupNum</a>: <i>Double</i>
<a href="#isha" title="IsHa">IsHa</a>: <i>Boolean</i>
<a href="#serverpem" title="ServerPem">ServerPem</a>: <i>String</i>
<a href="#usededicatednetwork" title="UseDedicatedNetwork">UseDedicatedNetwork</a>: <i>Boolean</i>
<a href="#nodeinfo" title="NodeInfo">NodeInfo</a>: <i>
      - <a href="nodeinfodefinition.md">NodeInfoDefinition</a></i>
<a href="#server" title="Server">Server</a>: <i>
      - <a href="serverdefinition.md">ServerDefinition</a></i>
</pre>

## Properties

#### HaGroupNum

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHa

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerPem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDedicatedNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeInfo

_Required_: No

_Type_: List of <a href="nodeinfodefinition.md">NodeInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

_Required_: No

_Type_: List of <a href="serverdefinition.md">ServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

