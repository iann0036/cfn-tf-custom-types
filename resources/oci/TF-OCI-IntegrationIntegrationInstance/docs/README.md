# TF::OCI::IntegrationIntegrationInstance

This resource provides the Integration Instance resource in Oracle Cloud Infrastructure Integration service.

Creates a new Integration Instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::IntegrationIntegrationInstance",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#consumptionmodel" title="ConsumptionModel">ConsumptionModel</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#idcsat" title="IdcsAt">IdcsAt</a>" : <i>String</i>,
        "<a href="#integrationinstancetype" title="IntegrationInstanceType">IntegrationInstanceType</a>" : <i>String</i>,
        "<a href="#isbyol" title="IsByol">IsByol</a>" : <i>Boolean</i>,
        "<a href="#isfileserverenabled" title="IsFileServerEnabled">IsFileServerEnabled</a>" : <i>Boolean</i>,
        "<a href="#isvisualbuilderenabled" title="IsVisualBuilderEnabled">IsVisualBuilderEnabled</a>" : <i>Boolean</i>,
        "<a href="#messagepacks" title="MessagePacks">MessagePacks</a>" : <i>Double</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#alternatecustomendpoints" title="AlternateCustomEndpoints">AlternateCustomEndpoints</a>" : <i>[ <a href="alternatecustomendpointsdefinition.md">AlternateCustomEndpointsDefinition</a>, ... ]</i>,
        "<a href="#customendpoint" title="CustomEndpoint">CustomEndpoint</a>" : <i>[ <a href="customendpointdefinition.md">CustomEndpointDefinition</a>, ... ]</i>,
        "<a href="#networkendpointdetails" title="NetworkEndpointDetails">NetworkEndpointDetails</a>" : <i>[ <a href="networkendpointdetailsdefinition.md">NetworkEndpointDetailsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::IntegrationIntegrationInstance
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#consumptionmodel" title="ConsumptionModel">ConsumptionModel</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#idcsat" title="IdcsAt">IdcsAt</a>: <i>String</i>
    <a href="#integrationinstancetype" title="IntegrationInstanceType">IntegrationInstanceType</a>: <i>String</i>
    <a href="#isbyol" title="IsByol">IsByol</a>: <i>Boolean</i>
    <a href="#isfileserverenabled" title="IsFileServerEnabled">IsFileServerEnabled</a>: <i>Boolean</i>
    <a href="#isvisualbuilderenabled" title="IsVisualBuilderEnabled">IsVisualBuilderEnabled</a>: <i>Boolean</i>
    <a href="#messagepacks" title="MessagePacks">MessagePacks</a>: <i>Double</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#alternatecustomendpoints" title="AlternateCustomEndpoints">AlternateCustomEndpoints</a>: <i>
      - <a href="alternatecustomendpointsdefinition.md">AlternateCustomEndpointsDefinition</a></i>
    <a href="#customendpoint" title="CustomEndpoint">CustomEndpoint</a>: <i>
      - <a href="customendpointdefinition.md">CustomEndpointDefinition</a></i>
    <a href="#networkendpointdetails" title="NetworkEndpointDetails">NetworkEndpointDetails</a>: <i>
      - <a href="networkendpointdetailsdefinition.md">NetworkEndpointDetailsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) Compartment Identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsumptionModel

Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) Integration Instance Identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdcsAt

(Updatable) IDCS Authentication token. This is required for all realms with IDCS. Its optional as its not required for non IDCS realms.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationInstanceType

(Updatable) Standard or Enterprise type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsByol

(Updatable) Bring your own license.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFileServerEnabled

(Updatable) The file server is enabled or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsVisualBuilderEnabled

(Updatable) Visual Builder is enabled or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessagePacks

(Updatable) The number of configured message packs.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

(Updatable) The target state for the instance. Could be set to ACTIVE or INACTIVE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlternateCustomEndpoints

_Required_: No

_Type_: List of <a href="alternatecustomendpointsdefinition.md">AlternateCustomEndpointsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomEndpoint

_Required_: No

_Type_: List of <a href="customendpointdefinition.md">CustomEndpointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkEndpointDetails

_Required_: No

_Type_: List of <a href="networkendpointdetailsdefinition.md">NetworkEndpointDetailsDefinition</a>

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

The Virtual Cloud Network OCID.
* `is_integration_vcn_allowlisted` - (Optional) The Integration service's VCN is allow-listed to allow integrations to call back into other integrations
* `network_endpoint_type` - (Required) The type of network endpoint.

#### InstanceUrl

Returns the <code>InstanceUrl</code> value.

#### StateMessage

Returns the <code>StateMessage</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

