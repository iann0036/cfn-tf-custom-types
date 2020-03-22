# Terraform::OCI::KmsKeyVersion

This resource provides the Key Version resource in Oracle Cloud Infrastructure Kms service.

Generates a new [KeyVersion](https://docs.cloud.oracle.com/iaas/api/#/en/key/release/KeyVersion/) resource that provides new cryptographic
material for a master encryption key. The key must be in an ENABLED state to be rotated.

As a management operation, this call is subject to a Key Management limit that applies to the total number 
of requests across all  management write operations. Key Management might throttle this call to reject an 
otherwise valid request when the total rate of management write operations exceeds 10 requests per second 
for a given tenancy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::KmsKeyVersion",
    "Properties" : {
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#managementendpoint" title="ManagementEndpoint">ManagementEndpoint</a>" : <i>String</i>,
        "<a href="#timeofdeletion" title="TimeOfDeletion">TimeOfDeletion</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::KmsKeyVersion
Properties:
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#managementendpoint" title="ManagementEndpoint">ManagementEndpoint</a>: <i>String</i>
    <a href="#timeofdeletion" title="TimeOfDeletion">TimeOfDeletion</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### KeyId

The OCID of the key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementEndpoint

The service endpoint to perform management operations against. Management operations include 'Create,' 'Update,' 'List,' 'Get,' and 'Delete' operations. See Vault Management endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeOfDeletion

(Updatable) An optional property for the deletion time of the key version, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. Example: `2019-04-03T21:10:29.600Z`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeyVersionId

Returns the <code>KeyVersionId</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### VaultId

Returns the <code>VaultId</code> value.

