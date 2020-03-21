# Terraform::AzureRM::ApplicationGateway Identity

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

Specifies a list with a single user managed identity id to be assigned to the Application Gateway.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The Managed Service Identity Type of this Application Gateway. The only possible value is `UserAssigned`. Defaults to `UserAssigned`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

