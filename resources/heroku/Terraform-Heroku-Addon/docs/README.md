# Terraform::Heroku::Addon

Provides a Heroku Add-On resource. These can be attach
services to a Heroku app.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::Addon",
    "Properties" : {
        "<a href="#app" title="App">App</a>" : <i>String</i>,
        "<a href="#config" title="Config">Config</a>" : <i>[ <a href="config.md">Config</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::Addon
Properties:
    <a href="#app" title="App">App</a>: <i>String</i>
    <a href="#config" title="Config">Config</a>: <i>
      - <a href="config.md">Config</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#plan" title="Plan">Plan</a>: <i>String</i>
</pre>

## Properties

#### App

The Heroku app to add to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

Optional plan configuration.

_Required_: No

_Type_: List of <a href="config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Globally unique name of the add-on.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

The addon to add.

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

#### ConfigVars

Returns the <code>ConfigVars</code> value.

#### Id

Returns the <code>Id</code> value.

#### ProviderId

Returns the <code>ProviderId</code> value.

