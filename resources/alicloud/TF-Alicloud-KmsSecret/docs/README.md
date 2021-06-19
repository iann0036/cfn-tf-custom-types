# TF::Alicloud::KmsSecret

CloudFormation equivalent of alicloud_kms_secret

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::KmsSecret",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enableautomaticrotation" title="EnableAutomaticRotation">EnableAutomaticRotation</a>" : <i>Boolean</i>,
        "<a href="#encryptionkeyid" title="EncryptionKeyId">EncryptionKeyId</a>" : <i>String</i>,
        "<a href="#forcedeletewithoutrecovery" title="ForceDeleteWithoutRecovery">ForceDeleteWithoutRecovery</a>" : <i>Boolean</i>,
        "<a href="#recoverywindowindays" title="RecoveryWindowInDays">RecoveryWindowInDays</a>" : <i>Double</i>,
        "<a href="#rotationinterval" title="RotationInterval">RotationInterval</a>" : <i>String</i>,
        "<a href="#secretdata" title="SecretData">SecretData</a>" : <i>String</i>,
        "<a href="#secretdatatype" title="SecretDataType">SecretDataType</a>" : <i>String</i>,
        "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#versionid" title="VersionId">VersionId</a>" : <i>String</i>,
        "<a href="#versionstages" title="VersionStages">VersionStages</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::KmsSecret
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enableautomaticrotation" title="EnableAutomaticRotation">EnableAutomaticRotation</a>: <i>Boolean</i>
    <a href="#encryptionkeyid" title="EncryptionKeyId">EncryptionKeyId</a>: <i>String</i>
    <a href="#forcedeletewithoutrecovery" title="ForceDeleteWithoutRecovery">ForceDeleteWithoutRecovery</a>: <i>Boolean</i>
    <a href="#recoverywindowindays" title="RecoveryWindowInDays">RecoveryWindowInDays</a>: <i>Double</i>
    <a href="#rotationinterval" title="RotationInterval">RotationInterval</a>: <i>String</i>
    <a href="#secretdata" title="SecretData">SecretData</a>: <i>String</i>
    <a href="#secretdatatype" title="SecretDataType">SecretDataType</a>: <i>String</i>
    <a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#versionid" title="VersionId">VersionId</a>: <i>String</i>
    <a href="#versionstages" title="VersionStages">VersionStages</a>: <i>
      - String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutomaticRotation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDeleteWithoutRecovery

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryWindowInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationInterval

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretData

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretDataType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionStages

_Required_: No

_Type_: List of String

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### PlannedDeleteTime

Returns the <code>PlannedDeleteTime</code> value.

