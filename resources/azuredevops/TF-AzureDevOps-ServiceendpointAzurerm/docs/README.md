# TF::AzureDevOps::ServiceendpointAzurerm

Manages Manual or Automatic AzureRM service endpoint within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::ServiceendpointAzurerm",
    "Properties" : {
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="authorizationdefinition.md">AuthorizationDefinition</a>, ... ]</i>,
        "<a href="#azurermspntenantid" title="AzurermSpnTenantid">AzurermSpnTenantid</a>" : <i>String</i>,
        "<a href="#azurermsubscriptionid" title="AzurermSubscriptionId">AzurermSubscriptionId</a>" : <i>String</i>,
        "<a href="#azurermsubscriptionname" title="AzurermSubscriptionName">AzurermSubscriptionName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
        "<a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>" : <i>String</i>,
        "<a href="#credentials" title="Credentials">Credentials</a>" : <i>[ <a href="credentialsdefinition.md">CredentialsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::ServiceendpointAzurerm
Properties:
    <a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="authorizationdefinition.md">AuthorizationDefinition</a></i>
    <a href="#azurermspntenantid" title="AzurermSpnTenantid">AzurermSpnTenantid</a>: <i>String</i>
    <a href="#azurermsubscriptionid" title="AzurermSubscriptionId">AzurermSubscriptionId</a>: <i>String</i>
    <a href="#azurermsubscriptionname" title="AzurermSubscriptionName">AzurermSubscriptionName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
    <a href="#serviceendpointname" title="ServiceEndpointName">ServiceEndpointName</a>: <i>String</i>
    <a href="#credentials" title="Credentials">Credentials</a>: <i>
      - <a href="credentialsdefinition.md">CredentialsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Authorization

_Required_: No

_Type_: List of <a href="authorizationdefinition.md">AuthorizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurermSpnTenantid

The tenant id if the service principal.
- `azurerm_subscription_id` - (Required) The subscription Id of the Azure targets.
- `azurerm_subscription_name` - (Required) The subscription Name of the targets.
- `description` - (Optional) Service connection description.
- `credentials` - (Optional) A `credentials` block.
- `resource_group` - (Optional) The resource group used for scope of automatic service endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurermSubscriptionId

The subscription Id of the Azure targets.
- `azurerm_subscription_name` - (Required) The subscription Name of the targets.
- `description` - (Optional) Service connection description.
- `credentials` - (Optional) A `credentials` block.
- `resource_group` - (Optional) The resource group used for scope of automatic service endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurermSubscriptionName

The subscription Name of the targets.
- `description` - (Optional) Service connection description.
- `credentials` - (Optional) A `credentials` block.
- `resource_group` - (Optional) The resource group used for scope of automatic service endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Service connection description.
- `credentials` - (Optional) A `credentials` block.
- `resource_group` - (Optional) The resource group used for scope of automatic service endpoint.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID or project name.
- `service_endpoint_name` - (Required) The Service Endpoint name.
- `azurerm_spn_tenantid` - (Required) The tenant id if the service principal.
- `azurerm_subscription_id` - (Required) The subscription Id of the Azure targets.
- `azurerm_subscription_name` - (Required) The subscription Name of the targets.
- `description` - (Optional) Service connection description.
- `credentials` - (Optional) A `credentials` block.
- `resource_group` - (Optional) The resource group used for scope of automatic service endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

The resource group used for scope of automatic service endpoint.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceEndpointName

The Service Endpoint name.
- `azurerm_spn_tenantid` - (Required) The tenant id if the service principal.
- `azurerm_subscription_id` - (Required) The subscription Id of the Azure targets.
- `azurerm_subscription_name` - (Required) The subscription Name of the targets.
- `description` - (Optional) Service connection description.
- `credentials` - (Optional) A `credentials` block.
- `resource_group` - (Optional) The resource group used for scope of automatic service endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credentials

_Required_: No

_Type_: List of <a href="credentialsdefinition.md">CredentialsDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

