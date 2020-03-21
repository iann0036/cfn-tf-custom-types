# Terraform::Mailgun::Route

Provides a Mailgun Route resource. This can be used to create and manage routes on Mailgun.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Mailgun::Route",
    "Properties" : {
        "<a href="#actions" title="Actions">Actions</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#expression" title="Expression">Expression</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Mailgun::Route
Properties:
    <a href="#actions" title="Actions">Actions</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#expression" title="Expression">Expression</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
</pre>

## Properties

#### Actions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

(Required).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expression

(Required) A filter expression like `match_recipient('.*@gmail.com')`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

(Required) Smaller number indicates higher priority. Higher priority routes are handled first.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

(Optional) The region where domain will be created. Default value is `us`.

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

