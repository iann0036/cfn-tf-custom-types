# TF::AzureRM::DataProtectionBackupPolicyPostgresql RetentionRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#duration" title="Duration">Duration</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#criteria" title="Criteria">Criteria</a>" : <i>[ <a href="criteriadefinition.md">CriteriaDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#duration" title="Duration">Duration</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#criteria" title="Criteria">Criteria</a>: <i>
      - <a href="criteriadefinition.md">CriteriaDefinition</a></i>
</pre>

## Properties

#### Duration

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Criteria

_Required_: No

_Type_: List of <a href="criteriadefinition.md">CriteriaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

