# TF::Civo::KubernetesCluster PoolsDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#instancenames" title="InstanceNames">InstanceNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#instances" title="Instances">Instances</a>" : <i>[ <a href="instancesdefinition.md">InstancesDefinition</a>, ... ]</i>,
    "<a href="#size" title="Size">Size</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#instancenames" title="InstanceNames">InstanceNames</a>: <i>
      - String</i>
<a href="#instances" title="Instances">Instances</a>: <i>
      - <a href="instancesdefinition.md">InstancesDefinition</a></i>
<a href="#size" title="Size">Size</a>: <i>String</i>
</pre>

## Properties

#### Count

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

_Required_: No

_Type_: List of <a href="instancesdefinition.md">InstancesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

