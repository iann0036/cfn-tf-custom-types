# TF::AzureRM::BackupPolicyFileShare RetentionYearlyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#months" title="Months">Months</a>" : <i>[ String, ... ]</i>,
    "<a href="#weekdays" title="Weekdays">Weekdays</a>" : <i>[ String, ... ]</i>,
    "<a href="#weeks" title="Weeks">Weeks</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#months" title="Months">Months</a>: <i>
      - String</i>
<a href="#weekdays" title="Weekdays">Weekdays</a>: <i>
      - String</i>
<a href="#weeks" title="Weeks">Weeks</a>: <i>
      - String</i>
</pre>

## Properties

#### Count

The number of yearly backups to keep. Must be between `1` and `10`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Months

The months of the year to retain backups of. Must be one of `January`, `February`, `March`, `April`, `May`, `June`, `July`, `Augest`, `September`, `October`, `November` and `December`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weekdays

The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weeks

The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

