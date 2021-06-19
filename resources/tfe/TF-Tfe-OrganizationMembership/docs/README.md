# TF::Tfe::OrganizationMembership

Add or remove a user from an organization.

~> **NOTE:** This resource requires using the provider with Terraform Cloud or
an instance of Terraform Enterprise at least as recent as v202004-1.

~> **NOTE:** This resource cannot be used to update an existing user's email address
since users themselves are the only ones permitted to update their email address.
If a user updates their email address, configurations using the email address should
be updated manually.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Tfe::OrganizationMembership",
    "Properties" : {
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Tfe::OrganizationMembership
Properties:
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
</pre>

## Properties

#### Email

Email of the user to add.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

Name of the organization.

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

#### Id

Returns the <code>Id</code> value.

#### UserId

Returns the <code>UserId</code> value.

