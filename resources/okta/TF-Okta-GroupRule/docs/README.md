# TF::Okta::GroupRule

Creates an Okta Group Rule.

This resource allows you to create and configure an Okta Group Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::GroupRule",
    "Properties" : {
        "<a href="#expressiontype" title="ExpressionType">ExpressionType</a>" : <i>String</i>,
        "<a href="#expressionvalue" title="ExpressionValue">ExpressionValue</a>" : <i>String</i>,
        "<a href="#groupassignments" title="GroupAssignments">GroupAssignments</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#removeassignedusers" title="RemoveAssignedUsers">RemoveAssignedUsers</a>" : <i>Boolean</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::GroupRule
Properties:
    <a href="#expressiontype" title="ExpressionType">ExpressionType</a>: <i>String</i>
    <a href="#expressionvalue" title="ExpressionValue">ExpressionValue</a>: <i>String</i>
    <a href="#groupassignments" title="GroupAssignments">GroupAssignments</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#removeassignedusers" title="RemoveAssignedUsers">RemoveAssignedUsers</a>: <i>Boolean</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### ExpressionType

The expression type to use to invoke the rule. The default
is `"urn:okta:expression:1.0"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpressionValue

The expression value.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupAssignments

The list of group ids to assign the users to.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Group Rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveAssignedUsers

This tells the provider to remove users added by this rule from the assigned
group after destroying this resource. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The status of the group rule.

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

#### Id

Returns the <code>Id</code> value.

