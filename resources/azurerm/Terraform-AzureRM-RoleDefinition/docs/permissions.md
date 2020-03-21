# Terraform::AzureRM::RoleDefinition Permissions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actions" title="Actions">Actions</a>" : <i>[ String, ... ]</i>,
    "<a href="#dataactions" title="DataActions">DataActions</a>" : <i>[ String, ... ]</i>,
    "<a href="#notactions" title="NotActions">NotActions</a>" : <i>[ String, ... ]</i>,
    "<a href="#notdataactions" title="NotDataActions">NotDataActions</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#actions" title="Actions">Actions</a>: <i>
      - String</i>
<a href="#dataactions" title="DataActions">DataActions</a>: <i>
      - String</i>
<a href="#notactions" title="NotActions">NotActions</a>: <i>
      - String</i>
<a href="#notdataactions" title="NotDataActions">NotDataActions</a>: <i>
      - String</i>
</pre>

## Properties

#### Actions

One or more Allowed Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataActions

One or more Allowed Data Actions, such as `*`, `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotActions

One or more Disallowed Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotDataActions

One or more Disallowed Data Actions, such as `*`, `Microsoft.Resources/subscriptions/resourceGroups/read`. See ['Azure Resource Manager resource provider operations'](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations) for details.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

