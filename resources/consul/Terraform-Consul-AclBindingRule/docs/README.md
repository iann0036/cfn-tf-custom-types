# Terraform::Consul::AclBindingRule

Starting with Consul 1.5.0, the consul_acl_binding_rule resource can be used to
managed Consul ACL binding rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Consul::AclBindingRule",
    "Properties" : {
        "<a href="#authmethod" title="AuthMethod">AuthMethod</a>" : <i>String</i>,
        "<a href="#bindname" title="BindName">BindName</a>" : <i>String</i>,
        "<a href="#bindtype" title="BindType">BindType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#selector" title="Selector">Selector</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Consul::AclBindingRule
Properties:
    <a href="#authmethod" title="AuthMethod">AuthMethod</a>: <i>String</i>
    <a href="#bindname" title="BindName">BindName</a>: <i>String</i>
    <a href="#bindtype" title="BindType">BindType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#selector" title="Selector">Selector</a>: <i>String</i>
</pre>

## Properties

#### AuthMethod

The name of the ACL auth method this rule apply.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BindName

The name to bind to a token at login-time.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BindType

Specifies the way the binding rule affects a token
created at login.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A free form human readable description of the
binding rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

The expression used to math this rule against valid
identities returned from an auth method validation.

_Required_: No

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

