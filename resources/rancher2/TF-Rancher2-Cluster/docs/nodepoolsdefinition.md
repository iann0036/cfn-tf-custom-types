# TF::Rancher2::Cluster NodePoolsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>" : <i>Double</i>,
    "<a href="#maxpodsconstraint" title="MaxPodsConstraint">MaxPodsConstraint</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#autoscaling" title="Autoscaling">Autoscaling</a>" : <i>[ <a href="autoscalingdefinition.md">AutoscalingDefinition</a>, ... ]</i>,
    "<a href="#config" title="Config">Config</a>" : <i>[ <a href="configdefinition.md">ConfigDefinition</a>, ... ]</i>,
    "<a href="#management" title="Management">Management</a>" : <i>[ <a href="managementdefinition.md">ManagementDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>: <i>Double</i>
<a href="#maxpodsconstraint" title="MaxPodsConstraint">MaxPodsConstraint</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#autoscaling" title="Autoscaling">Autoscaling</a>: <i>
      - <a href="autoscalingdefinition.md">AutoscalingDefinition</a></i>
<a href="#config" title="Config">Config</a>: <i>
      - <a href="configdefinition.md">ConfigDefinition</a></i>
<a href="#management" title="Management">Management</a>: <i>
      - <a href="managementdefinition.md">ManagementDefinition</a></i>
</pre>

## Properties

#### InitialNodeCount

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPodsConstraint

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscaling

_Required_: No

_Type_: List of <a href="autoscalingdefinition.md">AutoscalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

_Required_: No

_Type_: List of <a href="configdefinition.md">ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

_Required_: No

_Type_: List of <a href="managementdefinition.md">ManagementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
