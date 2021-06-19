# TF::AzureRM::ManagedApplicationDefinition AuthorizationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#roledefinitionid" title="RoleDefinitionId">RoleDefinitionId</a>" : <i>String</i>,
    "<a href="#serviceprincipalid" title="ServicePrincipalId">ServicePrincipalId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#roledefinitionid" title="RoleDefinitionId">RoleDefinitionId</a>: <i>String</i>
<a href="#serviceprincipalid" title="ServicePrincipalId">ServicePrincipalId</a>: <i>String</i>
</pre>

## Properties

#### RoleDefinitionId

Specifies a role definition identifier for the provider. This role will define all the permissions that the provider must have on the managed application's container resource group. This role definition cannot have permission to delete the resource group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipalId

Specifies a service principal identifier for the provider. This is the identity that the provider will use to call ARM to manage the managed application resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

