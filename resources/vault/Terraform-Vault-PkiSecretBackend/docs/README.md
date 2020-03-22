# Terraform::Vault::PkiSecretBackend

Creates an PKI Secret Backend for Vault. PKI secret backends can then issue certificates, once a role has been added to
the backend.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::PkiSecretBackend",
    "Properties" : {
        "<a href="#defaultleasettlseconds" title="DefaultLeaseTtlSeconds">DefaultLeaseTtlSeconds</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#maxleasettlseconds" title="MaxLeaseTtlSeconds">MaxLeaseTtlSeconds</a>" : <i>Double</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::PkiSecretBackend
Properties:
    <a href="#defaultleasettlseconds" title="DefaultLeaseTtlSeconds">DefaultLeaseTtlSeconds</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#maxleasettlseconds" title="MaxLeaseTtlSeconds">MaxLeaseTtlSeconds</a>: <i>Double</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### DefaultLeaseTtlSeconds

The default TTL for credentials issued by this backend.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description for this backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLeaseTtlSeconds

The maximum TTL that can be requested for credentials issued by this backend.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The unique path this backend should be mounted at. Must not begin or end with a `/`.

_Required_: Yes

_Type_: String

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

