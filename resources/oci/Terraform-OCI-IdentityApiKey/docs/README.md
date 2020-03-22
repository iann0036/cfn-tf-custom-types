# Terraform::OCI::IdentityApiKey

This resource provides the Api Key resource in Oracle Cloud Infrastructure Identity service.

Uploads an API signing key for the specified user.

Every user has permission to use this operation to upload a key for *their own user ID*. An
administrator in your organization does not need to write a policy to give users this ability.
To compare, administrators who have permission to the tenancy can use this operation to upload a
key for any user, including themselves.

**Important:** Even though you have permission to upload an API key, you might not yet
have permission to do much else. If you try calling an operation unrelated to your own credential
management (e.g., `ListUsers`, `LaunchInstance`) and receive an "unauthorized" error,
check with an administrator to confirm which IAM Service group(s) you're in and what access
you have. Also confirm you're working in the correct compartment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::IdentityApiKey",
    "Properties" : {
        "<a href="#keyvalue" title="KeyValue">KeyValue</a>" : <i>String</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::IdentityApiKey
Properties:
    <a href="#keyvalue" title="KeyValue">KeyValue</a>: <i>String</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### KeyValue

The public key.  Must be an RSA key in PEM format.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

The OCID of the user.

_Required_: Yes

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

#### Fingerprint

Returns the <code>Fingerprint</code> value.

#### Id

Returns the <code>Id</code> value.

#### InactiveStatus

Returns the <code>InactiveStatus</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

