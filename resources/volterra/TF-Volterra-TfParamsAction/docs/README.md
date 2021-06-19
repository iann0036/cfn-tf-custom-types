# TF::Volterra::TfParamsAction

CloudFormation equivalent of volterra_tf_params_action

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::TfParamsAction",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#ignoreonupdate" title="IgnoreOnUpdate">IgnoreOnUpdate</a>" : <i>Boolean</i>,
        "<a href="#sitekind" title="SiteKind">SiteKind</a>" : <i>String</i>,
        "<a href="#sitename" title="SiteName">SiteName</a>" : <i>String</i>,
        "<a href="#waitforaction" title="WaitForAction">WaitForAction</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::TfParamsAction
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#ignoreonupdate" title="IgnoreOnUpdate">IgnoreOnUpdate</a>: <i>Boolean</i>
    <a href="#sitekind" title="SiteKind">SiteKind</a>: <i>String</i>
    <a href="#sitename" title="SiteName">SiteName</a>: <i>String</i>
    <a href="#waitforaction" title="WaitForAction">WaitForAction</a>: <i>Boolean</i>
</pre>

## Properties

#### Action

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreOnUpdate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteKind

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForAction

_Required_: No

_Type_: Boolean

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

#### TfOutput

Returns the <code>TfOutput</code> value.

