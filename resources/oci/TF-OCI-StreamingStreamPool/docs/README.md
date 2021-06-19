# TF::OCI::StreamingStreamPool

This resource provides the Stream Pool resource in Oracle Cloud Infrastructure Streaming service.

Starts the provisioning of a new stream pool.
To track the progress of the provisioning, you can periodically call GetStreamPool.
In the response, the `lifecycleState` parameter of the object tells you its current state.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::StreamingStreamPool",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#customencryptionkey" title="CustomEncryptionKey">CustomEncryptionKey</a>" : <i>[ <a href="customencryptionkeydefinition.md">CustomEncryptionKeyDefinition</a>, ... ]</i>,
        "<a href="#kafkasettings" title="KafkaSettings">KafkaSettings</a>" : <i>[ <a href="kafkasettingsdefinition.md">KafkaSettingsDefinition</a>, ... ]</i>,
        "<a href="#privateendpointsettings" title="PrivateEndpointSettings">PrivateEndpointSettings</a>" : <i>[ <a href="privateendpointsettingsdefinition.md">PrivateEndpointSettingsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::StreamingStreamPool
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#customencryptionkey" title="CustomEncryptionKey">CustomEncryptionKey</a>: <i>
      - <a href="customencryptionkeydefinition.md">CustomEncryptionKeyDefinition</a></i>
    <a href="#kafkasettings" title="KafkaSettings">KafkaSettings</a>: <i>
      - <a href="kafkasettingsdefinition.md">KafkaSettingsDefinition</a></i>
    <a href="#privateendpointsettings" title="PrivateEndpointSettings">PrivateEndpointSettings</a>: <i>
      - <a href="privateendpointsettingsdefinition.md">PrivateEndpointSettingsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The OCID of the compartment that contains the stream.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

(Updatable) The name of the stream pool. Avoid entering confidential information.  Example: `MyStreamPool`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomEncryptionKey

_Required_: No

_Type_: List of <a href="customencryptionkeydefinition.md">CustomEncryptionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KafkaSettings

_Required_: No

_Type_: List of <a href="kafkasettingsdefinition.md">KafkaSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateEndpointSettings

_Required_: No

_Type_: List of <a href="privateendpointsettingsdefinition.md">PrivateEndpointSettingsDefinition</a>

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

#### EndpointFqdn

Returns the <code>EndpointFqdn</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsPrivate

Returns the <code>IsPrivate</code> value.

#### LifecycleStateDetails

Returns the <code>LifecycleStateDetails</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

