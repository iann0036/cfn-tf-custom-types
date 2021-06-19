# TF::Google::KmsKeyRingImportJob

A `KeyRingImportJob` can be used to create `CryptoKeys` and `CryptoKeyVersions` using pre-existing
key material, generated outside of Cloud KMS. A `KeyRingImportJob` expires 3 days after it is created.
Once expired, Cloud KMS will no longer be able to import or unwrap any key material that
was wrapped with the `KeyRingImportJob`'s public key.


~> **Note:** KeyRingImportJobs cannot be deleted from Google Cloud Platform.
Destroying a Terraform-managed KeyRingImportJob will remove it from state but
*will not delete the resource from the project.* 


To get more information about KeyRingImportJob, see:

* [API documentation](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs)
* How-to Guides
    * [Importing a key](https://cloud.google.com/kms/docs/importing-a-key)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::KmsKeyRingImportJob",
    "Properties" : {
        "<a href="#importjobid" title="ImportJobId">ImportJobId</a>" : <i>String</i>,
        "<a href="#importmethod" title="ImportMethod">ImportMethod</a>" : <i>String</i>,
        "<a href="#keyring" title="KeyRing">KeyRing</a>" : <i>String</i>,
        "<a href="#protectionlevel" title="ProtectionLevel">ProtectionLevel</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::KmsKeyRingImportJob
Properties:
    <a href="#importjobid" title="ImportJobId">ImportJobId</a>: <i>String</i>
    <a href="#importmethod" title="ImportMethod">ImportMethod</a>: <i>String</i>
    <a href="#keyring" title="KeyRing">KeyRing</a>: <i>String</i>
    <a href="#protectionlevel" title="ProtectionLevel">ProtectionLevel</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ImportJobId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportMethod

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyRing

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionLevel

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

#### Attestation

Returns the <code>Attestation</code> value.

#### ExpireTime

Returns the <code>ExpireTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### PublicKey

Returns the <code>PublicKey</code> value.

#### State

Returns the <code>State</code> value.

