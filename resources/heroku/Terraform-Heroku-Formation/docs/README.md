# Terraform::Heroku::Formation

Provides a [Heroku Formation](https://devcenter.heroku.com/articles/platform-api-reference#formation)
resource.

A formation represents the formation of processes that should be set for an application.

~> **NOTE:** 
- The application must have a dyno in order to update its formation.
- If the heroku formation resource is removed and deleted, this will be a no-op action in Heroku.
The Heroku Platform does not have a `DELETE` endpoint for `formation`.
- This resource works well with the `heroku_app_release` resource, which allows you to deploy a slug/release to an application
before the formation can be updated.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::Formation",
    "Properties" : {
        "<a href="#app" title="App">App</a>" : <i>String</i>,
        "<a href="#quantity" title="Quantity">Quantity</a>" : <i>Double</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::Formation
Properties:
    <a href="#app" title="App">App</a>: <i>String</i>
    <a href="#quantity" title="Quantity">Quantity</a>: <i>Double</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### App

The name of the application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quantity

number of processes to maintain.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

dyno size (Example: “standard-1X”). Capitalization does not matter.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

type of process such as "web".

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

