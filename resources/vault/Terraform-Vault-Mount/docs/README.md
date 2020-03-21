# Terraform::Vault::Mount

CloudFormation equivalent of vault_mount

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::Mount",
    "Properties" : {
        "<a href="#defaultleasettlseconds" title="DefaultLeaseTtlSeconds">DefaultLeaseTtlSeconds</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#local" title="Local">Local</a>" : <i>Boolean</i>,
        "<a href="#maxleasettlseconds" title="MaxLeaseTtlSeconds">MaxLeaseTtlSeconds</a>" : <i>Double</i>,
        "<a href="#options" title="Options">Options</a>" : <i>[ <a href="options.md">Options</a>, ... ]</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#sealwrap" title="SealWrap">SealWrap</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::Mount
Properties:
    <a href="#defaultleasettlseconds" title="DefaultLeaseTtlSeconds">DefaultLeaseTtlSeconds</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#local" title="Local">Local</a>: <i>Boolean</i>
    <a href="#maxleasettlseconds" title="MaxLeaseTtlSeconds">MaxLeaseTtlSeconds</a>: <i>Double</i>
    <a href="#options" title="Options">Options</a>: <i>
      - <a href="options.md">Options</a></i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#sealwrap" title="SealWrap">SealWrap</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### DefaultLeaseTtlSeconds

Default lease duration for tokens and secrets in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Human-friendly description of the mount.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Local

Boolean flag that can be explicitly set to true to enforce local mount in HA environment.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLeaseTtlSeconds

Maximum possible lease duration for tokens and secrets in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

Specifies mount type specific options that are passed to the backend.

_Required_: No

_Type_: List of <a href="options.md">Options</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Where the secret backend will be mounted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SealWrap

Boolean flag that can be explicitly set to true to enable seal wrapping for the mount, causing values stored by the mount to be wrapped by the seal's encryption capability.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the backend, such as "aws".

_Required_: Yes

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

#### Accessor

Returns the <code>Accessor</code> value.

