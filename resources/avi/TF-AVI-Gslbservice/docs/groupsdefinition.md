# TF::AVI::Gslbservice GroupsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
    "<a href="#consistenthashmask" title="ConsistentHashMask">ConsistentHashMask</a>" : <i>Double</i>,
    "<a href="#consistenthashmask6" title="ConsistentHashMask6">ConsistentHashMask6</a>" : <i>Double</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#fallbackalgorithm" title="FallbackAlgorithm">FallbackAlgorithm</a>" : <i>String</i>,
    "<a href="#minhealthmonitorsup" title="MinHealthMonitorsUp">MinHealthMonitorsUp</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#members" title="Members">Members</a>" : <i>[ <a href="membersdefinition.md">MembersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
<a href="#consistenthashmask" title="ConsistentHashMask">ConsistentHashMask</a>: <i>Double</i>
<a href="#consistenthashmask6" title="ConsistentHashMask6">ConsistentHashMask6</a>: <i>Double</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#fallbackalgorithm" title="FallbackAlgorithm">FallbackAlgorithm</a>: <i>String</i>
<a href="#minhealthmonitorsup" title="MinHealthMonitorsUp">MinHealthMonitorsUp</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#members" title="Members">Members</a>: <i>
      - <a href="membersdefinition.md">MembersDefinition</a></i>
</pre>

## Properties

#### Algorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsistentHashMask

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsistentHashMask6

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinHealthMonitorsUp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

_Required_: No

_Type_: List of <a href="membersdefinition.md">MembersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

