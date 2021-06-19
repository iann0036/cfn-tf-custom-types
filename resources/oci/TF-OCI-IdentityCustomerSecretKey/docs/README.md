# TF::OCI::IdentityCustomerSecretKey

This resource provides the Customer Secret Key resource in Oracle Cloud Infrastructure Identity service.

Creates a new secret key for the specified user. Secret keys are used for authentication with the Object Storage Service's Amazon S3
compatible API. The secret key consists of an Access Key/Secret Key pair. For information, see
[Managing User Credentials](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm).

You must specify a *description* for the secret key (although it can be an empty string). It does not
have to be unique, and you can change it anytime with
[UpdateCustomerSecretKey](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/CustomerSecretKeySummary/UpdateCustomerSecretKey).

Every user has permission to create a secret key for *their own user ID*. An administrator in your organization
does not need to write a policy to give users this ability. To compare, administrators who have permission to the
tenancy can use this operation to create a secret k...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::IdentityCustomerSecretKey",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::IdentityCustomerSecretKey
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DisplayName

(Updatable) The name you assign to the secret key during creation. Does not have to be unique, and it's changeable.

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

#### Id

Returns the <code>Id</code> value.

#### InactiveState

Returns the <code>InactiveState</code> value.

#### Key

Returns the <code>Key</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeExpires

Returns the <code>TimeExpires</code> value.

