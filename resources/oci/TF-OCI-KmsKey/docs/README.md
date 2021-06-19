# TF::OCI::KmsKey

This resource provides the Key resource in Oracle Cloud Infrastructure Kms service.

Creates a new master encryption key.

As a management operation, this call is subject to a Key Management limit that applies to the total
number of requests across all management write operations. Key Management might throttle this call
to reject an otherwise valid request when the total rate of management write operations exceeds 10
requests per second for a given tenancy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::KmsKey",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#desiredstate" title="DesiredState">DesiredState</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#managementendpoint" title="ManagementEndpoint">ManagementEndpoint</a>" : <i>String</i>,
        "<a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>" : <i>String</i>,
        "<a href="#restoretrigger" title="RestoreTrigger">RestoreTrigger</a>" : <i>Boolean</i>,
        "<a href="#timeofdeletion" title="TimeOfDeletion">TimeOfDeletion</a>" : <i>String</i>,
        "<a href="#keyshape" title="KeyShape">KeyShape</a>" : <i>[ <a href="keyshapedefinition.md">KeyShapeDefinition</a>, ... ]</i>,
        "<a href="#restorefromfile" title="RestoreFromFile">RestoreFromFile</a>" : <i>[ <a href="restorefromfiledefinition.md">RestoreFromFileDefinition</a>, ... ]</i>,
        "<a href="#restorefromobjectstore" title="RestoreFromObjectStore">RestoreFromObjectStore</a>" : <i>[ <a href="restorefromobjectstoredefinition.md">RestoreFromObjectStoreDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::KmsKey
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#desiredstate" title="DesiredState">DesiredState</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#managementendpoint" title="ManagementEndpoint">ManagementEndpoint</a>: <i>String</i>
    <a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>: <i>String</i>
    <a href="#restoretrigger" title="RestoreTrigger">RestoreTrigger</a>: <i>Boolean</i>
    <a href="#timeofdeletion" title="TimeOfDeletion">TimeOfDeletion</a>: <i>String</i>
    <a href="#keyshape" title="KeyShape">KeyShape</a>: <i>
      - <a href="keyshapedefinition.md">KeyShapeDefinition</a></i>
    <a href="#restorefromfile" title="RestoreFromFile">RestoreFromFile</a>: <i>
      - <a href="restorefromfiledefinition.md">RestoreFromFileDefinition</a></i>
    <a href="#restorefromobjectstore" title="RestoreFromObjectStore">RestoreFromObjectStore</a>: <i>
      - <a href="restorefromobjectstoredefinition.md">RestoreFromObjectStoreDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The OCID of the compartment where you want to create the master encryption key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredState

(Updatable) Desired state of the key. Possible values : `ENABLED` or `DISABLED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementEndpoint

The service endpoint to perform management operations against. Management operations include 'Create,' 'Update,' 'List,' 'Get,' and 'Delete' operations. See Vault Management endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionMode

The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed. A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists  on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,  a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestoreTrigger

(Updatable) An optional property when flipped triggers restore from restore option provided in config file.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeOfDeletion

(Updatable) An optional property for the deletion time of the key, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. Example: `2019-04-03T21:10:29.600Z`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyShape

_Required_: No

_Type_: List of <a href="keyshapedefinition.md">KeyShapeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestoreFromFile

_Required_: No

_Type_: List of <a href="restorefromfiledefinition.md">RestoreFromFileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestoreFromObjectStore

_Required_: No

_Type_: List of <a href="restorefromobjectstoredefinition.md">RestoreFromObjectStoreDefinition</a>

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

#### CurrentKeyVersion

Returns the <code>CurrentKeyVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsPrimary

Returns the <code>IsPrimary</code> value.

#### ReplicaDetails

Returns the <code>ReplicaDetails</code> value.

#### RestoredFromKeyId

Returns the <code>RestoredFromKeyId</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### VaultId

Returns the <code>VaultId</code> value.

