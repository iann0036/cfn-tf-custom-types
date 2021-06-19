# TF::Google::CloudRunService StatusDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="statusdefinition.md">StatusDefinition</a>, ... ]</i>,
    "<a href="#latestcreatedrevisionname" title="LatestCreatedRevisionName">LatestCreatedRevisionName</a>" : <i>String</i>,
    "<a href="#latestreadyrevisionname" title="LatestReadyRevisionName">LatestReadyRevisionName</a>" : <i>String</i>,
    "<a href="#observedgeneration" title="ObservedGeneration">ObservedGeneration</a>" : <i>Double</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="statusdefinition.md">StatusDefinition</a></i>
<a href="#latestcreatedrevisionname" title="LatestCreatedRevisionName">LatestCreatedRevisionName</a>: <i>String</i>
<a href="#latestreadyrevisionname" title="LatestReadyRevisionName">LatestReadyRevisionName</a>: <i>String</i>
<a href="#observedgeneration" title="ObservedGeneration">ObservedGeneration</a>: <i>Double</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### Conditions

_Required_: No

_Type_: List of <a href="statusdefinition.md">StatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LatestCreatedRevisionName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LatestReadyRevisionName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObservedGeneration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

