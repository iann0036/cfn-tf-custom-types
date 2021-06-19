# TF::Vultr::FirewallGroup

Provides a Vultr Firewall Group resource. This can be used to create, read, modify, and delete Firewall Group.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::FirewallGroup",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::FirewallGroup
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
</pre>

## Properties

#### Description

Description of the firewall group.

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

#### DateCreated

Returns the <code>DateCreated</code> value.

#### DateModified

Returns the <code>DateModified</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstanceCount

Returns the <code>InstanceCount</code> value.

#### MaxRuleCount

Returns the <code>MaxRuleCount</code> value.

#### RuleCount

Returns the <code>RuleCount</code> value.

