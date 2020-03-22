# Terraform::Google::KmsCryptoKey

A `CryptoKey` represents a logical key that can be used for cryptographic operations.


~> **Note:** CryptoKeys cannot be deleted from Google Cloud Platform.
Destroying a Terraform-managed CryptoKey will remove it from state
and delete all CryptoKeyVersions, rendering the key unusable, but *will
not delete the resource on the server.* When Terraform destroys these keys,
any data previously encrypted with these keys will be irrecoverable.
For this reason, it is strongly recommended that you add lifecycle hooks
to the resource to prevent accidental destruction.


To get more information about CryptoKey, see:

* [API documentation](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys)
* How-to Guides
    * [Creating a key](https://cloud.google.com/kms/docs/creating-keys#create_a_key)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::KmsCryptoKey",
    "Properties" : {
        "<a href="#keyring" title="KeyRing">KeyRing</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#purpose" title="Purpose">Purpose</a>" : <i>String</i>,
        "<a href="#rotationperiod" title="RotationPeriod">RotationPeriod</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#versiontemplate" title="VersionTemplate">VersionTemplate</a>" : <i>[ <a href="versiontemplate.md">VersionTemplate</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::KmsCryptoKey
Properties:
    <a href="#keyring" title="KeyRing">KeyRing</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#purpose" title="Purpose">Purpose</a>: <i>String</i>
    <a href="#rotationperiod" title="RotationPeriod">RotationPeriod</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#versiontemplate" title="VersionTemplate">VersionTemplate</a>: <i>
      - <a href="versiontemplate.md">VersionTemplate</a></i>
</pre>

## Properties

#### KeyRing

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Purpose

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationPeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionTemplate

_Required_: No

_Type_: List of <a href="versiontemplate.md">VersionTemplate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

