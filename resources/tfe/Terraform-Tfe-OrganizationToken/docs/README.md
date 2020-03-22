# Terraform::Tfe::OrganizationToken

Generates a new organization token, replacing any existing token. This token
can be used to act as the organization service account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Tfe::OrganizationToken",
    "Properties" : {
        "<a href="#forceregenerate" title="ForceRegenerate">ForceRegenerate</a>" : <i>Boolean</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Tfe::OrganizationToken
Properties:
    <a href="#forceregenerate" title="ForceRegenerate">ForceRegenerate</a>: <i>Boolean</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
</pre>

## Properties

#### ForceRegenerate

If set to `true`, a new token will be
generated even if a token already exists. This will invalidate the existing
token!.

_Required_: No

_Type_: Boolean

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

#### Token

Returns the <code>Token</code> value.

