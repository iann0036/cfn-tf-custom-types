# TF::TencentCloud::KmsExternalKey

Provide a resource to create a KMS external key.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::KmsExternalKey",
    "Properties" : {
        "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#isarchived" title="IsArchived">IsArchived</a>" : <i>Boolean</i>,
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#keymaterialbase64" title="KeyMaterialBase64">KeyMaterialBase64</a>" : <i>String</i>,
        "<a href="#pendingdeletewindowindays" title="PendingDeleteWindowInDays">PendingDeleteWindowInDays</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#validto" title="ValidTo">ValidTo</a>" : <i>Double</i>,
        "<a href="#wrappingalgorithm" title="WrappingAlgorithm">WrappingAlgorithm</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::KmsExternalKey
Properties:
    <a href="#alias" title="Alias">Alias</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#isarchived" title="IsArchived">IsArchived</a>: <i>Boolean</i>
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#keymaterialbase64" title="KeyMaterialBase64">KeyMaterialBase64</a>: <i>String</i>
    <a href="#pendingdeletewindowindays" title="PendingDeleteWindowInDays">PendingDeleteWindowInDays</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#validto" title="ValidTo">ValidTo</a>: <i>Double</i>
    <a href="#wrappingalgorithm" title="WrappingAlgorithm">WrappingAlgorithm</a>: <i>String</i>
</pre>

## Properties

#### Alias

Name of CMK. The name can only contain English letters, numbers, underscore and hyphen '-'. The first character must be a letter or number.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of CMK. The maximum is 1024 bytes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsArchived

Specify whether to archive key. Default value is `false`. This field is conflict with `is_enabled`, valid when key_state is `Enabled`, `Disabled`, `Archived`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

Specify whether to enable key. Default value is `false`. This field is conflict with `is_archived`, valid when key_state is `Enabled`, `Disabled`, `Archived`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyMaterialBase64

The base64-encoded key material encrypted with the public_key. For regions using the national secret version, the length of the imported key material is required to be 128 bits, and for regions using the FIPS version, the length of the imported key material is required to be 256 bits.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PendingDeleteWindowInDays

Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days. Defaults to 7 days.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags of CMK.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidTo

This value means the effective timestamp of the key material, 0 means it does not expire. Need to be greater than the current timestamp, the maximum support is 2147443200.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WrappingAlgorithm

The algorithm for encrypting key material. Available values include `RSAES_PKCS1_V1_5`, `RSAES_OAEP_SHA_1` and `RSAES_OAEP_SHA_256`. Default value is `RSAES_PKCS1_V1_5`.

_Required_: No

_Type_: String

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

#### KeyState

Returns the <code>KeyState</code> value.

