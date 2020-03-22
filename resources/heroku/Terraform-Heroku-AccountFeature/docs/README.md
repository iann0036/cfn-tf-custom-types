# Terraform::Heroku::AccountFeature

This resource is used to create and manage [User Features](https://devcenter.heroku.com/articles/heroku-beta-features) on Heroku.

~> **NOTE:** If this resource's HCL is removed from a `.tf` file, the behavior is to disable account feature
and remove resource from state.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::AccountFeature",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::AccountFeature
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Enabled

Enable or disable the account feature.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the account feature.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Description

Returns the <code>Description</code> value.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

