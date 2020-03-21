# Terraform::AWS::DlmLifecyclePolicy PolicyDetails

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#resourcetypes" title="ResourceTypes">ResourceTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#targettags" title="TargetTags">TargetTags</a>" : <i>[ <a href="policydetails-targettags.md">TargetTags</a>, ... ]</i>,
    "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="policydetails-schedule.md">Schedule</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#resourcetypes" title="ResourceTypes">ResourceTypes</a>: <i>
      - String</i>
<a href="#targettags" title="TargetTags">TargetTags</a>: <i>
      - <a href="policydetails-targettags.md">TargetTags</a></i>
<a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="policydetails-schedule.md">Schedule</a></i>
</pre>

## Properties

#### ResourceTypes

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetTags

_Required_: Yes
_Type_: List of <a href="policydetails-targettags.md">TargetTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No
_Type_: List of <a href="policydetails-schedule.md">Schedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

