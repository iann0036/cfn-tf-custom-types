# TF::AzureDevOps::ServiceendpointAzurecr

Manages a Azure Container Registry service endpoint within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::ServiceendpointAzurecr",
    "Properties" : {
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="authorizationdefinition.md">AuthorizationDefinition</a>, ... ]</i>,
        "<a href="#azurecrname" title="AzurecrName">AzurecrName</a>" : <i>String</i>,
        "<a href="#azurecrspntenantid" title="AzurecrSpnTenantid">AzurecrSpnTenantid</a>" : <i>String</i>,
        "<a href="#azurecrsubscriptionid" title="AzurecrSubscriptionId">AzurecrSubscriptionId</a>" : <i>String</i>,
        "<a href="#azurecrsubscriptionname" title="AzurecrSubscriptionName">AzurecrSubscriptionName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
        "<a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::ServiceendpointAzurecr
Properties:
    <a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="authorizationdefinition.md">AuthorizationDefinition</a></i>
    <a href="#azurecrname" title="AzurecrName">AzurecrName</a>: <i>String</i>
    <a href="#azurecrspntenantid" title="AzurecrSpnTenantid">AzurecrSpnTenantid</a>: <i>String</i>
    <a href="#azurecrsubscriptionid" title="AzurecrSubscriptionId">AzurecrSubscriptionId</a>: <i>String</i>
    <a href="#azurecrsubscriptionname" title="AzurecrSubscriptionName">AzurecrSubscriptionName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
    <a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Authorization

_Required_: No

_Type_: List of <a href="authorizationdefinition.md">AuthorizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurecrName

The Azure container registry name.
- `azurecr_subscription_id` - (Required) The subscription id of the Azure targets.
- `azurecr_subscription_name` - (Required) The subscription name of the Azure targets.
- `description` - (Optional) The name you will use to refer to this service connection in task inputs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurecrSpnTenantid

The tenant id of the service principal.
- `azurecr_name` - (Required) The Azure container registry name.
- `azurecr_subscription_id` - (Required) The subscription id of the Azure targets.
- `azurecr_subscription_name` - (Required) The subscription name of the Azure targets.
- `description` - (Optional) The name you will use to refer to this service connection in task inputs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurecrSubscriptionId

The subscription id of the Azure targets.
- `azurecr_subscription_name` - (Required) The subscription name of the Azure targets.
- `description` - (Optional) The name you will use to refer to this service connection in task inputs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurecrSubscriptionName

The subscription name of the Azure targets.
- `description` - (Optional) The name you will use to refer to this service connection in task inputs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The name you will use to refer to this service connection in task inputs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID or project name.
- `service_endpoint_name` - (Required) The name you will use to refer to this service connection in task inputs.
- `resource_group` - (Required) The resource group to which the container registry belongs.
- `azurecr_spn_tenantid` - (Required) The tenant id of the service principal.
- `azurecr_name` - (Required) The Azure container registry name.
- `azurecr_subscription_id` - (Required) The subscription id of the Azure targets.
- `azurecr_subscription_name` - (Required) The subscription name of the Azure targets.
- `description` - (Optional) The name you will use to refer to this service connection in task inputs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

The resource group to which the container registry belongs.
- `azurecr_spn_tenantid` - (Required) The tenant id of the service principal.
- `azurecr_name` - (Required) The Azure container registry name.
- `azurecr_subscription_id` - (Required) The subscription id of the Azure targets.
- `azurecr_subscription_name` - (Required) The subscription name of the Azure targets.
- `description` - (Optional) The name you will use to refer to this service connection in task inputs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceEndpointName

The name you will use to refer to this service connection in task inputs.
- `resource_group` - (Required) The resource group to which the container registry belongs.
- `azurecr_spn_tenantid` - (Required) The tenant id of the service principal.
- `azurecr_name` - (Required) The Azure container registry name.
- `azurecr_subscription_id` - (Required) The subscription id of the Azure targets.
- `azurecr_subscription_name` - (Required) The subscription name of the Azure targets.
- `description` - (Optional) The name you will use to refer to this service connection in task inputs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AppObjectId

Returns the <code>AppObjectId</code> value.

#### AzSpnRoleAssignmentId

Returns the <code>AzSpnRoleAssignmentId</code> value.

#### AzSpnRolePermissions

Returns the <code>AzSpnRolePermissions</code> value.

#### Id

Returns the <code>Id</code> value.

#### ServicePrincipalId

Returns the <code>ServicePrincipalId</code> value.

#### SpnObjectId

Returns the <code>SpnObjectId</code> value.

