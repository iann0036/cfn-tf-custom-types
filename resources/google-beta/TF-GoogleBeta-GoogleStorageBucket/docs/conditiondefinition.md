# TF::GoogleBeta::GoogleStorageBucket ConditionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#age" title="Age">Age</a>" : <i>Double</i>,
    "<a href="#createdbefore" title="CreatedBefore">CreatedBefore</a>" : <i>String</i>,
    "<a href="#customtimebefore" title="CustomTimeBefore">CustomTimeBefore</a>" : <i>String</i>,
    "<a href="#dayssincecustomtime" title="DaysSinceCustomTime">DaysSinceCustomTime</a>" : <i>Double</i>,
    "<a href="#dayssincenoncurrenttime" title="DaysSinceNoncurrentTime">DaysSinceNoncurrentTime</a>" : <i>Double</i>,
    "<a href="#matchesstorageclass" title="MatchesStorageClass">MatchesStorageClass</a>" : <i>[ String, ... ]</i>,
    "<a href="#noncurrenttimebefore" title="NoncurrentTimeBefore">NoncurrentTimeBefore</a>" : <i>String</i>,
    "<a href="#numnewerversions" title="NumNewerVersions">NumNewerVersions</a>" : <i>Double</i>,
    "<a href="#withstate" title="WithState">WithState</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#age" title="Age">Age</a>: <i>Double</i>
<a href="#createdbefore" title="CreatedBefore">CreatedBefore</a>: <i>String</i>
<a href="#customtimebefore" title="CustomTimeBefore">CustomTimeBefore</a>: <i>String</i>
<a href="#dayssincecustomtime" title="DaysSinceCustomTime">DaysSinceCustomTime</a>: <i>Double</i>
<a href="#dayssincenoncurrenttime" title="DaysSinceNoncurrentTime">DaysSinceNoncurrentTime</a>: <i>Double</i>
<a href="#matchesstorageclass" title="MatchesStorageClass">MatchesStorageClass</a>: <i>
      - String</i>
<a href="#noncurrenttimebefore" title="NoncurrentTimeBefore">NoncurrentTimeBefore</a>: <i>String</i>
<a href="#numnewerversions" title="NumNewerVersions">NumNewerVersions</a>: <i>Double</i>
<a href="#withstate" title="WithState">WithState</a>: <i>String</i>
</pre>

## Properties

#### Age

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedBefore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomTimeBefore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysSinceCustomTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysSinceNoncurrentTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchesStorageClass

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentTimeBefore

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumNewerVersions

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WithState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

