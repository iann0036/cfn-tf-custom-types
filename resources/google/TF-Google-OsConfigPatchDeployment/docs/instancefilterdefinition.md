# TF::Google::OsConfigPatchDeployment InstanceFilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#all" title="All">All</a>" : <i>Boolean</i>,
    "<a href="#instancenameprefixes" title="InstanceNamePrefixes">InstanceNamePrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#instances" title="Instances">Instances</a>" : <i>[ String, ... ]</i>,
    "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
    "<a href="#grouplabels" title="GroupLabels">GroupLabels</a>" : <i>[ <a href="grouplabelsdefinition.md">GroupLabelsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#all" title="All">All</a>: <i>Boolean</i>
<a href="#instancenameprefixes" title="InstanceNamePrefixes">InstanceNamePrefixes</a>: <i>
      - String</i>
<a href="#instances" title="Instances">Instances</a>: <i>
      - String</i>
<a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
<a href="#grouplabels" title="GroupLabels">GroupLabels</a>: <i>
      - <a href="grouplabelsdefinition.md">GroupLabelsDefinition</a></i>
</pre>

## Properties

#### All

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceNamePrefixes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupLabels

_Required_: No

_Type_: List of <a href="grouplabelsdefinition.md">GroupLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

