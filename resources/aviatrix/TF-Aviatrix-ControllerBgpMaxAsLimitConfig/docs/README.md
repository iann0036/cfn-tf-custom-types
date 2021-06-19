# TF::Aviatrix::ControllerBgpMaxAsLimitConfig

The **aviatrix_controller_bgp_max_as_limit_config** resource allows management of an Aviatrix Controller's BGP max AS limit for transit gateways. This resource is available as of provider version R2.18.1+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::ControllerBgpMaxAsLimitConfig",
    "Properties" : {
        "<a href="#maxaslimit" title="MaxAsLimit">MaxAsLimit</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::ControllerBgpMaxAsLimitConfig
Properties:
    <a href="#maxaslimit" title="MaxAsLimit">MaxAsLimit</a>: <i>Double</i>
</pre>

## Properties

#### MaxAsLimit

The maximum AS path limit allowed by transit gateways when handling BGP/Peering route propagation. Must be a number in the range [1-254].

_Required_: Yes

_Type_: Double

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

