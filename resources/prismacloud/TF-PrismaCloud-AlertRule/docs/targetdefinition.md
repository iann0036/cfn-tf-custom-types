# TF::PrismaCloud::AlertRule TargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountgroups" title="AccountGroups">AccountGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#excludedaccounts" title="ExcludedAccounts">ExcludedAccounts</a>" : <i>[ String, ... ]</i>,
    "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accountgroups" title="AccountGroups">AccountGroups</a>: <i>
      - String</i>
<a href="#excludedaccounts" title="ExcludedAccounts">ExcludedAccounts</a>: <i>
      - String</i>
<a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
</pre>

## Properties

#### AccountGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedAccounts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

