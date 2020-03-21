# Terraform::OpenTelekomCloud::ComputeSecgroupV2 Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
    "<a href="#fromgroupid" title="FromGroupId">FromGroupId</a>" : <i>String</i>,
    "<a href="#fromport" title="FromPort">FromPort</a>" : <i>Double</i>,
    "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>String</i>,
    "<a href="#self" title="Self">Self</a>" : <i>Boolean</i>,
    "<a href="#toport" title="ToPort">ToPort</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
<a href="#fromgroupid" title="FromGroupId">FromGroupId</a>: <i>String</i>
<a href="#fromport" title="FromPort">FromPort</a>: <i>Double</i>
<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>String</i>
<a href="#self" title="Self">Self</a>: <i>Boolean</i>
<a href="#toport" title="ToPort">ToPort</a>: <i>Double</i>
</pre>

## Properties

#### Cidr

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromGroupId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromPort

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Self

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToPort

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

