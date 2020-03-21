# Terraform::Cloudflare::AccountMember

Provides a resource which manages Cloudflare account members.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::AccountMember",
    "Properties" : {
        "<a href="#emailaddress" title="EmailAddress">EmailAddress</a>" : <i>String</i>,
        "<a href="#roleids" title="RoleIds">RoleIds</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::AccountMember
Properties:
    <a href="#emailaddress" title="EmailAddress">EmailAddress</a>: <i>String</i>
    <a href="#roleids" title="RoleIds">RoleIds</a>: <i>
      - String</i>
</pre>

## Properties

#### EmailAddress

The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleIds

Array of account role IDs that you want to assign to a member.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

