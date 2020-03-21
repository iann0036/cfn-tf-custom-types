# Terraform::AzureRM::StorageManagementPolicy Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#actions" title="Actions">Actions</a>" : <i>[ <a href="rule-actions.md">Actions</a>, ... ]</i>,
    "<a href="#filters" title="Filters">Filters</a>" : <i>[ <a href="rule-filters.md">Filters</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#actions" title="Actions">Actions</a>: <i>
      - <a href="rule-actions.md">Actions</a></i>
<a href="#filters" title="Filters">Filters</a>: <i>
      - <a href="rule-filters.md">Filters</a></i>
</pre>

## Properties

#### Enabled

Boolean to specify whether the rule is enabled.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A rule name can contain any combination of alpha numeric characters. Rule name is case-sensitive. It must be unique within a policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Actions

_Required_: No

_Type_: List of <a href="rule-actions.md">Actions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filters

_Required_: No

_Type_: List of <a href="rule-filters.md">Filters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

