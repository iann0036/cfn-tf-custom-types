# TF::PagerDuty::Addon

With [add-ons](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Add-ons/get_addons), third-party developers can write their own add-ons to PagerDuty's UI. Given a configuration containing a src parameter, that URL will be embedded in an iframe on a page that's available to users from a drop-down menu.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PagerDuty::Addon",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#src" title="Src">Src</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PagerDuty::Addon
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#src" title="Src">Src</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the add-on.
* `src` - (Required) The source URL to display in a frame in the PagerDuty UI. `HTTPS` is required.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Src

The source URL to display in a frame in the PagerDuty UI. `HTTPS` is required.

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

