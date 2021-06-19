# TF::AzureRM::SynapseSparkPool

Manages a Synapse Spark Pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SynapseSparkPool",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
        "<a href="#nodesize" title="NodeSize">NodeSize</a>" : <i>String</i>,
        "<a href="#nodesizefamily" title="NodeSizeFamily">NodeSizeFamily</a>" : <i>String</i>,
        "<a href="#sparkeventsfolder" title="SparkEventsFolder">SparkEventsFolder</a>" : <i>String</i>,
        "<a href="#sparklogfolder" title="SparkLogFolder">SparkLogFolder</a>" : <i>String</i>,
        "<a href="#sparkversion" title="SparkVersion">SparkVersion</a>" : <i>String</i>,
        "<a href="#synapseworkspaceid" title="SynapseWorkspaceId">SynapseWorkspaceId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#autopause" title="AutoPause">AutoPause</a>" : <i>[ <a href="autopausedefinition.md">AutoPauseDefinition</a>, ... ]</i>,
        "<a href="#autoscale" title="AutoScale">AutoScale</a>" : <i>[ <a href="autoscaledefinition.md">AutoScaleDefinition</a>, ... ]</i>,
        "<a href="#libraryrequirement" title="LibraryRequirement">LibraryRequirement</a>" : <i>[ <a href="libraryrequirementdefinition.md">LibraryRequirementDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SynapseSparkPool
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
    <a href="#nodesize" title="NodeSize">NodeSize</a>: <i>String</i>
    <a href="#nodesizefamily" title="NodeSizeFamily">NodeSizeFamily</a>: <i>String</i>
    <a href="#sparkeventsfolder" title="SparkEventsFolder">SparkEventsFolder</a>: <i>String</i>
    <a href="#sparklogfolder" title="SparkLogFolder">SparkLogFolder</a>: <i>String</i>
    <a href="#sparkversion" title="SparkVersion">SparkVersion</a>: <i>String</i>
    <a href="#synapseworkspaceid" title="SynapseWorkspaceId">SynapseWorkspaceId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#autopause" title="AutoPause">AutoPause</a>: <i>
      - <a href="autopausedefinition.md">AutoPauseDefinition</a></i>
    <a href="#autoscale" title="AutoScale">AutoScale</a>: <i>
      - <a href="autoscaledefinition.md">AutoScaleDefinition</a></i>
    <a href="#libraryrequirement" title="LibraryRequirement">LibraryRequirement</a>: <i>
      - <a href="libraryrequirementdefinition.md">LibraryRequirementDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeSize

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeSizeFamily

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkEventsFolder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkLogFolder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparkVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SynapseWorkspaceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoPause

_Required_: No

_Type_: List of <a href="autopausedefinition.md">AutoPauseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScale

_Required_: No

_Type_: List of <a href="autoscaledefinition.md">AutoScaleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LibraryRequirement

_Required_: No

_Type_: List of <a href="libraryrequirementdefinition.md">LibraryRequirementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

