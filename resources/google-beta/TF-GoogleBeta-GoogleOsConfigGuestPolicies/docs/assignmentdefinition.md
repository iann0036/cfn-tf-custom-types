# TF::GoogleBeta::GoogleOsConfigGuestPolicies AssignmentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instancenameprefixes" title="InstanceNamePrefixes">InstanceNamePrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#instances" title="Instances">Instances</a>" : <i>[ String, ... ]</i>,
    "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
    "<a href="#grouplabels" title="GroupLabels">GroupLabels</a>" : <i>[ <a href="grouplabelsdefinition.md">GroupLabelsDefinition</a>, ... ]</i>,
    "<a href="#ostypes" title="OsTypes">OsTypes</a>" : <i>[ <a href="ostypesdefinition.md">OsTypesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#instancenameprefixes" title="InstanceNamePrefixes">InstanceNamePrefixes</a>: <i>
      - String</i>
<a href="#instances" title="Instances">Instances</a>: <i>
      - String</i>
<a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
<a href="#grouplabels" title="GroupLabels">GroupLabels</a>: <i>
      - <a href="grouplabelsdefinition.md">GroupLabelsDefinition</a></i>
<a href="#ostypes" title="OsTypes">OsTypes</a>: <i>
      - <a href="ostypesdefinition.md">OsTypesDefinition</a></i>
</pre>

## Properties

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

#### OsTypes

_Required_: No

_Type_: List of <a href="ostypesdefinition.md">OsTypesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

