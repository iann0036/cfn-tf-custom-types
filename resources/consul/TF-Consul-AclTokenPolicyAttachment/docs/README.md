# TF::Consul::AclTokenPolicyAttachment

The `consul_acl_token_policy_attachment` resource links a Consul Token and an ACL
policy. The link is implemented through an update to the Consul ACL token.

~> **NOTE:** This resource is only useful to attach policies to an ACL token
that has been created outside the current Terraform configuration, like the
anonymous or the master token. If the token you need to attach a policy to has
been created in the current Terraform configuration and will only be used in it,
you should use the `policies` attribute of [`consul_acl_token`](/docs/providers/consul/r/acl_token.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Consul::AclTokenPolicyAttachment",
    "Properties" : {
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#tokenid" title="TokenId">TokenId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Consul::AclTokenPolicyAttachment
Properties:
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#tokenid" title="TokenId">TokenId</a>: <i>String</i>
</pre>

## Properties

#### Policy

The name of the policy attached to the token.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenId

The id of the token.

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

