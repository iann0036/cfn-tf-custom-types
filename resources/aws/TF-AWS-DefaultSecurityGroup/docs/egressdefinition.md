# TF::AWS::DefaultSecurityGroup EgressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>" : <i>[ String, ... ]</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#fromport" title="FromPort">FromPort</a>" : <i>Double</i>,
    "<a href="#ipv6cidrblocks" title="Ipv6CidrBlocks">Ipv6CidrBlocks</a>" : <i>[ String, ... ]</i>,
    "<a href="#prefixlistids" title="PrefixListIds">PrefixListIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#self" title="Self">Self</a>" : <i>Boolean</i>,
    "<a href="#toport" title="ToPort">ToPort</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>: <i>
      - String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#fromport" title="FromPort">FromPort</a>: <i>Double</i>
<a href="#ipv6cidrblocks" title="Ipv6CidrBlocks">Ipv6CidrBlocks</a>: <i>
      - String</i>
<a href="#prefixlistids" title="PrefixListIds">PrefixListIds</a>: <i>
      - String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
<a href="#self" title="Self">Self</a>: <i>Boolean</i>
<a href="#toport" title="ToPort">ToPort</a>: <i>Double</i>
</pre>

## Properties

#### CidrBlocks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6CidrBlocks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixListIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Self

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

