# TF::AzureRM::FrontdoorCustomHttpsConfiguration

Manages the Custom Https Configuration for an Azure Front Door Frontend Endpoint..

-> **NOTE:** Defining custom https configurations using a separate `azurerm_frontdoor_custom_https_configuration` resource allows for parallel creation/update.

!> **BREAKING CHANGE:** In order to address the ordering issue we have changed the design on how to retrieve existing sub resources such as frontend endpoints. Existing design will be deprecated and will result in an incorrect configuration. Please refer to the updated documentation below for more information.

!> **BREAKING CHANGE:** The `resource_group_name` field has been removed as of the `v2.58.0` provider release. If the `resource_group_name` field has been defined in your current `azurerm_frontdoor_custom_https_configuration` resource configuration file please remove it else you will receive a `An argument named "resource_group_name" is not expected here.` error. If your pre-existing Front Door instance contained inline `custom_https_configuration` blocks th...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::FrontdoorCustomHttpsConfiguration",
    "Properties" : {
        "<a href="#customhttpsprovisioningenabled" title="CustomHttpsProvisioningEnabled">CustomHttpsProvisioningEnabled</a>" : <i>Boolean</i>,
        "<a href="#frontendendpointid" title="FrontendEndpointId">FrontendEndpointId</a>" : <i>String</i>,
        "<a href="#customhttpsconfiguration" title="CustomHttpsConfiguration">CustomHttpsConfiguration</a>" : <i>[ <a href="customhttpsconfigurationdefinition.md">CustomHttpsConfigurationDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::FrontdoorCustomHttpsConfiguration
Properties:
    <a href="#customhttpsprovisioningenabled" title="CustomHttpsProvisioningEnabled">CustomHttpsProvisioningEnabled</a>: <i>Boolean</i>
    <a href="#frontendendpointid" title="FrontendEndpointId">FrontendEndpointId</a>: <i>String</i>
    <a href="#customhttpsconfiguration" title="CustomHttpsConfiguration">CustomHttpsConfiguration</a>: <i>
      - <a href="customhttpsconfigurationdefinition.md">CustomHttpsConfigurationDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CustomHttpsProvisioningEnabled

Should the HTTPS protocol be enabled for this custom domain associated with the Front Door?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendEndpointId

The ID of the FrontDoor Frontend Endpoint which this configuration refers to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHttpsConfiguration

_Required_: No

_Type_: List of <a href="customhttpsconfigurationdefinition.md">CustomHttpsConfigurationDefinition</a>

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

