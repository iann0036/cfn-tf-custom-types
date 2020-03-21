# Terraform::AzureRM::PolicyAssignment Identity

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Type

The Managed Service Identity Type of this Policy Assignment. Possible values are `SystemAssigned` (where Azure will generate a Service Principal for you), or `None` (no use of a Managed Service Identity).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

