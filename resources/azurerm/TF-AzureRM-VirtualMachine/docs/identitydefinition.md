# TF::AzureRM::VirtualMachine IdentityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#identityids" title="IdentityIds">IdentityIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#identityids" title="IdentityIds">IdentityIds</a>: <i>
      - String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### IdentityIds

Specifies a list of user managed identity ids to be assigned to the VM. Required if `type` is `UserAssigned`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The Managed Service Identity Type of this Virtual Machine. Possible values are `SystemAssigned` (where Azure will generate a Service Principal for you), `UserAssigned` (where you can specify the Service Principal ID's) to be used by this Virtual Machine using the `identity_ids` field, and `SystemAssigned, UserAssigned` which assigns both a system managed identity as well as the specified user assigned identities.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

