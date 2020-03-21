# Terraform::Vault::OktaAuthBackendGroup

Provides a resource to create a group in an
[Okta auth backend within Vault](https://www.vaultproject.io/docs/auth/okta.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::OktaAuthBackendGroup",
    "Properties" : {
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::OktaAuthBackendGroup
Properties:
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
</pre>

## Properties

#### GroupName

Name of the group within the Okta.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path where the Okta auth backend is mounted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

Vault policies to associate with this group.

_Required_: No

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

